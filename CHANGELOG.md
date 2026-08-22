# Changelog

All notable changes to this skill are documented here. This file is the preferred human-readable source for update checks.

| Date | Time | Version | Changes |
|---|---|---|---|
| 2026-08-21 | 12:00 GMT-3 | 2026.08.21 | Content 3.2.0. Added a dedicated section on the colon used as an explanatory crutch (":" introducing an explanation, conclusion or consequence, giving prose a formal-definition feel), with a diagnostic test and a note on when the colon remains correct. Added a deterministic invisible-character sanitization rule (zero-width characters, soft hyphen, bidi marks, Unicode tag block, variation selectors, homoglyphs), applied in every profile and mode, reporting the counts to the user instead of removing them without notice. Added a README section distinguishing invisible characters (removed, verifiable) from statistical watermarks such as SynthID-Text (not promised, not verifiable, degraded only as a side effect of substantive rewriting). Added the corresponding pattern-library rows. Corrected `last_standardized_at`, which had been misdated 2026-08-05. |
| 2026-08-05 | 12:00 GMT-3 | 2026.08.05 | Content 3.1.0: added a dedicated section on negative parallelism ("não é X, é Y") as the top structural AI tell, with frequency-based detection and rewrite guidance; added pattern-library entries for bait transitions and mechanical rule-of-three; HUMANIZADOR.md is now generated from SKILL.md (frontmatter and version-check stripped) to end manual duplication. |
| 2026-06-11 | 12:00 GMT-3 | 2026.06.11 | Removed dead Manus-era files (SKILL.yaml, manifest.txt), consolidated metadata, removed platform-specific mention, declared zero surface capabilities. |
| 2026-06-10 | 19:15 GMT-3 | 2026.06.10 | Synced shared version check protocol to v2: version source priority, HTTP and API check methods that work without Git, session cooldown rule, generalized regression-free update rule. |
| 2026-06-02 | 09:02 GMT-3 | 2026.06.02 | Standardized the repository as an update-aware skill: added origin version check protocol, metadata, governance, contribution guidelines and local validation requirements. |
