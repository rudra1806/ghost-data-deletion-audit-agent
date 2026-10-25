# Run trace

Per-case audit trail from the last full run: resolved subject, intent verdict, and the state basis for every resource the plan touches.

Status distribution: {'NOT_APPLICABLE': 10, 'INCOMPLETE': 355, 'COMPLETE': 153}

## case_33 -> INCOMPLETE (subject user_18)
- intent: DELETION via gemini
- export_service/export_1842 [USER_EXPORT->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_18 :: latest pdf:alias@evidence_18 2026-07-18T11:00:00+00:00

## case_34 -> INCOMPLETE (subject user_11)
- intent: DELETION via gemini
- account_service/account_5762 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_04 :: latest vision@evidence_04 2026-09-26T11:00:00+00:00
- security_service/audit_record_3753 [SECURITY_AUDIT_LOG->RETAIN] present=False direct=False ref=False flow=None restore=None ev=evidence_05 :: latest log:audit_record_read_completed@evidence_01 2026-09-15T11:54:47+00:00 | superseded by scope-absence evidence_05

## case_35 -> INCOMPLETE (subject user_13)
- intent: DELETION via gemini
- search_service/search_428 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_09 :: latest vision@evidence_09 2026-09-01T06:00:00+00:00

## case_36 -> INCOMPLETE (subject user_34)
- intent: DELETION via gemini
- account_service/account_5823 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- security_service/audit_record_2966 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- export_service/export_7689 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- search_service/search_5575 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00

## case_37 -> INCOMPLETE (subject user_35)
- intent: DELETION via gemini
- account_service/account_5193 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- security_service/audit_record_2019 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- integration_service/data_flow_2528 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- search_service/search_1934 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00

## case_38 -> INCOMPLETE (subject user_36)
- intent: DELETION via gemini
- account_service/account_2381 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- security_service/audit_record_633 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- integration_service/data_flow_7495 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00

## case_39 -> INCOMPLETE (subject user_14)
- intent: DELETION via gemini
- integration_service/data_flow_1121 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_14 :: latest vision@evidence_14 2026-08-07T08:00:00+00:00

## case_40 -> INCOMPLETE (subject user_38)
- intent: DELETION via gemini
- account_service/account_1810 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- security_service/audit_record_8349 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- search_service/search_3200 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- support_platform/support_4887 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00

## case_41 -> COMPLETE (subject user_39)
- intent: DELETION via gemini
- account_service/account_4051 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- analytics_platform/analytics_6830 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- security_service/audit_record_7814 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- backup_service/backup_706 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=False ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- integration_service/data_flow_2901 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- support_platform/support_2667 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00

## case_42 -> INCOMPLETE (subject user_40)
- intent: DELETION via gemini
- account_service/account_4337 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- security_service/audit_record_6760 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- search_service/search_7078 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00
- support_platform/support_7769 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_03 :: latest text:handover@evidence_03 2026-10-01T12:00:00+00:00

## case_43 -> INCOMPLETE (subject user_41)
- intent: DELETION via gemini
- account_service/account_8681 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_94 :: latest log:profile_lookup_completed@evidence_94 2026-09-26T09:21:55+00:00

## case_44 -> COMPLETE (subject user_42)
- intent: DELETION via gemini
- account_service/account_2064 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_94 :: latest log:profile_lookup_completed@evidence_94 2026-09-26T07:49:50+00:00
- analytics_platform/analytics_5589 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_94 :: latest log:analytics_profile_read_completed@evidence_94 2026-09-26T08:57:38+00:00
- security_service/audit_record_1105 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_94 :: latest log:audit_record_read_completed@evidence_94 2026-09-26T08:10:20+00:00
- backup_service/backup_6266 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_94 :: latest log:restore_policy_read_completed@evidence_94 2026-09-26T10:21:52+00:00
- integration_service/data_flow_223 [DATA_FLOW->DISABLE] present=True direct=False ref=True flow=False restore=None ev=evidence_94 :: latest log:connector_config_read_completed@evidence_94 2026-09-26T09:05:46+00:00
- support_platform/support_1066 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_94 :: latest log:support_ticket_read_completed@evidence_94 2026-09-26T09:19:47+00:00

## case_45 -> COMPLETE (subject user_03)
- intent: DELETION via gemini
- security_service/audit_record_003 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_37 :: latest vision@evidence_37 2026-09-05T07:00:00+00:00

## case_46 -> COMPLETE (subject user_17)
- intent: DELETION via gemini
- account_service/account_6523 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_67 :: latest log:profile_lookup_completed@evidence_67 2026-03-10T06:18:01+00:00
- identity_service/tombstone_17 [ACCOUNT_TOMBSTONE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_42 :: latest vision@evidence_42 2026-03-10T06:00:00+00:00

## case_47 -> INCOMPLETE (subject user_45)
- intent: DELETION via gemini
- account_service/account_617 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_05 :: scope-absence evidence_05
- analytics_platform/analytics_9447 [ANALYTICS_PROFILE->ANONYMIZE] present=False direct=False ref=False flow=None restore=None ev=evidence_05 :: scope-absence evidence_05
- search_service/search_4324 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_94 :: latest log:index_query_completed@evidence_94 2026-09-26T09:41:03+00:00
- support_platform/support_5742 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_94 :: latest log:support_ticket_read_completed@evidence_94 2026-09-26T08:49:37+00:00

## case_48 -> INCOMPLETE (subject user_46)
- intent: DELETION via gemini
- account_service/account_483 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_05 :: scope-absence evidence_05
- integration_service/data_flow_7759 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_94 :: latest log:connector_config_read_completed@evidence_94 2026-09-26T09:33:53+00:00
- search_service/search_2127 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_94 :: latest log:index_query_completed@evidence_94 2026-09-26T09:58:35+00:00

## case_49 -> INCOMPLETE (subject user_47)
- intent: DELETION via gemini
- account_service/account_034 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_05 :: scope-absence evidence_05
- integration_service/data_flow_1043 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_94 :: latest log:connector_config_read_completed@evidence_94 2026-09-26T09:46:41+00:00
- search_service/search_459 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_94 :: latest log:index_query_completed@evidence_94 2026-09-26T10:38:56+00:00

## case_50 -> INCOMPLETE (subject user_20)
- intent: DELETION via gemini
- analytics_platform/analytics_7438 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_19 :: latest vision@evidence_19 2026-07-13T10:00:00+00:00

## case_51 -> COMPLETE (subject user_49)
- intent: DELETION via gemini
- account_service/account_3610 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_94 :: latest log:profile_lookup_completed@evidence_94 2026-09-26T08:37:56+00:00
- analytics_platform/analytics_2265 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_94 :: latest log:analytics_profile_read_completed@evidence_94 2026-09-26T09:58:42+00:00
- security_service/audit_record_3308 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_94 :: latest log:audit_record_read_completed@evidence_94 2026-09-26T10:37:23+00:00
- backup_service/backup_7809 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_94 :: latest log:restore_policy_read_completed@evidence_94 2026-09-26T07:54:41+00:00
- integration_service/data_flow_4713 [DATA_FLOW->DISABLE] present=True direct=False ref=True flow=False restore=None ev=evidence_94 :: latest log:connector_config_read_completed@evidence_94 2026-09-26T07:51:26+00:00
- support_platform/support_1097 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_94 :: latest log:support_ticket_read_completed@evidence_94 2026-09-26T10:00:17+00:00

## case_52 -> INCOMPLETE (subject user_18)
- intent: DELETION via gemini
- export_service/export_1260 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_23 :: latest vision@evidence_23 2026-06-18T12:00:00+00:00

## case_53 -> INCOMPLETE (subject user_22)
- intent: DELETION via gemini
- support_platform/support_1034 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_28 :: latest vision@evidence_28 2026-05-24T07:00:00+00:00

## case_54 -> INCOMPLETE (subject user_52)
- intent: DELETION via gemini
- account_service/account_6829 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_05 :: scope-absence evidence_05
- analytics_platform/analytics_1738 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00
- security_service/audit_record_6325 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00
- integration_service/data_flow_5080 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00
- search_service/search_3995 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00
- support_platform/support_835 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00

## case_55 -> INCOMPLETE (subject user_16)
- intent: DELETION via gemini
- backup_service/backup_9287 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_32 :: latest vision@evidence_32 2026-04-29T09:00:00+00:00

## case_56 -> INCOMPLETE (subject user_54)
- intent: DELETION via gemini
- account_service/account_5715 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_05 :: scope-absence evidence_05
- security_service/audit_record_4078 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00
- integration_service/data_flow_373 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00

## case_57 -> COMPLETE (subject user_55)
- intent: DELETION via gemini
- account_service/account_1298 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_05 :: scope-absence evidence_05
- analytics_platform/analytics_8858 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00
- security_service/audit_record_7219 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00
- backup_service/backup_7711 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00
- integration_service/data_flow_1368 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00
- support_platform/support_7479 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00

## case_58 -> COMPLETE (subject user_56)
- intent: DELETION via gemini
- account_service/account_9862 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_05 :: scope-absence evidence_05
- analytics_platform/analytics_2572 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00
- security_service/audit_record_8465 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00

## case_59 -> COMPLETE (subject user_57)
- intent: DELETION via gemini
- account_service/account_631 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_05 :: scope-absence evidence_05
- analytics_platform/analytics_9069 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00
- security_service/audit_record_962 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00

## case_60 -> COMPLETE (subject user_58)
- intent: DELETION via gemini
- account_service/account_5661 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_05 :: scope-absence evidence_05
- security_service/audit_record_629 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00

## case_61 -> INCOMPLETE (subject user_07)
- intent: DELETION via gemini
- object_storage/object_19 [SUPPORT_ATTACHMENT->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_46 :: latest vision@evidence_46 2026-02-13T08:00:00+00:00

## case_62 -> INCOMPLETE (subject user_60)
- intent: DELETION via gemini
- account_service/account_7119 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_05 :: scope-absence evidence_05
- analytics_platform/analytics_5715 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00
- security_service/audit_record_4889 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00
- integration_service/data_flow_108 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00
- search_service/search_5960 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00
- support_platform/support_8765 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_05 :: latest sql:customer_data_read_replica@evidence_05 2026-09-21T10:00:00+00:00

## case_63 -> INCOMPLETE (subject user_09)
- intent: DELETION via gemini
- marketing_platform/marketing_001 [MARKETING_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_60 :: latest vision@evidence_60 2026-09-16T07:20:00+00:00

## case_64 -> COMPLETE (subject user_62)
- intent: DELETION via gemini
- account_service/account_565 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:profile_lookup_completed@evidence_06 2026-09-16T08:56:26+00:00
- analytics_platform/analytics_5718 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:analytics_profile_read@evidence_06 2026-09-16T08:57:07+00:00
- security_service/audit_record_1892 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:audit_record_read_completed@evidence_06 2026-09-16T08:56:31+00:00
- backup_service/backup_3933 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=False ev=evidence_93 :: latest log:restore_authorization_completed@evidence_06 2026-09-16T08:54:49+00:00
- integration_service/data_flow_6846 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_93 :: latest log:connector_config_loaded@evidence_06 2026-09-16T08:52:09+00:00
- support_platform/support_6334 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:message_read@evidence_06 2026-09-16T08:57:24+00:00

## case_65 -> INCOMPLETE (subject user_63)
- intent: DELETION via gemini
- account_service/account_5488 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:profile_lookup_completed@evidence_06 2026-09-16T08:51:33+00:00
- analytics_platform/analytics_9246 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_93 :: latest log:analytics_identity_scan@evidence_06 2026-09-16T08:53:55+00:00
- security_service/audit_record_1848 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_06 2026-09-16T08:58:57+00:00
- search_service/search_689 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:index_query_completed@evidence_06 2026-09-16T08:54:28+00:00

## case_66 -> INCOMPLETE (subject user_64)
- intent: DELETION via gemini
- account_service/account_1602 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:profile_lookup_completed@evidence_06 2026-09-16T08:58:06+00:00
- security_service/audit_record_184 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_06 2026-09-16T08:57:11+00:00
- support_platform/support_4249 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_93 :: latest log:message_pii_scan@evidence_06 2026-09-16T08:51:30+00:00

## case_67 -> INCOMPLETE (subject user_65)
- intent: DELETION via gemini
- account_service/account_9079 [USER_PROFILE->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:profile_lookup_completed@evidence_06 2026-09-16T08:56:34+00:00
- security_service/audit_record_2877 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_06 2026-09-16T08:54:41+00:00

## case_68 -> INCOMPLETE (subject user_66)
- intent: DELETION via gemini
- account_service/account_902 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:profile_lookup_completed@evidence_06 2026-09-16T08:54:05+00:00
- security_service/audit_record_4049 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_06 2026-09-16T08:54:45+00:00
- integration_service/data_flow_2406 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_93 :: latest log:connector_heartbeat@evidence_06 2026-09-16T08:56:20+00:00
- search_service/search_2568 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:index_query_completed@evidence_06 2026-09-16T08:54:00+00:00

## case_69 -> COMPLETE (subject user_67)
- intent: DELETION via gemini
- account_service/account_6138 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:profile_lookup_completed@evidence_06 2026-09-16T08:57:19+00:00
- security_service/audit_record_9011 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:audit_record_read_completed@evidence_06 2026-09-16T08:56:52+00:00

## case_70 -> COMPLETE (subject user_68)
- intent: DELETION via gemini
- account_service/account_6633 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:profile_lookup_completed@evidence_06 2026-09-16T08:56:42+00:00
- security_service/audit_record_1738 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:audit_record_read_completed@evidence_06 2026-09-16T08:52:11+00:00

## case_71 -> INCOMPLETE (subject user_69)
- intent: DELETION via gemini
- account_service/account_1378 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:profile_lookup_completed@evidence_06 2026-09-16T08:57:34+00:00
- security_service/audit_record_1096 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_06 2026-09-16T08:58:32+00:00
- search_service/search_684 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:index_query_completed@evidence_06 2026-09-16T08:52:24+00:00
- support_platform/support_1370 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_93 :: latest log:attachment_pii_scan@evidence_06 2026-09-16T08:59:28+00:00

## case_72 -> INCOMPLETE (subject user_70)
- intent: DELETION via gemini
- account_service/account_7643 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:profile_lookup_completed@evidence_06 2026-09-16T08:58:00+00:00
- security_service/audit_record_1310 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_06 2026-09-16T08:58:14+00:00
- export_service/export_4091 [USER_EXPORT->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_93 :: latest log:export_download_check_completed@evidence_06 2026-09-16T08:57:36+00:00

## case_73 -> COMPLETE (subject user_71)
- intent: DELETION via gemini
- account_service/account_6070 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_91 :: latest log:profile_lookup_completed@evidence_91 2026-09-11T06:55:19+00:00
- analytics_platform/analytics_1161 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- security_service/audit_record_5710 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00

## case_74 -> INCOMPLETE (subject user_72)
- intent: DELETION via gemini
- account_service/account_9051 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_90 :: scope-absence evidence_90
- security_service/audit_record_7778 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- integration_service/data_flow_4595 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00

## case_75 -> INCOMPLETE (subject user_73)
- intent: DELETION via gemini
- account_service/account_1495 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_90 :: scope-absence evidence_90
- security_service/audit_record_7491 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- backup_service/backup_8673 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00

## case_76 -> INCOMPLETE (subject user_74)
- intent: DELETION via gemini
- account_service/account_925 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_90 :: scope-absence evidence_90
- security_service/audit_record_6766 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- support_platform/support_9746 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00

## case_77 -> COMPLETE (subject user_75)
- intent: DELETION via gemini
- account_service/account_9334 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_91 :: latest log:profile_lookup_completed@evidence_91 2026-09-11T06:31:32+00:00
- analytics_platform/analytics_5859 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- security_service/audit_record_5425 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- backup_service/backup_7303 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- integration_service/data_flow_7773 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- support_platform/support_008 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00

## case_78 -> INCOMPLETE (subject user_76)
- intent: DELETION via gemini
- account_service/account_8754 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_90 :: scope-absence evidence_90
- security_service/audit_record_6593 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- search_service/search_8295 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- support_platform/support_9652 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00

## case_79 -> COMPLETE (subject user_77)
- intent: DELETION via gemini
- account_service/account_5186 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_91 :: latest log:profile_lookup_completed@evidence_91 2026-09-11T06:55:37+00:00
- security_service/audit_record_1734 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00

## case_80 -> COMPLETE (subject user_78)
- intent: DELETION via gemini
- account_service/account_4006 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_91 :: latest log:profile_lookup_completed@evidence_91 2026-09-11T05:39:16+00:00
- security_service/audit_record_5681 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00

## case_81 -> COMPLETE (subject user_79)
- intent: DELETION via gemini
- account_service/account_9832 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_91 :: latest log:profile_lookup_completed@evidence_91 2026-09-11T06:36:30+00:00
- analytics_platform/analytics_5059 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- security_service/audit_record_9645 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- backup_service/backup_3332 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- integration_service/data_flow_3255 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- support_platform/support_5953 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00

## case_82 -> COMPLETE (subject user_80)
- intent: DELETION via gemini
- account_service/account_4156 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_91 :: latest log:profile_lookup_completed@evidence_91 2026-09-11T06:10:22+00:00
- analytics_platform/analytics_2176 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- security_service/audit_record_3747 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- backup_service/backup_317 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- integration_service/data_flow_9666 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00
- support_platform/support_9166 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_91 :: latest json:bundle@evidence_07 2026-09-11T08:00:00+00:00

## case_83 -> COMPLETE (subject user_81)
- intent: DELETION via gemini
- account_service/account_2449 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- security_service/audit_record_2636 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00

## case_84 -> COMPLETE (subject user_82)
- intent: DELETION via gemini
- account_service/account_2387 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- security_service/audit_record_3787 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00

## case_85 -> INCOMPLETE (subject user_83)
- intent: DELETION via gemini
- account_service/account_4911 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- security_service/audit_record_8094 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- integration_service/data_flow_9927 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- search_service/search_6302 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00

## case_86 -> COMPLETE (subject user_84)
- intent: DELETION via gemini
- account_service/account_8473 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- analytics_platform/analytics_9500 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- security_service/audit_record_5580 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00

## case_87 -> INCOMPLETE (subject user_85)
- intent: DELETION via gemini
- account_service/account_8166 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- security_service/audit_record_4474 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- backup_service/backup_4689 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=True ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00

## case_88 -> INCOMPLETE (subject user_86)
- intent: DELETION via gemini
- account_service/account_868 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- security_service/audit_record_3825 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- support_platform/support_2967 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00

## case_89 -> INCOMPLETE (subject user_87)
- intent: DELETION via gemini
- account_service/account_8764 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- analytics_platform/analytics_6499 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- security_service/audit_record_2539 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- search_service/search_1839 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00

## case_90 -> INCOMPLETE (subject user_88)
- intent: DELETION via gemini
- account_service/account_9673 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- analytics_platform/analytics_3181 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- security_service/audit_record_9355 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- integration_service/data_flow_2085 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- search_service/search_5561 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- support_platform/support_7460 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00

## case_91 -> INCOMPLETE (subject user_89)
- intent: DELETION via gemini
- account_service/account_6075 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- analytics_platform/analytics_8539 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- security_service/audit_record_8304 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- search_service/search_9156 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- support_platform/support_266 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00

## case_92 -> INCOMPLETE (subject user_90)
- intent: DELETION via gemini
- account_service/account_3609 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- security_service/audit_record_5625 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00
- integration_service/data_flow_7535 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_08 :: latest log:record_lookup@evidence_08 2026-09-06T07:00:00+00:00

## case_93 -> INCOMPLETE (subject user_91)
- intent: DELETION via gemini
- account_service/account_4421 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T05:06:02+00:00
- integration_service/data_flow_047 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T03:12:34+00:00
- search_service/search_1310 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T05:08:28+00:00
- support_platform/support_1824 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T05:26:52+00:00

## case_94 -> INCOMPLETE (subject user_92)
- intent: DELETION via gemini
- account_service/account_4037 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- search_service/search_7631 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T02:59:37+00:00
- support_platform/support_7691 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T03:57:56+00:00

## case_95 -> INCOMPLETE (subject user_93)
- intent: DELETION via gemini
- account_service/account_4176 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- analytics_platform/analytics_1316 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T02:46:10+00:00
- search_service/search_7807 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T05:12:30+00:00
- support_platform/support_5750 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T03:30:27+00:00
- support_platform/support_7311 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T04:13:52+00:00

## case_96 -> INCOMPLETE (subject user_94)
- intent: DELETION via gemini
- account_service/account_5815 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- export_service/export_8827 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T05:02:19+00:00
- search_service/search_5672 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T03:05:19+00:00

## case_97 -> COMPLETE (subject user_95)
- intent: DELETION via gemini
- account_service/account_6813 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T04:31:43+00:00
- analytics_platform/analytics_9103 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T04:13:46+00:00
- security_service/audit_record_8778 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T03:39:53+00:00

## case_98 -> INCOMPLETE (subject user_96)
- intent: DELETION via gemini
- account_service/account_9511 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- integration_service/data_flow_3165 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T03:43:18+00:00
- legal_service/legal_hold_668 [LEGAL_HOLD_RECORD->RETAIN] present=False direct=False ref=False flow=None restore=None ev=evidence_24 :: scope-absence evidence_24

## case_99 -> INCOMPLETE (subject user_97)
- intent: DELETION via gemini
- account_service/account_1034 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- backup_service/backup_7804 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T04:49:22+00:00

## case_100 -> INCOMPLETE (subject user_98)
- intent: DELETION via gemini
- account_service/account_7927 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- search_service/search_018 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T04:45:42+00:00
- support_platform/support_1630 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T04:10:02+00:00

## case_101 -> INCOMPLETE (subject user_99)
- intent: DELETION via gemini
- account_service/account_7169 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- analytics_platform/analytics_6105 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T03:47:46+00:00
- search_service/search_8561 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T04:44:40+00:00

## case_102 -> INCOMPLETE (subject user_100)
- intent: DELETION via gemini
- account_service/account_2056 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- search_service/search_4586 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T05:33:16+00:00
- support_platform/support_345 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_89 :: latest json:export@evidence_89 2026-09-01T03:15:20+00:00

## case_103 -> COMPLETE (subject user_101)
- intent: DELETION via gemini
- account_service/account_4070 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- analytics_platform/analytics_3264 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- security_service/audit_record_9522 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00

## case_104 -> INCOMPLETE (subject user_102)
- intent: DELETION via gemini
- account_service/account_8804 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- analytics_platform/analytics_4882 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- security_service/audit_record_6230 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- integration_service/data_flow_5127 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- search_service/search_8379 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- support_platform/support_4267 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00

## case_105 -> INCOMPLETE (subject user_103)
- intent: DELETION via gemini
- account_service/account_6345 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- security_service/audit_record_4520 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- search_service/search_4618 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00

## case_106 -> INCOMPLETE (subject user_104)
- intent: DELETION via gemini
- account_service/account_4514 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- security_service/audit_record_8723 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- search_service/search_7223 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00

## case_107 -> COMPLETE (subject user_105)
- intent: DELETION via gemini
- account_service/account_7510 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- analytics_platform/analytics_2777 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- security_service/audit_record_7572 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00

## case_108 -> COMPLETE (subject user_106)
- intent: DELETION via gemini
- account_service/account_6750 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- analytics_platform/analytics_5001 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- security_service/audit_record_1469 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00

## case_109 -> INCOMPLETE (subject user_107)
- intent: DELETION via gemini
- account_service/account_687 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- security_service/audit_record_2718 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- integration_service/data_flow_9949 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- search_service/search_2016 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00

## case_110 -> INCOMPLETE (subject user_108)
- intent: DELETION via gemini
- account_service/account_2259 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- security_service/audit_record_9268 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- integration_service/data_flow_8857 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- search_service/search_3993 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00

## case_111 -> COMPLETE (subject user_109)
- intent: DELETION via gemini
- account_service/account_9314 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- analytics_platform/analytics_800 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- security_service/audit_record_8933 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00

## case_112 -> COMPLETE (subject user_110)
- intent: DELETION via gemini
- account_service/account_7578 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_10 :: scope-absence evidence_10
- analytics_platform/analytics_9875 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- security_service/audit_record_4082 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- backup_service/backup_4863 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- integration_service/data_flow_3444 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00
- support_platform/support_2859 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_10 :: latest sql:customer_data_read_replica@evidence_10 2026-08-27T12:00:00+00:00

## case_113 -> COMPLETE (subject user_111)
- intent: DELETION via gemini
- account_service/account_6697 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:profile_lookup_completed@evidence_11 2026-08-22T10:52:05+00:00
- analytics_platform/analytics_4800 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:analytics_profile_read@evidence_11 2026-08-22T10:55:27+00:00
- security_service/audit_record_1127 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:audit_record_read_completed@evidence_11 2026-08-22T10:55:04+00:00

## case_114 -> INCOMPLETE (subject user_112)
- intent: DELETION via gemini
- account_service/account_4833 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_12 :: latest log:profile_lookup_completed@evidence_11 2026-08-22T10:54:40+00:00
- security_service/audit_record_6504 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_11 2026-08-22T10:53:32+00:00
- search_service/search_5696 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:index_query_completed@evidence_11 2026-08-22T10:54:36+00:00
- support_platform/support_3786 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_88 :: latest log:message_pii_scan@evidence_11 2026-08-22T10:53:27+00:00

## case_115 -> INCOMPLETE (subject user_113)
- intent: DELETION via gemini
- account_service/account_1785 [USER_PROFILE->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:profile_lookup_completed@evidence_11 2026-08-22T10:51:17+00:00
- security_service/audit_record_670 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_11 2026-08-22T10:52:01+00:00
- search_service/search_4417 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:index_query_completed@evidence_11 2026-08-22T10:57:41+00:00

## case_116 -> INCOMPLETE (subject user_114)
- intent: DELETION via gemini
- account_service/account_1823 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_12 :: latest log:profile_lookup_completed@evidence_11 2026-08-22T10:57:28+00:00
- security_service/audit_record_6007 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_11 2026-08-22T10:53:04+00:00
- integration_service/data_flow_6699 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_88 :: latest log:connector_heartbeat@evidence_11 2026-08-22T10:58:04+00:00
- search_service/search_696 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:index_query_completed@evidence_11 2026-08-22T10:52:29+00:00

## case_117 -> COMPLETE (subject user_115)
- intent: DELETION via gemini
- account_service/account_1220 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:profile_lookup_completed@evidence_11 2026-08-22T10:52:35+00:00
- analytics_platform/analytics_8698 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:analytics_profile_read@evidence_11 2026-08-22T10:59:42+00:00
- security_service/audit_record_1598 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:audit_record_read_completed@evidence_11 2026-08-22T10:59:03+00:00

## case_118 -> INCOMPLETE (subject user_116)
- intent: DELETION via gemini
- account_service/account_5785 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_12 :: latest log:profile_lookup_completed@evidence_11 2026-08-22T10:53:37+00:00
- security_service/audit_record_2848 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_11 2026-08-22T10:54:20+00:00
- search_service/search_9556 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:index_query_completed@evidence_11 2026-08-22T10:52:18+00:00
- support_platform/support_036 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_88 :: latest log:message_pii_scan@evidence_11 2026-08-22T10:54:27+00:00

## case_119 -> INCOMPLETE (subject user_117)
- intent: DELETION via gemini
- account_service/account_8058 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_12 :: latest log:profile_lookup_completed@evidence_11 2026-08-22T10:56:22+00:00
- security_service/audit_record_9445 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_11 2026-08-22T10:56:57+00:00
- search_service/search_5259 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:index_query_completed@evidence_11 2026-08-22T10:52:37+00:00
- support_platform/support_9309 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_88 :: latest log:attachment_pii_scan@evidence_11 2026-08-22T10:51:33+00:00

## case_120 -> INCOMPLETE (subject user_118)
- intent: DELETION via gemini
- account_service/account_8656 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_12 :: latest log:profile_lookup_completed@evidence_11 2026-08-22T10:52:27+00:00
- security_service/audit_record_5496 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_11 2026-08-22T10:55:06+00:00
- export_service/export_4289 [USER_EXPORT->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:export_download_check_completed@evidence_11 2026-08-22T10:55:39+00:00
- search_service/search_943 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:index_query_completed@evidence_11 2026-08-22T10:58:30+00:00

## case_121 -> COMPLETE (subject user_119)
- intent: DELETION via gemini
- account_service/account_081 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:profile_lookup_completed@evidence_11 2026-08-22T10:57:33+00:00
- security_service/audit_record_2103 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:audit_record_read_completed@evidence_11 2026-08-22T10:53:02+00:00

## case_122 -> INCOMPLETE (subject user_120)
- intent: DELETION via gemini
- account_service/account_9580 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_12 :: latest log:profile_lookup_completed@evidence_11 2026-08-22T10:51:52+00:00
- security_service/audit_record_9833 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_11 2026-08-22T10:58:45+00:00
- integration_service/data_flow_3199 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_88 :: latest log:connector_heartbeat@evidence_11 2026-08-22T10:56:57+00:00
- search_service/search_1752 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_88 :: latest log:index_query_completed@evidence_11 2026-08-22T10:55:30+00:00

## case_123 -> INCOMPLETE (subject user_121)
- intent: DELETION via gemini
- account_service/account_2988 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_87 :: scope-absence evidence_87
- security_service/audit_record_5645 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- backup_service/backup_8742 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00

## case_124 -> INCOMPLETE (subject user_122)
- intent: DELETION via gemini
- account_service/account_8951 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_87 :: scope-absence evidence_87
- security_service/audit_record_282 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- support_platform/support_9126 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00

## case_125 -> INCOMPLETE (subject user_123)
- intent: DELETION via gemini
- account_service/account_7637 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_87 :: scope-absence evidence_87
- analytics_platform/analytics_1103 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- security_service/audit_record_023 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- search_service/search_9752 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00

## case_126 -> COMPLETE (subject user_124)
- intent: DELETION via gemini
- account_service/account_8819 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-11T10:00:00+00:00 | superseded by scope-absence evidence_87
- analytics_platform/analytics_1402 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- security_service/audit_record_6884 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00

## case_127 -> COMPLETE (subject user_125)
- intent: DELETION via gemini
- account_service/account_6805 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_87 :: scope-absence evidence_87
- analytics_platform/analytics_7150 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- security_service/audit_record_9649 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00

## case_128 -> INCOMPLETE (subject user_126)
- intent: DELETION via gemini
- account_service/account_7878 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_87 :: scope-absence evidence_87
- security_service/audit_record_4249 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- integration_service/data_flow_5550 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00

## case_129 -> INCOMPLETE (subject user_127)
- intent: DELETION via gemini
- account_service/account_6673 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- security_service/audit_record_5606 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- search_service/search_5148 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00

## case_130 -> INCOMPLETE (subject user_128)
- intent: DELETION via gemini
- account_service/account_8729 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_87 :: scope-absence evidence_87
- security_service/audit_record_7634 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- search_service/search_2364 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- support_platform/support_187 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00

## case_131 -> INCOMPLETE (subject user_129)
- intent: DELETION via gemini
- account_service/account_426 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_87 :: scope-absence evidence_87
- analytics_platform/analytics_514 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- security_service/audit_record_8457 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- search_service/search_538 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- support_platform/support_2315 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- support_platform/support_7208 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00

## case_132 -> INCOMPLETE (subject user_130)
- intent: DELETION via gemini
- account_service/account_4395 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_87 :: scope-absence evidence_87
- security_service/audit_record_1424 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- export_service/export_9157 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00
- search_service/search_3112 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_87 :: latest json:bundle@evidence_12 2026-08-17T10:00:00+00:00

## case_133 -> INCOMPLETE (subject user_131)
- intent: DELETION via gemini
- account_service/account_9191 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- security_service/audit_record_3130 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- integration_service/data_flow_4227 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- search_service/search_1474 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00

## case_134 -> INCOMPLETE (subject user_132)
- intent: DELETION via gemini
- account_service/account_1084 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- analytics_platform/analytics_7772 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- security_service/audit_record_4064 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- integration_service/data_flow_7812 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- search_service/search_7941 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- support_platform/support_4410 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00

## case_135 -> COMPLETE (subject user_133)
- intent: DELETION via gemini
- account_service/account_1417 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- analytics_platform/analytics_1626 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T07:41:04+00:00
- security_service/audit_record_5140 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00

## case_136 -> INCOMPLETE (subject user_134)
- intent: DELETION via gemini
- account_service/account_4079 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- security_service/audit_record_7931 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- search_service/search_1110 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- support_platform/support_4442 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00

## case_137 -> COMPLETE (subject user_135)
- intent: DELETION via gemini
- account_service/account_3734 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- security_service/audit_record_6779 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00

## case_138 -> INCOMPLETE (subject user_136)
- intent: DELETION via gemini
- account_service/account_6452 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- security_service/audit_record_122 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- search_service/search_4464 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- support_platform/support_2716 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00

## case_139 -> INCOMPLETE (subject user_137)
- intent: DELETION via gemini
- account_service/account_907 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- security_service/audit_record_7689 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- search_service/search_6677 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00

## case_140 -> INCOMPLETE (subject user_138)
- intent: DELETION via gemini
- account_service/account_6372 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- analytics_platform/analytics_3006 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- security_service/audit_record_8086 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- integration_service/data_flow_9030 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- search_service/search_7363 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- support_platform/support_5323 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00

## case_141 -> INCOMPLETE (subject user_139)
- intent: DELETION via gemini
- account_service/account_923 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- security_service/audit_record_5497 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- search_service/search_460 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00

## case_142 -> INCOMPLETE (subject user_140)
- intent: DELETION via gemini
- account_service/account_2434 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- security_service/audit_record_280 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- search_service/search_2024 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00
- support_platform/support_771 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_13 :: latest json:ledger@evidence_13 2026-08-12T09:00:00+00:00

## case_143 -> INCOMPLETE (subject user_141)
- intent: DELETION via gemini
- account_service/account_2900 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_15 :: scope-absence evidence_15
- search_service/search_6137 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T06:07:38+00:00
- support_platform/support_6560 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T07:06:13+00:00

## case_144 -> INCOMPLETE (subject user_142)
- intent: DELETION via gemini
- account_service/account_6826 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_15 :: scope-absence evidence_15
- export_service/export_7992 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T06:10:31+00:00

## case_145 -> INCOMPLETE (subject user_143)
- intent: DELETION via gemini
- account_service/account_5572 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_15 :: scope-absence evidence_15
- integration_service/data_flow_7253 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T06:49:45+00:00
- search_service/search_1725 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T04:49:16+00:00

## case_146 -> INCOMPLETE (subject user_144)
- intent: DELETION via gemini
- account_service/account_5023 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_15 :: scope-absence evidence_15
- integration_service/data_flow_4889 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T05:17:19+00:00
- search_service/search_2262 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T05:50:33+00:00

## case_147 -> INCOMPLETE (subject user_145)
- intent: DELETION via gemini
- account_service/account_8632 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_15 :: scope-absence evidence_15
- backup_service/backup_4244 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T07:35:24+00:00

## case_148 -> INCOMPLETE (subject user_146)
- intent: DELETION via gemini
- account_service/account_7864 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_15 :: scope-absence evidence_15
- search_service/search_7239 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T05:53:09+00:00
- support_platform/support_5716 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T07:11:08+00:00

## case_149 -> INCOMPLETE (subject user_147)
- intent: DELETION via gemini
- account_service/account_9505 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_15 :: scope-absence evidence_15
- analytics_platform/analytics_5886 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T04:45:16+00:00
- search_service/search_7672 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T06:09:49+00:00

## case_150 -> COMPLETE (subject user_148)
- intent: DELETION via gemini
- account_service/account_3897 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T05:55:37+00:00
- analytics_platform/analytics_7254 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T06:25:11+00:00
- security_service/audit_record_1584 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T07:19:45+00:00

## case_151 -> COMPLETE (subject user_149)
- intent: DELETION via gemini
- account_service/account_874 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T05:59:32+00:00
- security_service/audit_record_8905 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T04:48:17+00:00
- backup_service/backup_9557 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T06:27:21+00:00
- integration_service/data_flow_2437 [DATA_FLOW->DISABLE] present=True direct=False ref=True flow=False restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T06:10:12+00:00
- support_platform/support_5400 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T06:50:56+00:00

## case_152 -> COMPLETE (subject user_150)
- intent: DELETION via gemini
- account_service/account_8854 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T07:39:36+00:00
- security_service/audit_record_3579 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_86 :: latest json:export@evidence_86 2026-08-07T05:22:56+00:00

## case_153 -> INCOMPLETE (subject user_151)
- intent: DELETION via gemini
- account_service/account_8023 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00
- security_service/audit_record_5652 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00
- search_service/search_9831 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00

## case_154 -> INCOMPLETE (subject user_152)
- intent: DELETION via gemini
- account_service/account_7680 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_15 :: scope-absence evidence_15
- security_service/audit_record_2580 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00
- search_service/search_1446 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00

## case_155 -> COMPLETE (subject user_153)
- intent: DELETION via gemini
- account_service/account_1992 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_15 :: scope-absence evidence_15
- analytics_platform/analytics_7372 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00
- security_service/audit_record_4199 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00
- backup_service/backup_161 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00
- integration_service/data_flow_4305 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00
- support_platform/support_7867 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00

## case_156 -> INCOMPLETE (subject user_154)
- intent: DELETION via gemini
- account_service/account_2362 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_15 :: scope-absence evidence_15
- security_service/audit_record_5890 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00
- export_service/export_5897 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00
- search_service/search_4870 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00

## case_157 -> COMPLETE (subject user_155)
- intent: DELETION via gemini
- account_service/account_2154 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_15 :: scope-absence evidence_15
- analytics_platform/analytics_8425 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00
- security_service/audit_record_8821 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00

## case_158 -> INCOMPLETE (subject user_156)
- intent: DELETION via gemini
- account_service/account_1421 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_15 :: scope-absence evidence_15
- security_service/audit_record_9665 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00
- integration_service/data_flow_7704 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00
- search_service/search_9834 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00

## case_159 -> INCOMPLETE (subject user_157)
- intent: DELETION via gemini
- account_service/account_4272 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_15 :: scope-absence evidence_15
- security_service/audit_record_8742 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00
- backup_service/backup_1214 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00

## case_160 -> INCOMPLETE (subject user_158)
- intent: DELETION via gemini
- account_service/account_1688 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_15 :: scope-absence evidence_15
- security_service/audit_record_9882 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00
- support_platform/support_4148 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00

## case_161 -> INCOMPLETE (subject user_159)
- intent: DELETION via gemini
- account_service/account_5501 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_15 :: scope-absence evidence_15
- analytics_platform/analytics_2008 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00
- security_service/audit_record_8002 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00

## case_162 -> COMPLETE (subject user_160)
- intent: DELETION via gemini
- account_service/account_5983 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_15 :: scope-absence evidence_15
- security_service/audit_record_6362 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_15 :: latest sql:customer_data_read_replica@evidence_15 2026-08-02T07:00:00+00:00

## case_163 -> INCOMPLETE (subject user_161)
- intent: DELETION via gemini
- account_service/account_4289 [USER_PROFILE->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_85 :: latest log:profile_lookup_completed@evidence_16 2026-07-28T05:51:51+00:00
- security_service/audit_record_1053 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_16 2026-07-28T05:58:32+00:00
- search_service/search_4509 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_85 :: latest log:index_query_completed@evidence_16 2026-07-28T05:59:09+00:00

## case_164 -> COMPLETE (subject user_162)
- intent: DELETION via gemini
- account_service/account_9549 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_85 :: latest log:profile_lookup_completed@evidence_16 2026-07-28T05:57:13+00:00
- analytics_platform/analytics_6402 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_85 :: latest log:analytics_profile_read@evidence_16 2026-07-28T05:56:00+00:00
- security_service/audit_record_6780 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_85 :: latest log:audit_record_read_completed@evidence_16 2026-07-28T05:54:05+00:00

## case_165 -> INCOMPLETE (subject user_163)
- intent: DELETION via gemini
- account_service/account_3064 [USER_PROFILE->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_85 :: latest log:profile_lookup_completed@evidence_16 2026-07-28T05:56:35+00:00
- analytics_platform/analytics_2713 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_85 :: latest log:analytics_identity_scan@evidence_16 2026-07-28T05:59:03+00:00
- security_service/audit_record_4964 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_16 2026-07-28T05:51:49+00:00
- search_service/search_8678 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_85 :: latest log:index_query_completed@evidence_16 2026-07-28T05:58:05+00:00
- support_platform/support_3586 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_85 :: latest log:message_pii_scan@evidence_16 2026-07-28T05:56:53+00:00

## case_166 -> INCOMPLETE (subject user_164)
- intent: DELETION via gemini
- account_service/account_1837 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_17 :: latest log:profile_lookup_completed@evidence_16 2026-07-28T05:53:19+00:00
- security_service/audit_record_7082 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_16 2026-07-28T05:54:33+00:00
- search_service/search_5261 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_85 :: latest log:index_query_completed@evidence_16 2026-07-28T05:54:04+00:00
- support_platform/support_3155 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_85 :: latest log:message_pii_scan@evidence_16 2026-07-28T05:55:35+00:00

## case_167 -> COMPLETE (subject user_165)
- intent: DELETION via gemini
- account_service/account_5284 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_85 :: latest log:profile_lookup_completed@evidence_16 2026-07-28T05:55:56+00:00
- security_service/audit_record_3088 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_85 :: latest log:audit_record_read_completed@evidence_16 2026-07-28T05:56:42+00:00

## case_168 -> INCOMPLETE (subject user_166)
- intent: DELETION via gemini
- account_service/account_8748 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_17 :: latest log:profile_lookup_completed@evidence_16 2026-07-28T05:53:55+00:00
- security_service/audit_record_2503 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_16 2026-07-28T05:55:39+00:00
- export_service/export_4102 [USER_EXPORT->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_85 :: latest log:export_download_check_completed@evidence_16 2026-07-28T05:57:25+00:00

## case_169 -> INCOMPLETE (subject user_167)
- intent: DELETION via gemini
- account_service/account_7268 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_17 :: latest log:profile_lookup_completed@evidence_16 2026-07-28T05:52:42+00:00
- security_service/audit_record_5374 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_16 2026-07-28T05:55:24+00:00
- integration_service/data_flow_7004 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_85 :: latest log:connector_heartbeat@evidence_16 2026-07-28T05:57:08+00:00
- search_service/search_2126 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_85 :: latest log:index_query_completed@evidence_16 2026-07-28T05:56:33+00:00

## case_170 -> COMPLETE (subject user_168)
- intent: DELETION via gemini
- account_service/account_665 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_85 :: latest log:profile_lookup_completed@evidence_16 2026-07-28T05:59:04+00:00
- analytics_platform/analytics_6980 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_85 :: latest log:analytics_profile_read@evidence_16 2026-07-28T05:54:16+00:00
- security_service/audit_record_4443 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_85 :: latest log:audit_record_read_completed@evidence_16 2026-07-28T05:55:46+00:00

## case_171 -> INCOMPLETE (subject user_169)
- intent: DELETION via gemini
- account_service/account_7947 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_17 :: latest log:profile_lookup_completed@evidence_16 2026-07-28T05:51:21+00:00
- security_service/audit_record_1665 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_16 2026-07-28T05:54:49+00:00
- backup_service/backup_5520 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=True ev=evidence_85 :: latest log:restore_candidate_evaluated@evidence_16 2026-07-28T05:56:08+00:00

## case_172 -> INCOMPLETE (subject user_170)
- intent: DELETION via gemini
- account_service/account_5675 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_17 :: latest log:profile_lookup_completed@evidence_16 2026-07-28T05:55:47+00:00
- security_service/audit_record_6136 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_16 2026-07-28T05:56:14+00:00
- search_service/search_7102 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_85 :: latest log:index_query_completed@evidence_16 2026-07-28T05:53:25+00:00
- support_platform/support_2322 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_85 :: latest log:message_pii_scan@evidence_16 2026-07-28T05:51:41+00:00

## case_173 -> INCOMPLETE (subject user_171)
- intent: DELETION via gemini
- account_service/account_6554 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_84 :: scope-absence evidence_84
- analytics_platform/analytics_6000 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- security_service/audit_record_4126 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- search_service/search_9523 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00

## case_174 -> INCOMPLETE (subject user_172)
- intent: DELETION via gemini
- account_service/account_6659 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_84 :: scope-absence evidence_84
- security_service/audit_record_7011 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- search_service/search_2138 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- support_platform/support_1887 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00

## case_175 -> COMPLETE (subject user_173)
- intent: DELETION via gemini
- account_service/account_246 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_84 :: scope-absence evidence_84
- analytics_platform/analytics_9505 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- security_service/audit_record_7166 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- backup_service/backup_549 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- integration_service/data_flow_4319 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- support_platform/support_8164 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00

## case_176 -> INCOMPLETE (subject user_174)
- intent: DELETION via gemini
- account_service/account_9877 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_84 :: scope-absence evidence_84
- security_service/audit_record_1222 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- integration_service/data_flow_296 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- search_service/search_8860 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00

## case_177 -> INCOMPLETE (subject user_175)
- intent: DELETION via gemini
- account_service/account_8423 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- security_service/audit_record_6729 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- search_service/search_3038 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00

## case_178 -> COMPLETE (subject user_176)
- intent: DELETION via gemini
- account_service/account_1090 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_84 :: scope-absence evidence_84
- analytics_platform/analytics_2414 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- security_service/audit_record_8521 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00

## case_179 -> INCOMPLETE (subject user_177)
- intent: DELETION via gemini
- account_service/account_3482 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_84 :: scope-absence evidence_84
- security_service/audit_record_919 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- support_platform/support_2283 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00

## case_180 -> INCOMPLETE (subject user_178)
- intent: DELETION via gemini
- account_service/account_9876 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_84 :: scope-absence evidence_84
- analytics_platform/analytics_1391 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- security_service/audit_record_2207 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- export_service/export_7156 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- search_service/search_5570 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- support_platform/support_2609 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00

## case_181 -> INCOMPLETE (subject user_179)
- intent: DELETION via gemini
- account_service/account_5309 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_84 :: scope-absence evidence_84
- security_service/audit_record_3625 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- integration_service/data_flow_8346 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- search_service/search_4894 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00

## case_182 -> INCOMPLETE (subject user_180)
- intent: DELETION via gemini
- account_service/account_2322 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_84 :: scope-absence evidence_84
- analytics_platform/analytics_1522 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- security_service/audit_record_8354 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- integration_service/data_flow_7450 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- search_service/search_2073 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00
- support_platform/support_4806 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_84 :: latest json:bundle@evidence_17 2026-07-23T12:00:00+00:00

## case_183 -> COMPLETE (subject user_181)
- intent: DELETION via gemini
- account_service/account_4854 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T09:33:26+00:00
- security_service/audit_record_3262 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T08:12:52+00:00

## case_184 -> INCOMPLETE (subject user_182)
- intent: DELETION via gemini
- account_service/account_9620 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- search_service/search_8680 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T08:15:33+00:00
- support_platform/support_1892 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T10:24:35+00:00

## case_185 -> INCOMPLETE (subject user_183)
- intent: DELETION via gemini
- account_service/account_9579 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- analytics_platform/analytics_1950 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T08:42:46+00:00
- search_service/search_8463 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T08:38:52+00:00

## case_186 -> INCOMPLETE (subject user_184)
- intent: DELETION via gemini
- account_service/account_3878 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- integration_service/data_flow_7428 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T09:57:31+00:00
- search_service/search_4062 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T08:22:10+00:00

## case_187 -> INCOMPLETE (subject user_185)
- intent: DELETION via gemini
- account_service/account_5375 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T10:24:53+00:00
- search_service/search_9921 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T09:54:37+00:00

## case_188 -> INCOMPLETE (subject user_186)
- intent: DELETION via gemini
- account_service/account_796 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- integration_service/data_flow_707 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T10:25:35+00:00
- search_service/search_3223 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T09:40:08+00:00

## case_189 -> INCOMPLETE (subject user_187)
- intent: DELETION via gemini
- account_service/account_5848 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T08:26:21+00:00
- analytics_platform/analytics_1120 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T08:18:22+00:00
- search_service/search_4334 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T08:47:12+00:00
- support_platform/support_8447 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T09:10:21+00:00

## case_190 -> COMPLETE (subject user_188)
- intent: DELETION via gemini
- account_service/account_7063 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T10:12:32+00:00
- analytics_platform/analytics_8767 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T09:25:51+00:00
- security_service/audit_record_4417 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T08:21:37+00:00

## case_191 -> COMPLETE (subject user_189)
- intent: DELETION via gemini
- account_service/account_9317 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T10:02:15+00:00
- analytics_platform/analytics_5614 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T08:44:27+00:00
- security_service/audit_record_7493 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T09:12:12+00:00
- backup_service/backup_3010 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T09:01:16+00:00
- integration_service/data_flow_1611 [DATA_FLOW->DISABLE] present=True direct=False ref=True flow=False restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T09:03:09+00:00
- support_platform/support_5049 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T10:43:35+00:00

## case_192 -> INCOMPLETE (subject user_190)
- intent: DELETION via gemini
- account_service/account_6608 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- analytics_platform/analytics_4472 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T10:03:39+00:00
- export_service/export_2705 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T07:49:26+00:00
- search_service/search_6680 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T08:42:44+00:00
- support_platform/support_5493 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_83 :: latest json:export@evidence_83 2026-07-18T09:57:11+00:00

## case_193 -> COMPLETE (subject user_191)
- intent: DELETION via gemini
- account_service/account_1065 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_82 :: latest log:profile_lookup_completed@evidence_82 2026-07-13T08:08:21+00:00
- analytics_platform/analytics_8037 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_82 :: latest log:analytics_profile_read_completed@evidence_82 2026-07-13T08:58:47+00:00
- security_service/audit_record_1839 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_82 :: latest log:audit_record_read_completed@evidence_82 2026-07-13T08:41:11+00:00

## case_194 -> INCOMPLETE (subject user_192)
- intent: DELETION via gemini
- account_service/account_660 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- integration_service/data_flow_3195 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_82 :: latest log:connector_config_read_completed@evidence_82 2026-07-13T07:25:54+00:00
- search_service/search_8302 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_82 :: latest log:index_query_completed@evidence_82 2026-07-13T08:03:45+00:00

## case_195 -> COMPLETE (subject user_193)
- intent: DELETION via gemini
- account_service/account_4320 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_82 :: latest log:profile_lookup_completed@evidence_82 2026-07-13T06:53:09+00:00
- analytics_platform/analytics_3454 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_82 :: latest log:analytics_profile_read_completed@evidence_82 2026-07-13T08:27:15+00:00
- security_service/audit_record_1524 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_82 :: latest log:audit_record_read_completed@evidence_82 2026-07-13T07:05:05+00:00

## case_196 -> COMPLETE (subject user_194)
- intent: DELETION via gemini
- account_service/account_5599 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_82 :: latest log:profile_lookup_completed@evidence_82 2026-07-13T07:20:27+00:00
- analytics_platform/analytics_5166 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_82 :: latest log:analytics_profile_read_completed@evidence_82 2026-07-13T07:14:06+00:00
- security_service/audit_record_6389 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_82 :: latest log:audit_record_read_completed@evidence_82 2026-07-13T08:28:57+00:00

## case_197 -> INCOMPLETE (subject user_195)
- intent: DELETION via gemini
- account_service/account_2952 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- analytics_platform/analytics_6093 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_82 :: latest log:analytics_profile_read_completed@evidence_82 2026-07-13T07:52:45+00:00
- search_service/search_6762 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_82 :: latest log:index_query_completed@evidence_82 2026-07-13T07:57:23+00:00

## case_198 -> INCOMPLETE (subject user_196)
- intent: DELETION via gemini
- account_service/account_2210 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- search_service/search_1414 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_82 :: latest log:index_query_completed@evidence_82 2026-07-13T09:10:03+00:00
- support_platform/support_6131 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_82 :: latest log:support_ticket_read_completed@evidence_82 2026-07-13T09:13:20+00:00

## case_199 -> INCOMPLETE (subject user_197)
- intent: DELETION via gemini
- account_service/account_9917 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_82 :: latest log:profile_lookup_completed@evidence_82 2026-07-13T09:20:12+00:00
- search_service/search_9161 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_82 :: latest log:index_query_completed@evidence_82 2026-07-13T07:39:16+00:00

## case_200 -> INCOMPLETE (subject user_198)
- intent: DELETION via gemini
- account_service/account_1964 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- integration_service/data_flow_2310 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_82 :: latest log:connector_config_read_completed@evidence_82 2026-07-13T07:13:44+00:00
- search_service/search_7472 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_82 :: latest log:index_query_completed@evidence_82 2026-07-13T07:24:22+00:00

## case_201 -> INCOMPLETE (subject user_199)
- intent: DELETION via gemini
- account_service/account_2933 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_82 :: latest log:profile_lookup_completed@evidence_82 2026-07-13T06:48:43+00:00
- integration_service/data_flow_5688 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_82 :: latest log:connector_config_read_completed@evidence_82 2026-07-13T09:33:59+00:00
- search_service/search_5135 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_82 :: latest log:index_query_completed@evidence_82 2026-07-13T08:12:10+00:00
- support_platform/support_2863 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_82 :: latest log:support_ticket_read_completed@evidence_82 2026-07-13T09:09:52+00:00

## case_202 -> COMPLETE (subject user_200)
- intent: DELETION via gemini
- account_service/account_5547 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_82 :: latest log:profile_lookup_completed@evidence_82 2026-07-13T07:43:22+00:00
- analytics_platform/analytics_349 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_82 :: latest log:analytics_profile_read_completed@evidence_82 2026-07-13T09:08:17+00:00
- security_service/audit_record_5401 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_82 :: latest log:audit_record_read_completed@evidence_82 2026-07-13T08:23:17+00:00

## case_203 -> INCOMPLETE (subject user_201)
- intent: DELETION via gemini
- account_service/account_2399 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- security_service/audit_record_1159 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- search_service/search_7542 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- support_platform/support_8903 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00

## case_204 -> COMPLETE (subject user_202)
- intent: DELETION via gemini
- account_service/account_9268 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- analytics_platform/analytics_2463 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- security_service/audit_record_2736 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- backup_service/backup_9519 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- integration_service/data_flow_5877 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- support_platform/support_9505 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00

## case_205 -> INCOMPLETE (subject user_203)
- intent: DELETION via gemini
- account_service/account_6726 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- security_service/audit_record_5023 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- integration_service/data_flow_3530 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- search_service/search_540 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00

## case_206 -> COMPLETE (subject user_204)
- intent: DELETION via gemini
- account_service/account_4522 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- analytics_platform/analytics_9580 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- security_service/audit_record_9878 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00

## case_207 -> INCOMPLETE (subject user_205)
- intent: DELETION via gemini
- account_service/account_5678 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- security_service/audit_record_3578 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- backup_service/backup_6407 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00

## case_208 -> INCOMPLETE (subject user_206)
- intent: DELETION via gemini
- account_service/account_3685 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- security_service/audit_record_2697 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- search_service/search_1118 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- support_platform/support_2134 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00

## case_209 -> INCOMPLETE (subject user_207)
- intent: DELETION via gemini
- account_service/account_6934 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- analytics_platform/analytics_3156 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- security_service/audit_record_8189 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- integration_service/data_flow_5196 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- search_service/search_7288 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- support_platform/support_8999 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00

## case_210 -> INCOMPLETE (subject user_208)
- intent: DELETION via gemini
- account_service/account_4362 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- security_service/audit_record_6796 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- search_service/search_045 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- support_platform/support_4491 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00

## case_211 -> INCOMPLETE (subject user_209)
- intent: DELETION via gemini
- account_service/account_4348 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- security_service/audit_record_7804 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- search_service/search_9955 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00

## case_212 -> INCOMPLETE (subject user_210)
- intent: DELETION via gemini
- account_service/account_418 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_20 :: scope-absence evidence_20
- security_service/audit_record_3261 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- integration_service/data_flow_8676 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00
- search_service/search_2274 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_20 :: latest sql:customer_data_read_replica@evidence_20 2026-07-08T09:00:00+00:00

## case_213 -> COMPLETE (subject user_211)
- intent: DELETION via gemini
- account_service/account_6674 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:profile_lookup_completed@evidence_21 2026-07-03T07:58:36+00:00
- analytics_platform/analytics_4460 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:analytics_profile_read@evidence_21 2026-07-03T07:55:32+00:00
- security_service/audit_record_4413 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:audit_record_read_completed@evidence_21 2026-07-03T07:51:32+00:00
- backup_service/backup_5626 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=False ev=evidence_81 :: latest log:restore_authorization_completed@evidence_21 2026-07-03T07:57:07+00:00
- integration_service/data_flow_5279 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_81 :: latest log:connector_config_loaded@evidence_21 2026-07-03T07:59:22+00:00
- support_platform/support_1360 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:message_read@evidence_21 2026-07-03T07:58:41+00:00

## case_214 -> INCOMPLETE (subject user_212)
- intent: DELETION via gemini
- account_service/account_4752 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:profile_lookup_completed@evidence_21 2026-07-03T07:59:34+00:00
- security_service/audit_record_1666 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_21 2026-07-03T07:58:45+00:00
- search_service/search_7351 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:index_query_completed@evidence_21 2026-07-03T07:57:49+00:00
- support_platform/support_1146 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_81 :: latest log:message_pii_scan@evidence_21 2026-07-03T07:56:58+00:00

## case_215 -> COMPLETE (subject user_213)
- intent: DELETION via gemini
- account_service/account_1956 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:profile_lookup_completed@evidence_21 2026-07-03T07:54:47+00:00
- analytics_platform/analytics_2504 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:analytics_profile_read@evidence_21 2026-07-03T07:56:28+00:00
- security_service/audit_record_1718 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:audit_record_read_completed@evidence_21 2026-07-03T07:52:02+00:00

## case_216 -> INCOMPLETE (subject user_214)
- intent: DELETION via gemini
- account_service/account_9682 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:profile_lookup_completed@evidence_21 2026-07-03T07:52:31+00:00
- analytics_platform/analytics_4527 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_81 :: latest log:analytics_identity_scan@evidence_21 2026-07-03T07:59:41+00:00
- security_service/audit_record_713 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_21 2026-07-03T07:56:03+00:00
- export_service/export_5351 [USER_EXPORT->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:export_download_check_completed@evidence_21 2026-07-03T07:54:16+00:00
- search_service/search_5216 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:index_query_completed@evidence_21 2026-07-03T07:57:20+00:00
- support_platform/support_8453 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_81 :: latest log:message_pii_scan@evidence_21 2026-07-03T07:58:45+00:00

## case_217 -> INCOMPLETE (subject user_215)
- intent: DELETION via gemini
- account_service/account_7030 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:profile_lookup_completed@evidence_21 2026-07-03T07:59:04+00:00
- security_service/audit_record_188 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_21 2026-07-03T07:54:57+00:00
- integration_service/data_flow_1791 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_81 :: latest log:connector_heartbeat@evidence_21 2026-07-03T07:55:35+00:00
- search_service/search_3120 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:index_query_completed@evidence_21 2026-07-03T07:55:06+00:00

## case_218 -> COMPLETE (subject user_216)
- intent: DELETION via gemini
- account_service/account_4066 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:profile_lookup_completed@evidence_21 2026-07-03T07:58:08+00:00
- analytics_platform/analytics_257 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:analytics_profile_read@evidence_21 2026-07-03T07:51:59+00:00
- security_service/audit_record_8792 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:audit_record_read_completed@evidence_21 2026-07-03T07:57:40+00:00

## case_219 -> COMPLETE (subject user_217)
- intent: DELETION via gemini
- account_service/account_4678 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:profile_lookup_completed@evidence_21 2026-07-03T07:59:11+00:00
- analytics_platform/analytics_7004 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:analytics_profile_read@evidence_21 2026-07-03T07:56:02+00:00
- security_service/audit_record_3382 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:audit_record_read_completed@evidence_21 2026-07-03T07:58:42+00:00

## case_220 -> INCOMPLETE (subject user_218)
- intent: DELETION via gemini
- account_service/account_1007 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:profile_lookup_completed@evidence_21 2026-07-03T07:57:30+00:00
- security_service/audit_record_3698 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_21 2026-07-03T07:55:56+00:00
- legal_service/legal_hold_4961 [LEGAL_HOLD_RECORD->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:retained_order_loaded@evidence_21 2026-07-03T07:57:01+00:00
- search_service/search_941 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:index_query_completed@evidence_21 2026-07-03T07:57:58+00:00
- support_platform/support_4529 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_81 :: latest log:message_pii_scan@evidence_21 2026-07-03T07:56:33+00:00

## case_221 -> COMPLETE (subject user_219)
- intent: DELETION via gemini
- account_service/account_4512 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:profile_lookup_completed@evidence_21 2026-07-03T07:52:15+00:00
- security_service/audit_record_3880 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:audit_record_read_completed@evidence_21 2026-07-03T07:56:08+00:00

## case_222 -> INCOMPLETE (subject user_220)
- intent: DELETION via gemini
- account_service/account_7237 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:profile_lookup_completed@evidence_21 2026-07-03T07:58:33+00:00
- security_service/audit_record_7211 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_21 2026-07-03T07:56:59+00:00
- search_service/search_6405 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_81 :: latest log:index_query_completed@evidence_21 2026-07-03T07:57:29+00:00
- support_platform/support_111 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_81 :: latest log:message_pii_scan@evidence_21 2026-07-03T07:55:58+00:00

## case_223 -> INCOMPLETE (subject user_221)
- intent: DELETION via gemini
- account_service/account_5479 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- security_service/audit_record_234 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- search_service/search_8764 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00

## case_224 -> INCOMPLETE (subject user_222)
- intent: DELETION via gemini
- account_service/account_669 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_80 :: latest json:export@evidence_80 2026-06-28T05:35:02+00:00
- analytics_platform/analytics_2501 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- security_service/audit_record_6515 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- integration_service/data_flow_1140 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00

## case_225 -> COMPLETE (subject user_223)
- intent: DELETION via gemini
- account_service/account_392 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_80 :: latest json:export@evidence_80 2026-06-28T05:40:45+00:00
- analytics_platform/analytics_8127 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- security_service/audit_record_9389 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00

## case_226 -> COMPLETE (subject user_224)
- intent: DELETION via gemini
- account_service/account_7605 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: scope-absence evidence_78
- security_service/audit_record_9964 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00

## case_227 -> INCOMPLETE (subject user_225)
- intent: DELETION via gemini
- account_service/account_5549 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: scope-absence evidence_78
- security_service/audit_record_9043 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- search_service/search_8181 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- support_platform/support_5830 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00

## case_228 -> INCOMPLETE (subject user_226)
- intent: DELETION via gemini
- account_service/account_7146 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: scope-absence evidence_78
- security_service/audit_record_5029 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- export_service/export_3210 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- search_service/search_7054 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00

## case_229 -> INCOMPLETE (subject user_227)
- intent: DELETION via gemini
- account_service/account_4552 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: scope-absence evidence_78
- security_service/audit_record_4310 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- integration_service/data_flow_5831 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- search_service/search_3627 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00

## case_230 -> INCOMPLETE (subject user_228)
- intent: DELETION via gemini
- account_service/account_8165 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: scope-absence evidence_78
- security_service/audit_record_7027 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- integration_service/data_flow_2516 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- search_service/search_5612 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00

## case_231 -> COMPLETE (subject user_229)
- intent: DELETION via gemini
- account_service/account_7324 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_80 :: latest json:export@evidence_80 2026-06-28T06:25:56+00:00
- analytics_platform/analytics_1544 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- security_service/audit_record_4425 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- backup_service/backup_6564 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- integration_service/data_flow_2576 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- support_platform/support_3964 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00

## case_232 -> INCOMPLETE (subject user_230)
- intent: DELETION via gemini
- account_service/account_8936 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: scope-absence evidence_78
- security_service/audit_record_7757 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00
- support_platform/support_9862 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_80 :: latest json:bundle@evidence_22 2026-06-28T07:00:00+00:00

## case_233 -> COMPLETE (subject user_231)
- intent: DELETION via gemini
- account_service/account_5264 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- analytics_platform/analytics_6723 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- security_service/audit_record_8350 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- backup_service/backup_8162 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=False ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- integration_service/data_flow_6754 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- support_platform/support_9670 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00

## case_234 -> INCOMPLETE (subject user_232)
- intent: DELETION via gemini
- account_service/account_2614 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- security_service/audit_record_4438 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- search_service/search_2615 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- support_platform/support_1254 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00

## case_235 -> COMPLETE (subject user_233)
- intent: DELETION via gemini
- account_service/account_886 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- analytics_platform/analytics_8565 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- security_service/audit_record_7103 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- backup_service/backup_2775 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=False ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- integration_service/data_flow_593 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- support_platform/support_9391 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00

## case_236 -> INCOMPLETE (subject user_234)
- intent: DELETION via gemini
- account_service/account_629 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- security_service/audit_record_9285 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- integration_service/data_flow_7352 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- search_service/search_5385 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00

## case_237 -> INCOMPLETE (subject user_235)
- intent: DELETION via gemini
- account_service/account_2788 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- security_service/audit_record_2859 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- search_service/search_2433 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00

## case_238 -> COMPLETE (subject user_236)
- intent: DELETION via gemini
- account_service/account_945 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- security_service/audit_record_6797 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00

## case_239 -> COMPLETE (subject user_237)
- intent: DELETION via gemini
- account_service/account_2838 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- analytics_platform/analytics_1964 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- security_service/audit_record_4940 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00

## case_240 -> INCOMPLETE (subject user_238)
- intent: DELETION via gemini
- account_service/account_6013 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- security_service/audit_record_8918 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- export_service/export_5242 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- search_service/search_9335 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00

## case_241 -> INCOMPLETE (subject user_239)
- intent: DELETION via gemini
- account_service/account_1789 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- security_service/audit_record_436 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- integration_service/data_flow_4568 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- search_service/search_5659 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00

## case_242 -> INCOMPLETE (subject user_240)
- intent: DELETION via gemini
- account_service/account_3905 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- security_service/audit_record_3046 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- integration_service/data_flow_4475 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00
- search_service/search_2904 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_79 :: latest json:history@evidence_22 2026-06-23T06:00:00+00:00

## case_243 -> COMPLETE (subject user_241)
- intent: DELETION via gemini
- account_service/account_7650 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: scope-absence evidence_78
- analytics_platform/analytics_5891 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_78 :: latest sql:customer_analytics_profiles@evidence_78 2026-06-18T11:44:03+00:00
- security_service/audit_record_7202 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_78 :: latest sql:security_audit_records@evidence_78 2026-06-18T11:44:03+00:00

## case_244 -> COMPLETE (subject user_242)
- intent: DELETION via gemini
- account_service/account_4264 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: scope-absence evidence_78
- analytics_platform/analytics_9166 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_78 :: latest sql:customer_analytics_profiles@evidence_78 2026-06-18T11:44:03+00:00
- security_service/audit_record_9314 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_78 :: latest sql:security_audit_records@evidence_78 2026-06-18T11:44:03+00:00

## case_245 -> INCOMPLETE (subject user_243)
- intent: DELETION via gemini
- account_service/account_1264 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: scope-absence evidence_78
- analytics_platform/analytics_4010 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_78 :: latest sql:customer_analytics_profiles@evidence_78 2026-06-18T11:44:03+00:00

## case_246 -> INCOMPLETE (subject user_244)
- intent: DELETION via gemini
- account_service/account_2481 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: scope-absence evidence_78
- search_service/search_2725 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_78 :: latest sql:customer_search_documents@evidence_78 2026-06-18T11:44:03+00:00
- support_platform/support_579 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_78 :: latest sql:support_records@evidence_78 2026-06-18T11:44:03+00:00

## case_247 -> INCOMPLETE (subject user_245)
- intent: DELETION via gemini
- account_service/account_2981 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_78 :: latest sql:customer_profiles@evidence_78 2026-06-18T11:44:03+00:00
- search_service/search_9473 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_78 :: latest sql:customer_search_documents@evidence_78 2026-06-18T11:44:03+00:00

## case_248 -> INCOMPLETE (subject user_246)
- intent: DELETION via gemini
- account_service/account_3631 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: scope-absence evidence_78
- integration_service/data_flow_677 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_78 :: latest sql:connector_subscriptions@evidence_78 2026-06-18T11:44:03+00:00

## case_249 -> INCOMPLETE (subject user_247)
- intent: DELETION via gemini
- account_service/account_4181 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_78 :: latest sql:customer_profiles@evidence_78 2026-06-18T11:44:03+00:00
- analytics_platform/analytics_8527 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_78 :: latest sql:customer_analytics_profiles@evidence_78 2026-06-18T11:44:03+00:00
- search_service/search_8190 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_78 :: latest sql:customer_search_documents@evidence_78 2026-06-18T11:44:03+00:00
- support_platform/support_1364 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_78 :: latest sql:support_records@evidence_78 2026-06-18T11:44:03+00:00

## case_250 -> INCOMPLETE (subject user_248)
- intent: DELETION via gemini
- account_service/account_7010 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: scope-absence evidence_78
- search_service/search_3760 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_78 :: latest sql:customer_search_documents@evidence_78 2026-06-18T11:44:03+00:00

## case_251 -> INCOMPLETE (subject user_249)
- intent: DELETION via gemini
- account_service/account_7518 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: scope-absence evidence_78
- search_service/search_730 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_78 :: latest sql:customer_search_documents@evidence_78 2026-06-18T11:44:03+00:00
- support_platform/support_4541 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_78 :: latest sql:support_records@evidence_78 2026-06-18T11:44:03+00:00

## case_252 -> INCOMPLETE (subject user_250)
- intent: DELETION via gemini
- account_service/account_4643 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_78 :: scope-absence evidence_78
- export_service/export_8598 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_78 :: latest sql:customer_exports@evidence_78 2026-06-18T11:44:03+00:00
- search_service/search_2936 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_78 :: latest sql:customer_search_documents@evidence_78 2026-06-18T11:44:03+00:00

## case_253 -> COMPLETE (subject user_251)
- intent: DELETION via gemini
- account_service/account_6073 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_24 :: scope-absence evidence_24
- analytics_platform/analytics_6136 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00
- security_service/audit_record_2927 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00

## case_254 -> INCOMPLETE (subject user_252)
- intent: DELETION via gemini
- account_service/account_5047 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_24 :: scope-absence evidence_24
- security_service/audit_record_9256 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00
- integration_service/data_flow_6233 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00
- search_service/search_3011 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00

## case_255 -> INCOMPLETE (subject user_253)
- intent: DELETION via gemini
- account_service/account_5091 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_24 :: scope-absence evidence_24
- security_service/audit_record_2513 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00
- backup_service/backup_2427 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00

## case_256 -> INCOMPLETE (subject user_254)
- intent: DELETION via gemini
- account_service/account_7542 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_24 :: scope-absence evidence_24
- security_service/audit_record_2453 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00
- search_service/search_4027 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00
- support_platform/support_3772 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00

## case_257 -> COMPLETE (subject user_255)
- intent: DELETION via gemini
- account_service/account_3601 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_24 :: scope-absence evidence_24
- analytics_platform/analytics_2977 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00
- security_service/audit_record_7193 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00

## case_258 -> INCOMPLETE (subject user_256)
- intent: DELETION via gemini
- account_service/account_7942 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_24 :: scope-absence evidence_24
- security_service/audit_record_9890 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00
- search_service/search_5296 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00
- support_platform/support_3834 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00

## case_259 -> INCOMPLETE (subject user_257)
- intent: DELETION via gemini
- account_service/account_9608 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00
- security_service/audit_record_1421 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00
- search_service/search_6990 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00

## case_260 -> COMPLETE (subject user_258)
- intent: DELETION via gemini
- account_service/account_7811 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_24 :: scope-absence evidence_24
- analytics_platform/analytics_5053 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00
- security_service/audit_record_1876 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00

## case_261 -> INCOMPLETE (subject user_259)
- intent: DELETION via gemini
- account_service/account_3150 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00
- security_service/audit_record_3335 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00
- legal_service/legal_hold_8017 [LEGAL_HOLD_RECORD->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00
- search_service/search_6781 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00

## case_262 -> INCOMPLETE (subject user_260)
- intent: DELETION via gemini
- account_service/account_5072 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_24 :: scope-absence evidence_24
- security_service/audit_record_4812 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00
- search_service/search_2228 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_24 :: latest sql:customer_data_read_replica@evidence_24 2026-06-13T11:00:00+00:00

## case_263 -> INCOMPLETE (subject user_261)
- intent: DELETION via gemini
- account_service/account_106 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:profile_lookup_completed@evidence_25 2026-06-08T09:55:47+00:00
- analytics_platform/analytics_515 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_25 :: latest log:analytics_identity_scan@evidence_25 2026-06-08T09:52:44+00:00
- security_service/audit_record_6863 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:audit_record_read_completed@evidence_25 2026-06-08T09:57:22+00:00
- search_service/search_5331 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:index_query_completed@evidence_25 2026-06-08T09:53:34+00:00
- support_platform/support_2498 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_25 :: latest log:message_pii_scan@evidence_25 2026-06-08T09:51:04+00:00
- support_platform/support_5234 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_25 :: latest log:attachment_pii_scan@evidence_25 2026-06-08T09:54:59+00:00

## case_264 -> COMPLETE (subject user_262)
- intent: DELETION via gemini
- account_service/account_8316 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:profile_lookup_completed@evidence_25 2026-06-08T09:56:01+00:00
- analytics_platform/analytics_1851 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:analytics_profile_read@evidence_25 2026-06-08T09:58:28+00:00
- security_service/audit_record_6711 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:audit_record_read_completed@evidence_25 2026-06-08T09:55:35+00:00
- backup_service/backup_3250 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=False ev=evidence_25 :: latest log:restore_authorization_completed@evidence_25 2026-06-08T09:55:17+00:00
- integration_service/data_flow_4885 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_25 :: latest log:connector_config_loaded@evidence_25 2026-06-08T09:55:58+00:00
- support_platform/support_9996 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:message_read@evidence_25 2026-06-08T09:51:47+00:00

## case_265 -> COMPLETE (subject user_263)
- intent: DELETION via gemini
- account_service/account_5015 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:profile_lookup_completed@evidence_25 2026-06-08T09:53:46+00:00
- security_service/audit_record_6378 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:audit_record_read_completed@evidence_25 2026-06-08T09:52:24+00:00

## case_266 -> INCOMPLETE (subject user_264)
- intent: DELETION via gemini
- account_service/account_1057 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:profile_lookup_completed@evidence_25 2026-06-08T09:54:50+00:00
- security_service/audit_record_1857 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:audit_record_read_completed@evidence_25 2026-06-08T09:55:29+00:00
- integration_service/data_flow_8277 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_25 :: latest log:connector_heartbeat@evidence_25 2026-06-08T09:56:18+00:00
- search_service/search_8935 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:index_query_completed@evidence_25 2026-06-08T09:53:26+00:00

## case_267 -> COMPLETE (subject user_265)
- intent: DELETION via gemini
- account_service/account_8384 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:profile_lookup_completed@evidence_25 2026-06-08T09:51:52+00:00
- analytics_platform/analytics_3793 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:analytics_profile_read@evidence_25 2026-06-08T09:57:17+00:00
- security_service/audit_record_6621 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:audit_record_read_completed@evidence_25 2026-06-08T09:52:27+00:00

## case_268 -> INCOMPLETE (subject user_266)
- intent: DELETION via gemini
- account_service/account_9179 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:profile_lookup_completed@evidence_25 2026-06-08T09:53:34+00:00
- security_service/audit_record_4636 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:audit_record_read_completed@evidence_25 2026-06-08T09:54:19+00:00
- search_service/search_3000 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:index_query_completed@evidence_25 2026-06-08T09:53:44+00:00
- support_platform/support_8215 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_25 :: latest log:message_pii_scan@evidence_25 2026-06-08T09:55:05+00:00

## case_269 -> INCOMPLETE (subject user_267)
- intent: DELETION via gemini
- account_service/account_7699 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:profile_lookup_completed@evidence_25 2026-06-08T09:52:10+00:00
- analytics_platform/analytics_6766 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_25 :: latest log:analytics_identity_scan@evidence_25 2026-06-08T09:53:39+00:00
- security_service/audit_record_4534 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:audit_record_read_completed@evidence_25 2026-06-08T09:56:14+00:00
- integration_service/data_flow_8612 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_25 :: latest log:connector_heartbeat@evidence_25 2026-06-08T09:55:04+00:00
- search_service/search_1730 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:index_query_completed@evidence_25 2026-06-08T09:54:05+00:00
- support_platform/support_8301 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_25 :: latest log:message_pii_scan@evidence_25 2026-06-08T09:55:52+00:00

## case_270 -> INCOMPLETE (subject user_268)
- intent: DELETION via gemini
- account_service/account_4331 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:profile_lookup_completed@evidence_25 2026-06-08T09:51:35+00:00
- security_service/audit_record_5206 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:audit_record_read_completed@evidence_25 2026-06-08T09:57:14+00:00
- search_service/search_9020 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:index_query_completed@evidence_25 2026-06-08T09:52:29+00:00
- support_platform/support_7707 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_25 :: latest log:message_pii_scan@evidence_25 2026-06-08T09:57:11+00:00

## case_271 -> INCOMPLETE (subject user_269)
- intent: DELETION via gemini
- account_service/account_7107 [USER_PROFILE->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:profile_lookup_completed@evidence_25 2026-06-08T09:51:49+00:00
- security_service/audit_record_2546 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:audit_record_read_completed@evidence_25 2026-06-08T09:57:40+00:00
- search_service/search_1390 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:index_query_completed@evidence_25 2026-06-08T09:52:31+00:00

## case_272 -> INCOMPLETE (subject user_270)
- intent: DELETION via gemini
- account_service/account_4226 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:profile_lookup_completed@evidence_25 2026-06-08T09:53:48+00:00
- security_service/audit_record_4646 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:audit_record_read_completed@evidence_25 2026-06-08T09:57:07+00:00
- integration_service/data_flow_2010 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_25 :: latest log:connector_heartbeat@evidence_25 2026-06-08T09:51:18+00:00
- search_service/search_3875 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_25 :: latest log:index_query_completed@evidence_25 2026-06-08T09:56:27+00:00

## case_273 -> INCOMPLETE (subject user_271)
- intent: DELETION via gemini
- account_service/account_8689 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- security_service/audit_record_3428 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- legal_service/legal_hold_1745 [LEGAL_HOLD_RECORD->RETAIN] present=False direct=False ref=False flow=None restore=None ev=evidence_40 :: scope-absence evidence_40
- search_service/search_5454 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00

## case_274 -> COMPLETE (subject user_272)
- intent: DELETION via gemini
- account_service/account_6575 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_77 :: latest json:export@evidence_77 2026-06-03T08:09:19+00:00
- analytics_platform/analytics_4051 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- security_service/audit_record_6398 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00

## case_275 -> INCOMPLETE (subject user_273)
- intent: DELETION via gemini
- account_service/account_2352 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- security_service/audit_record_4188 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- search_service/search_5264 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- support_platform/support_3684 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00

## case_276 -> COMPLETE (subject user_274)
- intent: DELETION via gemini
- account_service/account_4853 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_77 :: latest json:export@evidence_77 2026-06-03T08:02:40+00:00
- analytics_platform/analytics_5923 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- security_service/audit_record_8323 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00

## case_277 -> COMPLETE (subject user_275)
- intent: DELETION via gemini
- account_service/account_731 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_77 :: latest json:export@evidence_77 2026-06-03T06:44:31+00:00
- analytics_platform/analytics_6191 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- security_service/audit_record_8228 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- backup_service/backup_9728 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- integration_service/data_flow_2439 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- support_platform/support_2036 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00

## case_278 -> INCOMPLETE (subject user_276)
- intent: DELETION via gemini
- account_service/account_6306 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- analytics_platform/analytics_5959 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- security_service/audit_record_6384 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- integration_service/data_flow_4629 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- search_service/search_8082 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- support_platform/support_6333 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00

## case_279 -> INCOMPLETE (subject user_277)
- intent: DELETION via gemini
- account_service/account_4664 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- security_service/audit_record_5055 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- backup_service/backup_8588 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00

## case_280 -> INCOMPLETE (subject user_278)
- intent: DELETION via gemini
- account_service/account_2430 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- security_service/audit_record_1518 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- support_platform/support_7073 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00

## case_281 -> INCOMPLETE (subject user_279)
- intent: DELETION via gemini
- account_service/account_4985 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- analytics_platform/analytics_6265 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- security_service/audit_record_111 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- integration_service/data_flow_9008 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- search_service/search_3364 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- support_platform/support_2757 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00

## case_282 -> INCOMPLETE (subject user_280)
- intent: DELETION via gemini
- account_service/account_9763 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- security_service/audit_record_3198 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00
- support_platform/support_8370 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_77 :: latest json:bundle@evidence_26 2026-06-03T09:00:00+00:00

## case_283 -> COMPLETE (subject user_281)
- intent: DELETION via gemini
- account_service/account_947 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_76 :: latest log:profile_lookup_completed@evidence_76 2026-05-29T07:38:43+00:00
- analytics_platform/analytics_8408 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_76 :: latest log:analytics_profile_read_completed@evidence_76 2026-05-29T06:19:56+00:00
- security_service/audit_record_5680 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_76 :: latest log:audit_record_read_completed@evidence_76 2026-05-29T07:28:05+00:00

## case_284 -> INCOMPLETE (subject user_282)
- intent: DELETION via gemini
- account_service/account_8322 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- integration_service/data_flow_6953 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_76 :: latest log:connector_config_read_completed@evidence_76 2026-05-29T06:46:09+00:00

## case_285 -> INCOMPLETE (subject user_283)
- intent: DELETION via gemini
- account_service/account_285 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_76 :: latest log:profile_lookup_completed@evidence_76 2026-05-29T04:54:21+00:00
- search_service/search_036 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_76 :: latest log:index_query_completed@evidence_76 2026-05-29T06:39:38+00:00

## case_286 -> COMPLETE (subject user_284)
- intent: DELETION via gemini
- account_service/account_2016 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_76 :: latest log:profile_lookup_completed@evidence_76 2026-05-29T07:43:13+00:00
- analytics_platform/analytics_7283 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_76 :: latest log:analytics_profile_read_completed@evidence_76 2026-05-29T06:00:28+00:00
- security_service/audit_record_1714 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_76 :: latest log:audit_record_read_completed@evidence_76 2026-05-29T05:46:12+00:00

## case_287 -> INCOMPLETE (subject user_285)
- intent: DELETION via gemini
- account_service/account_4485 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- search_service/search_5705 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_76 :: latest log:index_query_completed@evidence_76 2026-05-29T06:50:34+00:00
- support_platform/support_7432 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_76 :: latest log:support_ticket_read_completed@evidence_76 2026-05-29T05:22:37+00:00

## case_288 -> INCOMPLETE (subject user_286)
- intent: DELETION via gemini
- account_service/account_6988 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- export_service/export_7906 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_76 :: latest log:export_metadata_read_completed@evidence_76 2026-05-29T05:49:15+00:00

## case_289 -> INCOMPLETE (subject user_287)
- intent: DELETION via gemini
- account_service/account_4232 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- integration_service/data_flow_743 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_76 :: latest log:connector_config_read_completed@evidence_76 2026-05-29T07:26:53+00:00
- search_service/search_6432 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_76 :: latest log:index_query_completed@evidence_76 2026-05-29T06:36:35+00:00

## case_290 -> INCOMPLETE (subject user_288)
- intent: DELETION via gemini
- account_service/account_7177 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- integration_service/data_flow_179 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_76 :: latest log:connector_config_read_completed@evidence_76 2026-05-29T05:42:55+00:00
- search_service/search_3144 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_76 :: latest log:index_query_completed@evidence_76 2026-05-29T05:26:36+00:00

## case_291 -> INCOMPLETE (subject user_289)
- intent: DELETION via gemini
- account_service/account_8914 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- backup_service/backup_7079 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_76 :: latest log:restore_policy_read_completed@evidence_76 2026-05-29T06:06:44+00:00

## case_292 -> COMPLETE (subject user_290)
- intent: DELETION via gemini
- account_service/account_1125 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_76 :: latest log:profile_lookup_completed@evidence_76 2026-05-29T07:10:16+00:00
- analytics_platform/analytics_2322 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_76 :: latest log:analytics_profile_read_completed@evidence_76 2026-05-29T06:03:36+00:00
- security_service/audit_record_3432 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_76 :: latest log:audit_record_read_completed@evidence_76 2026-05-29T06:48:53+00:00
- backup_service/backup_1825 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_76 :: latest log:restore_policy_read_completed@evidence_76 2026-05-29T05:36:24+00:00
- integration_service/data_flow_5598 [DATA_FLOW->DISABLE] present=True direct=False ref=True flow=False restore=None ev=evidence_76 :: latest log:connector_config_read_completed@evidence_76 2026-05-29T05:54:49+00:00
- support_platform/support_1526 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_76 :: latest log:support_ticket_read_completed@evidence_76 2026-05-29T07:37:13+00:00

## case_293 -> INCOMPLETE (subject user_291)
- intent: DELETION via gemini
- account_service/account_9091 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- analytics_platform/analytics_5854 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_75 :: latest sql:customer_analytics_profiles@evidence_75 2026-05-24T06:39:55+00:00

## case_294 -> COMPLETE (subject user_292)
- intent: DELETION via gemini
- account_service/account_6996 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- analytics_platform/analytics_096 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- security_service/audit_record_4387 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_75 :: latest sql:security_audit_records@evidence_75 2026-05-24T06:39:55+00:00

## case_295 -> COMPLETE (subject user_293)
- intent: DELETION via gemini
- account_service/account_8353 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- analytics_platform/analytics_3678 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- security_service/audit_record_1269 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_75 :: latest sql:security_audit_records@evidence_75 2026-05-24T06:39:55+00:00

## case_296 -> INCOMPLETE (subject user_294)
- intent: DELETION via gemini
- account_service/account_4267 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- integration_service/data_flow_085 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_75 :: latest sql:connector_subscriptions@evidence_75 2026-05-24T06:39:55+00:00
- search_service/search_9631 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_75 :: latest sql:customer_search_documents@evidence_75 2026-05-24T06:39:55+00:00

## case_297 -> COMPLETE (subject user_295)
- intent: DELETION via gemini
- account_service/account_6023 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- analytics_platform/analytics_7164 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_75 :: latest sql:customer_analytics_profiles@evidence_75 2026-05-24T06:39:55+00:00
- security_service/audit_record_7878 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_75 :: latest sql:security_audit_records@evidence_75 2026-05-24T06:39:55+00:00
- backup_service/backup_7308 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_75 :: latest sql:backup_restore_entries@evidence_75 2026-05-24T06:39:55+00:00
- integration_service/data_flow_3391 [DATA_FLOW->DISABLE] present=True direct=False ref=True flow=False restore=None ev=evidence_75 :: latest sql:connector_subscriptions@evidence_75 2026-05-24T06:39:55+00:00
- support_platform/support_1983 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_75 :: latest sql:support_records@evidence_75 2026-05-24T06:39:55+00:00

## case_298 -> INCOMPLETE (subject user_296)
- intent: DELETION via gemini
- account_service/account_4880 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- search_service/search_6282 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_75 :: latest sql:customer_search_documents@evidence_75 2026-05-24T06:39:55+00:00
- support_platform/support_643 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_75 :: latest sql:support_records@evidence_75 2026-05-24T06:39:55+00:00

## case_299 -> COMPLETE (subject user_297)
- intent: DELETION via gemini
- account_service/account_9993 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- analytics_platform/analytics_1733 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_75 :: latest sql:customer_analytics_profiles@evidence_75 2026-05-24T06:39:55+00:00
- security_service/audit_record_5194 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_75 :: latest sql:security_audit_records@evidence_75 2026-05-24T06:39:55+00:00

## case_300 -> INCOMPLETE (subject user_298)
- intent: DELETION via gemini
- account_service/account_7249 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- export_service/export_6623 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_75 :: latest sql:customer_exports@evidence_75 2026-05-24T06:39:55+00:00
- search_service/search_4299 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_75 :: latest sql:customer_search_documents@evidence_75 2026-05-24T06:39:55+00:00

## case_301 -> INCOMPLETE (subject user_299)
- intent: DELETION via gemini
- account_service/account_1618 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- integration_service/data_flow_4521 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_75 :: latest sql:connector_subscriptions@evidence_75 2026-05-24T06:39:55+00:00
- search_service/search_5268 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_75 :: latest sql:customer_search_documents@evidence_75 2026-05-24T06:39:55+00:00

## case_302 -> INCOMPLETE (subject user_300)
- intent: DELETION via gemini
- account_service/account_4835 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_75 :: scope-absence evidence_75
- analytics_platform/analytics_1133 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_75 :: latest sql:customer_analytics_profiles@evidence_75 2026-05-24T06:39:55+00:00
- integration_service/data_flow_7594 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_75 :: latest sql:connector_subscriptions@evidence_75 2026-05-24T06:39:55+00:00
- search_service/search_1033 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_75 :: latest sql:customer_search_documents@evidence_75 2026-05-24T06:39:55+00:00
- support_platform/support_2983 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_75 :: latest sql:support_records@evidence_75 2026-05-24T06:39:55+00:00

## case_303 -> INCOMPLETE (subject user_301)
- intent: DELETION via gemini
- account_service/account_7907 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_29 :: scope-absence evidence_29
- security_service/audit_record_7923 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- backup_service/backup_4935 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00

## case_304 -> COMPLETE (subject user_302)
- intent: DELETION via gemini
- account_service/account_4771 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_29 :: scope-absence evidence_29
- security_service/audit_record_4759 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00

## case_305 -> INCOMPLETE (subject user_303)
- intent: DELETION via gemini
- account_service/account_6680 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_29 :: scope-absence evidence_29
- analytics_platform/analytics_9285 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- security_service/audit_record_507 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- search_service/search_4321 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00

## case_306 -> INCOMPLETE (subject user_304)
- intent: DELETION via gemini
- account_service/account_7248 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_29 :: scope-absence evidence_29
- security_service/audit_record_9051 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- search_service/search_8250 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- support_platform/support_450 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00

## case_307 -> INCOMPLETE (subject user_305)
- intent: DELETION via gemini
- account_service/account_585 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_ap_south@evidence_29 2026-05-19T06:00:00+00:00
- security_service/audit_record_5129 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- search_service/search_7660 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00

## case_308 -> COMPLETE (subject user_306)
- intent: DELETION via gemini
- account_service/account_8647 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_29 :: scope-absence evidence_29
- analytics_platform/analytics_7575 [ANALYTICS_PROFILE->ANONYMIZE] present=False direct=False ref=False flow=None restore=None ev=evidence_29 :: scope-absence evidence_29
- security_service/audit_record_3221 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- backup_service/backup_4917 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- integration_service/data_flow_8933 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- support_platform/support_6046 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00

## case_309 -> COMPLETE (subject user_307)
- intent: DELETION via gemini
- account_service/account_4319 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_29 :: scope-absence evidence_29
- security_service/audit_record_1945 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00

## case_310 -> INCOMPLETE (subject user_308)
- intent: DELETION via gemini
- account_service/account_1235 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_29 :: scope-absence evidence_29
- analytics_platform/analytics_061 [ANALYTICS_PROFILE->ANONYMIZE] present=False direct=False ref=False flow=None restore=None ev=evidence_29 :: scope-absence evidence_29
- security_service/audit_record_5640 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- search_service/search_6265 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- support_platform/support_4263 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00

## case_311 -> INCOMPLETE (subject user_309)
- intent: DELETION via gemini
- account_service/account_3275 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_29 :: scope-absence evidence_29
- security_service/audit_record_6245 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- search_service/search_3004 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- support_platform/support_4952 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00

## case_312 -> INCOMPLETE (subject user_310)
- intent: DELETION via gemini
- account_service/account_4718 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_29 :: scope-absence evidence_29
- security_service/audit_record_6559 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- export_service/export_9860 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00
- search_service/search_6805 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_29 :: latest sql:customer_data_replica_eu_west@evidence_29 2026-05-19T06:00:00+00:00

## case_313 -> COMPLETE (subject user_311)
- intent: DELETION via gemini
- account_service/account_8264 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:profile_lookup_completed@evidence_30 2026-05-14T11:54:21+00:00
- analytics_platform/analytics_6099 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:analytics_profile_read@evidence_30 2026-05-14T11:54:54+00:00
- security_service/audit_record_7020 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:audit_record_read_completed@evidence_30 2026-05-14T11:56:38+00:00

## case_314 -> COMPLETE (subject user_312)
- intent: DELETION via gemini
- account_service/account_591 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:profile_lookup_completed@evidence_30 2026-05-14T11:57:49+00:00
- analytics_platform/analytics_5532 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:analytics_profile_read@evidence_30 2026-05-14T11:57:30+00:00
- security_service/audit_record_7893 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:audit_record_read_completed@evidence_30 2026-05-14T11:53:44+00:00

## case_315 -> INCOMPLETE (subject user_313)
- intent: DELETION via gemini
- account_service/account_782 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_31 :: latest log:profile_lookup_completed@evidence_30 2026-05-14T11:55:39+00:00
- security_service/audit_record_2407 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_30 2026-05-14T11:58:48+00:00
- backup_service/backup_7421 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=True ev=evidence_74 :: latest log:restore_candidate_evaluated@evidence_30 2026-05-14T11:55:29+00:00

## case_316 -> INCOMPLETE (subject user_314)
- intent: DELETION via gemini
- account_service/account_9523 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_31 :: latest log:profile_lookup_completed@evidence_30 2026-05-14T11:54:44+00:00
- security_service/audit_record_4286 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_30 2026-05-14T11:59:37+00:00
- search_service/search_8583 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:index_query_completed@evidence_30 2026-05-14T11:58:01+00:00
- support_platform/support_1176 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_74 :: latest log:message_pii_scan@evidence_30 2026-05-14T11:56:51+00:00

## case_317 -> INCOMPLETE (subject user_315)
- intent: DELETION via gemini
- account_service/account_1972 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_31 :: latest log:profile_lookup_completed@evidence_30 2026-05-14T11:58:27+00:00
- analytics_platform/analytics_1488 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_74 :: latest log:analytics_identity_scan@evidence_30 2026-05-14T11:55:13+00:00
- security_service/audit_record_6170 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_30 2026-05-14T11:58:50+00:00
- integration_service/data_flow_3064 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_74 :: latest log:connector_heartbeat@evidence_30 2026-05-14T11:54:23+00:00
- search_service/search_8665 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:index_query_completed@evidence_30 2026-05-14T11:51:33+00:00
- support_platform/support_4439 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_74 :: latest log:message_pii_scan@evidence_30 2026-05-14T11:58:44+00:00

## case_318 -> INCOMPLETE (subject user_316)
- intent: DELETION via gemini
- account_service/account_1530 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_31 :: latest log:profile_lookup_completed@evidence_30 2026-05-14T11:51:20+00:00
- security_service/audit_record_6708 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_30 2026-05-14T11:54:03+00:00
- search_service/search_5472 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:index_query_completed@evidence_30 2026-05-14T11:53:53+00:00
- support_platform/support_7995 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_74 :: latest log:message_pii_scan@evidence_30 2026-05-14T11:56:43+00:00

## case_319 -> COMPLETE (subject user_317)
- intent: DELETION via gemini
- account_service/account_2088 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:profile_lookup_completed@evidence_30 2026-05-14T11:58:45+00:00
- analytics_platform/analytics_2601 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:analytics_profile_read@evidence_30 2026-05-14T11:52:51+00:00
- security_service/audit_record_7337 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:audit_record_read_completed@evidence_30 2026-05-14T11:58:51+00:00

## case_320 -> INCOMPLETE (subject user_318)
- intent: DELETION via gemini
- account_service/account_9178 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_31 :: latest log:profile_lookup_completed@evidence_30 2026-05-14T11:52:56+00:00
- security_service/audit_record_1409 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_30 2026-05-14T11:57:43+00:00
- integration_service/data_flow_8828 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_74 :: latest log:connector_heartbeat@evidence_30 2026-05-14T11:55:29+00:00
- search_service/search_2256 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:index_query_completed@evidence_30 2026-05-14T11:53:37+00:00

## case_321 -> INCOMPLETE (subject user_319)
- intent: DELETION via gemini
- account_service/account_3525 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_31 :: latest log:profile_lookup_completed@evidence_30 2026-05-14T11:52:38+00:00
- security_service/audit_record_5151 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_30 2026-05-14T11:55:30+00:00
- integration_service/data_flow_4964 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_74 :: latest log:connector_heartbeat@evidence_30 2026-05-14T11:55:48+00:00
- search_service/search_3667 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:index_query_completed@evidence_30 2026-05-14T11:55:36+00:00

## case_322 -> COMPLETE (subject user_320)
- intent: DELETION via gemini
- account_service/account_9354 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:profile_lookup_completed@evidence_30 2026-05-14T11:54:06+00:00
- analytics_platform/analytics_4229 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:analytics_profile_read@evidence_30 2026-05-14T11:53:19+00:00
- security_service/audit_record_3201 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_74 :: latest log:audit_record_read_completed@evidence_30 2026-05-14T11:56:01+00:00

## case_323 -> COMPLETE (subject user_321)
- intent: DELETION via gemini
- account_service/account_2917 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_73 :: latest log:profile_lookup_completed@evidence_73 2026-05-09T07:55:18+00:00
- security_service/audit_record_3338 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00

## case_324 -> COMPLETE (subject user_322)
- intent: DELETION via gemini
- account_service/account_1242 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_73 :: latest log:profile_lookup_completed@evidence_73 2026-05-09T09:07:26+00:00
- analytics_platform/analytics_136 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- security_service/audit_record_4466 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- backup_service/backup_6458 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- integration_service/data_flow_4769 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- support_platform/support_7249 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00

## case_325 -> INCOMPLETE (subject user_323)
- intent: DELETION via gemini
- account_service/account_2595 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_72 :: scope-absence evidence_72
- security_service/audit_record_2236 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- integration_service/data_flow_9962 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- search_service/search_4054 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00

## case_326 -> COMPLETE (subject user_324)
- intent: DELETION via gemini
- account_service/account_3785 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_73 :: latest log:profile_lookup_completed@evidence_73 2026-05-09T09:32:04+00:00
- analytics_platform/analytics_2072 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- security_service/audit_record_1219 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- backup_service/backup_2894 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- integration_service/data_flow_2468 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- support_platform/support_305 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00

## case_327 -> COMPLETE (subject user_325)
- intent: DELETION via gemini
- account_service/account_4606 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_73 :: latest log:profile_lookup_completed@evidence_73 2026-05-09T10:29:49+00:00
- analytics_platform/analytics_9681 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- security_service/audit_record_461 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00

## case_328 -> INCOMPLETE (subject user_326)
- intent: DELETION via gemini
- account_service/account_206 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_72 :: scope-absence evidence_72
- security_service/audit_record_5012 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- search_service/search_9107 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- support_platform/support_7926 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00

## case_329 -> INCOMPLETE (subject user_327)
- intent: DELETION via gemini
- account_service/account_6301 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_72 :: scope-absence evidence_72
- analytics_platform/analytics_671 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- security_service/audit_record_3525 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- search_service/search_5226 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00

## case_330 -> INCOMPLETE (subject user_328)
- intent: DELETION via gemini
- account_service/account_2583 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_72 :: scope-absence evidence_72
- security_service/audit_record_6629 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- search_service/search_4560 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- support_platform/support_4851 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00

## case_331 -> COMPLETE (subject user_329)
- intent: DELETION via gemini
- account_service/account_6814 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_73 :: latest log:profile_lookup_completed@evidence_73 2026-05-09T08:15:29+00:00
- analytics_platform/analytics_2022 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- security_service/audit_record_6731 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- backup_service/backup_9376 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- integration_service/data_flow_8534 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- support_platform/support_1403 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00

## case_332 -> INCOMPLETE (subject user_330)
- intent: DELETION via gemini
- account_service/account_5992 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_72 :: scope-absence evidence_72
- security_service/audit_record_8914 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- integration_service/data_flow_4392 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00
- search_service/search_049 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_73 :: latest json:bundle@evidence_31 2026-05-09T11:00:00+00:00

## case_333 -> INCOMPLETE (subject user_331)
- intent: DELETION via gemini
- account_service/account_2475 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- security_service/audit_record_4647 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- search_service/search_5970 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00

## case_334 -> INCOMPLETE (subject user_332)
- intent: DELETION via gemini
- account_service/account_2255 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- security_service/audit_record_8558 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- search_service/search_7348 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- support_platform/support_214 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00

## case_335 -> COMPLETE (subject user_333)
- intent: DELETION via gemini
- account_service/account_8892 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- analytics_platform/analytics_3108 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- security_service/audit_record_711 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- backup_service/backup_3136 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=False ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- integration_service/data_flow_7452 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- support_platform/support_4712 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00

## case_336 -> COMPLETE (subject user_334)
- intent: DELETION via gemini
- account_service/account_2282 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- analytics_platform/analytics_1072 [ANALYTICS_PROFILE->ANONYMIZE] present=False direct=False ref=False flow=None restore=None ev=evidence_72 :: latest json:export@evidence_71 2026-04-29T06:18:18+00:00 | superseded by scope-absence evidence_72
- security_service/audit_record_5022 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00

## case_337 -> INCOMPLETE (subject user_335)
- intent: DELETION via gemini
- account_service/account_767 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- security_service/audit_record_1961 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- integration_service/data_flow_5200 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- search_service/search_3773 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00

## case_338 -> INCOMPLETE (subject user_336)
- intent: DELETION via gemini
- account_service/account_4231 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- security_service/audit_record_9226 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- integration_service/data_flow_9392 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- search_service/search_1392 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00

## case_339 -> COMPLETE (subject user_337)
- intent: DELETION via gemini
- account_service/account_1340 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- analytics_platform/analytics_2079 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- security_service/audit_record_2922 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00

## case_340 -> INCOMPLETE (subject user_338)
- intent: DELETION via gemini
- account_service/account_1015 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- security_service/audit_record_3872 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- integration_service/data_flow_5916 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- search_service/search_5411 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00

## case_341 -> INCOMPLETE (subject user_339)
- intent: DELETION via gemini
- account_service/account_4377 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- analytics_platform/analytics_183 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- security_service/audit_record_2862 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- search_service/search_7367 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00

## case_342 -> INCOMPLETE (subject user_340)
- intent: DELETION via gemini
- account_service/account_614 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- security_service/audit_record_4058 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00
- support_platform/support_3399 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_72 :: latest json:history@evidence_31 2026-05-04T10:00:00+00:00

## case_343 -> COMPLETE (subject user_341)
- intent: DELETION via gemini
- account_service/account_1949 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T07:42:28+00:00
- analytics_platform/analytics_4751 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T08:32:22+00:00
- security_service/audit_record_9233 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T08:01:21+00:00

## case_344 -> INCOMPLETE (subject user_342)
- intent: DELETION via gemini
- account_service/account_486 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_33 :: scope-absence evidence_33
- analytics_platform/analytics_7102 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T07:53:10+00:00
- integration_service/data_flow_5544 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T06:40:36+00:00
- search_service/search_5267 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T08:11:53+00:00

## case_345 -> COMPLETE (subject user_343)
- intent: DELETION via gemini
- account_service/account_5214 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T05:53:44+00:00
- analytics_platform/analytics_3990 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T07:55:27+00:00
- security_service/audit_record_454 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T08:15:11+00:00

## case_346 -> COMPLETE (subject user_344)
- intent: DELETION via gemini
- account_service/account_8834 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T05:56:53+00:00
- security_service/audit_record_1700 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T07:50:23+00:00

## case_347 -> INCOMPLETE (subject user_345)
- intent: DELETION via gemini
- account_service/account_3372 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_33 :: scope-absence evidence_33
- search_service/search_8185 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T07:51:48+00:00
- support_platform/support_9474 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T06:53:16+00:00

## case_348 -> INCOMPLETE (subject user_346)
- intent: DELETION via gemini
- account_service/account_421 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_33 :: scope-absence evidence_33
- analytics_platform/analytics_9196 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T06:14:29+00:00
- export_service/export_4871 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T06:17:56+00:00
- search_service/search_6170 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T07:59:37+00:00
- support_platform/support_2897 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T07:38:08+00:00

## case_349 -> INCOMPLETE (subject user_347)
- intent: DELETION via gemini
- account_service/account_9881 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_33 :: scope-absence evidence_33
- integration_service/data_flow_3178 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T05:55:41+00:00
- search_service/search_3944 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T07:03:14+00:00

## case_350 -> INCOMPLETE (subject user_348)
- intent: DELETION via gemini
- account_service/account_5202 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_33 :: scope-absence evidence_33
- integration_service/data_flow_9775 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T05:58:22+00:00

## case_351 -> COMPLETE (subject user_349)
- intent: DELETION via gemini
- account_service/account_5059 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T06:48:58+00:00
- security_service/audit_record_8787 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T08:27:54+00:00
- backup_service/backup_024 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T07:17:59+00:00
- integration_service/data_flow_4323 [DATA_FLOW->DISABLE] present=True direct=False ref=True flow=False restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T06:29:15+00:00
- support_platform/support_7137 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T08:06:22+00:00

## case_352 -> INCOMPLETE (subject user_350)
- intent: DELETION via gemini
- account_service/account_6215 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_33 :: scope-absence evidence_33
- search_service/search_5685 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T06:43:37+00:00
- support_platform/support_3980 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_71 :: latest json:export@evidence_71 2026-04-29T06:20:30+00:00

## case_353 -> INCOMPLETE (subject user_351)
- intent: DELETION via gemini
- account_service/account_9056 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_33 :: scope-absence evidence_33
- analytics_platform/analytics_8011 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- security_service/audit_record_5773 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- integration_service/data_flow_3180 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- search_service/search_495 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- support_platform/support_2406 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00

## case_354 -> COMPLETE (subject user_352)
- intent: DELETION via gemini
- account_service/account_3918 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_33 :: scope-absence evidence_33
- analytics_platform/analytics_439 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- security_service/audit_record_9286 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00

## case_355 -> INCOMPLETE (subject user_353)
- intent: DELETION via gemini
- account_service/account_6539 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- security_service/audit_record_1151 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00

## case_356 -> INCOMPLETE (subject user_354)
- intent: DELETION via gemini
- account_service/account_6093 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_33 :: scope-absence evidence_33
- analytics_platform/analytics_5413 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- security_service/audit_record_771 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- integration_service/data_flow_4472 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- search_service/search_5025 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- support_platform/support_6224 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00

## case_357 -> INCOMPLETE (subject user_355)
- intent: DELETION via gemini
- account_service/account_8105 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- security_service/audit_record_350 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- search_service/search_6828 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00

## case_358 -> INCOMPLETE (subject user_356)
- intent: DELETION via gemini
- account_service/account_1850 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_33 :: scope-absence evidence_33
- security_service/audit_record_1395 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- search_service/search_4067 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- support_platform/support_1846 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00

## case_359 -> INCOMPLETE (subject user_357)
- intent: DELETION via gemini
- account_service/account_6445 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_33 :: scope-absence evidence_33
- security_service/audit_record_2641 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- search_service/search_2492 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- support_platform/support_2537 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00

## case_360 -> INCOMPLETE (subject user_358)
- intent: DELETION via gemini
- account_service/account_6312 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_33 :: scope-absence evidence_33
- security_service/audit_record_2605 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- export_service/export_350 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- search_service/search_957 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00

## case_361 -> INCOMPLETE (subject user_359)
- intent: DELETION via gemini
- account_service/account_7118 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_33 :: scope-absence evidence_33
- security_service/audit_record_7587 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- integration_service/data_flow_3052 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- search_service/search_496 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00

## case_362 -> COMPLETE (subject user_360)
- intent: DELETION via gemini
- account_service/account_507 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_33 :: scope-absence evidence_33
- analytics_platform/analytics_4273 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00
- security_service/audit_record_8638 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_33 :: latest sql:customer_data_replica_eu_west@evidence_33 2026-04-24T08:00:00+00:00

## case_363 -> INCOMPLETE (subject user_361)
- intent: DELETION via gemini
- account_service/account_9205 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:profile_lookup_completed@evidence_34 2026-04-19T06:58:59+00:00
- security_service/audit_record_9777 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:audit_record_read_completed@evidence_34 2026-04-19T06:54:14+00:00
- backup_service/backup_7253 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=True ev=evidence_34 :: latest log:restore_candidate_evaluated@evidence_34 2026-04-19T06:51:41+00:00

## case_364 -> INCOMPLETE (subject user_362)
- intent: DELETION via gemini
- account_service/account_7653 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:profile_lookup_completed@evidence_34 2026-04-19T06:51:55+00:00
- security_service/audit_record_7136 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:audit_record_read_completed@evidence_34 2026-04-19T06:58:13+00:00
- search_service/search_8198 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:index_query_completed@evidence_34 2026-04-19T06:54:27+00:00
- support_platform/support_9699 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_34 :: latest log:message_pii_scan@evidence_34 2026-04-19T06:58:06+00:00

## case_365 -> INCOMPLETE (subject user_363)
- intent: DELETION via gemini
- account_service/account_3016 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:profile_lookup_completed@evidence_34 2026-04-19T06:52:30+00:00
- analytics_platform/analytics_547 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_34 :: latest log:analytics_identity_scan@evidence_34 2026-04-19T06:51:41+00:00
- security_service/audit_record_5798 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:audit_record_read_completed@evidence_34 2026-04-19T06:51:35+00:00
- integration_service/data_flow_1021 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_34 :: latest log:connector_heartbeat@evidence_34 2026-04-19T06:56:50+00:00
- search_service/search_6311 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:index_query_completed@evidence_34 2026-04-19T06:54:37+00:00
- support_platform/support_3294 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_34 :: latest log:message_pii_scan@evidence_34 2026-04-19T06:51:45+00:00

## case_366 -> INCOMPLETE (subject user_364)
- intent: DELETION via gemini
- account_service/account_4788 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:profile_lookup_completed@evidence_34 2026-04-19T06:56:50+00:00
- analytics_platform/analytics_8593 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_34 :: latest log:analytics_identity_scan@evidence_34 2026-04-19T06:54:16+00:00
- security_service/audit_record_4655 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:audit_record_read_completed@evidence_34 2026-04-19T06:59:20+00:00
- integration_service/data_flow_8256 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_34 :: latest log:connector_heartbeat@evidence_34 2026-04-19T06:53:19+00:00
- search_service/search_5301 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:index_query_completed@evidence_34 2026-04-19T06:59:41+00:00
- support_platform/support_5609 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_34 :: latest log:message_pii_scan@evidence_34 2026-04-19T06:51:21+00:00

## case_367 -> INCOMPLETE (subject user_365)
- intent: DELETION via gemini
- account_service/account_3204 [USER_PROFILE->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:profile_lookup_completed@evidence_34 2026-04-19T06:58:17+00:00
- analytics_platform/analytics_946 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_34 :: latest log:analytics_identity_scan@evidence_34 2026-04-19T06:58:34+00:00
- security_service/audit_record_9082 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:audit_record_read_completed@evidence_34 2026-04-19T06:55:10+00:00
- search_service/search_9950 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:index_query_completed@evidence_34 2026-04-19T06:54:03+00:00
- support_platform/support_4691 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_34 :: latest log:message_pii_scan@evidence_34 2026-04-19T06:56:25+00:00

## case_368 -> INCOMPLETE (subject user_366)
- intent: DELETION via gemini
- account_service/account_9570 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:profile_lookup_completed@evidence_34 2026-04-19T06:56:10+00:00
- security_service/audit_record_3738 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:audit_record_read_completed@evidence_34 2026-04-19T06:54:38+00:00
- integration_service/data_flow_8293 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_34 :: latest log:connector_heartbeat@evidence_34 2026-04-19T06:58:52+00:00
- search_service/search_4359 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:index_query_completed@evidence_34 2026-04-19T06:53:19+00:00

## case_369 -> COMPLETE (subject user_367)
- intent: DELETION via gemini
- account_service/account_8590 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:profile_lookup_completed@evidence_34 2026-04-19T06:53:06+00:00
- analytics_platform/analytics_2807 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:analytics_profile_read@evidence_34 2026-04-19T06:55:00+00:00
- security_service/audit_record_337 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:audit_record_read_completed@evidence_34 2026-04-19T06:55:01+00:00

## case_370 -> INCOMPLETE (subject user_368)
- intent: DELETION via gemini
- account_service/account_6567 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:profile_lookup_completed@evidence_34 2026-04-19T06:56:59+00:00
- analytics_platform/analytics_7215 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_34 :: latest log:analytics_identity_scan@evidence_34 2026-04-19T06:56:24+00:00
- security_service/audit_record_9696 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:audit_record_read_completed@evidence_34 2026-04-19T06:54:00+00:00
- integration_service/data_flow_5608 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_34 :: latest log:connector_heartbeat@evidence_34 2026-04-19T06:56:32+00:00
- search_service/search_9365 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:index_query_completed@evidence_34 2026-04-19T06:51:21+00:00
- support_platform/support_6949 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_34 :: latest log:message_pii_scan@evidence_34 2026-04-19T06:53:12+00:00

## case_371 -> INCOMPLETE (subject user_369)
- intent: DELETION via gemini
- account_service/account_5896 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:profile_lookup_completed@evidence_34 2026-04-19T06:53:30+00:00
- security_service/audit_record_689 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:audit_record_read_completed@evidence_34 2026-04-19T06:58:38+00:00
- search_service/search_6847 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:index_query_completed@evidence_34 2026-04-19T06:54:45+00:00
- support_platform/support_3110 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_34 :: latest log:attachment_pii_scan@evidence_34 2026-04-19T06:55:00+00:00

## case_372 -> INCOMPLETE (subject user_370)
- intent: DELETION via gemini
- account_service/account_2062 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:profile_lookup_completed@evidence_34 2026-04-19T06:54:04+00:00
- security_service/audit_record_5705 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:audit_record_read_completed@evidence_34 2026-04-19T06:54:12+00:00
- export_service/export_5081 [USER_EXPORT->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_34 :: latest log:export_download_check_completed@evidence_34 2026-04-19T06:55:49+00:00

## case_373 -> INCOMPLETE (subject user_371)
- intent: DELETION via gemini
- account_service/account_8684 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_69 :: scope-absence evidence_69
- security_service/audit_record_9163 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00
- integration_service/data_flow_2984 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00
- search_service/search_7859 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00

## case_374 -> COMPLETE (subject user_372)
- intent: DELETION via gemini
- account_service/account_8598 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_70 :: latest log:profile_lookup_completed@evidence_70 2026-04-14T03:37:08+00:00
- analytics_platform/analytics_9394 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00
- security_service/audit_record_5137 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00

## case_375 -> COMPLETE (subject user_373)
- intent: DELETION via gemini
- account_service/account_2854 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_70 :: latest log:profile_lookup_completed@evidence_70 2026-04-14T03:26:36+00:00
- analytics_platform/analytics_5779 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00
- security_service/audit_record_6359 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00

## case_376 -> INCOMPLETE (subject user_374)
- intent: DELETION via gemini
- account_service/account_5454 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_69 :: scope-absence evidence_69
- security_service/audit_record_4137 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00
- search_service/search_3126 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00
- support_platform/support_475 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00

## case_377 -> INCOMPLETE (subject user_375)
- intent: DELETION via gemini
- account_service/account_1824 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_69 :: scope-absence evidence_69
- analytics_platform/analytics_3651 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00
- security_service/audit_record_3685 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00

## case_378 -> COMPLETE (subject user_376)
- intent: DELETION via gemini
- account_service/account_976 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_70 :: latest log:profile_lookup_completed@evidence_70 2026-04-14T03:55:48+00:00
- analytics_platform/analytics_3234 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00
- security_service/audit_record_7312 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00

## case_379 -> INCOMPLETE (subject user_377)
- intent: DELETION via gemini
- account_service/account_6246 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00
- security_service/audit_record_8830 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00
- search_service/search_9124 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00

## case_380 -> COMPLETE (subject user_378)
- intent: DELETION via gemini
- account_service/account_4001 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_70 :: latest log:profile_lookup_completed@evidence_70 2026-04-14T04:45:32+00:00
- analytics_platform/analytics_9326 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00
- security_service/audit_record_4489 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00

## case_381 -> INCOMPLETE (subject user_379)
- intent: DELETION via gemini
- account_service/account_6784 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00
- security_service/audit_record_6833 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00

## case_382 -> INCOMPLETE (subject user_380)
- intent: DELETION via gemini
- account_service/account_2041 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_69 :: scope-absence evidence_69
- analytics_platform/analytics_9918 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00
- security_service/audit_record_6238 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00
- integration_service/data_flow_6090 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00
- search_service/search_8171 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00
- support_platform/support_5071 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_70 :: latest json:bundle@evidence_35 2026-04-14T06:00:00+00:00

## case_383 -> COMPLETE (subject user_381)
- intent: DELETION via gemini
- account_service/account_5043 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- analytics_platform/analytics_9702 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- security_service/audit_record_989 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00

## case_384 -> INCOMPLETE (subject user_382)
- intent: DELETION via gemini
- account_service/account_4441 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- security_service/audit_record_2342 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- export_service/export_9989 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- search_service/search_7562 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00

## case_385 -> INCOMPLETE (subject user_383)
- intent: DELETION via gemini
- account_service/account_4844 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- security_service/audit_record_3007 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- integration_service/data_flow_3913 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- search_service/search_3355 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00

## case_386 -> INCOMPLETE (subject user_384)
- intent: DELETION via gemini
- account_service/account_807 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- analytics_platform/analytics_4420 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- security_service/audit_record_8245 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- integration_service/data_flow_7623 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- search_service/search_3630 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- support_platform/support_1693 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00

## case_387 -> INCOMPLETE (subject user_385)
- intent: DELETION via gemini
- account_service/account_3978 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- security_service/audit_record_2536 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- backup_service/backup_1668 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=True ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00

## case_388 -> INCOMPLETE (subject user_386)
- intent: DELETION via gemini
- account_service/account_8186 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- analytics_platform/analytics_2784 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- security_service/audit_record_8683 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- integration_service/data_flow_3250 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- search_service/search_182 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- support_platform/support_8378 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00

## case_389 -> INCOMPLETE (subject user_387)
- intent: DELETION via gemini
- account_service/account_3206 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- analytics_platform/analytics_5354 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- security_service/audit_record_9005 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- search_service/search_2794 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00

## case_390 -> COMPLETE (subject user_388)
- intent: DELETION via gemini
- account_service/account_7618 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- analytics_platform/analytics_448 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- security_service/audit_record_101 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- backup_service/backup_5165 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=False ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- integration_service/data_flow_5737 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- legal_service/legal_hold_8049 [LEGAL_HOLD_RECORD->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- support_platform/support_5720 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00

## case_391 -> INCOMPLETE (subject user_389)
- intent: DELETION via gemini
- account_service/account_4446 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- security_service/audit_record_5007 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- search_service/search_9470 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00

## case_392 -> COMPLETE (subject user_390)
- intent: DELETION via gemini
- account_service/account_1718 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- analytics_platform/analytics_4328 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00
- security_service/audit_record_7510 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_36 :: latest json:ledger@evidence_36 2026-04-09T12:00:00+00:00

## case_393 -> COMPLETE (subject user_391)
- intent: DELETION via gemini
- account_service/account_1093 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_69 :: scope-absence evidence_69
- analytics_platform/analytics_542 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- security_service/audit_record_7330 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_69 :: latest sql:security_audit_records@evidence_69 2026-04-04T10:04:19+00:00

## case_394 -> INCOMPLETE (subject user_392)
- intent: DELETION via gemini
- account_service/account_2191 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_69 :: scope-absence evidence_69
- search_service/search_195 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_69 :: latest sql:customer_search_documents@evidence_69 2026-04-04T10:04:19+00:00

## case_395 -> COMPLETE (subject user_393)
- intent: DELETION via gemini
- account_service/account_2464 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_69 :: scope-absence evidence_69
- analytics_platform/analytics_298 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- security_service/audit_record_2839 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_69 :: latest sql:security_audit_records@evidence_69 2026-04-04T10:04:19+00:00

## case_396 -> INCOMPLETE (subject user_394)
- intent: DELETION via gemini
- account_service/account_3492 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_69 :: scope-absence evidence_69
- analytics_platform/analytics_4651 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_69 :: latest sql:customer_analytics_profiles@evidence_69 2026-04-04T10:04:19+00:00
- export_service/export_4664 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_69 :: latest sql:customer_exports@evidence_69 2026-04-04T10:04:19+00:00
- search_service/search_7293 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_69 :: latest sql:customer_search_documents@evidence_69 2026-04-04T10:04:19+00:00

## case_397 -> INCOMPLETE (subject user_395)
- intent: DELETION via gemini
- account_service/account_6443 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_69 :: scope-absence evidence_69
- integration_service/data_flow_626 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_69 :: latest sql:connector_subscriptions@evidence_69 2026-04-04T10:04:19+00:00
- search_service/search_3232 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_69 :: latest sql:customer_search_documents@evidence_69 2026-04-04T10:04:19+00:00

## case_398 -> COMPLETE (subject user_396)
- intent: DELETION via gemini
- account_service/account_1140 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_69 :: scope-absence evidence_69
- analytics_platform/analytics_4455 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_69 :: latest sql:customer_analytics_profiles@evidence_69 2026-04-04T10:04:19+00:00
- security_service/audit_record_7361 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_69 :: latest sql:security_audit_records@evidence_69 2026-04-04T10:04:19+00:00

## case_399 -> INCOMPLETE (subject user_397)
- intent: DELETION via gemini
- account_service/account_2138 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_69 :: scope-absence evidence_69
- backup_service/backup_2642 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_69 :: latest sql:backup_restore_entries@evidence_69 2026-04-04T10:04:19+00:00

## case_400 -> INCOMPLETE (subject user_398)
- intent: DELETION via gemini
- account_service/account_928 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_69 :: scope-absence evidence_69
- search_service/search_4649 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_69 :: latest sql:customer_search_documents@evidence_69 2026-04-04T10:04:19+00:00
- support_platform/support_4521 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_69 :: latest sql:support_records@evidence_69 2026-04-04T10:04:19+00:00

## case_401 -> INCOMPLETE (subject user_399)
- intent: DELETION via gemini
- account_service/account_9820 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_69 :: scope-absence evidence_69
- analytics_platform/analytics_6872 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_69 :: latest sql:customer_analytics_profiles@evidence_69 2026-04-04T10:04:19+00:00

## case_402 -> INCOMPLETE (subject user_400)
- intent: DELETION via gemini
- account_service/account_3370 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_69 :: scope-absence evidence_69
- analytics_platform/analytics_5811 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_69 :: latest sql:customer_analytics_profiles@evidence_69 2026-04-04T10:04:19+00:00
- integration_service/data_flow_9411 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_69 :: latest sql:connector_subscriptions@evidence_69 2026-04-04T10:04:19+00:00
- search_service/search_1338 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_69 :: latest sql:customer_search_documents@evidence_69 2026-04-04T10:04:19+00:00
- support_platform/support_4290 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_69 :: latest sql:support_records@evidence_69 2026-04-04T10:04:19+00:00

## case_403 -> COMPLETE (subject user_401)
- intent: DELETION via gemini
- account_service/account_1246 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_38 :: scope-absence evidence_38
- analytics_platform/analytics_7090 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- security_service/audit_record_4733 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00

## case_404 -> INCOMPLETE (subject user_402)
- intent: DELETION via gemini
- account_service/account_1759 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_38 :: scope-absence evidence_38
- analytics_platform/analytics_1792 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- security_service/audit_record_6099 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- integration_service/data_flow_8093 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- search_service/search_7022 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- support_platform/support_880 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00

## case_405 -> INCOMPLETE (subject user_403)
- intent: DELETION via gemini
- account_service/account_5389 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_ap_south@evidence_38 2026-03-30T10:00:00+00:00
- security_service/audit_record_4522 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- search_service/search_1606 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00

## case_406 -> INCOMPLETE (subject user_404)
- intent: DELETION via gemini
- account_service/account_8997 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_38 :: scope-absence evidence_38
- security_service/audit_record_5455 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- search_service/search_2804 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- support_platform/support_6047 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00

## case_407 -> INCOMPLETE (subject user_405)
- intent: DELETION via gemini
- account_service/account_9087 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_38 :: scope-absence evidence_38
- analytics_platform/analytics_1922 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- security_service/audit_record_6152 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- search_service/search_5146 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- support_platform/support_3802 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- support_platform/support_6569 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00

## case_408 -> COMPLETE (subject user_406)
- intent: DELETION via gemini
- account_service/account_5754 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_38 :: scope-absence evidence_38
- analytics_platform/analytics_8973 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- security_service/audit_record_4216 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00

## case_409 -> COMPLETE (subject user_407)
- intent: DELETION via gemini
- account_service/account_7174 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_38 :: scope-absence evidence_38
- security_service/audit_record_2559 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00

## case_410 -> INCOMPLETE (subject user_408)
- intent: DELETION via gemini
- account_service/account_163 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_38 :: scope-absence evidence_38
- security_service/audit_record_896 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- integration_service/data_flow_8300 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00
- search_service/search_9987 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00

## case_411 -> COMPLETE (subject user_409)
- intent: DELETION via gemini
- account_service/account_2775 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_38 :: scope-absence evidence_38
- security_service/audit_record_4330 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00

## case_412 -> COMPLETE (subject user_410)
- intent: DELETION via gemini
- account_service/account_8985 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_38 :: scope-absence evidence_38
- security_service/audit_record_5637 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_38 :: latest sql:customer_data_replica_eu_west@evidence_38 2026-03-30T10:00:00+00:00

## case_413 -> INCOMPLETE (subject user_411)
- intent: DELETION via gemini
- account_service/account_563 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:profile_lookup_completed@evidence_39 2026-03-25T08:57:33+00:00
- analytics_platform/analytics_4523 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_39 :: latest log:analytics_identity_scan@evidence_39 2026-03-25T08:55:11+00:00
- security_service/audit_record_9099 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:audit_record_read_completed@evidence_39 2026-03-25T08:53:50+00:00
- search_service/search_6162 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:index_query_completed@evidence_39 2026-03-25T08:54:22+00:00

## case_414 -> INCOMPLETE (subject user_412)
- intent: DELETION via gemini
- account_service/account_5260 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:profile_lookup_completed@evidence_39 2026-03-25T08:56:00+00:00
- security_service/audit_record_3768 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:audit_record_read_completed@evidence_39 2026-03-25T08:58:33+00:00
- search_service/search_8770 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:index_query_completed@evidence_39 2026-03-25T08:58:27+00:00
- support_platform/support_3768 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_39 :: latest log:message_pii_scan@evidence_39 2026-03-25T08:58:22+00:00

## case_415 -> INCOMPLETE (subject user_413)
- intent: DELETION via gemini
- account_service/account_9975 [USER_PROFILE->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:profile_lookup_completed@evidence_39 2026-03-25T08:58:06+00:00
- analytics_platform/analytics_2102 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_39 :: latest log:analytics_identity_scan@evidence_39 2026-03-25T08:56:48+00:00
- security_service/audit_record_6154 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:audit_record_read_completed@evidence_39 2026-03-25T08:55:32+00:00
- search_service/search_3864 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:index_query_completed@evidence_39 2026-03-25T08:56:41+00:00
- support_platform/support_1993 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_39 :: latest log:message_pii_scan@evidence_39 2026-03-25T08:52:52+00:00

## case_416 -> INCOMPLETE (subject user_414)
- intent: DELETION via gemini
- account_service/account_3075 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:profile_lookup_completed@evidence_39 2026-03-25T08:52:11+00:00
- security_service/audit_record_8832 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:audit_record_read_completed@evidence_39 2026-03-25T08:57:06+00:00
- integration_service/data_flow_1412 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_39 :: latest log:connector_heartbeat@evidence_39 2026-03-25T08:59:15+00:00
- search_service/search_6600 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:index_query_completed@evidence_39 2026-03-25T08:59:08+00:00

## case_417 -> INCOMPLETE (subject user_415)
- intent: DELETION via gemini
- account_service/account_4921 [USER_PROFILE->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:profile_lookup_completed@evidence_39 2026-03-25T08:53:25+00:00
- security_service/audit_record_7959 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:audit_record_read_completed@evidence_39 2026-03-25T08:58:43+00:00
- search_service/search_5479 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:index_query_completed@evidence_39 2026-03-25T08:52:27+00:00

## case_418 -> INCOMPLETE (subject user_416)
- intent: DELETION via gemini
- account_service/account_9120 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:profile_lookup_completed@evidence_39 2026-03-25T08:53:09+00:00
- security_service/audit_record_5493 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:audit_record_read_completed@evidence_39 2026-03-25T08:56:52+00:00
- search_service/search_8686 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:index_query_completed@evidence_39 2026-03-25T08:53:15+00:00
- support_platform/support_9464 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_39 :: latest log:message_pii_scan@evidence_39 2026-03-25T08:51:23+00:00

## case_419 -> INCOMPLETE (subject user_417)
- intent: DELETION via gemini
- account_service/account_1966 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:profile_lookup_completed@evidence_39 2026-03-25T08:58:08+00:00
- security_service/audit_record_7716 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:audit_record_read_completed@evidence_39 2026-03-25T08:56:17+00:00
- search_service/search_5797 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:index_query_completed@evidence_39 2026-03-25T08:57:08+00:00
- support_platform/support_2944 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_39 :: latest log:attachment_pii_scan@evidence_39 2026-03-25T08:51:55+00:00

## case_420 -> INCOMPLETE (subject user_418)
- intent: DELETION via gemini
- account_service/account_7606 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:profile_lookup_completed@evidence_39 2026-03-25T08:51:54+00:00
- security_service/audit_record_9687 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:audit_record_read_completed@evidence_39 2026-03-25T08:57:06+00:00
- export_service/export_389 [USER_EXPORT->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:export_download_check_completed@evidence_39 2026-03-25T08:57:36+00:00
- search_service/search_8472 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:index_query_completed@evidence_39 2026-03-25T08:59:44+00:00

## case_421 -> INCOMPLETE (subject user_419)
- intent: DELETION via gemini
- account_service/account_8482 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:profile_lookup_completed@evidence_39 2026-03-25T08:56:43+00:00
- security_service/audit_record_1256 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:audit_record_read_completed@evidence_39 2026-03-25T08:56:24+00:00
- integration_service/data_flow_4750 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_39 :: latest log:connector_heartbeat@evidence_39 2026-03-25T08:55:00+00:00
- search_service/search_3251 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:index_query_completed@evidence_39 2026-03-25T08:59:32+00:00

## case_422 -> INCOMPLETE (subject user_420)
- intent: DELETION via gemini
- account_service/account_4087 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:profile_lookup_completed@evidence_39 2026-03-25T08:58:44+00:00
- security_service/audit_record_4218 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:audit_record_read_completed@evidence_39 2026-03-25T08:56:26+00:00
- integration_service/data_flow_8871 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_39 :: latest log:connector_heartbeat@evidence_39 2026-03-25T08:59:09+00:00
- search_service/search_7614 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_39 :: latest log:index_query_completed@evidence_39 2026-03-25T08:56:22+00:00

## case_423 -> COMPLETE (subject user_421)
- intent: DELETION via gemini
- account_service/account_2420 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_68 :: latest json:export@evidence_68 2026-03-20T06:07:21+00:00
- analytics_platform/analytics_6249 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- security_service/audit_record_8082 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00

## case_424 -> COMPLETE (subject user_422)
- intent: DELETION via gemini
- account_service/account_2696 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_68 :: latest json:export@evidence_68 2026-03-20T06:29:58+00:00
- analytics_platform/analytics_3845 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- security_service/audit_record_1474 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00

## case_425 -> INCOMPLETE (subject user_423)
- intent: DELETION via gemini
- account_service/account_9633 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_66 :: scope-absence evidence_66
- analytics_platform/analytics_891 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- security_service/audit_record_4863 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- integration_service/data_flow_7718 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- search_service/search_9072 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- support_platform/support_1662 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00

## case_426 -> INCOMPLETE (subject user_424)
- intent: DELETION via gemini
- account_service/account_1576 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_66 :: scope-absence evidence_66
- security_service/audit_record_5472 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- search_service/search_2635 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- support_platform/support_9212 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00

## case_427 -> COMPLETE (subject user_425)
- intent: DELETION via gemini
- account_service/account_8461 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_68 :: latest json:export@evidence_68 2026-03-20T06:08:40+00:00
- analytics_platform/analytics_8091 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- security_service/audit_record_999 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00

## case_428 -> INCOMPLETE (subject user_426)
- intent: DELETION via gemini
- account_service/account_2157 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_66 :: scope-absence evidence_66
- security_service/audit_record_7557 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- integration_service/data_flow_2107 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- search_service/search_2625 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00

## case_429 -> INCOMPLETE (subject user_427)
- intent: DELETION via gemini
- account_service/account_4204 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- security_service/audit_record_9805 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- search_service/search_1449 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00

## case_430 -> COMPLETE (subject user_428)
- intent: DELETION via gemini
- account_service/account_6006 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_68 :: latest json:export@evidence_68 2026-03-20T05:29:33+00:00
- security_service/audit_record_5292 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00

## case_431 -> INCOMPLETE (subject user_429)
- intent: DELETION via gemini
- account_service/account_6101 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_66 :: scope-absence evidence_66
- security_service/audit_record_3236 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- search_service/search_7427 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- support_platform/support_3615 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00

## case_432 -> INCOMPLETE (subject user_430)
- intent: DELETION via gemini
- account_service/account_6489 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_66 :: scope-absence evidence_66
- security_service/audit_record_3548 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- export_service/export_9343 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- legal_service/legal_hold_438 [LEGAL_HOLD_RECORD->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00
- search_service/search_3844 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_68 :: latest json:bundle@evidence_40 2026-03-20T08:00:00+00:00

## case_433 -> INCOMPLETE (subject user_431)
- intent: DELETION via gemini
- account_service/account_5817 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- security_service/audit_record_6665 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- integration_service/data_flow_1283 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- search_service/search_9100 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00

## case_434 -> INCOMPLETE (subject user_432)
- intent: DELETION via gemini
- account_service/account_4813 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- analytics_platform/analytics_2354 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- security_service/audit_record_4043 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- integration_service/data_flow_9854 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- search_service/search_5626 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- support_platform/support_3364 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00

## case_435 -> INCOMPLETE (subject user_433)
- intent: DELETION via gemini
- account_service/account_9194 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- security_service/audit_record_9695 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- backup_service/backup_5237 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=True ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00

## case_436 -> INCOMPLETE (subject user_434)
- intent: DELETION via gemini
- account_service/account_3078 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- security_service/audit_record_2748 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- search_service/search_6599 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- support_platform/support_165 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00

## case_437 -> INCOMPLETE (subject user_435)
- intent: DELETION via gemini
- account_service/account_022 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- analytics_platform/analytics_6172 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- security_service/audit_record_6846 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00

## case_438 -> INCOMPLETE (subject user_436)
- intent: DELETION via gemini
- account_service/account_1680 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- analytics_platform/analytics_6528 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- security_service/audit_record_1366 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- integration_service/data_flow_3226 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- search_service/search_2052 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- support_platform/support_6688 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00

## case_439 -> INCOMPLETE (subject user_437)
- intent: DELETION via gemini
- account_service/account_3002 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- security_service/audit_record_1149 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00

## case_440 -> INCOMPLETE (subject user_438)
- intent: DELETION via gemini
- account_service/account_790 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- security_service/audit_record_5488 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- integration_service/data_flow_5967 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- search_service/search_2922 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00

## case_441 -> INCOMPLETE (subject user_439)
- intent: DELETION via gemini
- account_service/account_1538 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- security_service/audit_record_7313 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- search_service/search_3058 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00

## case_442 -> INCOMPLETE (subject user_440)
- intent: DELETION via gemini
- account_service/account_1897 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- security_service/audit_record_4839 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- search_service/search_1194 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00
- support_platform/support_4123 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_41 :: latest log:record_lookup@evidence_41 2026-03-15T07:00:00+00:00

## case_443 -> INCOMPLETE (subject user_441)
- intent: DELETION via gemini
- account_service/account_1776 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_66 :: scope-absence evidence_66
- search_service/search_4925 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_66 :: latest sql:customer_search_documents@evidence_66 2026-03-10T05:38:48+00:00
- support_platform/support_8341 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_66 :: latest sql:support_records@evidence_66 2026-03-10T05:38:48+00:00

## case_444 -> INCOMPLETE (subject user_442)
- intent: DELETION via gemini
- account_service/account_4042 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_66 :: scope-absence evidence_66
- export_service/export_4293 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_66 :: latest sql:customer_exports@evidence_66 2026-03-10T05:38:48+00:00
- search_service/search_3250 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_66 :: latest sql:customer_search_documents@evidence_66 2026-03-10T05:38:48+00:00

## case_445 -> INCOMPLETE (subject user_443)
- intent: DELETION via gemini
- account_service/account_1736 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_66 :: scope-absence evidence_66
- integration_service/data_flow_7584 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_66 :: latest sql:connector_subscriptions@evidence_66 2026-03-10T05:38:48+00:00
- search_service/search_2886 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_66 :: latest sql:customer_search_documents@evidence_66 2026-03-10T05:38:48+00:00

## case_446 -> INCOMPLETE (subject user_444)
- intent: DELETION via gemini
- account_service/account_3827 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_66 :: scope-absence evidence_66
- analytics_platform/analytics_195 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_66 :: latest sql:customer_analytics_profiles@evidence_66 2026-03-10T05:38:48+00:00
- integration_service/data_flow_1068 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_66 :: latest sql:connector_subscriptions@evidence_66 2026-03-10T05:38:48+00:00
- search_service/search_3780 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_66 :: latest sql:customer_search_documents@evidence_66 2026-03-10T05:38:48+00:00
- support_platform/support_9938 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_66 :: latest sql:support_records@evidence_66 2026-03-10T05:38:48+00:00

## case_447 -> INCOMPLETE (subject user_445)
- intent: DELETION via gemini
- account_service/account_7340 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_66 :: scope-absence evidence_66
- backup_service/backup_5192 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_66 :: latest sql:backup_restore_entries@evidence_66 2026-03-10T05:38:48+00:00

## case_448 -> COMPLETE (subject user_446)
- intent: DELETION via gemini
- account_service/account_6635 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_66 :: scope-absence evidence_66
- analytics_platform/analytics_7270 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_66 :: latest sql:customer_analytics_profiles@evidence_66 2026-03-10T05:38:48+00:00
- security_service/audit_record_753 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_66 :: latest sql:security_audit_records@evidence_66 2026-03-10T05:38:48+00:00

## case_449 -> INCOMPLETE (subject user_447)
- intent: DELETION via gemini
- account_service/account_5718 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_66 :: scope-absence evidence_66
- analytics_platform/analytics_1138 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_66 :: latest sql:customer_analytics_profiles@evidence_66 2026-03-10T05:38:48+00:00
- search_service/search_1685 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_66 :: latest sql:customer_search_documents@evidence_66 2026-03-10T05:38:48+00:00

## case_450 -> INCOMPLETE (subject user_448)
- intent: DELETION via gemini
- account_service/account_9275 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_66 :: scope-absence evidence_66
- analytics_platform/analytics_8202 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_66 :: latest sql:customer_analytics_profiles@evidence_66 2026-03-10T05:38:48+00:00
- integration_service/data_flow_9755 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_66 :: latest sql:connector_subscriptions@evidence_66 2026-03-10T05:38:48+00:00
- search_service/search_2365 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_66 :: latest sql:customer_search_documents@evidence_66 2026-03-10T05:38:48+00:00
- support_platform/support_7245 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_66 :: latest sql:support_records@evidence_66 2026-03-10T05:38:48+00:00

## case_451 -> INCOMPLETE (subject user_449)
- intent: DELETION via gemini
- account_service/account_1895 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_66 :: scope-absence evidence_66
- integration_service/data_flow_7263 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_66 :: latest sql:connector_subscriptions@evidence_66 2026-03-10T05:38:48+00:00
- search_service/search_360 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_66 :: latest sql:customer_search_documents@evidence_66 2026-03-10T05:38:48+00:00

## case_452 -> COMPLETE (subject user_450)
- intent: DELETION via gemini
- account_service/account_6294 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_66 :: scope-absence evidence_66
- analytics_platform/analytics_4031 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_66 :: latest sql:customer_analytics_profiles@evidence_66 2026-03-10T05:38:48+00:00
- security_service/audit_record_8608 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_66 :: latest sql:security_audit_records@evidence_66 2026-03-10T05:38:48+00:00

## case_453 -> INCOMPLETE (subject user_451)
- intent: DELETION via gemini
- account_service/account_3183 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00
- security_service/audit_record_3600 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00
- search_service/search_1317 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00

## case_454 -> INCOMPLETE (subject user_452)
- intent: DELETION via gemini
- account_service/account_3024 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_43 :: scope-absence evidence_43
- security_service/audit_record_2775 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00
- search_service/search_892 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00

## case_455 -> INCOMPLETE (subject user_453)
- intent: DELETION via gemini
- account_service/account_6373 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_43 :: scope-absence evidence_43
- security_service/audit_record_2788 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00
- search_service/search_887 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00
- support_platform/support_2055 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00

## case_456 -> COMPLETE (subject user_454)
- intent: DELETION via gemini
- account_service/account_3584 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_43 :: scope-absence evidence_43
- analytics_platform/analytics_6750 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00
- security_service/audit_record_8176 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00

## case_457 -> COMPLETE (subject user_455)
- intent: DELETION via gemini
- account_service/account_2761 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_43 :: scope-absence evidence_43
- analytics_platform/analytics_1126 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00
- security_service/audit_record_1171 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00

## case_458 -> COMPLETE (subject user_456)
- intent: DELETION via gemini
- account_service/account_077 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_43 :: scope-absence evidence_43
- analytics_platform/analytics_5221 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00
- security_service/audit_record_6750 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00

## case_459 -> INCOMPLETE (subject user_457)
- intent: DELETION via gemini
- account_service/account_5892 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_43 :: scope-absence evidence_43
- security_service/audit_record_6171 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00
- backup_service/backup_1140 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00

## case_460 -> INCOMPLETE (subject user_458)
- intent: DELETION via gemini
- account_service/account_5167 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_43 :: scope-absence evidence_43
- security_service/audit_record_1369 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00
- legal_service/legal_hold_5622 [LEGAL_HOLD_RECORD->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00
- support_platform/support_4146 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00

## case_461 -> INCOMPLETE (subject user_459)
- intent: DELETION via gemini
- account_service/account_4490 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_43 :: scope-absence evidence_43
- analytics_platform/analytics_8403 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00
- security_service/audit_record_3883 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00
- integration_service/data_flow_4612 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00
- search_service/search_9014 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00
- support_platform/support_3901 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00

## case_462 -> COMPLETE (subject user_460)
- intent: DELETION via gemini
- account_service/account_1881 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_43 :: scope-absence evidence_43
- security_service/audit_record_641 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_43 :: latest sql:customer_data_reporting_replica@evidence_43 2026-03-05T12:00:00+00:00

## case_463 -> COMPLETE (subject user_461)
- intent: DELETION via gemini
- account_service/account_1698 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:profile_lookup_completed@evidence_44 2026-02-28T10:59:43+00:00
- analytics_platform/analytics_689 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:analytics_profile_read@evidence_44 2026-02-28T10:56:18+00:00
- security_service/audit_record_8444 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:audit_record_read_completed@evidence_44 2026-02-28T10:55:40+00:00
- backup_service/backup_2005 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=False ev=evidence_65 :: latest log:restore_authorization_completed@evidence_44 2026-02-28T10:59:08+00:00
- integration_service/data_flow_8024 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_65 :: latest log:connector_config_loaded@evidence_44 2026-02-28T10:51:26+00:00
- support_platform/support_2659 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:message_read@evidence_44 2026-02-28T10:57:57+00:00

## case_464 -> COMPLETE (subject user_462)
- intent: DELETION via gemini
- account_service/account_2480 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:profile_lookup_completed@evidence_44 2026-02-28T10:55:37+00:00
- analytics_platform/analytics_8746 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:analytics_profile_read@evidence_44 2026-02-28T10:55:57+00:00
- security_service/audit_record_5183 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:audit_record_read_completed@evidence_44 2026-02-28T10:59:35+00:00
- backup_service/backup_7400 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=False ev=evidence_65 :: latest log:restore_authorization_completed@evidence_44 2026-02-28T10:51:46+00:00
- integration_service/data_flow_1344 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_65 :: latest log:connector_config_loaded@evidence_44 2026-02-28T10:52:49+00:00
- support_platform/support_5586 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:message_read@evidence_44 2026-02-28T10:58:36+00:00

## case_465 -> INCOMPLETE (subject user_463)
- intent: DELETION via gemini
- account_service/account_3653 [USER_PROFILE->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:profile_lookup_completed@evidence_44 2026-02-28T10:54:29+00:00
- security_service/audit_record_7099 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_44 2026-02-28T10:57:56+00:00
- search_service/search_728 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:index_query_completed@evidence_44 2026-02-28T10:51:37+00:00

## case_466 -> INCOMPLETE (subject user_464)
- intent: DELETION via gemini
- account_service/account_7503 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_45 :: latest log:profile_lookup_completed@evidence_44 2026-02-28T10:56:51+00:00
- security_service/audit_record_8892 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_44 2026-02-28T10:56:52+00:00
- search_service/search_8417 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:index_query_completed@evidence_44 2026-02-28T10:51:16+00:00

## case_467 -> COMPLETE (subject user_465)
- intent: DELETION via gemini
- account_service/account_2437 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:profile_lookup_completed@evidence_44 2026-02-28T10:56:40+00:00
- security_service/audit_record_8992 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:audit_record_read_completed@evidence_44 2026-02-28T10:54:14+00:00

## case_468 -> INCOMPLETE (subject user_466)
- intent: DELETION via gemini
- account_service/account_641 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_45 :: latest log:profile_lookup_completed@evidence_44 2026-02-28T10:57:40+00:00
- security_service/audit_record_307 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_44 2026-02-28T10:55:52+00:00
- export_service/export_9399 [USER_EXPORT->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:export_download_check_completed@evidence_44 2026-02-28T10:52:07+00:00
- search_service/search_9827 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:index_query_completed@evidence_44 2026-02-28T10:53:10+00:00

## case_469 -> INCOMPLETE (subject user_467)
- intent: DELETION via gemini
- account_service/account_6645 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_45 :: latest log:profile_lookup_completed@evidence_44 2026-02-28T10:53:18+00:00
- security_service/audit_record_7723 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_44 2026-02-28T10:53:56+00:00
- integration_service/data_flow_8730 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_65 :: latest log:connector_heartbeat@evidence_44 2026-02-28T10:57:11+00:00
- search_service/search_8450 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:index_query_completed@evidence_44 2026-02-28T10:57:35+00:00

## case_470 -> COMPLETE (subject user_468)
- intent: DELETION via gemini
- account_service/account_7023 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:profile_lookup_completed@evidence_44 2026-02-28T10:59:13+00:00
- analytics_platform/analytics_4066 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:analytics_profile_read@evidence_44 2026-02-28T10:56:29+00:00
- security_service/audit_record_2706 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:audit_record_read_completed@evidence_44 2026-02-28T10:57:11+00:00

## case_471 -> INCOMPLETE (subject user_469)
- intent: DELETION via gemini
- account_service/account_9034 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_45 :: latest log:profile_lookup_completed@evidence_44 2026-02-28T10:57:27+00:00
- security_service/audit_record_3862 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_44 2026-02-28T10:52:40+00:00
- backup_service/backup_7543 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=True ev=evidence_65 :: latest log:restore_candidate_evaluated@evidence_44 2026-02-28T10:59:32+00:00

## case_472 -> INCOMPLETE (subject user_470)
- intent: DELETION via gemini
- account_service/account_1957 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_45 :: latest log:profile_lookup_completed@evidence_44 2026-02-28T10:58:18+00:00
- security_service/audit_record_157 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=None :: latest log:audit_record_read_completed@evidence_44 2026-02-28T10:51:52+00:00
- search_service/search_9152 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_65 :: latest log:index_query_completed@evidence_44 2026-02-28T10:57:55+00:00
- support_platform/support_6987 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_65 :: latest log:message_pii_scan@evidence_44 2026-02-28T10:59:01+00:00

## case_473 -> INCOMPLETE (subject user_471)
- intent: DELETION via gemini
- account_service/account_6474 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_45 :: scope-absence evidence_45
- analytics_platform/analytics_8577 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- security_service/audit_record_519 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- legal_service/legal_hold_4743 [LEGAL_HOLD_RECORD->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- search_service/search_7375 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00

## case_474 -> INCOMPLETE (subject user_472)
- intent: DELETION via gemini
- account_service/account_9904 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_45 :: scope-absence evidence_45
- security_service/audit_record_712 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- search_service/search_9925 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- support_platform/support_4509 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00

## case_475 -> INCOMPLETE (subject user_473)
- intent: DELETION via gemini
- account_service/account_3205 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- security_service/audit_record_5667 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00

## case_476 -> INCOMPLETE (subject user_474)
- intent: DELETION via gemini
- account_service/account_3510 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_45 :: scope-absence evidence_45
- security_service/audit_record_4197 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- integration_service/data_flow_8899 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- search_service/search_3759 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00

## case_477 -> INCOMPLETE (subject user_475)
- intent: DELETION via gemini
- account_service/account_3119 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- security_service/audit_record_6405 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- search_service/search_5052 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00

## case_478 -> INCOMPLETE (subject user_476)
- intent: DELETION via gemini
- account_service/account_5934 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_45 :: scope-absence evidence_45
- security_service/audit_record_8754 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- search_service/search_5412 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- support_platform/support_3824 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00

## case_479 -> INCOMPLETE (subject user_477)
- intent: DELETION via gemini
- account_service/account_5582 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_45 :: scope-absence evidence_45
- security_service/audit_record_5745 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- support_platform/support_4665 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00

## case_480 -> COMPLETE (subject user_478)
- intent: DELETION via gemini
- account_service/account_2465 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_45 :: scope-absence evidence_45
- analytics_platform/analytics_1794 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- security_service/audit_record_7742 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- backup_service/backup_7706 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- integration_service/data_flow_2893 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- support_platform/support_5854 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00

## case_481 -> INCOMPLETE (subject user_479)
- intent: DELETION via gemini
- account_service/account_9449 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_45 :: scope-absence evidence_45
- security_service/audit_record_9025 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- integration_service/data_flow_173 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- search_service/search_8587 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00

## case_482 -> INCOMPLETE (subject user_480)
- intent: DELETION via gemini
- account_service/account_9394 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_45 :: scope-absence evidence_45
- security_service/audit_record_2180 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- integration_service/data_flow_8519 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00
- search_service/search_3728 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_45 :: latest json:bundle@evidence_45 2026-02-23T10:00:00+00:00

## case_483 -> INCOMPLETE (subject user_481)
- intent: DELETION via gemini
- account_service/account_9398 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_63 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- security_service/audit_record_4738 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- backup_service/backup_4600 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=True ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- integration_service/data_flow_3669 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- search_service/search_1613 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- support_platform/support_4364 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00

## case_484 -> INCOMPLETE (subject user_482)
- intent: DELETION via gemini
- account_service/account_2961 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_63 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- security_service/audit_record_5270 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- support_platform/support_7973 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00

## case_485 -> INCOMPLETE (subject user_483)
- intent: DELETION via gemini
- account_service/account_3378 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_63 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- analytics_platform/analytics_1981 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- security_service/audit_record_4405 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- search_service/search_3582 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00

## case_486 -> COMPLETE (subject user_484)
- intent: DELETION via gemini
- account_service/account_9031 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- analytics_platform/analytics_5948 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- security_service/audit_record_5451 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00

## case_487 -> INCOMPLETE (subject user_485)
- intent: DELETION via gemini
- account_service/account_5293 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- analytics_platform/analytics_7818 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- security_service/audit_record_1039 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- search_service/search_901 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- support_platform/support_5361 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00

## case_488 -> INCOMPLETE (subject user_486)
- intent: DELETION via gemini
- account_service/account_1433 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_63 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- security_service/audit_record_6252 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- integration_service/data_flow_3755 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- search_service/search_4216 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00

## case_489 -> INCOMPLETE (subject user_487)
- intent: DELETION via gemini
- account_service/account_6654 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- security_service/audit_record_1372 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- search_service/search_3426 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00

## case_490 -> INCOMPLETE (subject user_488)
- intent: DELETION via gemini
- account_service/account_4036 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_63 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- security_service/audit_record_5868 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- search_service/search_9931 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- support_platform/support_4247 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00

## case_491 -> COMPLETE (subject user_489)
- intent: DELETION via gemini
- account_service/account_7455 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- security_service/audit_record_7073 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00

## case_492 -> INCOMPLETE (subject user_490)
- intent: DELETION via gemini
- account_service/account_3589 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_63 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- analytics_platform/analytics_1575 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- security_service/audit_record_9341 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- export_service/export_6406 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- search_service/search_9733 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00
- support_platform/support_6737 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_64 :: latest json:history@evidence_45 2026-02-18T09:00:00+00:00

## case_493 -> COMPLETE (subject user_491)
- intent: DELETION via gemini
- account_service/account_7766 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_63 :: scope-absence evidence_63
- analytics_platform/analytics_5893 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_63 :: latest sql:customer_analytics_profiles@evidence_63 2026-02-13T07:43:27+00:00
- security_service/audit_record_730 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_63 :: latest sql:security_audit_records@evidence_63 2026-02-13T07:43:27+00:00

## case_494 -> COMPLETE (subject user_492)
- intent: DELETION via gemini
- account_service/account_3479 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_63 :: scope-absence evidence_63
- analytics_platform/analytics_5443 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_63 :: latest sql:customer_analytics_profiles@evidence_63 2026-02-13T07:43:27+00:00
- security_service/audit_record_1112 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_63 :: latest sql:security_audit_records@evidence_63 2026-02-13T07:43:27+00:00

## case_495 -> INCOMPLETE (subject user_493)
- intent: DELETION via gemini
- account_service/account_9784 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_63 :: scope-absence evidence_63
- backup_service/backup_5061 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_63 :: latest sql:backup_restore_entries@evidence_63 2026-02-13T07:43:27+00:00

## case_496 -> INCOMPLETE (subject user_494)
- intent: DELETION via gemini
- account_service/account_2512 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_63 :: scope-absence evidence_63
- search_service/search_3169 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_63 :: latest sql:customer_search_documents@evidence_63 2026-02-13T07:43:27+00:00
- support_platform/support_6391 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_63 :: latest sql:support_records@evidence_63 2026-02-13T07:43:27+00:00

## case_497 -> COMPLETE (subject user_495)
- intent: DELETION via gemini
- account_service/account_5281 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_63 :: scope-absence evidence_63
- analytics_platform/analytics_1558 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00
- security_service/audit_record_9796 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_63 :: latest sql:security_audit_records@evidence_63 2026-02-13T07:43:27+00:00

## case_498 -> INCOMPLETE (subject user_496)
- intent: DELETION via gemini
- account_service/account_282 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_63 :: scope-absence evidence_63
- analytics_platform/analytics_6565 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_63 :: latest sql:customer_analytics_profiles@evidence_63 2026-02-13T07:43:27+00:00
- search_service/search_6093 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_63 :: latest sql:customer_search_documents@evidence_63 2026-02-13T07:43:27+00:00
- support_platform/support_9075 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_63 :: latest sql:support_records@evidence_63 2026-02-13T07:43:27+00:00

## case_499 -> INCOMPLETE (subject user_497)
- intent: DELETION via gemini
- account_service/account_3626 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_63 :: latest sql:customer_profiles@evidence_63 2026-02-13T07:43:27+00:00

## case_500 -> INCOMPLETE (subject user_498)
- intent: DELETION via gemini
- account_service/account_5738 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_63 :: scope-absence evidence_63
- integration_service/data_flow_006 [DATA_FLOW->DISABLE] present=True direct=True ref=False flow=True restore=None ev=evidence_63 :: latest sql:connector_subscriptions@evidence_63 2026-02-13T07:43:27+00:00
- search_service/search_6092 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_63 :: latest sql:customer_search_documents@evidence_63 2026-02-13T07:43:27+00:00

## case_501 -> INCOMPLETE (subject user_499)
- intent: DELETION via gemini
- account_service/account_634 [USER_PROFILE->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_63 :: latest sql:customer_profiles@evidence_63 2026-02-13T07:43:27+00:00
- search_service/search_2799 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_63 :: latest sql:customer_search_documents@evidence_63 2026-02-13T07:43:27+00:00

## case_502 -> COMPLETE (subject user_500)
- intent: DELETION via gemini
- account_service/account_2554 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_63 :: scope-absence evidence_63
- security_service/audit_record_5238 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_63 :: latest sql:security_audit_records@evidence_63 2026-02-13T07:43:27+00:00

## case_503 -> INCOMPLETE (subject user_501)
- intent: DELETION via gemini
- account_service/account_5394 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_47 :: scope-absence evidence_47
- security_service/audit_record_5454 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00
- support_platform/support_2295 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00

## case_504 -> INCOMPLETE (subject user_502)
- intent: DELETION via gemini
- account_service/account_7244 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_47 :: scope-absence evidence_47
- security_service/audit_record_3733 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00
- export_service/export_3120 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00

## case_505 -> INCOMPLETE (subject user_503)
- intent: DELETION via gemini
- account_service/account_8136 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_47 :: scope-absence evidence_47
- security_service/audit_record_3441 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00
- integration_service/data_flow_5281 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00
- legal_service/legal_hold_2227 [LEGAL_HOLD_RECORD->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00
- search_service/search_2591 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00

## case_506 -> COMPLETE (subject user_504)
- intent: DELETION via gemini
- account_service/account_6161 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_47 :: scope-absence evidence_47
- security_service/audit_record_1361 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00

## case_507 -> INCOMPLETE (subject user_505)
- intent: DELETION via gemini
- account_service/account_3772 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_47 :: scope-absence evidence_47
- security_service/audit_record_7627 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00
- backup_service/backup_369 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00

## case_508 -> INCOMPLETE (subject user_506)
- intent: DELETION via gemini
- account_service/account_5423 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_47 :: scope-absence evidence_47
- security_service/audit_record_8154 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00
- support_platform/support_2691 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00

## case_509 -> INCOMPLETE (subject user_507)
- intent: DELETION via gemini
- account_service/account_6623 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_47 :: scope-absence evidence_47
- analytics_platform/analytics_784 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00
- security_service/audit_record_2323 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00
- search_service/search_6246 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00

## case_510 -> INCOMPLETE (subject user_508)
- intent: DELETION via gemini
- account_service/account_6049 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_47 :: scope-absence evidence_47
- security_service/audit_record_4266 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00
- search_service/search_6147 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00
- support_platform/support_9648 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00

## case_511 -> INCOMPLETE (subject user_509)
- intent: DELETION via gemini
- account_service/account_1035 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00
- security_service/audit_record_4883 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00
- legal_service/legal_hold_4887 [LEGAL_HOLD_RECORD->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00

## case_512 -> COMPLETE (subject user_510)
- intent: DELETION via gemini
- account_service/account_445 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_47 :: scope-absence evidence_47
- security_service/audit_record_4219 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_47 :: latest sql:customer_data_reporting_replica@evidence_47 2026-02-08T07:00:00+00:00

## case_513 -> INCOMPLETE (subject user_511)
- intent: DELETION via gemini
- account_service/account_1334 [USER_PROFILE->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:profile_lookup_completed@evidence_48 2026-02-03T05:57:51+00:00
- security_service/audit_record_2044 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:audit_record_read_completed@evidence_48 2026-02-03T05:57:45+00:00
- search_service/search_4739 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:index_query_completed@evidence_48 2026-02-03T05:55:14+00:00

## case_514 -> INCOMPLETE (subject user_512)
- intent: DELETION via gemini
- account_service/account_6473 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:profile_lookup_completed@evidence_48 2026-02-03T05:53:45+00:00
- analytics_platform/analytics_9920 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=False flow=None restore=None ev=evidence_48 :: latest log:analytics_identity_scan@evidence_48 2026-02-03T05:56:22+00:00
- security_service/audit_record_1967 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:audit_record_read_completed@evidence_48 2026-02-03T05:52:46+00:00
- integration_service/data_flow_9556 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_48 :: latest log:connector_heartbeat@evidence_48 2026-02-03T05:54:19+00:00
- search_service/search_2715 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:index_query_completed@evidence_48 2026-02-03T05:59:24+00:00
- support_platform/support_3982 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_48 :: latest log:message_pii_scan@evidence_48 2026-02-03T05:58:59+00:00

## case_515 -> INCOMPLETE (subject user_513)
- intent: DELETION via gemini
- account_service/account_3411 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:profile_lookup_completed@evidence_48 2026-02-03T05:53:58+00:00
- security_service/audit_record_7062 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:audit_record_read_completed@evidence_48 2026-02-03T05:51:50+00:00
- search_service/search_1928 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:index_query_completed@evidence_48 2026-02-03T05:53:36+00:00
- support_platform/support_4533 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_48 :: latest log:attachment_pii_scan@evidence_48 2026-02-03T05:59:27+00:00

## case_516 -> COMPLETE (subject user_514)
- intent: DELETION via gemini
- account_service/account_141 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:profile_lookup_completed@evidence_48 2026-02-03T05:52:14+00:00
- analytics_platform/analytics_4804 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:analytics_profile_read@evidence_48 2026-02-03T05:51:56+00:00
- security_service/audit_record_3777 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:audit_record_read_completed@evidence_48 2026-02-03T05:54:21+00:00

## case_517 -> INCOMPLETE (subject user_515)
- intent: DELETION via gemini
- account_service/account_3407 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:profile_lookup_completed@evidence_48 2026-02-03T05:53:49+00:00
- security_service/audit_record_946 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:audit_record_read_completed@evidence_48 2026-02-03T05:59:40+00:00
- integration_service/data_flow_8165 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_48 :: latest log:connector_heartbeat@evidence_48 2026-02-03T05:52:51+00:00
- search_service/search_2818 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:index_query_completed@evidence_48 2026-02-03T05:53:54+00:00

## case_518 -> INCOMPLETE (subject user_516)
- intent: DELETION via gemini
- account_service/account_9641 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:profile_lookup_completed@evidence_48 2026-02-03T05:54:17+00:00
- security_service/audit_record_5572 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:audit_record_read_completed@evidence_48 2026-02-03T05:51:59+00:00
- integration_service/data_flow_3518 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_48 :: latest log:connector_heartbeat@evidence_48 2026-02-03T05:56:16+00:00
- search_service/search_6401 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:index_query_completed@evidence_48 2026-02-03T05:52:59+00:00

## case_519 -> INCOMPLETE (subject user_517)
- intent: DELETION via gemini
- account_service/account_1506 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:profile_lookup_completed@evidence_48 2026-02-03T05:57:13+00:00
- security_service/audit_record_4027 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:audit_record_read_completed@evidence_48 2026-02-03T05:51:30+00:00
- backup_service/backup_8264 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=False flow=None restore=True ev=evidence_48 :: latest log:restore_candidate_evaluated@evidence_48 2026-02-03T05:58:20+00:00

## case_520 -> INCOMPLETE (subject user_518)
- intent: DELETION via gemini
- account_service/account_4979 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:profile_lookup_completed@evidence_48 2026-02-03T05:52:39+00:00
- security_service/audit_record_9504 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:audit_record_read_completed@evidence_48 2026-02-03T05:56:38+00:00
- support_platform/support_9251 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_48 :: latest log:message_pii_scan@evidence_48 2026-02-03T05:58:08+00:00

## case_521 -> COMPLETE (subject user_519)
- intent: DELETION via gemini
- account_service/account_1482 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:profile_lookup_completed@evidence_48 2026-02-03T05:54:10+00:00
- analytics_platform/analytics_7277 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:analytics_profile_read@evidence_48 2026-02-03T05:56:53+00:00
- security_service/audit_record_3567 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:audit_record_read_completed@evidence_48 2026-02-03T05:58:14+00:00

## case_522 -> INCOMPLETE (subject user_520)
- intent: DELETION via gemini
- account_service/account_1096 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:profile_lookup_completed@evidence_48 2026-02-03T05:57:59+00:00
- security_service/audit_record_5513 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=False flow=None restore=None ev=evidence_48 :: latest log:audit_record_read_completed@evidence_48 2026-02-03T05:57:34+00:00
- support_platform/support_8538 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=False flow=None restore=None ev=evidence_48 :: latest log:message_pii_scan@evidence_48 2026-02-03T05:57:48+00:00

## case_523 -> INCOMPLETE (subject user_521)
- intent: DELETION via gemini
- account_service/account_2424 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- security_service/audit_record_2172 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- search_service/search_9075 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00

## case_524 -> COMPLETE (subject user_522)
- intent: DELETION via gemini
- account_service/account_704 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_62 :: latest json:export@evidence_62 2026-01-29T09:38:08+00:00
- security_service/audit_record_5429 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00

## case_525 -> INCOMPLETE (subject user_523)
- intent: DELETION via gemini
- account_service/account_4974 [USER_PROFILE->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- security_service/audit_record_3803 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00

## case_526 -> INCOMPLETE (subject user_524)
- intent: DELETION via gemini
- account_service/account_1400 [USER_PROFILE->DELETE] present=None direct=False ref=False flow=None restore=None ev=None :: 
- analytics_platform/analytics_131 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- security_service/audit_record_5792 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- integration_service/data_flow_2263 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- search_service/search_3879 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- support_platform/support_1191 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00

## case_527 -> INCOMPLETE (subject user_525)
- intent: DELETION via gemini
- account_service/account_3693 [USER_PROFILE->DELETE] present=None direct=False ref=False flow=None restore=None ev=None :: 
- analytics_platform/analytics_7468 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- security_service/audit_record_2758 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- search_service/search_1091 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- support_platform/support_3896 [SUPPORT_ATTACHMENT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- support_platform/support_9832 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00

## case_528 -> INCOMPLETE (subject user_526)
- intent: DELETION via gemini
- account_service/account_1184 [USER_PROFILE->DELETE] present=None direct=False ref=False flow=None restore=None ev=None :: 
- analytics_platform/analytics_8476 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=True ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- security_service/audit_record_2284 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- export_service/export_9388 [USER_EXPORT->DELETE] present=True direct=True ref=False flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- search_service/search_1429 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- support_platform/support_193 [SUPPORT_MESSAGE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00

## case_529 -> INCOMPLETE (subject user_527)
- intent: DELETION via gemini
- account_service/account_4063 [USER_PROFILE->DELETE] present=None direct=False ref=False flow=None restore=None ev=None :: 
- security_service/audit_record_4542 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- integration_service/data_flow_6588 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=True restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- search_service/search_3382 [SEARCH_INDEX_ENTRY->DELETE] present=True direct=True ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00

## case_530 -> COMPLETE (subject user_528)
- intent: DELETION via gemini
- account_service/account_6169 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_62 :: latest json:export@evidence_62 2026-01-29T09:12:03+00:00
- analytics_platform/analytics_893 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- security_service/audit_record_2152 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00

## case_531 -> INCOMPLETE (subject user_529)
- intent: DELETION via gemini
- account_service/account_3146 [USER_PROFILE->DELETE] present=None direct=False ref=False flow=None restore=None ev=None :: 
- security_service/audit_record_8556 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=None :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- backup_service/backup_3382 [BACKUP_ARCHIVE->RETAIN] present=True direct=True ref=False flow=None restore=True ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00

## case_532 -> COMPLETE (subject user_530)
- intent: DELETION via gemini
- account_service/account_470 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_62 :: latest json:export@evidence_62 2026-01-29T11:44:14+00:00
- analytics_platform/analytics_3744 [ANALYTICS_PROFILE->ANONYMIZE] present=True direct=False ref=False flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- security_service/audit_record_4828 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- backup_service/backup_6344 [BACKUP_ARCHIVE->RETAIN] present=True direct=False ref=True flow=None restore=False ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- integration_service/data_flow_6987 [DATA_FLOW->DISABLE] present=True direct=False ref=False flow=False restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00
- support_platform/support_7724 [SUPPORT_MESSAGE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_62 :: latest json:bundle@evidence_49 2026-01-29T12:00:00+00:00

## case_533 -> NOT_APPLICABLE (subject -)
- intent: CORRECTION via gemini

## case_534 -> NOT_APPLICABLE (subject -)
- intent: MARKETING_OPT_OUT via gemini

## case_535 -> NOT_APPLICABLE (subject -)
- intent: PORTABILITY via gemini

## case_536 -> NOT_APPLICABLE (subject -)
- intent: ACCOUNT_RECOVERY via gemini

## case_537 -> NOT_APPLICABLE (subject -)
- intent: CORRECTION via gemini

## case_538 -> NOT_APPLICABLE (subject -)
- intent: MARKETING_OPT_OUT via gemini

## case_539 -> NOT_APPLICABLE (subject -)
- intent: ACCESS via gemini

## case_540 -> NOT_APPLICABLE (subject -)
- intent: ACCESS via gemini

## case_541 -> NOT_APPLICABLE (subject -)
- intent: CORRECTION via gemini

## case_542 -> NOT_APPLICABLE (subject -)
- intent: ACCESS via gemini

## case_543 -> COMPLETE (subject user_543)
- intent: DELETION via gemini
- account_service/account_8931 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_02 :: scope-absence evidence_02
- security_service/audit_record_6244 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_52 :: latest sql:customer_data_primary@evidence_52 2026-09-20T12:00:00+00:00
- identity_service/tombstone_205 [ACCOUNT_TOMBSTONE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_52 :: latest sql:customer_data_primary@evidence_52 2026-09-20T12:00:00+00:00

## case_544 -> INCOMPLETE (subject user_544)
- intent: DELETION via gemini
- account_service/account_7320 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_02 :: scope-absence evidence_02
- security_service/audit_record_1037 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_52 :: latest sql:customer_data_primary@evidence_52 2026-09-20T12:00:00+00:00
- identity_service/tombstone_8648 [ACCOUNT_TOMBSTONE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_52 :: latest sql:customer_data_primary@evidence_52 2026-09-20T12:00:00+00:00

## case_545 -> COMPLETE (subject user_545)
- intent: DELETION via gemini
- account_service/account_2577 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_02 :: scope-absence evidence_02
- security_service/audit_record_5041 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_52 :: latest sql:customer_data_primary@evidence_52 2026-09-20T12:00:00+00:00
- identity_service/tombstone_946 [ACCOUNT_TOMBSTONE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_52 :: latest sql:customer_data_primary@evidence_52 2026-09-20T12:00:00+00:00

## case_546 -> INCOMPLETE (subject user_546)
- intent: DELETION via gemini
- account_service/account_8832 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_02 :: scope-absence evidence_02
- security_service/audit_record_518 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_52 :: latest sql:customer_data_primary@evidence_52 2026-09-20T12:00:00+00:00
- identity_service/tombstone_8095 [ACCOUNT_TOMBSTONE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_52 :: latest sql:customer_data_primary@evidence_52 2026-09-20T12:00:00+00:00

## case_547 -> COMPLETE (subject user_547)
- intent: DELETION via gemini
- account_service/account_7015 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_02 :: scope-absence evidence_02
- security_service/audit_record_7352 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_52 :: latest sql:customer_data_primary@evidence_52 2026-09-20T12:00:00+00:00
- identity_service/tombstone_8774 [ACCOUNT_TOMBSTONE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_52 :: latest sql:customer_data_primary@evidence_52 2026-09-20T12:00:00+00:00

## case_548 -> INCOMPLETE (subject user_548)
- intent: DELETION via gemini
- account_service/account_9155 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_02 :: scope-absence evidence_02
- security_service/audit_record_6970 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_52 :: latest sql:customer_data_primary@evidence_52 2026-09-20T12:00:00+00:00
- identity_service/tombstone_3745 [ACCOUNT_TOMBSTONE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_52 :: latest sql:customer_data_primary@evidence_52 2026-09-20T12:00:00+00:00

## case_549 -> COMPLETE (subject user_549)
- intent: DELETION via gemini
- account_service/account_4842 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_02 :: scope-absence evidence_02
- security_service/audit_record_1491 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_52 :: latest sql:customer_data_primary@evidence_52 2026-09-20T12:00:00+00:00
- identity_service/tombstone_3963 [ACCOUNT_TOMBSTONE->REDACT] present=True direct=False ref=True flow=None restore=None ev=evidence_52 :: latest sql:customer_data_primary@evidence_52 2026-09-20T12:00:00+00:00

## case_550 -> INCOMPLETE (subject user_550)
- intent: DELETION via gemini
- account_service/account_7225 [USER_PROFILE->DELETE] present=False direct=False ref=False flow=None restore=None ev=evidence_02 :: scope-absence evidence_02
- security_service/audit_record_3831 [SECURITY_AUDIT_LOG->RETAIN] present=True direct=False ref=True flow=None restore=None ev=evidence_52 :: latest sql:customer_data_primary@evidence_52 2026-09-20T12:00:00+00:00
- identity_service/tombstone_7389 [ACCOUNT_TOMBSTONE->REDACT] present=True direct=True ref=True flow=None restore=None ev=evidence_52 :: latest sql:customer_data_primary@evidence_52 2026-09-20T12:00:00+00:00
