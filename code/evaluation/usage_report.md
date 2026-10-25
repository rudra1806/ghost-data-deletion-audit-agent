# Token Usage and Cost Report

Generated automatically by `code/main.py` at 2026-10-25T08:16:13Z for the final full-dataset run that produced `output.csv` (518 requests, wall time 0s; the first live execution of the same pipeline took ~17 minutes because calls are throttled to the free-tier per-minute limits, and reruns are served from the response cache).

Provider: **Google Gemini API** (REST `generateContent`), free tier, so the actual spend was $0. The estimate below prices tokens at published list rates per 1M tokens; Gemini 3.x models are priced at the rate of their 2.5 class (Flash-Lite $0.10/$0.40, Flash $0.30/$2.50) as a stated proxy. Roles: vision = strongest Flash model allowed by the free tier, text (intent + investigator) = Flash-Lite with the larger daily quota; each has a fallback model if its quota is exhausted. `api_calls` are live requests in this run; `cache_hits` are identical prompts answered from `code/cache/llm/` (same tokens, no new spend). Token counts include both, so they describe the full workload of producing the output.

## Per-model totals

| Model | Logical calls | Live API calls | Cache hits | Input tokens | Output tokens | Total tokens | Est. cost (USD) |
|---|---|---|---|---|---|---|---|
| gemini-3.6-flash | 11 | 0 | 11 | 15,228 | 37,726 | 52,954 | $0.0989 |
| gemini-3.5-flash-lite | 139 | 0 | 139 | 174,708 | 36,195 | 210,903 | $0.0319 |
| **Overall** | **150** | **0** | | **189,936** | **73,921** | **263,857** | **$0.1308** |

## Per-request averages

- Requests processed: 518
- Average tokens per request: 509.4 (input 366.7, output 142.7)
- Estimated cost per request: $0.000253
- Estimated total cost: $0.1308

## Calls by purpose

| Model | Purpose | Calls |
|---|---|---|
| gemini-3.6-flash | image_extraction | 11 |
| gemini-3.5-flash-lite | intent_classification | 20 |
| gemini-3.5-flash-lite | investigator_agent | 119 |

## Why the token bill is small

- Request texts are deduplicated before classification and sent in batches of 20, so intent costs scale with distinct texts, not cases.
- Each screenshot is transcribed once and cached; the deterministic reasoner consumes the structured transcription, never the image again.
- Evidence parsing, identity resolution, state reconstruction, policy application and ordering are deterministic code with zero tokens.
- The investigator agent is invoked only for cases whose attribution the deterministic matcher marks as contested.
