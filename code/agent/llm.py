"""Minimal Gemini client (REST, standard library only).

* reads GEMINI_API_KEY from the environment or an uncommitted `.env`
* JSON-mode generation, optional inline images, optional function calling
* retries with backoff on 429/5xx, hard timeout
* on-disk response cache keyed by (model, prompt) so reruns are free and
  deterministic
* per-model token accounting for evaluation/usage_report.md
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from .data import REPO_ROOT

API = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
CACHE_DIR = REPO_ROOT / "code" / "cache" / "llm"
# Model per role.  Vision gets a strong Flash model the free tier allows
# (20 requests/day is plenty for 11 screenshots); high-volume text work
# (intent batches, investigator tool loop) goes to a Flash-Lite model with a
# 500/day budget.  Each role has a fallback if its quota is exhausted.
TEXT_MODEL = os.environ.get("GEMINI_TEXT_MODEL", "gemini-3.5-flash-lite")
VISION_MODEL = os.environ.get("GEMINI_VISION_MODEL", "gemini-3.6-flash")
DEFAULT_MODEL = TEXT_MODEL
FALLBACKS = {"gemini-3.5-flash-lite": "gemini-3.1-flash-lite",
             "gemini-3.8-flash": "gemini-3.6-flash",
             "gemini-3.6-flash": "gemini-3-flash-preview"}
# Free-tier requests per minute; the client spaces calls to stay under them.
RPM = {"gemini-3.5-flash-lite": 15, "gemini-3.1-flash-lite": 15, "gemini-3.8-flash": 5,
       "gemini-3.6-flash": 5, "gemini-3-flash-preview": 5, "gemini-2.5-flash": 5,
       "gemini-2.5-flash-lite": 10}

# USD per 1M tokens (input, output) used only for the cost estimate.  The run
# itself used the free tier (actual spend $0); 3.x models are priced at the
# published rate of their 2.5 class (Flash-Lite / Flash) as a stated proxy.
PRICES = {
    "gemini-2.5-flash": (0.30, 2.50),
    "gemini-2.5-flash-lite": (0.10, 0.40),
    "gemini-2.5-pro": (1.25, 10.00),
}
for _m in ("gemini-3.5-flash-lite", "gemini-3.1-flash-lite"):
    PRICES[_m] = PRICES["gemini-2.5-flash-lite"]
for _m in ("gemini-3.8-flash", "gemini-3.6-flash", "gemini-3-flash-preview", "gemini-3.5-flash"):
    PRICES[_m] = PRICES["gemini-2.5-flash"]


def load_env() -> None:
    env = REPO_ROOT / ".env"
    if not env.exists():
        return
    for line in env.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


class QuotaExhausted(RuntimeError):
    """Daily quota for a model is used up; the caller may fall back."""


@dataclass
class Usage:
    calls: int = 0
    cached_calls: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    failures: int = 0
    by_purpose: Dict[str, int] = field(default_factory=dict)


class GeminiClient:
    def __init__(self, model: str = DEFAULT_MODEL, use_cache: bool = True):
        load_env()
        self.api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        self.model = model
        self.use_cache = use_cache
        self.usage: Dict[str, Usage] = {}
        self._last_call: Dict[str, float] = {}
        CACHE_DIR.mkdir(parents=True, exist_ok=True)

    @property
    def available(self) -> bool:
        return bool(self.api_key)

    def _usage(self, model: str) -> Usage:
        return self.usage.setdefault(model, Usage())

    def generate(self, contents: List[dict], purpose: str, system: Optional[str] = None,
                 json_schema: Optional[dict] = None, tools: Optional[List[dict]] = None,
                 model: Optional[str] = None, temperature: float = 0.0) -> Dict[str, Any]:
        """Call generateContent; returns the raw response dict (or raises)."""
        model = model or self.model
        body: Dict[str, Any] = {"contents": contents,
                                "generationConfig": {"temperature": temperature}}
        if system:
            body["systemInstruction"] = {"parts": [{"text": system}]}
        if json_schema is not None:
            body["generationConfig"]["responseMimeType"] = "application/json"
            body["generationConfig"]["responseSchema"] = json_schema
        if tools:
            body["tools"] = [{"functionDeclarations": tools}]
        key = hashlib.sha256(json.dumps([model, body], sort_keys=True).encode()).hexdigest()
        cache_file = CACHE_DIR / f"{key}.json"
        usage = self._usage(model)
        usage.by_purpose[purpose] = usage.by_purpose.get(purpose, 0) + 1
        if self.use_cache and cache_file.exists():
            data = json.loads(cache_file.read_text(encoding="utf-8"))
            usage.cached_calls += 1
            self._count(usage, data)
            return data
        if not self.available:
            raise RuntimeError("GEMINI_API_KEY is not configured")
        try:
            data = self._post(model, body)
        except QuotaExhausted:
            fallback = FALLBACKS.get(model)
            if not fallback:
                raise
            usage.by_purpose[purpose] -= 1
            return self.generate(contents, purpose, system, json_schema, tools, fallback, temperature)
        usage.calls += 1
        self._count(usage, data)
        cache_file.write_text(json.dumps(data), encoding="utf-8")
        return data

    @staticmethod
    def _count(usage: Usage, data: dict) -> None:
        meta = data.get("usageMetadata", {})
        usage.input_tokens += int(meta.get("promptTokenCount", 0))
        usage.output_tokens += int(meta.get("candidatesTokenCount", 0)) + \
            int(meta.get("thoughtsTokenCount", 0))

    def _throttle(self, model: str) -> None:
        gap = 60.0 / RPM.get(model, 10) * 1.1
        wait = self._last_call.get(model, 0.0) + gap - time.time()
        if wait > 0:
            time.sleep(wait)
        self._last_call[model] = time.time()

    def _post(self, model: str, body: dict) -> dict:
        self._throttle(model)
        req = urllib.request.Request(
            API.format(model=model), data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json", "x-goog-api-key": self.api_key},
            method="POST")
        delay = 2.0
        for attempt in range(6):
            try:
                with urllib.request.urlopen(req, timeout=120) as resp:
                    return json.loads(resp.read().decode("utf-8"))
            except urllib.error.HTTPError as err:
                detail = err.read().decode("utf-8", "replace")[:300]
                if err.code == 429 and ("PerDay" in detail or "per day" in detail.lower()):
                    raise QuotaExhausted(detail)
                if err.code in (429, 500, 502, 503, 504) and attempt < 5:
                    time.sleep(delay)
                    delay *= 2
                    continue
                self._usage(model).failures += 1
                raise RuntimeError(f"Gemini HTTP {err.code}: {detail}") from None
            except (urllib.error.URLError, OSError) as err:  # socket.timeout is an OSError on 3.9
                self._usage(model).failures += 1
                if attempt < 2:
                    time.sleep(delay)
                    delay *= 2
                    continue
                # A model that keeps timing out is treated like an exhausted one,
                # so generate() moves on to the role's fallback model.
                raise QuotaExhausted(f"{model} unreachable: {err}") from None
        raise RuntimeError("unreachable")

    # ------------------------------------------------------------ helpers
    def json_call(self, prompt: str, schema: dict, purpose: str, system: Optional[str] = None,
                  images: Optional[List[Path]] = None, model: Optional[str] = None) -> Any:
        parts: List[dict] = []
        for img in images or []:
            parts.append({"inlineData": {"mimeType": "image/png",
                                         "data": base64.b64encode(img.read_bytes()).decode()}})
        parts.append({"text": prompt})
        data = self.generate([{"role": "user", "parts": parts}], purpose, system=system,
                             json_schema=schema, model=model)
        return json.loads(response_text(data))

    def summary(self) -> Dict[str, dict]:
        out = {}
        for model, u in self.usage.items():
            price_in, price_out = PRICES.get(model, PRICES["gemini-2.5-flash"])
            cost = u.input_tokens / 1e6 * price_in + u.output_tokens / 1e6 * price_out
            out[model] = {"api_calls": u.calls, "cache_hits": u.cached_calls,
                          "logical_calls": u.calls + u.cached_calls,
                          "input_tokens": u.input_tokens, "output_tokens": u.output_tokens,
                          "failures": u.failures, "by_purpose": dict(u.by_purpose),
                          "estimated_cost_usd": round(cost, 6),
                          "price_per_mtok": [price_in, price_out]}
        return out


def response_text(data: dict) -> str:
    cands = data.get("candidates") or []
    if not cands:
        raise RuntimeError(f"empty Gemini response: {str(data)[:200]}")
    parts = cands[0].get("content", {}).get("parts", [])
    return "".join(p.get("text", "") for p in parts if not p.get("thought"))


def function_calls(data: dict) -> List[dict]:
    cands = data.get("candidates") or []
    if not cands:
        return []
    return [p["functionCall"] for p in cands[0].get("content", {}).get("parts", [])
            if "functionCall" in p]
