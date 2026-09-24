# Data dictionary

JSON locations use RFC 6901-style pointers. For arrays, the first element documents the retained schema; `extent` records array or CSV row counts.

| File | Location | Type | Extent |
|---|---|---|---:|
| `claim_evidence_ledger.csv` | `claim_id` | CSV column | 19 |
| `claim_evidence_ledger.csv` | `claim` | CSV column | 19 |
| `claim_evidence_ledger.csv` | `maturity` | CSV column | 19 |
| `claim_evidence_ledger.csv` | `proof_or_argument` | CSV column | 19 |
| `claim_evidence_ledger.csv` | `implementation` | CSV column | 19 |
| `claim_evidence_ledger.csv` | `test_or_source` | CSV column | 19 |
| `claim_evidence_ledger.csv` | `raw_evidence` | CSV column | 19 |
| `claim_evidence_ledger.csv` | `paper_location` | CSV column | 19 |
| `claim_evidence_ledger.csv` | `fresh_recheck` | CSV column | 19 |
| `claim_evidence_ledger.csv` | `independent_recheck` | CSV column | 19 |
| `docs/claim-evidence-index.json` | `/` | object | 6 |
| `docs/claim-evidence-index.json` | `/artifact_root` | str |  |
| `docs/claim-evidence-index.json` | `/claims` | array | 9 |
| `docs/claim-evidence-index.json` | `/claims/0` | object | 7 |
| `docs/claim-evidence-index.json` | `/claims/0/id` | str |  |
| `docs/claim-evidence-index.json` | `/claims/0/machine_evidence` | object | 1 |
| `docs/claim-evidence-index.json` | `/claims/0/machine_evidence/676354` | array | 3 |
| `docs/claim-evidence-index.json` | `/claims/0/machine_evidence/676354/0` | object | 4 |
| `docs/claim-evidence-index.json` | `/claims/0/machine_evidence/676354/0/file` | str |  |
| `docs/claim-evidence-index.json` | `/claims/0/machine_evidence/676354/0/format` | str |  |
| `docs/claim-evidence-index.json` | `/claims/0/machine_evidence/676354/0/location` | str |  |
| `docs/claim-evidence-index.json` | `/claims/0/machine_evidence/676354/0/value` | int |  |
| `docs/claim-evidence-index.json` | `/claims/0/paper_occurrences` | object | 1 |
| `docs/claim-evidence-index.json` | `/claims/0/paper_occurrences/676354` | array | 0 |
| `docs/claim-evidence-index.json` | `/claims/0/scope` | str |  |
| `docs/claim-evidence-index.json` | `/claims/0/statement` | str |  |
| `docs/claim-evidence-index.json` | `/claims/0/status` | str |  |
| `docs/claim-evidence-index.json` | `/claims/0/values` | array | 1 |
| `docs/claim-evidence-index.json` | `/claims/0/values/0` | int |  |
| `docs/claim-evidence-index.json` | `/interpretation` | str |  |
| `docs/claim-evidence-index.json` | `/machine_parse_errors` | array | 0 |
| `docs/claim-evidence-index.json` | `/missing` | array | 0 |
| `docs/claim-evidence-index.json` | `/schema_version` | int |  |
| `docs/literature-calibration.csv` | `category` | CSV column | 22 |
| `docs/literature-calibration.csv` | `citation_key` | CSV column | 22 |
| `docs/literature-calibration.csv` | `title` | CSV column | 22 |
| `docs/literature-calibration.csv` | `year` | CSV column | 22 |
| `docs/literature-calibration.csv` | `venue` | CSV column | 22 |
| `docs/literature-calibration.csv` | `access_basis` | CSV column | 22 |
| `docs/literature-calibration.csv` | `motivating_problem` | CSV column | 22 |
| `docs/literature-calibration.csv` | `general_principle` | CSV column | 22 |
| `docs/literature-calibration.csv` | `proof_or_performance_argument` | CSV column | 22 |
| `docs/literature-calibration.csv` | `practical_connection` | CSV column | 22 |
| `docs/literature-calibration.csv` | `evaluation_breadth` | CSV column | 22 |
| `docs/literature-calibration.csv` | `artifact_strength` | CSV column | 22 |
| `docs/literature-calibration.csv` | `narrative_sequence` | CSV column | 22 |
| `docs/literature-calibration.csv` | `lesson_for_this_project` | CSV column | 22 |
| `docs/reference-audit.csv` | `citation_key` | CSV column | 9 |
| `docs/reference-audit.csv` | `defect_found` | CSV column | 9 |
| `docs/reference-audit.csv` | `verified_correction` | CSV column | 9 |
| `docs/reference-audit.csv` | `authoritative_identifier` | CSV column | 9 |
| `docs/reference-audit.csv` | `audit_date` | CSV column | 9 |
| `docs/reference-crossref-audit.json` | `/` | object | 2 |
| `docs/reference-crossref-audit.json` | `/records` | array | 54 |
| `docs/reference-crossref-audit.json` | `/records/0` | object | 7 |
| `docs/reference-crossref-audit.json` | `/records/0/author` | str |  |
| `docs/reference-crossref-audit.json` | `/records/0/doi` | str |  |
| `docs/reference-crossref-audit.json` | `/records/0/key` | str |  |
| `docs/reference-crossref-audit.json` | `/records/0/normalized_doi` | str |  |
| `docs/reference-crossref-audit.json` | `/records/0/status` | str |  |
| `docs/reference-crossref-audit.json` | `/records/0/title` | str |  |
| `docs/reference-crossref-audit.json` | `/records/0/year` | str |  |
| `docs/reference-crossref-audit.json` | `/schema_version` | int |  |
| `docs/release-audit.json` | `/` | object | 5 |
| `docs/release-audit.json` | `/artifact` | str |  |
| `docs/release-audit.json` | `/checks` | object | 7 |
| `docs/release-audit.json` | `/checks/archives` | object | 2 |
| `docs/release-audit.json` | `/checks/archives/count` | int |  |
| `docs/release-audit.json` | `/checks/archives/errors` | array | 0 |
| `docs/release-audit.json` | `/checks/claim_index` | object | 2 |
| `docs/release-audit.json` | `/checks/claim_index/output` | str |  |
| `docs/release-audit.json` | `/checks/claim_index/returncode` | int |  |
| `docs/release-audit.json` | `/checks/csv` | object | 2 |
| `docs/release-audit.json` | `/checks/csv/count` | int |  |
| `docs/release-audit.json` | `/checks/csv/errors` | array | 0 |
| `docs/release-audit.json` | `/checks/inventory` | object | 3 |
| `docs/release-audit.json` | `/checks/inventory/bytes` | int |  |
| `docs/release-audit.json` | `/checks/inventory/files` | int |  |
| `docs/release-audit.json` | `/checks/inventory/symlinks` | array | 0 |
| `docs/release-audit.json` | `/checks/json` | object | 2 |
| `docs/release-audit.json` | `/checks/json/count` | int |  |
| `docs/release-audit.json` | `/checks/json/errors` | array | 0 |
| `docs/release-audit.json` | `/checks/paper` | object | 8 |
| `docs/release-audit.json` | `/checks/paper/bib_files` | int |  |
| `docs/release-audit.json` | `/checks/paper/bibliography_entries` | int |  |
| `docs/release-audit.json` | `/checks/paper/cited_keys` | int |  |
| `docs/release-audit.json` | `/checks/paper/issues` | array | 2 |
| `docs/release-audit.json` | `/checks/paper/issues/0` | str |  |
| `docs/release-audit.json` | `/checks/paper/missing_keys` | array | 0 |
| `docs/release-audit.json` | `/checks/paper/present` | bool |  |
| `docs/release-audit.json` | `/checks/paper/tex_files` | int |  |
| `docs/release-audit.json` | `/checks/paper/uncited_keys` | array | 0 |
| `docs/release-audit.json` | `/checks/python` | object | 2 |
| `docs/release-audit.json` | `/checks/python/count` | int |  |
| `docs/release-audit.json` | `/checks/python/errors` | array | 0 |
| `docs/release-audit.json` | `/issues` | array | 2 |
| `docs/release-audit.json` | `/issues/0` | str |  |
| `docs/release-audit.json` | `/schema_version` | int |  |
| `docs/release-audit.json` | `/status` | str |  |
| `docs/third-party-input-inventory.json` | `/` | object | 5 |
| `docs/third-party-input-inventory.json` | `/archive_inputs` | array | 45 |
| `docs/third-party-input-inventory.json` | `/archive_inputs/0` | object | 3 |
| `docs/third-party-input-inventory.json` | `/archive_inputs/0/bytes` | int |  |
| `docs/third-party-input-inventory.json` | `/archive_inputs/0/path` | str |  |
| `docs/third-party-input-inventory.json` | `/archive_inputs/0/sha256` | str |  |
| `docs/third-party-input-inventory.json` | `/candidate_provenance_manifests` | array | 1 |
| `docs/third-party-input-inventory.json` | `/candidate_provenance_manifests/0` | str |  |
| `docs/third-party-input-inventory.json` | `/legal_note` | str |  |
| `docs/third-party-input-inventory.json` | `/license_notice_records` | array | 13 |
| `docs/third-party-input-inventory.json` | `/license_notice_records/0` | object | 3 |
| `docs/third-party-input-inventory.json` | `/license_notice_records/0/bytes` | int |  |
| `docs/third-party-input-inventory.json` | `/license_notice_records/0/path` | str |  |
| `docs/third-party-input-inventory.json` | `/license_notice_records/0/sha256` | str |  |
| `docs/third-party-input-inventory.json` | `/schema_version` | int |  |
| `external_resources.csv` | `name` | CSV column | 68 |
| `external_resources.csv` | `scholarly_or_official_url` | CSV column | 68 |
| `external_resources.csv` | `license_or_access_scope` | CSV column | 68 |
| `external_resources.csv` | `resource_type` | CSV column | 68 |
| `external_resources.csv` | `acquisition_method` | CSV column | 68 |
| `external_resources.csv` | `integration_mode` | CSV column | 68 |
| `external_resources.csv` | `supported_claim` | CSV column | 68 |
| `external_resources.csv` | `internals_modified` | CSV column | 68 |
| `external_resources.csv` | `access_date` | CSV column | 68 |
| `inputs/fixtures/f001.json` | `/` | object | 4 |
| `inputs/fixtures/f001.json` | `/kind` | str |  |
| `inputs/fixtures/f001.json` | `/owners` | array | 1 |
| `inputs/fixtures/f001.json` | `/owners/0` | str |  |
| `inputs/fixtures/f001.json` | `/before` | array | 0 |
| `inputs/fixtures/f001.json` | `/rows` | array | 1 |
| `inputs/fixtures/f001.json` | `/rows/0` | object | 3 |
| `inputs/fixtures/f001.json` | `/rows/0/key` | str |  |
| `inputs/fixtures/f001.json` | `/rows/0/present` | array | 1 |
| `inputs/fixtures/f001.json` | `/rows/0/present/0` | int |  |
| `inputs/fixtures/f001.json` | `/rows/0/good` | array | 1 |
| `inputs/fixtures/f001.json` | `/rows/0/good/0` | int |  |
| `inputs/fixtures/f002.json` | `/` | object | 4 |
| `inputs/fixtures/f002.json` | `/kind` | str |  |
| `inputs/fixtures/f002.json` | `/owners` | array | 1 |
| `inputs/fixtures/f002.json` | `/owners/0` | str |  |
| `inputs/fixtures/f002.json` | `/before` | array | 0 |
| `inputs/fixtures/f002.json` | `/rows` | array | 1 |
| `inputs/fixtures/f002.json` | `/rows/0` | object | 3 |
| `inputs/fixtures/f002.json` | `/rows/0/key` | str |  |
| `inputs/fixtures/f002.json` | `/rows/0/present` | array | 1 |
| `inputs/fixtures/f002.json` | `/rows/0/present/0` | int |  |
| `inputs/fixtures/f002.json` | `/rows/0/good` | array | 1 |
| `inputs/fixtures/f002.json` | `/rows/0/good/0` | int |  |
| `inputs/fixtures/f003.json` | `/` | object | 4 |
| `inputs/fixtures/f003.json` | `/kind` | str |  |
| `inputs/fixtures/f003.json` | `/owners` | array | 2 |
| `inputs/fixtures/f003.json` | `/owners/0` | str |  |
| `inputs/fixtures/f003.json` | `/before` | array | 0 |
| `inputs/fixtures/f003.json` | `/rows` | array | 1 |
| `inputs/fixtures/f003.json` | `/rows/0` | object | 3 |
| `inputs/fixtures/f003.json` | `/rows/0/key` | str |  |
| `inputs/fixtures/f003.json` | `/rows/0/present` | array | 2 |
| `inputs/fixtures/f003.json` | `/rows/0/present/0` | int |  |
| `inputs/fixtures/f003.json` | `/rows/0/good` | array | 2 |
| `inputs/fixtures/f003.json` | `/rows/0/good/0` | int |  |
| `inputs/fixtures/f004.json` | `/` | object | 4 |
| `inputs/fixtures/f004.json` | `/kind` | str |  |
| `inputs/fixtures/f004.json` | `/owners` | array | 2 |
| `inputs/fixtures/f004.json` | `/owners/0` | str |  |
| `inputs/fixtures/f004.json` | `/before` | array | 0 |
| `inputs/fixtures/f004.json` | `/rows` | array | 1 |
| `inputs/fixtures/f004.json` | `/rows/0` | object | 3 |
| `inputs/fixtures/f004.json` | `/rows/0/key` | str |  |
| `inputs/fixtures/f004.json` | `/rows/0/present` | array | 2 |
| `inputs/fixtures/f004.json` | `/rows/0/present/0` | int |  |
| `inputs/fixtures/f004.json` | `/rows/0/good` | array | 2 |
| `inputs/fixtures/f004.json` | `/rows/0/good/0` | int |  |
| `inputs/fixtures/f005.json` | `/` | object | 4 |
| `inputs/fixtures/f005.json` | `/kind` | str |  |
| `inputs/fixtures/f005.json` | `/owners` | array | 2 |
| `inputs/fixtures/f005.json` | `/owners/0` | str |  |
| `inputs/fixtures/f005.json` | `/before` | array | 0 |
| `inputs/fixtures/f005.json` | `/rows` | array | 1 |
| `inputs/fixtures/f005.json` | `/rows/0` | object | 3 |
| `inputs/fixtures/f005.json` | `/rows/0/key` | str |  |
| `inputs/fixtures/f005.json` | `/rows/0/present` | array | 2 |
| `inputs/fixtures/f005.json` | `/rows/0/present/0` | int |  |
| `inputs/fixtures/f005.json` | `/rows/0/good` | array | 0 |
| `inputs/fixtures/f006.json` | `/` | object | 4 |
| `inputs/fixtures/f006.json` | `/kind` | str |  |
| `inputs/fixtures/f006.json` | `/owners` | array | 1 |
| `inputs/fixtures/f006.json` | `/owners/0` | str |  |
| `inputs/fixtures/f006.json` | `/before` | array | 0 |
| `inputs/fixtures/f006.json` | `/rows` | array | 1 |
| `inputs/fixtures/f006.json` | `/rows/0` | object | 3 |
| `inputs/fixtures/f006.json` | `/rows/0/key` | str |  |
| `inputs/fixtures/f006.json` | `/rows/0/present` | array | 0 |
| `inputs/fixtures/f006.json` | `/rows/0/good` | array | 0 |
| `inputs/fixtures/f007.json` | `/` | object | 4 |
| `inputs/fixtures/f007.json` | `/kind` | str |  |
| `inputs/fixtures/f007.json` | `/owners` | array | 2 |
| `inputs/fixtures/f007.json` | `/owners/0` | str |  |
| `inputs/fixtures/f007.json` | `/before` | array | 0 |
| `inputs/fixtures/f007.json` | `/rows` | array | 2 |
| `inputs/fixtures/f007.json` | `/rows/0` | object | 3 |
| `inputs/fixtures/f007.json` | `/rows/0/key` | str |  |
| `inputs/fixtures/f007.json` | `/rows/0/present` | array | 2 |
| `inputs/fixtures/f007.json` | `/rows/0/present/0` | int |  |
| `inputs/fixtures/f007.json` | `/rows/0/good` | array | 1 |
| `inputs/fixtures/f007.json` | `/rows/0/good/0` | int |  |
| `inputs/fixtures/f008.json` | `/` | object | 4 |
| `inputs/fixtures/f008.json` | `/kind` | str |  |
| `inputs/fixtures/f008.json` | `/owners` | array | 2 |
| `inputs/fixtures/f008.json` | `/owners/0` | str |  |
| `inputs/fixtures/f008.json` | `/before` | array | 2 |
| `inputs/fixtures/f008.json` | `/before/0` | array | 2 |
| `inputs/fixtures/f008.json` | `/before/0/0` | int |  |
| `inputs/fixtures/f008.json` | `/rows` | array | 1 |
| `inputs/fixtures/f008.json` | `/rows/0` | object | 3 |
| `inputs/fixtures/f008.json` | `/rows/0/key` | str |  |
| `inputs/fixtures/f008.json` | `/rows/0/present` | array | 2 |
| `inputs/fixtures/f008.json` | `/rows/0/present/0` | int |  |
| `inputs/fixtures/f008.json` | `/rows/0/good` | array | 2 |
| `inputs/fixtures/f008.json` | `/rows/0/good/0` | int |  |
| `inputs/fixtures/f009.json` | `/` | object | 4 |
| `inputs/fixtures/f009.json` | `/kind` | str |  |
| `inputs/fixtures/f009.json` | `/owners` | array | 1 |
| `inputs/fixtures/f009.json` | `/owners/0` | str |  |
| `inputs/fixtures/f009.json` | `/before` | array | 1 |
| `inputs/fixtures/f009.json` | `/before/0` | array | 2 |
| `inputs/fixtures/f009.json` | `/before/0/0` | int |  |
| `inputs/fixtures/f009.json` | `/rows` | array | 1 |
| `inputs/fixtures/f009.json` | `/rows/0` | object | 3 |
| `inputs/fixtures/f009.json` | `/rows/0/key` | str |  |
| `inputs/fixtures/f009.json` | `/rows/0/present` | array | 1 |
| `inputs/fixtures/f009.json` | `/rows/0/present/0` | int |  |
| `inputs/fixtures/f009.json` | `/rows/0/good` | array | 1 |
| `inputs/fixtures/f009.json` | `/rows/0/good/0` | int |  |
| `inputs/fixtures/f010.json` | `/` | object | 4 |
| `inputs/fixtures/f010.json` | `/kind` | str |  |
| `inputs/fixtures/f010.json` | `/owners` | array | 2 |
| `inputs/fixtures/f010.json` | `/owners/0` | str |  |
| `inputs/fixtures/f010.json` | `/before` | array | 0 |
| `inputs/fixtures/f010.json` | `/rows` | array | 0 |
| `inputs/fixtures/f011.json` | `/` | object | 4 |
| `inputs/fixtures/f011.json` | `/kind` | str |  |
| `inputs/fixtures/f011.json` | `/owners` | array | 3 |
| `inputs/fixtures/f011.json` | `/owners/0` | str |  |
| `inputs/fixtures/f011.json` | `/before` | array | 1 |
| `inputs/fixtures/f011.json` | `/before/0` | array | 2 |
| `inputs/fixtures/f011.json` | `/before/0/0` | int |  |
| `inputs/fixtures/f011.json` | `/rows` | array | 1 |
| `inputs/fixtures/f011.json` | `/rows/0` | object | 3 |
| `inputs/fixtures/f011.json` | `/rows/0/key` | str |  |
| `inputs/fixtures/f011.json` | `/rows/0/present` | array | 2 |
| `inputs/fixtures/f011.json` | `/rows/0/present/0` | int |  |
| `inputs/fixtures/f011.json` | `/rows/0/good` | array | 2 |
| `inputs/fixtures/f011.json` | `/rows/0/good/0` | int |  |
| `inputs/fixtures/f012.json` | `/` | object | 4 |
| `inputs/fixtures/f012.json` | `/kind` | str |  |
| `inputs/fixtures/f012.json` | `/owners` | array | 2 |
| `inputs/fixtures/f012.json` | `/owners/0` | str |  |
| `inputs/fixtures/f012.json` | `/before` | array | 0 |
| `inputs/fixtures/f012.json` | `/rows` | array | 2 |
| `inputs/fixtures/f012.json` | `/rows/0` | object | 3 |
| `inputs/fixtures/f012.json` | `/rows/0/key` | str |  |
| `inputs/fixtures/f012.json` | `/rows/0/present` | array | 2 |
| `inputs/fixtures/f012.json` | `/rows/0/present/0` | int |  |
| `inputs/fixtures/f012.json` | `/rows/0/good` | array | 2 |
| `inputs/fixtures/f012.json` | `/rows/0/good/0` | int |  |
| `inputs/fixtures/f013.json` | `/` | object | 4 |
| `inputs/fixtures/f013.json` | `/kind` | str |  |
| `inputs/fixtures/f013.json` | `/owners` | array | 3 |
| `inputs/fixtures/f013.json` | `/owners/0` | str |  |
| `inputs/fixtures/f013.json` | `/before` | array | 0 |
| `inputs/fixtures/f013.json` | `/rows` | array | 2 |
| `inputs/fixtures/f013.json` | `/rows/0` | object | 3 |
| `inputs/fixtures/f013.json` | `/rows/0/key` | str |  |
| `inputs/fixtures/f013.json` | `/rows/0/present` | array | 3 |
| `inputs/fixtures/f013.json` | `/rows/0/present/0` | int |  |
| `inputs/fixtures/f013.json` | `/rows/0/good` | array | 3 |
| `inputs/fixtures/f013.json` | `/rows/0/good/0` | int |  |
| `inputs/fixtures/f014.json` | `/` | object | 4 |
| `inputs/fixtures/f014.json` | `/kind` | str |  |
| `inputs/fixtures/f014.json` | `/owners` | array | 2 |
| `inputs/fixtures/f014.json` | `/owners/0` | str |  |
| `inputs/fixtures/f014.json` | `/before` | array | 1 |
| `inputs/fixtures/f014.json` | `/before/0` | array | 2 |
| `inputs/fixtures/f014.json` | `/before/0/0` | int |  |
| `inputs/fixtures/f014.json` | `/rows` | array | 1 |
| `inputs/fixtures/f014.json` | `/rows/0` | object | 3 |
| `inputs/fixtures/f014.json` | `/rows/0/key` | str |  |
| `inputs/fixtures/f014.json` | `/rows/0/present` | array | 2 |
| `inputs/fixtures/f014.json` | `/rows/0/present/0` | int |  |
| `inputs/fixtures/f014.json` | `/rows/0/good` | array | 2 |
| `inputs/fixtures/f014.json` | `/rows/0/good/0` | int |  |
| `inputs/fixtures/f015.json` | `/` | object | 4 |
| `inputs/fixtures/f015.json` | `/kind` | str |  |
| `inputs/fixtures/f015.json` | `/owners` | array | 3 |
| `inputs/fixtures/f015.json` | `/owners/0` | str |  |
| `inputs/fixtures/f015.json` | `/before` | array | 1 |
| `inputs/fixtures/f015.json` | `/before/0` | array | 2 |
| `inputs/fixtures/f015.json` | `/before/0/0` | int |  |
| `inputs/fixtures/f015.json` | `/rows` | array | 2 |
| `inputs/fixtures/f015.json` | `/rows/0` | object | 3 |
| `inputs/fixtures/f015.json` | `/rows/0/key` | str |  |
| `inputs/fixtures/f015.json` | `/rows/0/present` | array | 3 |
| `inputs/fixtures/f015.json` | `/rows/0/present/0` | int |  |
| `inputs/fixtures/f015.json` | `/rows/0/good` | array | 3 |
| `inputs/fixtures/f015.json` | `/rows/0/good/0` | int |  |
| `inputs/fixtures/f016.json` | `/` | object | 4 |
| `inputs/fixtures/f016.json` | `/kind` | str |  |
| `inputs/fixtures/f016.json` | `/providers` | array | 2 |
| `inputs/fixtures/f016.json` | `/providers/0` | object | 4 |
| `inputs/fixtures/f016.json` | `/providers/0/id` | str |  |
| `inputs/fixtures/f016.json` | `/providers/0/owner` | str |  |
| `inputs/fixtures/f016.json` | `/providers/0/relocations` | array | 1 |
| `inputs/fixtures/f016.json` | `/providers/0/relocations/0` | array | 2 |
| `inputs/fixtures/f016.json` | `/providers/0/relocations/0/0` | str |  |
| `inputs/fixtures/f016.json` | `/providers/0/entries` | array | 1 |
| `inputs/fixtures/f016.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/fixtures/f016.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/fixtures/f016.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/fixtures/f016.json` | `/before` | array | 0 |
| `inputs/fixtures/f016.json` | `/observed` | array | 2 |
| `inputs/fixtures/f016.json` | `/observed/0` | object | 2 |
| `inputs/fixtures/f016.json` | `/observed/0/name` | str |  |
| `inputs/fixtures/f016.json` | `/observed/0/payload` | str |  |
| `inputs/fixtures/f017.json` | `/` | object | 4 |
| `inputs/fixtures/f017.json` | `/kind` | str |  |
| `inputs/fixtures/f017.json` | `/providers` | array | 1 |
| `inputs/fixtures/f017.json` | `/providers/0` | object | 4 |
| `inputs/fixtures/f017.json` | `/providers/0/id` | str |  |
| `inputs/fixtures/f017.json` | `/providers/0/owner` | str |  |
| `inputs/fixtures/f017.json` | `/providers/0/relocations` | array | 2 |
| `inputs/fixtures/f017.json` | `/providers/0/relocations/0` | array | 2 |
| `inputs/fixtures/f017.json` | `/providers/0/relocations/0/0` | str |  |
| `inputs/fixtures/f017.json` | `/providers/0/entries` | array | 1 |
| `inputs/fixtures/f017.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/fixtures/f017.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/fixtures/f017.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/fixtures/f017.json` | `/before` | array | 0 |
| `inputs/fixtures/f017.json` | `/observed` | array | 1 |
| `inputs/fixtures/f017.json` | `/observed/0` | object | 2 |
| `inputs/fixtures/f017.json` | `/observed/0/name` | str |  |
| `inputs/fixtures/f017.json` | `/observed/0/payload` | str |  |
| `inputs/fixtures/f018.json` | `/` | object | 4 |
| `inputs/fixtures/f018.json` | `/kind` | str |  |
| `inputs/fixtures/f018.json` | `/providers` | array | 1 |
| `inputs/fixtures/f018.json` | `/providers/0` | object | 4 |
| `inputs/fixtures/f018.json` | `/providers/0/id` | str |  |
| `inputs/fixtures/f018.json` | `/providers/0/owner` | str |  |
| `inputs/fixtures/f018.json` | `/providers/0/relocations` | array | 2 |
| `inputs/fixtures/f018.json` | `/providers/0/relocations/0` | array | 2 |
| `inputs/fixtures/f018.json` | `/providers/0/relocations/0/0` | str |  |
| `inputs/fixtures/f018.json` | `/providers/0/entries` | array | 1 |
| `inputs/fixtures/f018.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/fixtures/f018.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/fixtures/f018.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/fixtures/f018.json` | `/before` | array | 0 |
| `inputs/fixtures/f018.json` | `/observed` | array | 1 |
| `inputs/fixtures/f018.json` | `/observed/0` | object | 2 |
| `inputs/fixtures/f018.json` | `/observed/0/name` | str |  |
| `inputs/fixtures/f018.json` | `/observed/0/payload` | str |  |
| `inputs/fixtures/f019.json` | `/` | object | 4 |
| `inputs/fixtures/f019.json` | `/kind` | str |  |
| `inputs/fixtures/f019.json` | `/providers` | array | 1 |
| `inputs/fixtures/f019.json` | `/providers/0` | object | 4 |
| `inputs/fixtures/f019.json` | `/providers/0/id` | str |  |
| `inputs/fixtures/f019.json` | `/providers/0/owner` | str |  |
| `inputs/fixtures/f019.json` | `/providers/0/relocations` | array | 2 |
| `inputs/fixtures/f019.json` | `/providers/0/relocations/0` | array | 2 |
| `inputs/fixtures/f019.json` | `/providers/0/relocations/0/0` | str |  |
| `inputs/fixtures/f019.json` | `/providers/0/entries` | array | 2 |
| `inputs/fixtures/f019.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/fixtures/f019.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/fixtures/f019.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/fixtures/f019.json` | `/before` | array | 0 |
| `inputs/fixtures/f019.json` | `/observed` | array | 1 |
| `inputs/fixtures/f019.json` | `/observed/0` | object | 2 |
| `inputs/fixtures/f019.json` | `/observed/0/name` | str |  |
| `inputs/fixtures/f019.json` | `/observed/0/payload` | str |  |
| `inputs/fixtures/f020.json` | `/` | object | 4 |
| `inputs/fixtures/f020.json` | `/kind` | str |  |
| `inputs/fixtures/f020.json` | `/providers` | array | 1 |
| `inputs/fixtures/f020.json` | `/providers/0` | object | 4 |
| `inputs/fixtures/f020.json` | `/providers/0/id` | str |  |
| `inputs/fixtures/f020.json` | `/providers/0/owner` | str |  |
| `inputs/fixtures/f020.json` | `/providers/0/relocations` | array | 1 |
| `inputs/fixtures/f020.json` | `/providers/0/relocations/0` | array | 2 |
| `inputs/fixtures/f020.json` | `/providers/0/relocations/0/0` | str |  |
| `inputs/fixtures/f020.json` | `/providers/0/entries` | array | 1 |
| `inputs/fixtures/f020.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/fixtures/f020.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/fixtures/f020.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/fixtures/f020.json` | `/before` | array | 0 |
| `inputs/fixtures/f020.json` | `/observed` | array | 1 |
| `inputs/fixtures/f020.json` | `/observed/0` | object | 2 |
| `inputs/fixtures/f020.json` | `/observed/0/name` | str |  |
| `inputs/fixtures/f020.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g001.json` | `/` | object | 4 |
| `inputs/generated/g001.json` | `/kind` | str |  |
| `inputs/generated/g001.json` | `/providers` | array | 2 |
| `inputs/generated/g001.json` | `/providers/0` | object | 4 |
| `inputs/generated/g001.json` | `/providers/0/id` | str |  |
| `inputs/generated/g001.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g001.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g001.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g001.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g001.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g001.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g001.json` | `/before` | array | 0 |
| `inputs/generated/g001.json` | `/observed` | array | 1 |
| `inputs/generated/g001.json` | `/observed/0` | object | 2 |
| `inputs/generated/g001.json` | `/observed/0/name` | str |  |
| `inputs/generated/g001.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g002.json` | `/` | object | 4 |
| `inputs/generated/g002.json` | `/kind` | str |  |
| `inputs/generated/g002.json` | `/providers` | array | 3 |
| `inputs/generated/g002.json` | `/providers/0` | object | 4 |
| `inputs/generated/g002.json` | `/providers/0/id` | str |  |
| `inputs/generated/g002.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g002.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g002.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g002.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g002.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g002.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g002.json` | `/before` | array | 0 |
| `inputs/generated/g002.json` | `/observed` | array | 1 |
| `inputs/generated/g002.json` | `/observed/0` | object | 2 |
| `inputs/generated/g002.json` | `/observed/0/name` | str |  |
| `inputs/generated/g002.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g003.json` | `/` | object | 4 |
| `inputs/generated/g003.json` | `/kind` | str |  |
| `inputs/generated/g003.json` | `/providers` | array | 5 |
| `inputs/generated/g003.json` | `/providers/0` | object | 4 |
| `inputs/generated/g003.json` | `/providers/0/id` | str |  |
| `inputs/generated/g003.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g003.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g003.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g003.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g003.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g003.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g003.json` | `/before` | array | 0 |
| `inputs/generated/g003.json` | `/observed` | array | 1 |
| `inputs/generated/g003.json` | `/observed/0` | object | 2 |
| `inputs/generated/g003.json` | `/observed/0/name` | str |  |
| `inputs/generated/g003.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g004.json` | `/` | object | 4 |
| `inputs/generated/g004.json` | `/kind` | str |  |
| `inputs/generated/g004.json` | `/providers` | array | 8 |
| `inputs/generated/g004.json` | `/providers/0` | object | 4 |
| `inputs/generated/g004.json` | `/providers/0/id` | str |  |
| `inputs/generated/g004.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g004.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g004.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g004.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g004.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g004.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g004.json` | `/before` | array | 0 |
| `inputs/generated/g004.json` | `/observed` | array | 1 |
| `inputs/generated/g004.json` | `/observed/0` | object | 2 |
| `inputs/generated/g004.json` | `/observed/0/name` | str |  |
| `inputs/generated/g004.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g005.json` | `/` | object | 4 |
| `inputs/generated/g005.json` | `/kind` | str |  |
| `inputs/generated/g005.json` | `/providers` | array | 16 |
| `inputs/generated/g005.json` | `/providers/0` | object | 4 |
| `inputs/generated/g005.json` | `/providers/0/id` | str |  |
| `inputs/generated/g005.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g005.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g005.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g005.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g005.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g005.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g005.json` | `/before` | array | 0 |
| `inputs/generated/g005.json` | `/observed` | array | 1 |
| `inputs/generated/g005.json` | `/observed/0` | object | 2 |
| `inputs/generated/g005.json` | `/observed/0/name` | str |  |
| `inputs/generated/g005.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g006.json` | `/` | object | 4 |
| `inputs/generated/g006.json` | `/kind` | str |  |
| `inputs/generated/g006.json` | `/providers` | array | 2 |
| `inputs/generated/g006.json` | `/providers/0` | object | 4 |
| `inputs/generated/g006.json` | `/providers/0/id` | str |  |
| `inputs/generated/g006.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g006.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g006.json` | `/providers/0/entries` | array | 2 |
| `inputs/generated/g006.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g006.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g006.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g006.json` | `/before` | array | 0 |
| `inputs/generated/g006.json` | `/observed` | array | 2 |
| `inputs/generated/g006.json` | `/observed/0` | object | 2 |
| `inputs/generated/g006.json` | `/observed/0/name` | str |  |
| `inputs/generated/g006.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g007.json` | `/` | object | 4 |
| `inputs/generated/g007.json` | `/kind` | str |  |
| `inputs/generated/g007.json` | `/providers` | array | 3 |
| `inputs/generated/g007.json` | `/providers/0` | object | 4 |
| `inputs/generated/g007.json` | `/providers/0/id` | str |  |
| `inputs/generated/g007.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g007.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g007.json` | `/providers/0/entries` | array | 2 |
| `inputs/generated/g007.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g007.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g007.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g007.json` | `/before` | array | 0 |
| `inputs/generated/g007.json` | `/observed` | array | 3 |
| `inputs/generated/g007.json` | `/observed/0` | object | 2 |
| `inputs/generated/g007.json` | `/observed/0/name` | str |  |
| `inputs/generated/g007.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g008.json` | `/` | object | 4 |
| `inputs/generated/g008.json` | `/kind` | str |  |
| `inputs/generated/g008.json` | `/providers` | array | 5 |
| `inputs/generated/g008.json` | `/providers/0` | object | 4 |
| `inputs/generated/g008.json` | `/providers/0/id` | str |  |
| `inputs/generated/g008.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g008.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g008.json` | `/providers/0/entries` | array | 2 |
| `inputs/generated/g008.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g008.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g008.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g008.json` | `/before` | array | 0 |
| `inputs/generated/g008.json` | `/observed` | array | 5 |
| `inputs/generated/g008.json` | `/observed/0` | object | 2 |
| `inputs/generated/g008.json` | `/observed/0/name` | str |  |
| `inputs/generated/g008.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g009.json` | `/` | object | 4 |
| `inputs/generated/g009.json` | `/kind` | str |  |
| `inputs/generated/g009.json` | `/providers` | array | 8 |
| `inputs/generated/g009.json` | `/providers/0` | object | 4 |
| `inputs/generated/g009.json` | `/providers/0/id` | str |  |
| `inputs/generated/g009.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g009.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g009.json` | `/providers/0/entries` | array | 2 |
| `inputs/generated/g009.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g009.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g009.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g009.json` | `/before` | array | 0 |
| `inputs/generated/g009.json` | `/observed` | array | 8 |
| `inputs/generated/g009.json` | `/observed/0` | object | 2 |
| `inputs/generated/g009.json` | `/observed/0/name` | str |  |
| `inputs/generated/g009.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g010.json` | `/` | object | 4 |
| `inputs/generated/g010.json` | `/kind` | str |  |
| `inputs/generated/g010.json` | `/providers` | array | 16 |
| `inputs/generated/g010.json` | `/providers/0` | object | 4 |
| `inputs/generated/g010.json` | `/providers/0/id` | str |  |
| `inputs/generated/g010.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g010.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g010.json` | `/providers/0/entries` | array | 2 |
| `inputs/generated/g010.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g010.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g010.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g010.json` | `/before` | array | 0 |
| `inputs/generated/g010.json` | `/observed` | array | 16 |
| `inputs/generated/g010.json` | `/observed/0` | object | 2 |
| `inputs/generated/g010.json` | `/observed/0/name` | str |  |
| `inputs/generated/g010.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g011.json` | `/` | object | 4 |
| `inputs/generated/g011.json` | `/kind` | str |  |
| `inputs/generated/g011.json` | `/providers` | array | 2 |
| `inputs/generated/g011.json` | `/providers/0` | object | 4 |
| `inputs/generated/g011.json` | `/providers/0/id` | str |  |
| `inputs/generated/g011.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g011.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g011.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g011.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g011.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g011.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g011.json` | `/before` | array | 0 |
| `inputs/generated/g011.json` | `/observed` | array | 1 |
| `inputs/generated/g011.json` | `/observed/0` | object | 2 |
| `inputs/generated/g011.json` | `/observed/0/name` | str |  |
| `inputs/generated/g011.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g012.json` | `/` | object | 4 |
| `inputs/generated/g012.json` | `/kind` | str |  |
| `inputs/generated/g012.json` | `/providers` | array | 3 |
| `inputs/generated/g012.json` | `/providers/0` | object | 4 |
| `inputs/generated/g012.json` | `/providers/0/id` | str |  |
| `inputs/generated/g012.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g012.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g012.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g012.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g012.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g012.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g012.json` | `/before` | array | 0 |
| `inputs/generated/g012.json` | `/observed` | array | 1 |
| `inputs/generated/g012.json` | `/observed/0` | object | 2 |
| `inputs/generated/g012.json` | `/observed/0/name` | str |  |
| `inputs/generated/g012.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g013.json` | `/` | object | 4 |
| `inputs/generated/g013.json` | `/kind` | str |  |
| `inputs/generated/g013.json` | `/providers` | array | 5 |
| `inputs/generated/g013.json` | `/providers/0` | object | 4 |
| `inputs/generated/g013.json` | `/providers/0/id` | str |  |
| `inputs/generated/g013.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g013.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g013.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g013.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g013.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g013.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g013.json` | `/before` | array | 0 |
| `inputs/generated/g013.json` | `/observed` | array | 1 |
| `inputs/generated/g013.json` | `/observed/0` | object | 2 |
| `inputs/generated/g013.json` | `/observed/0/name` | str |  |
| `inputs/generated/g013.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g014.json` | `/` | object | 4 |
| `inputs/generated/g014.json` | `/kind` | str |  |
| `inputs/generated/g014.json` | `/providers` | array | 8 |
| `inputs/generated/g014.json` | `/providers/0` | object | 4 |
| `inputs/generated/g014.json` | `/providers/0/id` | str |  |
| `inputs/generated/g014.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g014.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g014.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g014.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g014.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g014.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g014.json` | `/before` | array | 0 |
| `inputs/generated/g014.json` | `/observed` | array | 1 |
| `inputs/generated/g014.json` | `/observed/0` | object | 2 |
| `inputs/generated/g014.json` | `/observed/0/name` | str |  |
| `inputs/generated/g014.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g015.json` | `/` | object | 4 |
| `inputs/generated/g015.json` | `/kind` | str |  |
| `inputs/generated/g015.json` | `/providers` | array | 16 |
| `inputs/generated/g015.json` | `/providers/0` | object | 4 |
| `inputs/generated/g015.json` | `/providers/0/id` | str |  |
| `inputs/generated/g015.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g015.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g015.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g015.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g015.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g015.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g015.json` | `/before` | array | 0 |
| `inputs/generated/g015.json` | `/observed` | array | 1 |
| `inputs/generated/g015.json` | `/observed/0` | object | 2 |
| `inputs/generated/g015.json` | `/observed/0/name` | str |  |
| `inputs/generated/g015.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g016.json` | `/` | object | 4 |
| `inputs/generated/g016.json` | `/kind` | str |  |
| `inputs/generated/g016.json` | `/providers` | array | 2 |
| `inputs/generated/g016.json` | `/providers/0` | object | 4 |
| `inputs/generated/g016.json` | `/providers/0/id` | str |  |
| `inputs/generated/g016.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g016.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g016.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g016.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g016.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g016.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g016.json` | `/before` | array | 1 |
| `inputs/generated/g016.json` | `/before/0` | array | 2 |
| `inputs/generated/g016.json` | `/before/0/0` | int |  |
| `inputs/generated/g016.json` | `/observed` | array | 1 |
| `inputs/generated/g016.json` | `/observed/0` | object | 2 |
| `inputs/generated/g016.json` | `/observed/0/name` | str |  |
| `inputs/generated/g016.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g017.json` | `/` | object | 4 |
| `inputs/generated/g017.json` | `/kind` | str |  |
| `inputs/generated/g017.json` | `/providers` | array | 3 |
| `inputs/generated/g017.json` | `/providers/0` | object | 4 |
| `inputs/generated/g017.json` | `/providers/0/id` | str |  |
| `inputs/generated/g017.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g017.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g017.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g017.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g017.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g017.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g017.json` | `/before` | array | 2 |
| `inputs/generated/g017.json` | `/before/0` | array | 2 |
| `inputs/generated/g017.json` | `/before/0/0` | int |  |
| `inputs/generated/g017.json` | `/observed` | array | 1 |
| `inputs/generated/g017.json` | `/observed/0` | object | 2 |
| `inputs/generated/g017.json` | `/observed/0/name` | str |  |
| `inputs/generated/g017.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g018.json` | `/` | object | 4 |
| `inputs/generated/g018.json` | `/kind` | str |  |
| `inputs/generated/g018.json` | `/providers` | array | 5 |
| `inputs/generated/g018.json` | `/providers/0` | object | 4 |
| `inputs/generated/g018.json` | `/providers/0/id` | str |  |
| `inputs/generated/g018.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g018.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g018.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g018.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g018.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g018.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g018.json` | `/before` | array | 4 |
| `inputs/generated/g018.json` | `/before/0` | array | 2 |
| `inputs/generated/g018.json` | `/before/0/0` | int |  |
| `inputs/generated/g018.json` | `/observed` | array | 1 |
| `inputs/generated/g018.json` | `/observed/0` | object | 2 |
| `inputs/generated/g018.json` | `/observed/0/name` | str |  |
| `inputs/generated/g018.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g019.json` | `/` | object | 4 |
| `inputs/generated/g019.json` | `/kind` | str |  |
| `inputs/generated/g019.json` | `/providers` | array | 8 |
| `inputs/generated/g019.json` | `/providers/0` | object | 4 |
| `inputs/generated/g019.json` | `/providers/0/id` | str |  |
| `inputs/generated/g019.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g019.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g019.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g019.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g019.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g019.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g019.json` | `/before` | array | 7 |
| `inputs/generated/g019.json` | `/before/0` | array | 2 |
| `inputs/generated/g019.json` | `/before/0/0` | int |  |
| `inputs/generated/g019.json` | `/observed` | array | 1 |
| `inputs/generated/g019.json` | `/observed/0` | object | 2 |
| `inputs/generated/g019.json` | `/observed/0/name` | str |  |
| `inputs/generated/g019.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g020.json` | `/` | object | 4 |
| `inputs/generated/g020.json` | `/kind` | str |  |
| `inputs/generated/g020.json` | `/providers` | array | 16 |
| `inputs/generated/g020.json` | `/providers/0` | object | 4 |
| `inputs/generated/g020.json` | `/providers/0/id` | str |  |
| `inputs/generated/g020.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g020.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g020.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g020.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g020.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g020.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g020.json` | `/before` | array | 15 |
| `inputs/generated/g020.json` | `/before/0` | array | 2 |
| `inputs/generated/g020.json` | `/before/0/0` | int |  |
| `inputs/generated/g020.json` | `/observed` | array | 1 |
| `inputs/generated/g020.json` | `/observed/0` | object | 2 |
| `inputs/generated/g020.json` | `/observed/0/name` | str |  |
| `inputs/generated/g020.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g021.json` | `/` | object | 4 |
| `inputs/generated/g021.json` | `/kind` | str |  |
| `inputs/generated/g021.json` | `/providers` | array | 2 |
| `inputs/generated/g021.json` | `/providers/0` | object | 4 |
| `inputs/generated/g021.json` | `/providers/0/id` | str |  |
| `inputs/generated/g021.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g021.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g021.json` | `/providers/0/entries` | array | 2 |
| `inputs/generated/g021.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g021.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g021.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g021.json` | `/before` | array | 0 |
| `inputs/generated/g021.json` | `/observed` | array | 2 |
| `inputs/generated/g021.json` | `/observed/0` | object | 2 |
| `inputs/generated/g021.json` | `/observed/0/name` | str |  |
| `inputs/generated/g021.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g022.json` | `/` | object | 4 |
| `inputs/generated/g022.json` | `/kind` | str |  |
| `inputs/generated/g022.json` | `/providers` | array | 3 |
| `inputs/generated/g022.json` | `/providers/0` | object | 4 |
| `inputs/generated/g022.json` | `/providers/0/id` | str |  |
| `inputs/generated/g022.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g022.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g022.json` | `/providers/0/entries` | array | 2 |
| `inputs/generated/g022.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g022.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g022.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g022.json` | `/before` | array | 0 |
| `inputs/generated/g022.json` | `/observed` | array | 2 |
| `inputs/generated/g022.json` | `/observed/0` | object | 2 |
| `inputs/generated/g022.json` | `/observed/0/name` | str |  |
| `inputs/generated/g022.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g023.json` | `/` | object | 4 |
| `inputs/generated/g023.json` | `/kind` | str |  |
| `inputs/generated/g023.json` | `/providers` | array | 5 |
| `inputs/generated/g023.json` | `/providers/0` | object | 4 |
| `inputs/generated/g023.json` | `/providers/0/id` | str |  |
| `inputs/generated/g023.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g023.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g023.json` | `/providers/0/entries` | array | 2 |
| `inputs/generated/g023.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g023.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g023.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g023.json` | `/before` | array | 0 |
| `inputs/generated/g023.json` | `/observed` | array | 2 |
| `inputs/generated/g023.json` | `/observed/0` | object | 2 |
| `inputs/generated/g023.json` | `/observed/0/name` | str |  |
| `inputs/generated/g023.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g024.json` | `/` | object | 4 |
| `inputs/generated/g024.json` | `/kind` | str |  |
| `inputs/generated/g024.json` | `/providers` | array | 8 |
| `inputs/generated/g024.json` | `/providers/0` | object | 4 |
| `inputs/generated/g024.json` | `/providers/0/id` | str |  |
| `inputs/generated/g024.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g024.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g024.json` | `/providers/0/entries` | array | 2 |
| `inputs/generated/g024.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g024.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g024.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g024.json` | `/before` | array | 0 |
| `inputs/generated/g024.json` | `/observed` | array | 2 |
| `inputs/generated/g024.json` | `/observed/0` | object | 2 |
| `inputs/generated/g024.json` | `/observed/0/name` | str |  |
| `inputs/generated/g024.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g025.json` | `/` | object | 4 |
| `inputs/generated/g025.json` | `/kind` | str |  |
| `inputs/generated/g025.json` | `/providers` | array | 16 |
| `inputs/generated/g025.json` | `/providers/0` | object | 4 |
| `inputs/generated/g025.json` | `/providers/0/id` | str |  |
| `inputs/generated/g025.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g025.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g025.json` | `/providers/0/entries` | array | 2 |
| `inputs/generated/g025.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g025.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g025.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g025.json` | `/before` | array | 0 |
| `inputs/generated/g025.json` | `/observed` | array | 2 |
| `inputs/generated/g025.json` | `/observed/0` | object | 2 |
| `inputs/generated/g025.json` | `/observed/0/name` | str |  |
| `inputs/generated/g025.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g026.json` | `/` | object | 4 |
| `inputs/generated/g026.json` | `/kind` | str |  |
| `inputs/generated/g026.json` | `/providers` | array | 2 |
| `inputs/generated/g026.json` | `/providers/0` | object | 4 |
| `inputs/generated/g026.json` | `/providers/0/id` | str |  |
| `inputs/generated/g026.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g026.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g026.json` | `/providers/0/entries` | array | 3 |
| `inputs/generated/g026.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g026.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g026.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g026.json` | `/before` | array | 0 |
| `inputs/generated/g026.json` | `/observed` | array | 3 |
| `inputs/generated/g026.json` | `/observed/0` | object | 2 |
| `inputs/generated/g026.json` | `/observed/0/name` | str |  |
| `inputs/generated/g026.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g027.json` | `/` | object | 4 |
| `inputs/generated/g027.json` | `/kind` | str |  |
| `inputs/generated/g027.json` | `/providers` | array | 3 |
| `inputs/generated/g027.json` | `/providers/0` | object | 4 |
| `inputs/generated/g027.json` | `/providers/0/id` | str |  |
| `inputs/generated/g027.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g027.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g027.json` | `/providers/0/entries` | array | 3 |
| `inputs/generated/g027.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g027.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g027.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g027.json` | `/before` | array | 0 |
| `inputs/generated/g027.json` | `/observed` | array | 4 |
| `inputs/generated/g027.json` | `/observed/0` | object | 2 |
| `inputs/generated/g027.json` | `/observed/0/name` | str |  |
| `inputs/generated/g027.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g028.json` | `/` | object | 4 |
| `inputs/generated/g028.json` | `/kind` | str |  |
| `inputs/generated/g028.json` | `/providers` | array | 5 |
| `inputs/generated/g028.json` | `/providers/0` | object | 4 |
| `inputs/generated/g028.json` | `/providers/0/id` | str |  |
| `inputs/generated/g028.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g028.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g028.json` | `/providers/0/entries` | array | 3 |
| `inputs/generated/g028.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g028.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g028.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g028.json` | `/before` | array | 0 |
| `inputs/generated/g028.json` | `/observed` | array | 6 |
| `inputs/generated/g028.json` | `/observed/0` | object | 2 |
| `inputs/generated/g028.json` | `/observed/0/name` | str |  |
| `inputs/generated/g028.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g029.json` | `/` | object | 4 |
| `inputs/generated/g029.json` | `/kind` | str |  |
| `inputs/generated/g029.json` | `/providers` | array | 8 |
| `inputs/generated/g029.json` | `/providers/0` | object | 4 |
| `inputs/generated/g029.json` | `/providers/0/id` | str |  |
| `inputs/generated/g029.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g029.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g029.json` | `/providers/0/entries` | array | 3 |
| `inputs/generated/g029.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g029.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g029.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g029.json` | `/before` | array | 0 |
| `inputs/generated/g029.json` | `/observed` | array | 9 |
| `inputs/generated/g029.json` | `/observed/0` | object | 2 |
| `inputs/generated/g029.json` | `/observed/0/name` | str |  |
| `inputs/generated/g029.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g030.json` | `/` | object | 4 |
| `inputs/generated/g030.json` | `/kind` | str |  |
| `inputs/generated/g030.json` | `/providers` | array | 16 |
| `inputs/generated/g030.json` | `/providers/0` | object | 4 |
| `inputs/generated/g030.json` | `/providers/0/id` | str |  |
| `inputs/generated/g030.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g030.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g030.json` | `/providers/0/entries` | array | 3 |
| `inputs/generated/g030.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g030.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g030.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g030.json` | `/before` | array | 0 |
| `inputs/generated/g030.json` | `/observed` | array | 17 |
| `inputs/generated/g030.json` | `/observed/0` | object | 2 |
| `inputs/generated/g030.json` | `/observed/0/name` | str |  |
| `inputs/generated/g030.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g031.json` | `/` | object | 4 |
| `inputs/generated/g031.json` | `/kind` | str |  |
| `inputs/generated/g031.json` | `/providers` | array | 2 |
| `inputs/generated/g031.json` | `/providers/0` | object | 4 |
| `inputs/generated/g031.json` | `/providers/0/id` | str |  |
| `inputs/generated/g031.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g031.json` | `/providers/0/relocations` | array | 1 |
| `inputs/generated/g031.json` | `/providers/0/relocations/0` | array | 2 |
| `inputs/generated/g031.json` | `/providers/0/relocations/0/0` | str |  |
| `inputs/generated/g031.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g031.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g031.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g031.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g031.json` | `/before` | array | 0 |
| `inputs/generated/g031.json` | `/observed` | array | 1 |
| `inputs/generated/g031.json` | `/observed/0` | object | 2 |
| `inputs/generated/g031.json` | `/observed/0/name` | str |  |
| `inputs/generated/g031.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g032.json` | `/` | object | 4 |
| `inputs/generated/g032.json` | `/kind` | str |  |
| `inputs/generated/g032.json` | `/providers` | array | 3 |
| `inputs/generated/g032.json` | `/providers/0` | object | 4 |
| `inputs/generated/g032.json` | `/providers/0/id` | str |  |
| `inputs/generated/g032.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g032.json` | `/providers/0/relocations` | array | 1 |
| `inputs/generated/g032.json` | `/providers/0/relocations/0` | array | 2 |
| `inputs/generated/g032.json` | `/providers/0/relocations/0/0` | str |  |
| `inputs/generated/g032.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g032.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g032.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g032.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g032.json` | `/before` | array | 0 |
| `inputs/generated/g032.json` | `/observed` | array | 1 |
| `inputs/generated/g032.json` | `/observed/0` | object | 2 |
| `inputs/generated/g032.json` | `/observed/0/name` | str |  |
| `inputs/generated/g032.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g033.json` | `/` | object | 4 |
| `inputs/generated/g033.json` | `/kind` | str |  |
| `inputs/generated/g033.json` | `/providers` | array | 5 |
| `inputs/generated/g033.json` | `/providers/0` | object | 4 |
| `inputs/generated/g033.json` | `/providers/0/id` | str |  |
| `inputs/generated/g033.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g033.json` | `/providers/0/relocations` | array | 1 |
| `inputs/generated/g033.json` | `/providers/0/relocations/0` | array | 2 |
| `inputs/generated/g033.json` | `/providers/0/relocations/0/0` | str |  |
| `inputs/generated/g033.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g033.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g033.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g033.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g033.json` | `/before` | array | 0 |
| `inputs/generated/g033.json` | `/observed` | array | 1 |
| `inputs/generated/g033.json` | `/observed/0` | object | 2 |
| `inputs/generated/g033.json` | `/observed/0/name` | str |  |
| `inputs/generated/g033.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g034.json` | `/` | object | 4 |
| `inputs/generated/g034.json` | `/kind` | str |  |
| `inputs/generated/g034.json` | `/providers` | array | 8 |
| `inputs/generated/g034.json` | `/providers/0` | object | 4 |
| `inputs/generated/g034.json` | `/providers/0/id` | str |  |
| `inputs/generated/g034.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g034.json` | `/providers/0/relocations` | array | 1 |
| `inputs/generated/g034.json` | `/providers/0/relocations/0` | array | 2 |
| `inputs/generated/g034.json` | `/providers/0/relocations/0/0` | str |  |
| `inputs/generated/g034.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g034.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g034.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g034.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g034.json` | `/before` | array | 0 |
| `inputs/generated/g034.json` | `/observed` | array | 1 |
| `inputs/generated/g034.json` | `/observed/0` | object | 2 |
| `inputs/generated/g034.json` | `/observed/0/name` | str |  |
| `inputs/generated/g034.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g035.json` | `/` | object | 4 |
| `inputs/generated/g035.json` | `/kind` | str |  |
| `inputs/generated/g035.json` | `/providers` | array | 16 |
| `inputs/generated/g035.json` | `/providers/0` | object | 4 |
| `inputs/generated/g035.json` | `/providers/0/id` | str |  |
| `inputs/generated/g035.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g035.json` | `/providers/0/relocations` | array | 1 |
| `inputs/generated/g035.json` | `/providers/0/relocations/0` | array | 2 |
| `inputs/generated/g035.json` | `/providers/0/relocations/0/0` | str |  |
| `inputs/generated/g035.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g035.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g035.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g035.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g035.json` | `/before` | array | 0 |
| `inputs/generated/g035.json` | `/observed` | array | 1 |
| `inputs/generated/g035.json` | `/observed/0` | object | 2 |
| `inputs/generated/g035.json` | `/observed/0/name` | str |  |
| `inputs/generated/g035.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g036.json` | `/` | object | 4 |
| `inputs/generated/g036.json` | `/kind` | str |  |
| `inputs/generated/g036.json` | `/providers` | array | 2 |
| `inputs/generated/g036.json` | `/providers/0` | object | 4 |
| `inputs/generated/g036.json` | `/providers/0/id` | str |  |
| `inputs/generated/g036.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g036.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g036.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g036.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g036.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g036.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g036.json` | `/before` | array | 0 |
| `inputs/generated/g036.json` | `/observed` | array | 1 |
| `inputs/generated/g036.json` | `/observed/0` | object | 2 |
| `inputs/generated/g036.json` | `/observed/0/name` | str |  |
| `inputs/generated/g036.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g037.json` | `/` | object | 4 |
| `inputs/generated/g037.json` | `/kind` | str |  |
| `inputs/generated/g037.json` | `/providers` | array | 3 |
| `inputs/generated/g037.json` | `/providers/0` | object | 4 |
| `inputs/generated/g037.json` | `/providers/0/id` | str |  |
| `inputs/generated/g037.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g037.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g037.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g037.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g037.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g037.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g037.json` | `/before` | array | 0 |
| `inputs/generated/g037.json` | `/observed` | array | 1 |
| `inputs/generated/g037.json` | `/observed/0` | object | 2 |
| `inputs/generated/g037.json` | `/observed/0/name` | str |  |
| `inputs/generated/g037.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g038.json` | `/` | object | 4 |
| `inputs/generated/g038.json` | `/kind` | str |  |
| `inputs/generated/g038.json` | `/providers` | array | 5 |
| `inputs/generated/g038.json` | `/providers/0` | object | 4 |
| `inputs/generated/g038.json` | `/providers/0/id` | str |  |
| `inputs/generated/g038.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g038.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g038.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g038.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g038.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g038.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g038.json` | `/before` | array | 0 |
| `inputs/generated/g038.json` | `/observed` | array | 1 |
| `inputs/generated/g038.json` | `/observed/0` | object | 2 |
| `inputs/generated/g038.json` | `/observed/0/name` | str |  |
| `inputs/generated/g038.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g039.json` | `/` | object | 4 |
| `inputs/generated/g039.json` | `/kind` | str |  |
| `inputs/generated/g039.json` | `/providers` | array | 8 |
| `inputs/generated/g039.json` | `/providers/0` | object | 4 |
| `inputs/generated/g039.json` | `/providers/0/id` | str |  |
| `inputs/generated/g039.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g039.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g039.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g039.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g039.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g039.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g039.json` | `/before` | array | 0 |
| `inputs/generated/g039.json` | `/observed` | array | 1 |
| `inputs/generated/g039.json` | `/observed/0` | object | 2 |
| `inputs/generated/g039.json` | `/observed/0/name` | str |  |
| `inputs/generated/g039.json` | `/observed/0/payload` | str |  |
| `inputs/generated/g040.json` | `/` | object | 4 |
| `inputs/generated/g040.json` | `/kind` | str |  |
| `inputs/generated/g040.json` | `/providers` | array | 16 |
| `inputs/generated/g040.json` | `/providers/0` | object | 4 |
| `inputs/generated/g040.json` | `/providers/0/id` | str |  |
| `inputs/generated/g040.json` | `/providers/0/owner` | str |  |
| `inputs/generated/g040.json` | `/providers/0/relocations` | array | 0 |
| `inputs/generated/g040.json` | `/providers/0/entries` | array | 1 |
| `inputs/generated/g040.json` | `/providers/0/entries/0` | object | 2 |
| `inputs/generated/g040.json` | `/providers/0/entries/0/name` | str |  |
| `inputs/generated/g040.json` | `/providers/0/entries/0/payload` | str |  |
| `inputs/generated/g040.json` | `/before` | array | 0 |
| `inputs/generated/g040.json` | `/observed` | array | 1 |
| `inputs/generated/g040.json` | `/observed/0` | object | 2 |
| `inputs/generated/g040.json` | `/observed/0/name` | str |  |
| `inputs/generated/g040.json` | `/observed/0/payload` | str |  |
| `inputs/index.json` | `/` | array | 60 |
| `inputs/index.json` | `/0` | object | 6 |
| `inputs/index.json` | `/0/case` | str |  |
| `inputs/index.json` | `/0/group` | str |  |
| `inputs/index.json` | `/0/phenomenon` | str |  |
| `inputs/index.json` | `/0/providers` | int |  |
| `inputs/index.json` | `/0/path` | str |  |
| `inputs/index.json` | `/0/admission` | str |  |
| `inputs/public/collision_pairs.csv` | `pair_id` | CSV column | 40 |
| `inputs/public/collision_pairs.csv` | `left` | CSV column | 40 |
| `inputs/public/collision_pairs.csv` | `right` | CSV column | 40 |
| `inputs/public/collision_pairs.csv` | `kind` | CSV column | 40 |
| `inputs/public/collision_pairs.csv` | `shared_nonmeta` | CSV column | 40 |
| `inputs/public/collision_pairs.csv` | `equal_nonmeta` | CSV column | 40 |
| `inputs/public/collision_pairs.csv` | `different_nonmeta` | CSV column | 40 |
| `inputs/public/providers.csv` | `archive` | CSV column | 45 |
| `inputs/public/providers.csv` | `owner` | CSV column | 45 |
| `inputs/public/providers.csv` | `package` | CSV column | 45 |
| `inputs/public/providers.csv` | `package_version` | CSV column | 45 |
| `inputs/public/providers.csv` | `source_package` | CSV column | 45 |
| `inputs/public/providers.csv` | `homepage` | CSV column | 45 |
| `inputs/public/providers.csv` | `bytes` | CSV column | 45 |
| `inputs/public/selection.json` | `/` | object | 10 |
| `inputs/public/selection.json` | `/corpus_definition` | str |  |
| `inputs/public/selection.json` | `/selection_rule` | str |  |
| `inputs/public/selection.json` | `/pair_count` | int |  |
| `inputs/public/selection.json` | `/build_count` | int |  |
| `inputs/public/selection.json` | `/provider_count` | int |  |
| `inputs/public/selection.json` | `/builder_count` | int |  |
| `inputs/public/selection.json` | `/category_counts` | object | 3 |
| `inputs/public/selection.json` | `/category_counts/equal-only` | int |  |
| `inputs/public/selection.json` | `/category_counts/different-only` | int |  |
| `inputs/public/selection.json` | `/category_counts/mixed` | int |  |
| `inputs/public/selection.json` | `/builder_archives` | array | 2 |
| `inputs/public/selection.json` | `/builder_archives/0` | str |  |
| `inputs/public/selection.json` | `/license_records` | str |  |
| `inputs/public/selection.json` | `/scope_note` | str |  |
| `results/campaign_summary.json` | `/` | object | 19 |
| `results/campaign_summary.json` | `/cases` | int |  |
| `results/campaign_summary.json` | `/generated_cases` | int |  |
| `results/campaign_summary.json` | `/boundary_fixtures` | int |  |
| `results/campaign_summary.json` | `/public_builds` | int |  |
| `results/campaign_summary.json` | `/classified_inputs` | int |  |
| `results/campaign_summary.json` | `/inconsistent_inputs` | int |  |
| `results/campaign_summary.json` | `/admission_rejected_inputs` | int |  |
| `results/campaign_summary.json` | `/rows` | int |  |
| `results/campaign_summary.json` | `/incidences` | int |  |
| `results/campaign_summary.json` | `/developer` | int |  |
| `results/campaign_summary.json` | `/library` | int |  |
| `results/campaign_summary.json` | `/ambiguous` | int |  |
| `results/campaign_summary.json` | `/dependency_strictly_narrowed` | int |  |
| `results/campaign_summary.json` | `/bytes_strictly_narrowed` | int |  |
| `results/campaign_summary.json` | `/certificate_bytes` | int |  |
| `results/campaign_summary.json` | `/cpu_seconds` | float |  |
| `results/campaign_summary.json` | `/wall_seconds` | float |  |
| `results/campaign_summary.json` | `/peak_rss_kib` | int |  |
| `results/campaign_summary.json` | `/baseline_scope` | str |  |
| `results/cases.csv` | `case` | CSV column | 60 |
| `results/cases.csv` | `group` | CSV column | 60 |
| `results/cases.csv` | `phenomenon` | CSV column | 60 |
| `results/cases.csv` | `providers` | CSV column | 60 |
| `results/cases.csv` | `rows` | CSV column | 60 |
| `results/cases.csv` | `incidences` | CSV column | 60 |
| `results/cases.csv` | `status` | CSV column | 60 |
| `results/cases.csv` | `developer` | CSV column | 60 |
| `results/cases.csv` | `library` | CSV column | 60 |
| `results/cases.csv` | `ambiguous` | CSV column | 60 |
| `results/cases.csv` | `dependency_strictly_narrowed` | CSV column | 60 |
| `results/cases.csv` | `bytes_strictly_narrowed` | CSV column | 60 |
| `results/cases.csv` | `orders` | CSV column | 60 |
| `results/cases.csv` | `certificate_bytes` | CSV column | 60 |
| `results/cases.csv` | `producer_cpu_seconds` | CSV column | 60 |
| `results/cases.csv` | `checker_cpu_seconds` | CSV column | 60 |
| `results/certificates/f001.json` | `/` | object | 4 |
| `results/certificates/f001.json` | `/obstructions` | array | 0 |
| `results/certificates/f001.json` | `/orders` | array | 1 |
| `results/certificates/f001.json` | `/orders/0` | array | 1 |
| `results/certificates/f001.json` | `/orders/0/0` | int |  |
| `results/certificates/f001.json` | `/regions` | array | 1 |
| `results/certificates/f001.json` | `/regions/0` | object | 4 |
| `results/certificates/f001.json` | `/regions/0/class` | str |  |
| `results/certificates/f001.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/f001.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/f001.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/f001.json` | `/regions/0/support` | array | 1 |
| `results/certificates/f001.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/f001.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/f001.json` | `/status` | str |  |
| `results/certificates/f002.json` | `/` | object | 4 |
| `results/certificates/f002.json` | `/obstructions` | array | 0 |
| `results/certificates/f002.json` | `/orders` | array | 1 |
| `results/certificates/f002.json` | `/orders/0` | array | 1 |
| `results/certificates/f002.json` | `/orders/0/0` | int |  |
| `results/certificates/f002.json` | `/regions` | array | 1 |
| `results/certificates/f002.json` | `/regions/0` | object | 4 |
| `results/certificates/f002.json` | `/regions/0/class` | str |  |
| `results/certificates/f002.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/f002.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/f002.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/f002.json` | `/regions/0/support` | array | 1 |
| `results/certificates/f002.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/f002.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/f002.json` | `/status` | str |  |
| `results/certificates/f003.json` | `/` | object | 4 |
| `results/certificates/f003.json` | `/obstructions` | array | 0 |
| `results/certificates/f003.json` | `/orders` | array | 2 |
| `results/certificates/f003.json` | `/orders/0` | array | 2 |
| `results/certificates/f003.json` | `/orders/0/0` | int |  |
| `results/certificates/f003.json` | `/regions` | array | 1 |
| `results/certificates/f003.json` | `/regions/0` | object | 4 |
| `results/certificates/f003.json` | `/regions/0/class` | str |  |
| `results/certificates/f003.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/f003.json` | `/regions/0/owners` | array | 2 |
| `results/certificates/f003.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/f003.json` | `/regions/0/support` | array | 2 |
| `results/certificates/f003.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/f003.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/f003.json` | `/status` | str |  |
| `results/certificates/f004.json` | `/` | object | 4 |
| `results/certificates/f004.json` | `/obstructions` | array | 0 |
| `results/certificates/f004.json` | `/orders` | array | 1 |
| `results/certificates/f004.json` | `/orders/0` | array | 2 |
| `results/certificates/f004.json` | `/orders/0/0` | int |  |
| `results/certificates/f004.json` | `/regions` | array | 1 |
| `results/certificates/f004.json` | `/regions/0` | object | 4 |
| `results/certificates/f004.json` | `/regions/0/class` | str |  |
| `results/certificates/f004.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/f004.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/f004.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/f004.json` | `/regions/0/support` | array | 1 |
| `results/certificates/f004.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/f004.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/f004.json` | `/status` | str |  |
| `results/certificates/f005.json` | `/` | object | 2 |
| `results/certificates/f005.json` | `/obstruction` | object | 3 |
| `results/certificates/f005.json` | `/obstruction/kind` | str |  |
| `results/certificates/f005.json` | `/obstruction/nodes` | array | 2 |
| `results/certificates/f005.json` | `/obstruction/nodes/0` | int |  |
| `results/certificates/f005.json` | `/obstruction/reasons` | array | 2 |
| `results/certificates/f005.json` | `/obstruction/reasons/0` | object | 3 |
| `results/certificates/f005.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/certificates/f005.json` | `/obstruction/reasons/0/node` | int |  |
| `results/certificates/f005.json` | `/obstruction/reasons/0/row` | int |  |
| `results/certificates/f005.json` | `/status` | str |  |
| `results/certificates/f006.json` | `/` | object | 2 |
| `results/certificates/f006.json` | `/obstruction` | object | 2 |
| `results/certificates/f006.json` | `/obstruction/kind` | str |  |
| `results/certificates/f006.json` | `/obstruction/row` | int |  |
| `results/certificates/f006.json` | `/status` | str |  |
| `results/certificates/f007.json` | `/` | object | 2 |
| `results/certificates/f007.json` | `/obstruction` | object | 3 |
| `results/certificates/f007.json` | `/obstruction/kind` | str |  |
| `results/certificates/f007.json` | `/obstruction/nodes` | array | 2 |
| `results/certificates/f007.json` | `/obstruction/nodes/0` | int |  |
| `results/certificates/f007.json` | `/obstruction/reasons` | array | 2 |
| `results/certificates/f007.json` | `/obstruction/reasons/0` | object | 3 |
| `results/certificates/f007.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/certificates/f007.json` | `/obstruction/reasons/0/node` | int |  |
| `results/certificates/f007.json` | `/obstruction/reasons/0/row` | int |  |
| `results/certificates/f007.json` | `/status` | str |  |
| `results/certificates/f008.json` | `/` | object | 2 |
| `results/certificates/f008.json` | `/obstruction` | object | 3 |
| `results/certificates/f008.json` | `/obstruction/kind` | str |  |
| `results/certificates/f008.json` | `/obstruction/nodes` | array | 2 |
| `results/certificates/f008.json` | `/obstruction/nodes/0` | int |  |
| `results/certificates/f008.json` | `/obstruction/reasons` | array | 2 |
| `results/certificates/f008.json` | `/obstruction/reasons/0` | object | 3 |
| `results/certificates/f008.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/certificates/f008.json` | `/obstruction/reasons/0/node` | int |  |
| `results/certificates/f008.json` | `/obstruction/reasons/0/pred` | int |  |
| `results/certificates/f008.json` | `/status` | str |  |
| `results/certificates/f009.json` | `/` | object | 2 |
| `results/certificates/f009.json` | `/obstruction` | object | 3 |
| `results/certificates/f009.json` | `/obstruction/kind` | str |  |
| `results/certificates/f009.json` | `/obstruction/nodes` | array | 1 |
| `results/certificates/f009.json` | `/obstruction/nodes/0` | int |  |
| `results/certificates/f009.json` | `/obstruction/reasons` | array | 1 |
| `results/certificates/f009.json` | `/obstruction/reasons/0` | object | 3 |
| `results/certificates/f009.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/certificates/f009.json` | `/obstruction/reasons/0/node` | int |  |
| `results/certificates/f009.json` | `/obstruction/reasons/0/pred` | int |  |
| `results/certificates/f009.json` | `/status` | str |  |
| `results/certificates/f010.json` | `/` | object | 4 |
| `results/certificates/f010.json` | `/obstructions` | array | 0 |
| `results/certificates/f010.json` | `/orders` | array | 1 |
| `results/certificates/f010.json` | `/orders/0` | array | 2 |
| `results/certificates/f010.json` | `/orders/0/0` | int |  |
| `results/certificates/f010.json` | `/regions` | array | 0 |
| `results/certificates/f010.json` | `/status` | str |  |
| `results/certificates/f011.json` | `/` | object | 4 |
| `results/certificates/f011.json` | `/obstructions` | array | 0 |
| `results/certificates/f011.json` | `/orders` | array | 2 |
| `results/certificates/f011.json` | `/orders/0` | array | 3 |
| `results/certificates/f011.json` | `/orders/0/0` | int |  |
| `results/certificates/f011.json` | `/regions` | array | 1 |
| `results/certificates/f011.json` | `/regions/0` | object | 4 |
| `results/certificates/f011.json` | `/regions/0/class` | str |  |
| `results/certificates/f011.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/f011.json` | `/regions/0/owners` | array | 2 |
| `results/certificates/f011.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/f011.json` | `/regions/0/support` | array | 2 |
| `results/certificates/f011.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/f011.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/f011.json` | `/status` | str |  |
| `results/certificates/f012.json` | `/` | object | 4 |
| `results/certificates/f012.json` | `/obstructions` | array | 1 |
| `results/certificates/f012.json` | `/obstructions/0` | object | 3 |
| `results/certificates/f012.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/f012.json` | `/obstructions/0/nodes` | array | 2 |
| `results/certificates/f012.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/f012.json` | `/obstructions/0/reasons` | array | 2 |
| `results/certificates/f012.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/f012.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/f012.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/f012.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/f012.json` | `/orders` | array | 1 |
| `results/certificates/f012.json` | `/orders/0` | array | 2 |
| `results/certificates/f012.json` | `/orders/0/0` | int |  |
| `results/certificates/f012.json` | `/regions` | array | 2 |
| `results/certificates/f012.json` | `/regions/0` | object | 4 |
| `results/certificates/f012.json` | `/regions/0/class` | str |  |
| `results/certificates/f012.json` | `/regions/0/excluded` | array | 1 |
| `results/certificates/f012.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/f012.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/f012.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/f012.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/f012.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/f012.json` | `/regions/0/support` | array | 1 |
| `results/certificates/f012.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/f012.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/f012.json` | `/status` | str |  |
| `results/certificates/f013.json` | `/` | object | 4 |
| `results/certificates/f013.json` | `/obstructions` | array | 1 |
| `results/certificates/f013.json` | `/obstructions/0` | object | 3 |
| `results/certificates/f013.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/f013.json` | `/obstructions/0/nodes` | array | 3 |
| `results/certificates/f013.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/f013.json` | `/obstructions/0/reasons` | array | 3 |
| `results/certificates/f013.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/f013.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/f013.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/f013.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/f013.json` | `/orders` | array | 2 |
| `results/certificates/f013.json` | `/orders/0` | array | 3 |
| `results/certificates/f013.json` | `/orders/0/0` | int |  |
| `results/certificates/f013.json` | `/regions` | array | 2 |
| `results/certificates/f013.json` | `/regions/0` | object | 4 |
| `results/certificates/f013.json` | `/regions/0/class` | str |  |
| `results/certificates/f013.json` | `/regions/0/excluded` | array | 1 |
| `results/certificates/f013.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/f013.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/f013.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/f013.json` | `/regions/0/owners` | array | 2 |
| `results/certificates/f013.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/f013.json` | `/regions/0/support` | array | 2 |
| `results/certificates/f013.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/f013.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/f013.json` | `/status` | str |  |
| `results/certificates/f014.json` | `/` | object | 4 |
| `results/certificates/f014.json` | `/obstructions` | array | 1 |
| `results/certificates/f014.json` | `/obstructions/0` | object | 3 |
| `results/certificates/f014.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/f014.json` | `/obstructions/0/nodes` | array | 2 |
| `results/certificates/f014.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/f014.json` | `/obstructions/0/reasons` | array | 2 |
| `results/certificates/f014.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/f014.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/f014.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/f014.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/f014.json` | `/orders` | array | 1 |
| `results/certificates/f014.json` | `/orders/0` | array | 2 |
| `results/certificates/f014.json` | `/orders/0/0` | int |  |
| `results/certificates/f014.json` | `/regions` | array | 1 |
| `results/certificates/f014.json` | `/regions/0` | object | 4 |
| `results/certificates/f014.json` | `/regions/0/class` | str |  |
| `results/certificates/f014.json` | `/regions/0/excluded` | array | 1 |
| `results/certificates/f014.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/f014.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/f014.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/f014.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/f014.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/f014.json` | `/regions/0/support` | array | 1 |
| `results/certificates/f014.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/f014.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/f014.json` | `/status` | str |  |
| `results/certificates/f015.json` | `/` | object | 4 |
| `results/certificates/f015.json` | `/obstructions` | array | 1 |
| `results/certificates/f015.json` | `/obstructions/0` | object | 3 |
| `results/certificates/f015.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/f015.json` | `/obstructions/0/nodes` | array | 3 |
| `results/certificates/f015.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/f015.json` | `/obstructions/0/reasons` | array | 3 |
| `results/certificates/f015.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/f015.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/f015.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/f015.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/f015.json` | `/orders` | array | 1 |
| `results/certificates/f015.json` | `/orders/0` | array | 3 |
| `results/certificates/f015.json` | `/orders/0/0` | int |  |
| `results/certificates/f015.json` | `/regions` | array | 2 |
| `results/certificates/f015.json` | `/regions/0` | object | 4 |
| `results/certificates/f015.json` | `/regions/0/class` | str |  |
| `results/certificates/f015.json` | `/regions/0/excluded` | array | 1 |
| `results/certificates/f015.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/f015.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/f015.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/f015.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/f015.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/f015.json` | `/regions/0/support` | array | 1 |
| `results/certificates/f015.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/f015.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/f015.json` | `/status` | str |  |
| `results/certificates/f016.json` | `/` | object | 4 |
| `results/certificates/f016.json` | `/obstructions` | array | 0 |
| `results/certificates/f016.json` | `/orders` | array | 1 |
| `results/certificates/f016.json` | `/orders/0` | array | 2 |
| `results/certificates/f016.json` | `/orders/0/0` | int |  |
| `results/certificates/f016.json` | `/regions` | array | 2 |
| `results/certificates/f016.json` | `/regions/0` | object | 4 |
| `results/certificates/f016.json` | `/regions/0/class` | str |  |
| `results/certificates/f016.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/f016.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/f016.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/f016.json` | `/regions/0/support` | array | 1 |
| `results/certificates/f016.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/f016.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/f016.json` | `/status` | str |  |
| `results/certificates/f017.json` | `/` | object | 4 |
| `results/certificates/f017.json` | `/obstructions` | array | 0 |
| `results/certificates/f017.json` | `/orders` | array | 1 |
| `results/certificates/f017.json` | `/orders/0` | array | 1 |
| `results/certificates/f017.json` | `/orders/0/0` | int |  |
| `results/certificates/f017.json` | `/regions` | array | 1 |
| `results/certificates/f017.json` | `/regions/0` | object | 4 |
| `results/certificates/f017.json` | `/regions/0/class` | str |  |
| `results/certificates/f017.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/f017.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/f017.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/f017.json` | `/regions/0/support` | array | 1 |
| `results/certificates/f017.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/f017.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/f017.json` | `/status` | str |  |
| `results/certificates/f018.json` | `/` | object | 4 |
| `results/certificates/f018.json` | `/obstructions` | array | 0 |
| `results/certificates/f018.json` | `/orders` | array | 1 |
| `results/certificates/f018.json` | `/orders/0` | array | 1 |
| `results/certificates/f018.json` | `/orders/0/0` | int |  |
| `results/certificates/f018.json` | `/regions` | array | 1 |
| `results/certificates/f018.json` | `/regions/0` | object | 4 |
| `results/certificates/f018.json` | `/regions/0/class` | str |  |
| `results/certificates/f018.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/f018.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/f018.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/f018.json` | `/regions/0/support` | array | 1 |
| `results/certificates/f018.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/f018.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/f018.json` | `/status` | str |  |
| `results/certificates/g001.json` | `/` | object | 4 |
| `results/certificates/g001.json` | `/obstructions` | array | 0 |
| `results/certificates/g001.json` | `/orders` | array | 2 |
| `results/certificates/g001.json` | `/orders/0` | array | 2 |
| `results/certificates/g001.json` | `/orders/0/0` | int |  |
| `results/certificates/g001.json` | `/regions` | array | 1 |
| `results/certificates/g001.json` | `/regions/0` | object | 4 |
| `results/certificates/g001.json` | `/regions/0/class` | str |  |
| `results/certificates/g001.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/g001.json` | `/regions/0/owners` | array | 2 |
| `results/certificates/g001.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g001.json` | `/regions/0/support` | array | 2 |
| `results/certificates/g001.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g001.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g001.json` | `/status` | str |  |
| `results/certificates/g002.json` | `/` | object | 4 |
| `results/certificates/g002.json` | `/obstructions` | array | 0 |
| `results/certificates/g002.json` | `/orders` | array | 3 |
| `results/certificates/g002.json` | `/orders/0` | array | 3 |
| `results/certificates/g002.json` | `/orders/0/0` | int |  |
| `results/certificates/g002.json` | `/regions` | array | 1 |
| `results/certificates/g002.json` | `/regions/0` | object | 4 |
| `results/certificates/g002.json` | `/regions/0/class` | str |  |
| `results/certificates/g002.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/g002.json` | `/regions/0/owners` | array | 3 |
| `results/certificates/g002.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g002.json` | `/regions/0/support` | array | 3 |
| `results/certificates/g002.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g002.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g002.json` | `/status` | str |  |
| `results/certificates/g003.json` | `/` | object | 4 |
| `results/certificates/g003.json` | `/obstructions` | array | 0 |
| `results/certificates/g003.json` | `/orders` | array | 5 |
| `results/certificates/g003.json` | `/orders/0` | array | 5 |
| `results/certificates/g003.json` | `/orders/0/0` | int |  |
| `results/certificates/g003.json` | `/regions` | array | 1 |
| `results/certificates/g003.json` | `/regions/0` | object | 4 |
| `results/certificates/g003.json` | `/regions/0/class` | str |  |
| `results/certificates/g003.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/g003.json` | `/regions/0/owners` | array | 5 |
| `results/certificates/g003.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g003.json` | `/regions/0/support` | array | 5 |
| `results/certificates/g003.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g003.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g003.json` | `/status` | str |  |
| `results/certificates/g004.json` | `/` | object | 4 |
| `results/certificates/g004.json` | `/obstructions` | array | 0 |
| `results/certificates/g004.json` | `/orders` | array | 8 |
| `results/certificates/g004.json` | `/orders/0` | array | 8 |
| `results/certificates/g004.json` | `/orders/0/0` | int |  |
| `results/certificates/g004.json` | `/regions` | array | 1 |
| `results/certificates/g004.json` | `/regions/0` | object | 4 |
| `results/certificates/g004.json` | `/regions/0/class` | str |  |
| `results/certificates/g004.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/g004.json` | `/regions/0/owners` | array | 8 |
| `results/certificates/g004.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g004.json` | `/regions/0/support` | array | 8 |
| `results/certificates/g004.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g004.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g004.json` | `/status` | str |  |
| `results/certificates/g005.json` | `/` | object | 4 |
| `results/certificates/g005.json` | `/obstructions` | array | 0 |
| `results/certificates/g005.json` | `/orders` | array | 16 |
| `results/certificates/g005.json` | `/orders/0` | array | 16 |
| `results/certificates/g005.json` | `/orders/0/0` | int |  |
| `results/certificates/g005.json` | `/regions` | array | 1 |
| `results/certificates/g005.json` | `/regions/0` | object | 4 |
| `results/certificates/g005.json` | `/regions/0/class` | str |  |
| `results/certificates/g005.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/g005.json` | `/regions/0/owners` | array | 16 |
| `results/certificates/g005.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g005.json` | `/regions/0/support` | array | 16 |
| `results/certificates/g005.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g005.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g005.json` | `/status` | str |  |
| `results/certificates/g006.json` | `/` | object | 4 |
| `results/certificates/g006.json` | `/obstructions` | array | 1 |
| `results/certificates/g006.json` | `/obstructions/0` | object | 3 |
| `results/certificates/g006.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/g006.json` | `/obstructions/0/nodes` | array | 2 |
| `results/certificates/g006.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/g006.json` | `/obstructions/0/reasons` | array | 2 |
| `results/certificates/g006.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/g006.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/g006.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/g006.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/g006.json` | `/orders` | array | 1 |
| `results/certificates/g006.json` | `/orders/0` | array | 2 |
| `results/certificates/g006.json` | `/orders/0/0` | int |  |
| `results/certificates/g006.json` | `/regions` | array | 2 |
| `results/certificates/g006.json` | `/regions/0` | object | 4 |
| `results/certificates/g006.json` | `/regions/0/class` | str |  |
| `results/certificates/g006.json` | `/regions/0/excluded` | array | 1 |
| `results/certificates/g006.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/g006.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/g006.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/g006.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/g006.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g006.json` | `/regions/0/support` | array | 1 |
| `results/certificates/g006.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g006.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g006.json` | `/status` | str |  |
| `results/certificates/g007.json` | `/` | object | 4 |
| `results/certificates/g007.json` | `/obstructions` | array | 2 |
| `results/certificates/g007.json` | `/obstructions/0` | object | 3 |
| `results/certificates/g007.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/g007.json` | `/obstructions/0/nodes` | array | 3 |
| `results/certificates/g007.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/g007.json` | `/obstructions/0/reasons` | array | 3 |
| `results/certificates/g007.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/g007.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/g007.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/g007.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/g007.json` | `/orders` | array | 1 |
| `results/certificates/g007.json` | `/orders/0` | array | 3 |
| `results/certificates/g007.json` | `/orders/0/0` | int |  |
| `results/certificates/g007.json` | `/regions` | array | 3 |
| `results/certificates/g007.json` | `/regions/0` | object | 4 |
| `results/certificates/g007.json` | `/regions/0/class` | str |  |
| `results/certificates/g007.json` | `/regions/0/excluded` | array | 2 |
| `results/certificates/g007.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/g007.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/g007.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/g007.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/g007.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g007.json` | `/regions/0/support` | array | 1 |
| `results/certificates/g007.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g007.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g007.json` | `/status` | str |  |
| `results/certificates/g008.json` | `/` | object | 4 |
| `results/certificates/g008.json` | `/obstructions` | array | 4 |
| `results/certificates/g008.json` | `/obstructions/0` | object | 3 |
| `results/certificates/g008.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/g008.json` | `/obstructions/0/nodes` | array | 5 |
| `results/certificates/g008.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/g008.json` | `/obstructions/0/reasons` | array | 5 |
| `results/certificates/g008.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/g008.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/g008.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/g008.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/g008.json` | `/orders` | array | 1 |
| `results/certificates/g008.json` | `/orders/0` | array | 5 |
| `results/certificates/g008.json` | `/orders/0/0` | int |  |
| `results/certificates/g008.json` | `/regions` | array | 5 |
| `results/certificates/g008.json` | `/regions/0` | object | 4 |
| `results/certificates/g008.json` | `/regions/0/class` | str |  |
| `results/certificates/g008.json` | `/regions/0/excluded` | array | 4 |
| `results/certificates/g008.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/g008.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/g008.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/g008.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/g008.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g008.json` | `/regions/0/support` | array | 1 |
| `results/certificates/g008.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g008.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g008.json` | `/status` | str |  |
| `results/certificates/g009.json` | `/` | object | 4 |
| `results/certificates/g009.json` | `/obstructions` | array | 7 |
| `results/certificates/g009.json` | `/obstructions/0` | object | 3 |
| `results/certificates/g009.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/g009.json` | `/obstructions/0/nodes` | array | 8 |
| `results/certificates/g009.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/g009.json` | `/obstructions/0/reasons` | array | 8 |
| `results/certificates/g009.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/g009.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/g009.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/g009.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/g009.json` | `/orders` | array | 1 |
| `results/certificates/g009.json` | `/orders/0` | array | 8 |
| `results/certificates/g009.json` | `/orders/0/0` | int |  |
| `results/certificates/g009.json` | `/regions` | array | 8 |
| `results/certificates/g009.json` | `/regions/0` | object | 4 |
| `results/certificates/g009.json` | `/regions/0/class` | str |  |
| `results/certificates/g009.json` | `/regions/0/excluded` | array | 7 |
| `results/certificates/g009.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/g009.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/g009.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/g009.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/g009.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g009.json` | `/regions/0/support` | array | 1 |
| `results/certificates/g009.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g009.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g009.json` | `/status` | str |  |
| `results/certificates/g010.json` | `/` | object | 4 |
| `results/certificates/g010.json` | `/obstructions` | array | 15 |
| `results/certificates/g010.json` | `/obstructions/0` | object | 3 |
| `results/certificates/g010.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/g010.json` | `/obstructions/0/nodes` | array | 16 |
| `results/certificates/g010.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/g010.json` | `/obstructions/0/reasons` | array | 16 |
| `results/certificates/g010.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/g010.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/g010.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/g010.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/g010.json` | `/orders` | array | 1 |
| `results/certificates/g010.json` | `/orders/0` | array | 16 |
| `results/certificates/g010.json` | `/orders/0/0` | int |  |
| `results/certificates/g010.json` | `/regions` | array | 16 |
| `results/certificates/g010.json` | `/regions/0` | object | 4 |
| `results/certificates/g010.json` | `/regions/0/class` | str |  |
| `results/certificates/g010.json` | `/regions/0/excluded` | array | 15 |
| `results/certificates/g010.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/g010.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/g010.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/g010.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/g010.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g010.json` | `/regions/0/support` | array | 1 |
| `results/certificates/g010.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g010.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g010.json` | `/status` | str |  |
| `results/certificates/g011.json` | `/` | object | 4 |
| `results/certificates/g011.json` | `/obstructions` | array | 0 |
| `results/certificates/g011.json` | `/orders` | array | 1 |
| `results/certificates/g011.json` | `/orders/0` | array | 2 |
| `results/certificates/g011.json` | `/orders/0/0` | int |  |
| `results/certificates/g011.json` | `/regions` | array | 1 |
| `results/certificates/g011.json` | `/regions/0` | object | 4 |
| `results/certificates/g011.json` | `/regions/0/class` | str |  |
| `results/certificates/g011.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/g011.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/g011.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g011.json` | `/regions/0/support` | array | 1 |
| `results/certificates/g011.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g011.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g011.json` | `/status` | str |  |
| `results/certificates/g012.json` | `/` | object | 4 |
| `results/certificates/g012.json` | `/obstructions` | array | 0 |
| `results/certificates/g012.json` | `/orders` | array | 1 |
| `results/certificates/g012.json` | `/orders/0` | array | 3 |
| `results/certificates/g012.json` | `/orders/0/0` | int |  |
| `results/certificates/g012.json` | `/regions` | array | 1 |
| `results/certificates/g012.json` | `/regions/0` | object | 4 |
| `results/certificates/g012.json` | `/regions/0/class` | str |  |
| `results/certificates/g012.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/g012.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/g012.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g012.json` | `/regions/0/support` | array | 1 |
| `results/certificates/g012.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g012.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g012.json` | `/status` | str |  |
| `results/certificates/g013.json` | `/` | object | 4 |
| `results/certificates/g013.json` | `/obstructions` | array | 0 |
| `results/certificates/g013.json` | `/orders` | array | 1 |
| `results/certificates/g013.json` | `/orders/0` | array | 5 |
| `results/certificates/g013.json` | `/orders/0/0` | int |  |
| `results/certificates/g013.json` | `/regions` | array | 1 |
| `results/certificates/g013.json` | `/regions/0` | object | 4 |
| `results/certificates/g013.json` | `/regions/0/class` | str |  |
| `results/certificates/g013.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/g013.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/g013.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g013.json` | `/regions/0/support` | array | 1 |
| `results/certificates/g013.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g013.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g013.json` | `/status` | str |  |
| `results/certificates/g014.json` | `/` | object | 4 |
| `results/certificates/g014.json` | `/obstructions` | array | 0 |
| `results/certificates/g014.json` | `/orders` | array | 1 |
| `results/certificates/g014.json` | `/orders/0` | array | 8 |
| `results/certificates/g014.json` | `/orders/0/0` | int |  |
| `results/certificates/g014.json` | `/regions` | array | 1 |
| `results/certificates/g014.json` | `/regions/0` | object | 4 |
| `results/certificates/g014.json` | `/regions/0/class` | str |  |
| `results/certificates/g014.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/g014.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/g014.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g014.json` | `/regions/0/support` | array | 1 |
| `results/certificates/g014.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g014.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g014.json` | `/status` | str |  |
| `results/certificates/g015.json` | `/` | object | 4 |
| `results/certificates/g015.json` | `/obstructions` | array | 0 |
| `results/certificates/g015.json` | `/orders` | array | 1 |
| `results/certificates/g015.json` | `/orders/0` | array | 16 |
| `results/certificates/g015.json` | `/orders/0/0` | int |  |
| `results/certificates/g015.json` | `/regions` | array | 1 |
| `results/certificates/g015.json` | `/regions/0` | object | 4 |
| `results/certificates/g015.json` | `/regions/0/class` | str |  |
| `results/certificates/g015.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/g015.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/g015.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g015.json` | `/regions/0/support` | array | 1 |
| `results/certificates/g015.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g015.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g015.json` | `/status` | str |  |
| `results/certificates/g016.json` | `/` | object | 4 |
| `results/certificates/g016.json` | `/obstructions` | array | 1 |
| `results/certificates/g016.json` | `/obstructions/0` | object | 3 |
| `results/certificates/g016.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/g016.json` | `/obstructions/0/nodes` | array | 2 |
| `results/certificates/g016.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/g016.json` | `/obstructions/0/reasons` | array | 2 |
| `results/certificates/g016.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/g016.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/g016.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/g016.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/g016.json` | `/orders` | array | 1 |
| `results/certificates/g016.json` | `/orders/0` | array | 2 |
| `results/certificates/g016.json` | `/orders/0/0` | int |  |
| `results/certificates/g016.json` | `/regions` | array | 1 |
| `results/certificates/g016.json` | `/regions/0` | object | 4 |
| `results/certificates/g016.json` | `/regions/0/class` | str |  |
| `results/certificates/g016.json` | `/regions/0/excluded` | array | 1 |
| `results/certificates/g016.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/g016.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/g016.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/g016.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/g016.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g016.json` | `/regions/0/support` | array | 1 |
| `results/certificates/g016.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g016.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g016.json` | `/status` | str |  |
| `results/certificates/g017.json` | `/` | object | 4 |
| `results/certificates/g017.json` | `/obstructions` | array | 2 |
| `results/certificates/g017.json` | `/obstructions/0` | object | 3 |
| `results/certificates/g017.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/g017.json` | `/obstructions/0/nodes` | array | 3 |
| `results/certificates/g017.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/g017.json` | `/obstructions/0/reasons` | array | 3 |
| `results/certificates/g017.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/g017.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/g017.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/g017.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/g017.json` | `/orders` | array | 1 |
| `results/certificates/g017.json` | `/orders/0` | array | 3 |
| `results/certificates/g017.json` | `/orders/0/0` | int |  |
| `results/certificates/g017.json` | `/regions` | array | 1 |
| `results/certificates/g017.json` | `/regions/0` | object | 4 |
| `results/certificates/g017.json` | `/regions/0/class` | str |  |
| `results/certificates/g017.json` | `/regions/0/excluded` | array | 2 |
| `results/certificates/g017.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/g017.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/g017.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/g017.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/g017.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g017.json` | `/regions/0/support` | array | 1 |
| `results/certificates/g017.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g017.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g017.json` | `/status` | str |  |
| `results/certificates/g018.json` | `/` | object | 4 |
| `results/certificates/g018.json` | `/obstructions` | array | 4 |
| `results/certificates/g018.json` | `/obstructions/0` | object | 3 |
| `results/certificates/g018.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/g018.json` | `/obstructions/0/nodes` | array | 5 |
| `results/certificates/g018.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/g018.json` | `/obstructions/0/reasons` | array | 5 |
| `results/certificates/g018.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/g018.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/g018.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/g018.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/g018.json` | `/orders` | array | 1 |
| `results/certificates/g018.json` | `/orders/0` | array | 5 |
| `results/certificates/g018.json` | `/orders/0/0` | int |  |
| `results/certificates/g018.json` | `/regions` | array | 1 |
| `results/certificates/g018.json` | `/regions/0` | object | 4 |
| `results/certificates/g018.json` | `/regions/0/class` | str |  |
| `results/certificates/g018.json` | `/regions/0/excluded` | array | 4 |
| `results/certificates/g018.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/g018.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/g018.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/g018.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/g018.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g018.json` | `/regions/0/support` | array | 1 |
| `results/certificates/g018.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g018.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g018.json` | `/status` | str |  |
| `results/certificates/g019.json` | `/` | object | 4 |
| `results/certificates/g019.json` | `/obstructions` | array | 7 |
| `results/certificates/g019.json` | `/obstructions/0` | object | 3 |
| `results/certificates/g019.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/g019.json` | `/obstructions/0/nodes` | array | 8 |
| `results/certificates/g019.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/g019.json` | `/obstructions/0/reasons` | array | 8 |
| `results/certificates/g019.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/g019.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/g019.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/g019.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/g019.json` | `/orders` | array | 1 |
| `results/certificates/g019.json` | `/orders/0` | array | 8 |
| `results/certificates/g019.json` | `/orders/0/0` | int |  |
| `results/certificates/g019.json` | `/regions` | array | 1 |
| `results/certificates/g019.json` | `/regions/0` | object | 4 |
| `results/certificates/g019.json` | `/regions/0/class` | str |  |
| `results/certificates/g019.json` | `/regions/0/excluded` | array | 7 |
| `results/certificates/g019.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/g019.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/g019.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/g019.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/g019.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g019.json` | `/regions/0/support` | array | 1 |
| `results/certificates/g019.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g019.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g019.json` | `/status` | str |  |
| `results/certificates/g020.json` | `/` | object | 4 |
| `results/certificates/g020.json` | `/obstructions` | array | 15 |
| `results/certificates/g020.json` | `/obstructions/0` | object | 3 |
| `results/certificates/g020.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/g020.json` | `/obstructions/0/nodes` | array | 16 |
| `results/certificates/g020.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/g020.json` | `/obstructions/0/reasons` | array | 16 |
| `results/certificates/g020.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/g020.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/g020.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/g020.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/g020.json` | `/orders` | array | 1 |
| `results/certificates/g020.json` | `/orders/0` | array | 16 |
| `results/certificates/g020.json` | `/orders/0/0` | int |  |
| `results/certificates/g020.json` | `/regions` | array | 1 |
| `results/certificates/g020.json` | `/regions/0` | object | 4 |
| `results/certificates/g020.json` | `/regions/0/class` | str |  |
| `results/certificates/g020.json` | `/regions/0/excluded` | array | 15 |
| `results/certificates/g020.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/g020.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/g020.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/g020.json` | `/regions/0/owners` | array | 1 |
| `results/certificates/g020.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g020.json` | `/regions/0/support` | array | 1 |
| `results/certificates/g020.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g020.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g020.json` | `/status` | str |  |
| `results/certificates/g021.json` | `/` | object | 4 |
| `results/certificates/g021.json` | `/obstructions` | array | 0 |
| `results/certificates/g021.json` | `/orders` | array | 2 |
| `results/certificates/g021.json` | `/orders/0` | array | 2 |
| `results/certificates/g021.json` | `/orders/0/0` | int |  |
| `results/certificates/g021.json` | `/regions` | array | 2 |
| `results/certificates/g021.json` | `/regions/0` | object | 4 |
| `results/certificates/g021.json` | `/regions/0/class` | str |  |
| `results/certificates/g021.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/g021.json` | `/regions/0/owners` | array | 2 |
| `results/certificates/g021.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g021.json` | `/regions/0/support` | array | 2 |
| `results/certificates/g021.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g021.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g021.json` | `/status` | str |  |
| `results/certificates/g022.json` | `/` | object | 4 |
| `results/certificates/g022.json` | `/obstructions` | array | 1 |
| `results/certificates/g022.json` | `/obstructions/0` | object | 3 |
| `results/certificates/g022.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/g022.json` | `/obstructions/0/nodes` | array | 3 |
| `results/certificates/g022.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/g022.json` | `/obstructions/0/reasons` | array | 3 |
| `results/certificates/g022.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/g022.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/g022.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/g022.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/g022.json` | `/orders` | array | 2 |
| `results/certificates/g022.json` | `/orders/0` | array | 3 |
| `results/certificates/g022.json` | `/orders/0/0` | int |  |
| `results/certificates/g022.json` | `/regions` | array | 2 |
| `results/certificates/g022.json` | `/regions/0` | object | 4 |
| `results/certificates/g022.json` | `/regions/0/class` | str |  |
| `results/certificates/g022.json` | `/regions/0/excluded` | array | 1 |
| `results/certificates/g022.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/g022.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/g022.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/g022.json` | `/regions/0/owners` | array | 2 |
| `results/certificates/g022.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g022.json` | `/regions/0/support` | array | 2 |
| `results/certificates/g022.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g022.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g022.json` | `/status` | str |  |
| `results/certificates/g023.json` | `/` | object | 4 |
| `results/certificates/g023.json` | `/obstructions` | array | 3 |
| `results/certificates/g023.json` | `/obstructions/0` | object | 3 |
| `results/certificates/g023.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/g023.json` | `/obstructions/0/nodes` | array | 5 |
| `results/certificates/g023.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/g023.json` | `/obstructions/0/reasons` | array | 5 |
| `results/certificates/g023.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/g023.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/g023.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/g023.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/g023.json` | `/orders` | array | 2 |
| `results/certificates/g023.json` | `/orders/0` | array | 5 |
| `results/certificates/g023.json` | `/orders/0/0` | int |  |
| `results/certificates/g023.json` | `/regions` | array | 2 |
| `results/certificates/g023.json` | `/regions/0` | object | 4 |
| `results/certificates/g023.json` | `/regions/0/class` | str |  |
| `results/certificates/g023.json` | `/regions/0/excluded` | array | 3 |
| `results/certificates/g023.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/g023.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/g023.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/g023.json` | `/regions/0/owners` | array | 2 |
| `results/certificates/g023.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g023.json` | `/regions/0/support` | array | 2 |
| `results/certificates/g023.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g023.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g023.json` | `/status` | str |  |
| `results/certificates/g024.json` | `/` | object | 4 |
| `results/certificates/g024.json` | `/obstructions` | array | 6 |
| `results/certificates/g024.json` | `/obstructions/0` | object | 3 |
| `results/certificates/g024.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/g024.json` | `/obstructions/0/nodes` | array | 8 |
| `results/certificates/g024.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/g024.json` | `/obstructions/0/reasons` | array | 8 |
| `results/certificates/g024.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/g024.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/g024.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/g024.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/g024.json` | `/orders` | array | 2 |
| `results/certificates/g024.json` | `/orders/0` | array | 8 |
| `results/certificates/g024.json` | `/orders/0/0` | int |  |
| `results/certificates/g024.json` | `/regions` | array | 2 |
| `results/certificates/g024.json` | `/regions/0` | object | 4 |
| `results/certificates/g024.json` | `/regions/0/class` | str |  |
| `results/certificates/g024.json` | `/regions/0/excluded` | array | 6 |
| `results/certificates/g024.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/g024.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/g024.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/g024.json` | `/regions/0/owners` | array | 2 |
| `results/certificates/g024.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g024.json` | `/regions/0/support` | array | 2 |
| `results/certificates/g024.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g024.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g024.json` | `/status` | str |  |
| `results/certificates/g025.json` | `/` | object | 4 |
| `results/certificates/g025.json` | `/obstructions` | array | 14 |
| `results/certificates/g025.json` | `/obstructions/0` | object | 3 |
| `results/certificates/g025.json` | `/obstructions/0/kind` | str |  |
| `results/certificates/g025.json` | `/obstructions/0/nodes` | array | 16 |
| `results/certificates/g025.json` | `/obstructions/0/nodes/0` | int |  |
| `results/certificates/g025.json` | `/obstructions/0/reasons` | array | 16 |
| `results/certificates/g025.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/certificates/g025.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/certificates/g025.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/certificates/g025.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/certificates/g025.json` | `/orders` | array | 2 |
| `results/certificates/g025.json` | `/orders/0` | array | 16 |
| `results/certificates/g025.json` | `/orders/0/0` | int |  |
| `results/certificates/g025.json` | `/regions` | array | 2 |
| `results/certificates/g025.json` | `/regions/0` | object | 4 |
| `results/certificates/g025.json` | `/regions/0/class` | str |  |
| `results/certificates/g025.json` | `/regions/0/excluded` | array | 14 |
| `results/certificates/g025.json` | `/regions/0/excluded/0` | object | 2 |
| `results/certificates/g025.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/certificates/g025.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/certificates/g025.json` | `/regions/0/owners` | array | 2 |
| `results/certificates/g025.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g025.json` | `/regions/0/support` | array | 2 |
| `results/certificates/g025.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g025.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g025.json` | `/status` | str |  |
| `results/certificates/g026.json` | `/` | object | 2 |
| `results/certificates/g026.json` | `/obstruction` | object | 3 |
| `results/certificates/g026.json` | `/obstruction/kind` | str |  |
| `results/certificates/g026.json` | `/obstruction/nodes` | array | 2 |
| `results/certificates/g026.json` | `/obstruction/nodes/0` | int |  |
| `results/certificates/g026.json` | `/obstruction/reasons` | array | 2 |
| `results/certificates/g026.json` | `/obstruction/reasons/0` | object | 3 |
| `results/certificates/g026.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/certificates/g026.json` | `/obstruction/reasons/0/node` | int |  |
| `results/certificates/g026.json` | `/obstruction/reasons/0/row` | int |  |
| `results/certificates/g026.json` | `/status` | str |  |
| `results/certificates/g027.json` | `/` | object | 2 |
| `results/certificates/g027.json` | `/obstruction` | object | 3 |
| `results/certificates/g027.json` | `/obstruction/kind` | str |  |
| `results/certificates/g027.json` | `/obstruction/nodes` | array | 3 |
| `results/certificates/g027.json` | `/obstruction/nodes/0` | int |  |
| `results/certificates/g027.json` | `/obstruction/reasons` | array | 3 |
| `results/certificates/g027.json` | `/obstruction/reasons/0` | object | 3 |
| `results/certificates/g027.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/certificates/g027.json` | `/obstruction/reasons/0/node` | int |  |
| `results/certificates/g027.json` | `/obstruction/reasons/0/row` | int |  |
| `results/certificates/g027.json` | `/status` | str |  |
| `results/certificates/g028.json` | `/` | object | 2 |
| `results/certificates/g028.json` | `/obstruction` | object | 3 |
| `results/certificates/g028.json` | `/obstruction/kind` | str |  |
| `results/certificates/g028.json` | `/obstruction/nodes` | array | 5 |
| `results/certificates/g028.json` | `/obstruction/nodes/0` | int |  |
| `results/certificates/g028.json` | `/obstruction/reasons` | array | 5 |
| `results/certificates/g028.json` | `/obstruction/reasons/0` | object | 3 |
| `results/certificates/g028.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/certificates/g028.json` | `/obstruction/reasons/0/node` | int |  |
| `results/certificates/g028.json` | `/obstruction/reasons/0/row` | int |  |
| `results/certificates/g028.json` | `/status` | str |  |
| `results/certificates/g029.json` | `/` | object | 2 |
| `results/certificates/g029.json` | `/obstruction` | object | 3 |
| `results/certificates/g029.json` | `/obstruction/kind` | str |  |
| `results/certificates/g029.json` | `/obstruction/nodes` | array | 8 |
| `results/certificates/g029.json` | `/obstruction/nodes/0` | int |  |
| `results/certificates/g029.json` | `/obstruction/reasons` | array | 8 |
| `results/certificates/g029.json` | `/obstruction/reasons/0` | object | 3 |
| `results/certificates/g029.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/certificates/g029.json` | `/obstruction/reasons/0/node` | int |  |
| `results/certificates/g029.json` | `/obstruction/reasons/0/row` | int |  |
| `results/certificates/g029.json` | `/status` | str |  |
| `results/certificates/g030.json` | `/` | object | 2 |
| `results/certificates/g030.json` | `/obstruction` | object | 3 |
| `results/certificates/g030.json` | `/obstruction/kind` | str |  |
| `results/certificates/g030.json` | `/obstruction/nodes` | array | 16 |
| `results/certificates/g030.json` | `/obstruction/nodes/0` | int |  |
| `results/certificates/g030.json` | `/obstruction/reasons` | array | 16 |
| `results/certificates/g030.json` | `/obstruction/reasons/0` | object | 3 |
| `results/certificates/g030.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/certificates/g030.json` | `/obstruction/reasons/0/node` | int |  |
| `results/certificates/g030.json` | `/obstruction/reasons/0/row` | int |  |
| `results/certificates/g030.json` | `/status` | str |  |
| `results/certificates/g031.json` | `/` | object | 4 |
| `results/certificates/g031.json` | `/obstructions` | array | 0 |
| `results/certificates/g031.json` | `/orders` | array | 2 |
| `results/certificates/g031.json` | `/orders/0` | array | 2 |
| `results/certificates/g031.json` | `/orders/0/0` | int |  |
| `results/certificates/g031.json` | `/regions` | array | 1 |
| `results/certificates/g031.json` | `/regions/0` | object | 4 |
| `results/certificates/g031.json` | `/regions/0/class` | str |  |
| `results/certificates/g031.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/g031.json` | `/regions/0/owners` | array | 2 |
| `results/certificates/g031.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g031.json` | `/regions/0/support` | array | 2 |
| `results/certificates/g031.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g031.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g031.json` | `/status` | str |  |
| `results/certificates/g032.json` | `/` | object | 4 |
| `results/certificates/g032.json` | `/obstructions` | array | 0 |
| `results/certificates/g032.json` | `/orders` | array | 3 |
| `results/certificates/g032.json` | `/orders/0` | array | 3 |
| `results/certificates/g032.json` | `/orders/0/0` | int |  |
| `results/certificates/g032.json` | `/regions` | array | 1 |
| `results/certificates/g032.json` | `/regions/0` | object | 4 |
| `results/certificates/g032.json` | `/regions/0/class` | str |  |
| `results/certificates/g032.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/g032.json` | `/regions/0/owners` | array | 3 |
| `results/certificates/g032.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g032.json` | `/regions/0/support` | array | 3 |
| `results/certificates/g032.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g032.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g032.json` | `/status` | str |  |
| `results/certificates/g033.json` | `/` | object | 4 |
| `results/certificates/g033.json` | `/obstructions` | array | 0 |
| `results/certificates/g033.json` | `/orders` | array | 5 |
| `results/certificates/g033.json` | `/orders/0` | array | 5 |
| `results/certificates/g033.json` | `/orders/0/0` | int |  |
| `results/certificates/g033.json` | `/regions` | array | 1 |
| `results/certificates/g033.json` | `/regions/0` | object | 4 |
| `results/certificates/g033.json` | `/regions/0/class` | str |  |
| `results/certificates/g033.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/g033.json` | `/regions/0/owners` | array | 5 |
| `results/certificates/g033.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g033.json` | `/regions/0/support` | array | 5 |
| `results/certificates/g033.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g033.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g033.json` | `/status` | str |  |
| `results/certificates/g034.json` | `/` | object | 4 |
| `results/certificates/g034.json` | `/obstructions` | array | 0 |
| `results/certificates/g034.json` | `/orders` | array | 8 |
| `results/certificates/g034.json` | `/orders/0` | array | 8 |
| `results/certificates/g034.json` | `/orders/0/0` | int |  |
| `results/certificates/g034.json` | `/regions` | array | 1 |
| `results/certificates/g034.json` | `/regions/0` | object | 4 |
| `results/certificates/g034.json` | `/regions/0/class` | str |  |
| `results/certificates/g034.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/g034.json` | `/regions/0/owners` | array | 8 |
| `results/certificates/g034.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g034.json` | `/regions/0/support` | array | 8 |
| `results/certificates/g034.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g034.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g034.json` | `/status` | str |  |
| `results/certificates/g035.json` | `/` | object | 4 |
| `results/certificates/g035.json` | `/obstructions` | array | 0 |
| `results/certificates/g035.json` | `/orders` | array | 16 |
| `results/certificates/g035.json` | `/orders/0` | array | 16 |
| `results/certificates/g035.json` | `/orders/0/0` | int |  |
| `results/certificates/g035.json` | `/regions` | array | 1 |
| `results/certificates/g035.json` | `/regions/0` | object | 4 |
| `results/certificates/g035.json` | `/regions/0/class` | str |  |
| `results/certificates/g035.json` | `/regions/0/excluded` | array | 0 |
| `results/certificates/g035.json` | `/regions/0/owners` | array | 16 |
| `results/certificates/g035.json` | `/regions/0/owners/0` | str |  |
| `results/certificates/g035.json` | `/regions/0/support` | array | 16 |
| `results/certificates/g035.json` | `/regions/0/support/0` | array | 2 |
| `results/certificates/g035.json` | `/regions/0/support/0/0` | str |  |
| `results/certificates/g035.json` | `/status` | str |  |
| `results/certificates/g036.json` | `/` | object | 2 |
| `results/certificates/g036.json` | `/obstruction` | object | 3 |
| `results/certificates/g036.json` | `/obstruction/kind` | str |  |
| `results/certificates/g036.json` | `/obstruction/nodes` | array | 2 |
| `results/certificates/g036.json` | `/obstruction/nodes/0` | int |  |
| `results/certificates/g036.json` | `/obstruction/reasons` | array | 2 |
| `results/certificates/g036.json` | `/obstruction/reasons/0` | object | 3 |
| `results/certificates/g036.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/certificates/g036.json` | `/obstruction/reasons/0/node` | int |  |
| `results/certificates/g036.json` | `/obstruction/reasons/0/row` | int |  |
| `results/certificates/g036.json` | `/status` | str |  |
| `results/certificates/g037.json` | `/` | object | 2 |
| `results/certificates/g037.json` | `/obstruction` | object | 3 |
| `results/certificates/g037.json` | `/obstruction/kind` | str |  |
| `results/certificates/g037.json` | `/obstruction/nodes` | array | 3 |
| `results/certificates/g037.json` | `/obstruction/nodes/0` | int |  |
| `results/certificates/g037.json` | `/obstruction/reasons` | array | 3 |
| `results/certificates/g037.json` | `/obstruction/reasons/0` | object | 3 |
| `results/certificates/g037.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/certificates/g037.json` | `/obstruction/reasons/0/node` | int |  |
| `results/certificates/g037.json` | `/obstruction/reasons/0/row` | int |  |
| `results/certificates/g037.json` | `/status` | str |  |
| `results/certificates/g038.json` | `/` | object | 2 |
| `results/certificates/g038.json` | `/obstruction` | object | 3 |
| `results/certificates/g038.json` | `/obstruction/kind` | str |  |
| `results/certificates/g038.json` | `/obstruction/nodes` | array | 5 |
| `results/certificates/g038.json` | `/obstruction/nodes/0` | int |  |
| `results/certificates/g038.json` | `/obstruction/reasons` | array | 5 |
| `results/certificates/g038.json` | `/obstruction/reasons/0` | object | 3 |
| `results/certificates/g038.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/certificates/g038.json` | `/obstruction/reasons/0/node` | int |  |
| `results/certificates/g038.json` | `/obstruction/reasons/0/row` | int |  |
| `results/certificates/g038.json` | `/status` | str |  |
| `results/certificates/g039.json` | `/` | object | 2 |
| `results/certificates/g039.json` | `/obstruction` | object | 3 |
| `results/certificates/g039.json` | `/obstruction/kind` | str |  |
| `results/certificates/g039.json` | `/obstruction/nodes` | array | 8 |
| `results/certificates/g039.json` | `/obstruction/nodes/0` | int |  |
| `results/certificates/g039.json` | `/obstruction/reasons` | array | 8 |
| `results/certificates/g039.json` | `/obstruction/reasons/0` | object | 3 |
| `results/certificates/g039.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/certificates/g039.json` | `/obstruction/reasons/0/node` | int |  |
| `results/certificates/g039.json` | `/obstruction/reasons/0/row` | int |  |
| `results/certificates/g039.json` | `/status` | str |  |
| `results/certificates/g040.json` | `/` | object | 2 |
| `results/certificates/g040.json` | `/obstruction` | object | 3 |
| `results/certificates/g040.json` | `/obstruction/kind` | str |  |
| `results/certificates/g040.json` | `/obstruction/nodes` | array | 16 |
| `results/certificates/g040.json` | `/obstruction/nodes/0` | int |  |
| `results/certificates/g040.json` | `/obstruction/reasons` | array | 16 |
| `results/certificates/g040.json` | `/obstruction/reasons/0` | object | 3 |
| `results/certificates/g040.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/certificates/g040.json` | `/obstruction/reasons/0/node` | int |  |
| `results/certificates/g040.json` | `/obstruction/reasons/0/row` | int |  |
| `results/certificates/g040.json` | `/status` | str |  |
| `results/clean_reproduction/campaign_summary.json` | `/` | object | 19 |
| `results/clean_reproduction/campaign_summary.json` | `/cases` | int |  |
| `results/clean_reproduction/campaign_summary.json` | `/generated_cases` | int |  |
| `results/clean_reproduction/campaign_summary.json` | `/boundary_fixtures` | int |  |
| `results/clean_reproduction/campaign_summary.json` | `/public_builds` | int |  |
| `results/clean_reproduction/campaign_summary.json` | `/classified_inputs` | int |  |
| `results/clean_reproduction/campaign_summary.json` | `/inconsistent_inputs` | int |  |
| `results/clean_reproduction/campaign_summary.json` | `/admission_rejected_inputs` | int |  |
| `results/clean_reproduction/campaign_summary.json` | `/rows` | int |  |
| `results/clean_reproduction/campaign_summary.json` | `/incidences` | int |  |
| `results/clean_reproduction/campaign_summary.json` | `/developer` | int |  |
| `results/clean_reproduction/campaign_summary.json` | `/library` | int |  |
| `results/clean_reproduction/campaign_summary.json` | `/ambiguous` | int |  |
| `results/clean_reproduction/campaign_summary.json` | `/dependency_strictly_narrowed` | int |  |
| `results/clean_reproduction/campaign_summary.json` | `/bytes_strictly_narrowed` | int |  |
| `results/clean_reproduction/campaign_summary.json` | `/certificate_bytes` | int |  |
| `results/clean_reproduction/campaign_summary.json` | `/cpu_seconds` | float |  |
| `results/clean_reproduction/campaign_summary.json` | `/wall_seconds` | float |  |
| `results/clean_reproduction/campaign_summary.json` | `/peak_rss_kib` | int |  |
| `results/clean_reproduction/campaign_summary.json` | `/baseline_scope` | str |  |
| `results/clean_reproduction/cases.csv` | `case` | CSV column | 60 |
| `results/clean_reproduction/cases.csv` | `group` | CSV column | 60 |
| `results/clean_reproduction/cases.csv` | `phenomenon` | CSV column | 60 |
| `results/clean_reproduction/cases.csv` | `providers` | CSV column | 60 |
| `results/clean_reproduction/cases.csv` | `rows` | CSV column | 60 |
| `results/clean_reproduction/cases.csv` | `incidences` | CSV column | 60 |
| `results/clean_reproduction/cases.csv` | `status` | CSV column | 60 |
| `results/clean_reproduction/cases.csv` | `developer` | CSV column | 60 |
| `results/clean_reproduction/cases.csv` | `library` | CSV column | 60 |
| `results/clean_reproduction/cases.csv` | `ambiguous` | CSV column | 60 |
| `results/clean_reproduction/cases.csv` | `dependency_strictly_narrowed` | CSV column | 60 |
| `results/clean_reproduction/cases.csv` | `bytes_strictly_narrowed` | CSV column | 60 |
| `results/clean_reproduction/cases.csv` | `orders` | CSV column | 60 |
| `results/clean_reproduction/cases.csv` | `certificate_bytes` | CSV column | 60 |
| `results/clean_reproduction/cases.csv` | `producer_cpu_seconds` | CSV column | 60 |
| `results/clean_reproduction/cases.csv` | `checker_cpu_seconds` | CSV column | 60 |
| `results/clean_reproduction/certificates/f001.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/f001.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/f001.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/f001.json` | `/orders/0` | array | 1 |
| `results/clean_reproduction/certificates/f001.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/f001.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/f001.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/f001.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/f001.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/f001.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/f001.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/f001.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/f001.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/f001.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/f001.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f002.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/f002.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/f002.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/f002.json` | `/orders/0` | array | 1 |
| `results/clean_reproduction/certificates/f002.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/f002.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/f002.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/f002.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/f002.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/f002.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/f002.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/f002.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/f002.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/f002.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/f002.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f003.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/f003.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/f003.json` | `/orders` | array | 2 |
| `results/clean_reproduction/certificates/f003.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/certificates/f003.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/f003.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/f003.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/f003.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/f003.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/f003.json` | `/regions/0/owners` | array | 2 |
| `results/clean_reproduction/certificates/f003.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/f003.json` | `/regions/0/support` | array | 2 |
| `results/clean_reproduction/certificates/f003.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/f003.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/f003.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f004.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/f004.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/f004.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/f004.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/certificates/f004.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/f004.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/f004.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/f004.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/f004.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/f004.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/f004.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/f004.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/f004.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/f004.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/f004.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f005.json` | `/` | object | 2 |
| `results/clean_reproduction/certificates/f005.json` | `/obstruction` | object | 3 |
| `results/clean_reproduction/certificates/f005.json` | `/obstruction/kind` | str |  |
| `results/clean_reproduction/certificates/f005.json` | `/obstruction/nodes` | array | 2 |
| `results/clean_reproduction/certificates/f005.json` | `/obstruction/nodes/0` | int |  |
| `results/clean_reproduction/certificates/f005.json` | `/obstruction/reasons` | array | 2 |
| `results/clean_reproduction/certificates/f005.json` | `/obstruction/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/f005.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/f005.json` | `/obstruction/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/f005.json` | `/obstruction/reasons/0/row` | int |  |
| `results/clean_reproduction/certificates/f005.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f006.json` | `/` | object | 2 |
| `results/clean_reproduction/certificates/f006.json` | `/obstruction` | object | 2 |
| `results/clean_reproduction/certificates/f006.json` | `/obstruction/kind` | str |  |
| `results/clean_reproduction/certificates/f006.json` | `/obstruction/row` | int |  |
| `results/clean_reproduction/certificates/f006.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f007.json` | `/` | object | 2 |
| `results/clean_reproduction/certificates/f007.json` | `/obstruction` | object | 3 |
| `results/clean_reproduction/certificates/f007.json` | `/obstruction/kind` | str |  |
| `results/clean_reproduction/certificates/f007.json` | `/obstruction/nodes` | array | 2 |
| `results/clean_reproduction/certificates/f007.json` | `/obstruction/nodes/0` | int |  |
| `results/clean_reproduction/certificates/f007.json` | `/obstruction/reasons` | array | 2 |
| `results/clean_reproduction/certificates/f007.json` | `/obstruction/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/f007.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/f007.json` | `/obstruction/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/f007.json` | `/obstruction/reasons/0/row` | int |  |
| `results/clean_reproduction/certificates/f007.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f008.json` | `/` | object | 2 |
| `results/clean_reproduction/certificates/f008.json` | `/obstruction` | object | 3 |
| `results/clean_reproduction/certificates/f008.json` | `/obstruction/kind` | str |  |
| `results/clean_reproduction/certificates/f008.json` | `/obstruction/nodes` | array | 2 |
| `results/clean_reproduction/certificates/f008.json` | `/obstruction/nodes/0` | int |  |
| `results/clean_reproduction/certificates/f008.json` | `/obstruction/reasons` | array | 2 |
| `results/clean_reproduction/certificates/f008.json` | `/obstruction/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/f008.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/f008.json` | `/obstruction/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/f008.json` | `/obstruction/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/f008.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f009.json` | `/` | object | 2 |
| `results/clean_reproduction/certificates/f009.json` | `/obstruction` | object | 3 |
| `results/clean_reproduction/certificates/f009.json` | `/obstruction/kind` | str |  |
| `results/clean_reproduction/certificates/f009.json` | `/obstruction/nodes` | array | 1 |
| `results/clean_reproduction/certificates/f009.json` | `/obstruction/nodes/0` | int |  |
| `results/clean_reproduction/certificates/f009.json` | `/obstruction/reasons` | array | 1 |
| `results/clean_reproduction/certificates/f009.json` | `/obstruction/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/f009.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/f009.json` | `/obstruction/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/f009.json` | `/obstruction/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/f009.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f010.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/f010.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/f010.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/f010.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/certificates/f010.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/f010.json` | `/regions` | array | 0 |
| `results/clean_reproduction/certificates/f010.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f011.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/f011.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/f011.json` | `/orders` | array | 2 |
| `results/clean_reproduction/certificates/f011.json` | `/orders/0` | array | 3 |
| `results/clean_reproduction/certificates/f011.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/f011.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/f011.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/f011.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/f011.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/f011.json` | `/regions/0/owners` | array | 2 |
| `results/clean_reproduction/certificates/f011.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/f011.json` | `/regions/0/support` | array | 2 |
| `results/clean_reproduction/certificates/f011.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/f011.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/f011.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f012.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/f012.json` | `/obstructions` | array | 1 |
| `results/clean_reproduction/certificates/f012.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/f012.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/f012.json` | `/obstructions/0/nodes` | array | 2 |
| `results/clean_reproduction/certificates/f012.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/f012.json` | `/obstructions/0/reasons` | array | 2 |
| `results/clean_reproduction/certificates/f012.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/f012.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/f012.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/f012.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/f012.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/f012.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/certificates/f012.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/f012.json` | `/regions` | array | 2 |
| `results/clean_reproduction/certificates/f012.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/f012.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/f012.json` | `/regions/0/excluded` | array | 1 |
| `results/clean_reproduction/certificates/f012.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/f012.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/f012.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/f012.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/f012.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/f012.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/f012.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/f012.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/f012.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f013.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/f013.json` | `/obstructions` | array | 1 |
| `results/clean_reproduction/certificates/f013.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/f013.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/f013.json` | `/obstructions/0/nodes` | array | 3 |
| `results/clean_reproduction/certificates/f013.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/f013.json` | `/obstructions/0/reasons` | array | 3 |
| `results/clean_reproduction/certificates/f013.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/f013.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/f013.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/f013.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/f013.json` | `/orders` | array | 2 |
| `results/clean_reproduction/certificates/f013.json` | `/orders/0` | array | 3 |
| `results/clean_reproduction/certificates/f013.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/f013.json` | `/regions` | array | 2 |
| `results/clean_reproduction/certificates/f013.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/f013.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/f013.json` | `/regions/0/excluded` | array | 1 |
| `results/clean_reproduction/certificates/f013.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/f013.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/f013.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/f013.json` | `/regions/0/owners` | array | 2 |
| `results/clean_reproduction/certificates/f013.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/f013.json` | `/regions/0/support` | array | 2 |
| `results/clean_reproduction/certificates/f013.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/f013.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/f013.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f014.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/f014.json` | `/obstructions` | array | 1 |
| `results/clean_reproduction/certificates/f014.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/f014.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/f014.json` | `/obstructions/0/nodes` | array | 2 |
| `results/clean_reproduction/certificates/f014.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/f014.json` | `/obstructions/0/reasons` | array | 2 |
| `results/clean_reproduction/certificates/f014.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/f014.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/f014.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/f014.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/f014.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/f014.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/certificates/f014.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/f014.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/f014.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/f014.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/f014.json` | `/regions/0/excluded` | array | 1 |
| `results/clean_reproduction/certificates/f014.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/f014.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/f014.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/f014.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/f014.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/f014.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/f014.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/f014.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/f014.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f015.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/f015.json` | `/obstructions` | array | 1 |
| `results/clean_reproduction/certificates/f015.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/f015.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/f015.json` | `/obstructions/0/nodes` | array | 3 |
| `results/clean_reproduction/certificates/f015.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/f015.json` | `/obstructions/0/reasons` | array | 3 |
| `results/clean_reproduction/certificates/f015.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/f015.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/f015.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/f015.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/f015.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/f015.json` | `/orders/0` | array | 3 |
| `results/clean_reproduction/certificates/f015.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/f015.json` | `/regions` | array | 2 |
| `results/clean_reproduction/certificates/f015.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/f015.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/f015.json` | `/regions/0/excluded` | array | 1 |
| `results/clean_reproduction/certificates/f015.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/f015.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/f015.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/f015.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/f015.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/f015.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/f015.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/f015.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/f015.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f016.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/f016.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/f016.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/f016.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/certificates/f016.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/f016.json` | `/regions` | array | 2 |
| `results/clean_reproduction/certificates/f016.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/f016.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/f016.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/f016.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/f016.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/f016.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/f016.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/f016.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/f016.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f017.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/f017.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/f017.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/f017.json` | `/orders/0` | array | 1 |
| `results/clean_reproduction/certificates/f017.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/f017.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/f017.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/f017.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/f017.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/f017.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/f017.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/f017.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/f017.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/f017.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/f017.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/f018.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/f018.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/f018.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/f018.json` | `/orders/0` | array | 1 |
| `results/clean_reproduction/certificates/f018.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/f018.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/f018.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/f018.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/f018.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/f018.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/f018.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/f018.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/f018.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/f018.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/f018.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g001.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g001.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/g001.json` | `/orders` | array | 2 |
| `results/clean_reproduction/certificates/g001.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/certificates/g001.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g001.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g001.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g001.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g001.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/g001.json` | `/regions/0/owners` | array | 2 |
| `results/clean_reproduction/certificates/g001.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g001.json` | `/regions/0/support` | array | 2 |
| `results/clean_reproduction/certificates/g001.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g001.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g001.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g002.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g002.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/g002.json` | `/orders` | array | 3 |
| `results/clean_reproduction/certificates/g002.json` | `/orders/0` | array | 3 |
| `results/clean_reproduction/certificates/g002.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g002.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g002.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g002.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g002.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/g002.json` | `/regions/0/owners` | array | 3 |
| `results/clean_reproduction/certificates/g002.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g002.json` | `/regions/0/support` | array | 3 |
| `results/clean_reproduction/certificates/g002.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g002.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g002.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g003.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g003.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/g003.json` | `/orders` | array | 5 |
| `results/clean_reproduction/certificates/g003.json` | `/orders/0` | array | 5 |
| `results/clean_reproduction/certificates/g003.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g003.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g003.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g003.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g003.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/g003.json` | `/regions/0/owners` | array | 5 |
| `results/clean_reproduction/certificates/g003.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g003.json` | `/regions/0/support` | array | 5 |
| `results/clean_reproduction/certificates/g003.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g003.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g003.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g004.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g004.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/g004.json` | `/orders` | array | 8 |
| `results/clean_reproduction/certificates/g004.json` | `/orders/0` | array | 8 |
| `results/clean_reproduction/certificates/g004.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g004.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g004.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g004.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g004.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/g004.json` | `/regions/0/owners` | array | 8 |
| `results/clean_reproduction/certificates/g004.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g004.json` | `/regions/0/support` | array | 8 |
| `results/clean_reproduction/certificates/g004.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g004.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g004.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g005.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g005.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/g005.json` | `/orders` | array | 16 |
| `results/clean_reproduction/certificates/g005.json` | `/orders/0` | array | 16 |
| `results/clean_reproduction/certificates/g005.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g005.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g005.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g005.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g005.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/g005.json` | `/regions/0/owners` | array | 16 |
| `results/clean_reproduction/certificates/g005.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g005.json` | `/regions/0/support` | array | 16 |
| `results/clean_reproduction/certificates/g005.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g005.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g005.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g006.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g006.json` | `/obstructions` | array | 1 |
| `results/clean_reproduction/certificates/g006.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/g006.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/g006.json` | `/obstructions/0/nodes` | array | 2 |
| `results/clean_reproduction/certificates/g006.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g006.json` | `/obstructions/0/reasons` | array | 2 |
| `results/clean_reproduction/certificates/g006.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g006.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g006.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g006.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/g006.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/g006.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/certificates/g006.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g006.json` | `/regions` | array | 2 |
| `results/clean_reproduction/certificates/g006.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g006.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g006.json` | `/regions/0/excluded` | array | 1 |
| `results/clean_reproduction/certificates/g006.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/g006.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/g006.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/g006.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/g006.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g006.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/g006.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g006.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g006.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g007.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g007.json` | `/obstructions` | array | 2 |
| `results/clean_reproduction/certificates/g007.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/g007.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/g007.json` | `/obstructions/0/nodes` | array | 3 |
| `results/clean_reproduction/certificates/g007.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g007.json` | `/obstructions/0/reasons` | array | 3 |
| `results/clean_reproduction/certificates/g007.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g007.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g007.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g007.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/g007.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/g007.json` | `/orders/0` | array | 3 |
| `results/clean_reproduction/certificates/g007.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g007.json` | `/regions` | array | 3 |
| `results/clean_reproduction/certificates/g007.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g007.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g007.json` | `/regions/0/excluded` | array | 2 |
| `results/clean_reproduction/certificates/g007.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/g007.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/g007.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/g007.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/g007.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g007.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/g007.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g007.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g007.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g008.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g008.json` | `/obstructions` | array | 4 |
| `results/clean_reproduction/certificates/g008.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/g008.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/g008.json` | `/obstructions/0/nodes` | array | 5 |
| `results/clean_reproduction/certificates/g008.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g008.json` | `/obstructions/0/reasons` | array | 5 |
| `results/clean_reproduction/certificates/g008.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g008.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g008.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g008.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/g008.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/g008.json` | `/orders/0` | array | 5 |
| `results/clean_reproduction/certificates/g008.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g008.json` | `/regions` | array | 5 |
| `results/clean_reproduction/certificates/g008.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g008.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g008.json` | `/regions/0/excluded` | array | 4 |
| `results/clean_reproduction/certificates/g008.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/g008.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/g008.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/g008.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/g008.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g008.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/g008.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g008.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g008.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g009.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g009.json` | `/obstructions` | array | 7 |
| `results/clean_reproduction/certificates/g009.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/g009.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/g009.json` | `/obstructions/0/nodes` | array | 8 |
| `results/clean_reproduction/certificates/g009.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g009.json` | `/obstructions/0/reasons` | array | 8 |
| `results/clean_reproduction/certificates/g009.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g009.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g009.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g009.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/g009.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/g009.json` | `/orders/0` | array | 8 |
| `results/clean_reproduction/certificates/g009.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g009.json` | `/regions` | array | 8 |
| `results/clean_reproduction/certificates/g009.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g009.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g009.json` | `/regions/0/excluded` | array | 7 |
| `results/clean_reproduction/certificates/g009.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/g009.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/g009.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/g009.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/g009.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g009.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/g009.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g009.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g009.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g010.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g010.json` | `/obstructions` | array | 15 |
| `results/clean_reproduction/certificates/g010.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/g010.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/g010.json` | `/obstructions/0/nodes` | array | 16 |
| `results/clean_reproduction/certificates/g010.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g010.json` | `/obstructions/0/reasons` | array | 16 |
| `results/clean_reproduction/certificates/g010.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g010.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g010.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g010.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/g010.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/g010.json` | `/orders/0` | array | 16 |
| `results/clean_reproduction/certificates/g010.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g010.json` | `/regions` | array | 16 |
| `results/clean_reproduction/certificates/g010.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g010.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g010.json` | `/regions/0/excluded` | array | 15 |
| `results/clean_reproduction/certificates/g010.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/g010.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/g010.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/g010.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/g010.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g010.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/g010.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g010.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g010.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g011.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g011.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/g011.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/g011.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/certificates/g011.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g011.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g011.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g011.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g011.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/g011.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/g011.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g011.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/g011.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g011.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g011.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g012.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g012.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/g012.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/g012.json` | `/orders/0` | array | 3 |
| `results/clean_reproduction/certificates/g012.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g012.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g012.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g012.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g012.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/g012.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/g012.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g012.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/g012.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g012.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g012.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g013.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g013.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/g013.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/g013.json` | `/orders/0` | array | 5 |
| `results/clean_reproduction/certificates/g013.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g013.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g013.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g013.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g013.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/g013.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/g013.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g013.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/g013.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g013.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g013.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g014.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g014.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/g014.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/g014.json` | `/orders/0` | array | 8 |
| `results/clean_reproduction/certificates/g014.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g014.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g014.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g014.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g014.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/g014.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/g014.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g014.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/g014.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g014.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g014.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g015.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g015.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/g015.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/g015.json` | `/orders/0` | array | 16 |
| `results/clean_reproduction/certificates/g015.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g015.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g015.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g015.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g015.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/g015.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/g015.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g015.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/g015.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g015.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g015.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g016.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g016.json` | `/obstructions` | array | 1 |
| `results/clean_reproduction/certificates/g016.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/g016.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/g016.json` | `/obstructions/0/nodes` | array | 2 |
| `results/clean_reproduction/certificates/g016.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g016.json` | `/obstructions/0/reasons` | array | 2 |
| `results/clean_reproduction/certificates/g016.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g016.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g016.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g016.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/g016.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/g016.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/certificates/g016.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g016.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g016.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g016.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g016.json` | `/regions/0/excluded` | array | 1 |
| `results/clean_reproduction/certificates/g016.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/g016.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/g016.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/g016.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/g016.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g016.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/g016.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g016.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g016.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g017.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g017.json` | `/obstructions` | array | 2 |
| `results/clean_reproduction/certificates/g017.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/g017.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/g017.json` | `/obstructions/0/nodes` | array | 3 |
| `results/clean_reproduction/certificates/g017.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g017.json` | `/obstructions/0/reasons` | array | 3 |
| `results/clean_reproduction/certificates/g017.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g017.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g017.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g017.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/g017.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/g017.json` | `/orders/0` | array | 3 |
| `results/clean_reproduction/certificates/g017.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g017.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g017.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g017.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g017.json` | `/regions/0/excluded` | array | 2 |
| `results/clean_reproduction/certificates/g017.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/g017.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/g017.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/g017.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/g017.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g017.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/g017.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g017.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g017.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g018.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g018.json` | `/obstructions` | array | 4 |
| `results/clean_reproduction/certificates/g018.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/g018.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/g018.json` | `/obstructions/0/nodes` | array | 5 |
| `results/clean_reproduction/certificates/g018.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g018.json` | `/obstructions/0/reasons` | array | 5 |
| `results/clean_reproduction/certificates/g018.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g018.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g018.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g018.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/g018.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/g018.json` | `/orders/0` | array | 5 |
| `results/clean_reproduction/certificates/g018.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g018.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g018.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g018.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g018.json` | `/regions/0/excluded` | array | 4 |
| `results/clean_reproduction/certificates/g018.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/g018.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/g018.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/g018.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/g018.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g018.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/g018.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g018.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g018.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g019.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g019.json` | `/obstructions` | array | 7 |
| `results/clean_reproduction/certificates/g019.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/g019.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/g019.json` | `/obstructions/0/nodes` | array | 8 |
| `results/clean_reproduction/certificates/g019.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g019.json` | `/obstructions/0/reasons` | array | 8 |
| `results/clean_reproduction/certificates/g019.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g019.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g019.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g019.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/g019.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/g019.json` | `/orders/0` | array | 8 |
| `results/clean_reproduction/certificates/g019.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g019.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g019.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g019.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g019.json` | `/regions/0/excluded` | array | 7 |
| `results/clean_reproduction/certificates/g019.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/g019.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/g019.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/g019.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/g019.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g019.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/g019.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g019.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g019.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g020.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g020.json` | `/obstructions` | array | 15 |
| `results/clean_reproduction/certificates/g020.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/g020.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/g020.json` | `/obstructions/0/nodes` | array | 16 |
| `results/clean_reproduction/certificates/g020.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g020.json` | `/obstructions/0/reasons` | array | 16 |
| `results/clean_reproduction/certificates/g020.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g020.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g020.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g020.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/g020.json` | `/orders` | array | 1 |
| `results/clean_reproduction/certificates/g020.json` | `/orders/0` | array | 16 |
| `results/clean_reproduction/certificates/g020.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g020.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g020.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g020.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g020.json` | `/regions/0/excluded` | array | 15 |
| `results/clean_reproduction/certificates/g020.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/g020.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/g020.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/g020.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/certificates/g020.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g020.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/certificates/g020.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g020.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g020.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g021.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g021.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/g021.json` | `/orders` | array | 2 |
| `results/clean_reproduction/certificates/g021.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/certificates/g021.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g021.json` | `/regions` | array | 2 |
| `results/clean_reproduction/certificates/g021.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g021.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g021.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/g021.json` | `/regions/0/owners` | array | 2 |
| `results/clean_reproduction/certificates/g021.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g021.json` | `/regions/0/support` | array | 2 |
| `results/clean_reproduction/certificates/g021.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g021.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g021.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g022.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g022.json` | `/obstructions` | array | 1 |
| `results/clean_reproduction/certificates/g022.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/g022.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/g022.json` | `/obstructions/0/nodes` | array | 3 |
| `results/clean_reproduction/certificates/g022.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g022.json` | `/obstructions/0/reasons` | array | 3 |
| `results/clean_reproduction/certificates/g022.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g022.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g022.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g022.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/g022.json` | `/orders` | array | 2 |
| `results/clean_reproduction/certificates/g022.json` | `/orders/0` | array | 3 |
| `results/clean_reproduction/certificates/g022.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g022.json` | `/regions` | array | 2 |
| `results/clean_reproduction/certificates/g022.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g022.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g022.json` | `/regions/0/excluded` | array | 1 |
| `results/clean_reproduction/certificates/g022.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/g022.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/g022.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/g022.json` | `/regions/0/owners` | array | 2 |
| `results/clean_reproduction/certificates/g022.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g022.json` | `/regions/0/support` | array | 2 |
| `results/clean_reproduction/certificates/g022.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g022.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g022.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g023.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g023.json` | `/obstructions` | array | 3 |
| `results/clean_reproduction/certificates/g023.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/g023.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/g023.json` | `/obstructions/0/nodes` | array | 5 |
| `results/clean_reproduction/certificates/g023.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g023.json` | `/obstructions/0/reasons` | array | 5 |
| `results/clean_reproduction/certificates/g023.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g023.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g023.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g023.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/g023.json` | `/orders` | array | 2 |
| `results/clean_reproduction/certificates/g023.json` | `/orders/0` | array | 5 |
| `results/clean_reproduction/certificates/g023.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g023.json` | `/regions` | array | 2 |
| `results/clean_reproduction/certificates/g023.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g023.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g023.json` | `/regions/0/excluded` | array | 3 |
| `results/clean_reproduction/certificates/g023.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/g023.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/g023.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/g023.json` | `/regions/0/owners` | array | 2 |
| `results/clean_reproduction/certificates/g023.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g023.json` | `/regions/0/support` | array | 2 |
| `results/clean_reproduction/certificates/g023.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g023.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g023.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g024.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g024.json` | `/obstructions` | array | 6 |
| `results/clean_reproduction/certificates/g024.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/g024.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/g024.json` | `/obstructions/0/nodes` | array | 8 |
| `results/clean_reproduction/certificates/g024.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g024.json` | `/obstructions/0/reasons` | array | 8 |
| `results/clean_reproduction/certificates/g024.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g024.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g024.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g024.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/g024.json` | `/orders` | array | 2 |
| `results/clean_reproduction/certificates/g024.json` | `/orders/0` | array | 8 |
| `results/clean_reproduction/certificates/g024.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g024.json` | `/regions` | array | 2 |
| `results/clean_reproduction/certificates/g024.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g024.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g024.json` | `/regions/0/excluded` | array | 6 |
| `results/clean_reproduction/certificates/g024.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/g024.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/g024.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/g024.json` | `/regions/0/owners` | array | 2 |
| `results/clean_reproduction/certificates/g024.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g024.json` | `/regions/0/support` | array | 2 |
| `results/clean_reproduction/certificates/g024.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g024.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g024.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g025.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g025.json` | `/obstructions` | array | 14 |
| `results/clean_reproduction/certificates/g025.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/certificates/g025.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/certificates/g025.json` | `/obstructions/0/nodes` | array | 16 |
| `results/clean_reproduction/certificates/g025.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g025.json` | `/obstructions/0/reasons` | array | 16 |
| `results/clean_reproduction/certificates/g025.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g025.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g025.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g025.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/certificates/g025.json` | `/orders` | array | 2 |
| `results/clean_reproduction/certificates/g025.json` | `/orders/0` | array | 16 |
| `results/clean_reproduction/certificates/g025.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g025.json` | `/regions` | array | 2 |
| `results/clean_reproduction/certificates/g025.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g025.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g025.json` | `/regions/0/excluded` | array | 14 |
| `results/clean_reproduction/certificates/g025.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/certificates/g025.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/certificates/g025.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/certificates/g025.json` | `/regions/0/owners` | array | 2 |
| `results/clean_reproduction/certificates/g025.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g025.json` | `/regions/0/support` | array | 2 |
| `results/clean_reproduction/certificates/g025.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g025.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g025.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g026.json` | `/` | object | 2 |
| `results/clean_reproduction/certificates/g026.json` | `/obstruction` | object | 3 |
| `results/clean_reproduction/certificates/g026.json` | `/obstruction/kind` | str |  |
| `results/clean_reproduction/certificates/g026.json` | `/obstruction/nodes` | array | 2 |
| `results/clean_reproduction/certificates/g026.json` | `/obstruction/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g026.json` | `/obstruction/reasons` | array | 2 |
| `results/clean_reproduction/certificates/g026.json` | `/obstruction/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g026.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g026.json` | `/obstruction/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g026.json` | `/obstruction/reasons/0/row` | int |  |
| `results/clean_reproduction/certificates/g026.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g027.json` | `/` | object | 2 |
| `results/clean_reproduction/certificates/g027.json` | `/obstruction` | object | 3 |
| `results/clean_reproduction/certificates/g027.json` | `/obstruction/kind` | str |  |
| `results/clean_reproduction/certificates/g027.json` | `/obstruction/nodes` | array | 3 |
| `results/clean_reproduction/certificates/g027.json` | `/obstruction/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g027.json` | `/obstruction/reasons` | array | 3 |
| `results/clean_reproduction/certificates/g027.json` | `/obstruction/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g027.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g027.json` | `/obstruction/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g027.json` | `/obstruction/reasons/0/row` | int |  |
| `results/clean_reproduction/certificates/g027.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g028.json` | `/` | object | 2 |
| `results/clean_reproduction/certificates/g028.json` | `/obstruction` | object | 3 |
| `results/clean_reproduction/certificates/g028.json` | `/obstruction/kind` | str |  |
| `results/clean_reproduction/certificates/g028.json` | `/obstruction/nodes` | array | 5 |
| `results/clean_reproduction/certificates/g028.json` | `/obstruction/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g028.json` | `/obstruction/reasons` | array | 5 |
| `results/clean_reproduction/certificates/g028.json` | `/obstruction/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g028.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g028.json` | `/obstruction/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g028.json` | `/obstruction/reasons/0/row` | int |  |
| `results/clean_reproduction/certificates/g028.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g029.json` | `/` | object | 2 |
| `results/clean_reproduction/certificates/g029.json` | `/obstruction` | object | 3 |
| `results/clean_reproduction/certificates/g029.json` | `/obstruction/kind` | str |  |
| `results/clean_reproduction/certificates/g029.json` | `/obstruction/nodes` | array | 8 |
| `results/clean_reproduction/certificates/g029.json` | `/obstruction/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g029.json` | `/obstruction/reasons` | array | 8 |
| `results/clean_reproduction/certificates/g029.json` | `/obstruction/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g029.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g029.json` | `/obstruction/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g029.json` | `/obstruction/reasons/0/row` | int |  |
| `results/clean_reproduction/certificates/g029.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g030.json` | `/` | object | 2 |
| `results/clean_reproduction/certificates/g030.json` | `/obstruction` | object | 3 |
| `results/clean_reproduction/certificates/g030.json` | `/obstruction/kind` | str |  |
| `results/clean_reproduction/certificates/g030.json` | `/obstruction/nodes` | array | 16 |
| `results/clean_reproduction/certificates/g030.json` | `/obstruction/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g030.json` | `/obstruction/reasons` | array | 16 |
| `results/clean_reproduction/certificates/g030.json` | `/obstruction/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g030.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g030.json` | `/obstruction/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g030.json` | `/obstruction/reasons/0/row` | int |  |
| `results/clean_reproduction/certificates/g030.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g031.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g031.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/g031.json` | `/orders` | array | 2 |
| `results/clean_reproduction/certificates/g031.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/certificates/g031.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g031.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g031.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g031.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g031.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/g031.json` | `/regions/0/owners` | array | 2 |
| `results/clean_reproduction/certificates/g031.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g031.json` | `/regions/0/support` | array | 2 |
| `results/clean_reproduction/certificates/g031.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g031.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g031.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g032.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g032.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/g032.json` | `/orders` | array | 3 |
| `results/clean_reproduction/certificates/g032.json` | `/orders/0` | array | 3 |
| `results/clean_reproduction/certificates/g032.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g032.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g032.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g032.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g032.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/g032.json` | `/regions/0/owners` | array | 3 |
| `results/clean_reproduction/certificates/g032.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g032.json` | `/regions/0/support` | array | 3 |
| `results/clean_reproduction/certificates/g032.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g032.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g032.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g033.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g033.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/g033.json` | `/orders` | array | 5 |
| `results/clean_reproduction/certificates/g033.json` | `/orders/0` | array | 5 |
| `results/clean_reproduction/certificates/g033.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g033.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g033.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g033.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g033.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/g033.json` | `/regions/0/owners` | array | 5 |
| `results/clean_reproduction/certificates/g033.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g033.json` | `/regions/0/support` | array | 5 |
| `results/clean_reproduction/certificates/g033.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g033.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g033.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g034.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g034.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/g034.json` | `/orders` | array | 8 |
| `results/clean_reproduction/certificates/g034.json` | `/orders/0` | array | 8 |
| `results/clean_reproduction/certificates/g034.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g034.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g034.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g034.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g034.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/g034.json` | `/regions/0/owners` | array | 8 |
| `results/clean_reproduction/certificates/g034.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g034.json` | `/regions/0/support` | array | 8 |
| `results/clean_reproduction/certificates/g034.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g034.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g034.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g035.json` | `/` | object | 4 |
| `results/clean_reproduction/certificates/g035.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/certificates/g035.json` | `/orders` | array | 16 |
| `results/clean_reproduction/certificates/g035.json` | `/orders/0` | array | 16 |
| `results/clean_reproduction/certificates/g035.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/certificates/g035.json` | `/regions` | array | 1 |
| `results/clean_reproduction/certificates/g035.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/certificates/g035.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/certificates/g035.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/certificates/g035.json` | `/regions/0/owners` | array | 16 |
| `results/clean_reproduction/certificates/g035.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/certificates/g035.json` | `/regions/0/support` | array | 16 |
| `results/clean_reproduction/certificates/g035.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/certificates/g035.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/certificates/g035.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g036.json` | `/` | object | 2 |
| `results/clean_reproduction/certificates/g036.json` | `/obstruction` | object | 3 |
| `results/clean_reproduction/certificates/g036.json` | `/obstruction/kind` | str |  |
| `results/clean_reproduction/certificates/g036.json` | `/obstruction/nodes` | array | 2 |
| `results/clean_reproduction/certificates/g036.json` | `/obstruction/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g036.json` | `/obstruction/reasons` | array | 2 |
| `results/clean_reproduction/certificates/g036.json` | `/obstruction/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g036.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g036.json` | `/obstruction/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g036.json` | `/obstruction/reasons/0/row` | int |  |
| `results/clean_reproduction/certificates/g036.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g037.json` | `/` | object | 2 |
| `results/clean_reproduction/certificates/g037.json` | `/obstruction` | object | 3 |
| `results/clean_reproduction/certificates/g037.json` | `/obstruction/kind` | str |  |
| `results/clean_reproduction/certificates/g037.json` | `/obstruction/nodes` | array | 3 |
| `results/clean_reproduction/certificates/g037.json` | `/obstruction/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g037.json` | `/obstruction/reasons` | array | 3 |
| `results/clean_reproduction/certificates/g037.json` | `/obstruction/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g037.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g037.json` | `/obstruction/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g037.json` | `/obstruction/reasons/0/row` | int |  |
| `results/clean_reproduction/certificates/g037.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g038.json` | `/` | object | 2 |
| `results/clean_reproduction/certificates/g038.json` | `/obstruction` | object | 3 |
| `results/clean_reproduction/certificates/g038.json` | `/obstruction/kind` | str |  |
| `results/clean_reproduction/certificates/g038.json` | `/obstruction/nodes` | array | 5 |
| `results/clean_reproduction/certificates/g038.json` | `/obstruction/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g038.json` | `/obstruction/reasons` | array | 5 |
| `results/clean_reproduction/certificates/g038.json` | `/obstruction/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g038.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g038.json` | `/obstruction/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g038.json` | `/obstruction/reasons/0/row` | int |  |
| `results/clean_reproduction/certificates/g038.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g039.json` | `/` | object | 2 |
| `results/clean_reproduction/certificates/g039.json` | `/obstruction` | object | 3 |
| `results/clean_reproduction/certificates/g039.json` | `/obstruction/kind` | str |  |
| `results/clean_reproduction/certificates/g039.json` | `/obstruction/nodes` | array | 8 |
| `results/clean_reproduction/certificates/g039.json` | `/obstruction/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g039.json` | `/obstruction/reasons` | array | 8 |
| `results/clean_reproduction/certificates/g039.json` | `/obstruction/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g039.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g039.json` | `/obstruction/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g039.json` | `/obstruction/reasons/0/row` | int |  |
| `results/clean_reproduction/certificates/g039.json` | `/status` | str |  |
| `results/clean_reproduction/certificates/g040.json` | `/` | object | 2 |
| `results/clean_reproduction/certificates/g040.json` | `/obstruction` | object | 3 |
| `results/clean_reproduction/certificates/g040.json` | `/obstruction/kind` | str |  |
| `results/clean_reproduction/certificates/g040.json` | `/obstruction/nodes` | array | 16 |
| `results/clean_reproduction/certificates/g040.json` | `/obstruction/nodes/0` | int |  |
| `results/clean_reproduction/certificates/g040.json` | `/obstruction/reasons` | array | 16 |
| `results/clean_reproduction/certificates/g040.json` | `/obstruction/reasons/0` | object | 3 |
| `results/clean_reproduction/certificates/g040.json` | `/obstruction/reasons/0/kind` | str |  |
| `results/clean_reproduction/certificates/g040.json` | `/obstruction/reasons/0/node` | int |  |
| `results/clean_reproduction/certificates/g040.json` | `/obstruction/reasons/0/row` | int |  |
| `results/clean_reproduction/certificates/g040.json` | `/status` | str |  |
| `results/clean_reproduction/java/b0.certificate.json` | `/` | object | 4 |
| `results/clean_reproduction/java/b0.certificate.json` | `/status` | str |  |
| `results/clean_reproduction/java/b0.certificate.json` | `/orders` | array | 1 |
| `results/clean_reproduction/java/b0.certificate.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/java/b0.certificate.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/java/b0.certificate.json` | `/obstructions` | array | 1 |
| `results/clean_reproduction/java/b0.certificate.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/java/b0.certificate.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/java/b0.certificate.json` | `/obstructions/0/nodes` | array | 2 |
| `results/clean_reproduction/java/b0.certificate.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/java/b0.certificate.json` | `/obstructions/0/reasons` | array | 2 |
| `results/clean_reproduction/java/b0.certificate.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/java/b0.certificate.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/java/b0.certificate.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/java/b0.certificate.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/java/b0.certificate.json` | `/regions` | array | 2 |
| `results/clean_reproduction/java/b0.certificate.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/java/b0.certificate.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/java/b0.certificate.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/java/b0.certificate.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/java/b0.certificate.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/java/b0.certificate.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/java/b0.certificate.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/java/b0.certificate.json` | `/regions/0/excluded` | array | 1 |
| `results/clean_reproduction/java/b0.certificate.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/java/b0.certificate.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/java/b0.certificate.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/java/b0.input.json` | `/` | object | 4 |
| `results/clean_reproduction/java/b0.input.json` | `/kind` | str |  |
| `results/clean_reproduction/java/b0.input.json` | `/providers` | array | 2 |
| `results/clean_reproduction/java/b0.input.json` | `/providers/0` | object | 4 |
| `results/clean_reproduction/java/b0.input.json` | `/providers/0/id` | str |  |
| `results/clean_reproduction/java/b0.input.json` | `/providers/0/owner` | str |  |
| `results/clean_reproduction/java/b0.input.json` | `/providers/0/relocations` | array | 0 |
| `results/clean_reproduction/java/b0.input.json` | `/providers/0/entries` | array | 2 |
| `results/clean_reproduction/java/b0.input.json` | `/providers/0/entries/0` | object | 2 |
| `results/clean_reproduction/java/b0.input.json` | `/providers/0/entries/0/name` | str |  |
| `results/clean_reproduction/java/b0.input.json` | `/providers/0/entries/0/payload` | str |  |
| `results/clean_reproduction/java/b0.input.json` | `/before` | array | 0 |
| `results/clean_reproduction/java/b0.input.json` | `/observed` | array | 2 |
| `results/clean_reproduction/java/b0.input.json` | `/observed/0` | object | 2 |
| `results/clean_reproduction/java/b0.input.json` | `/observed/0/name` | str |  |
| `results/clean_reproduction/java/b0.input.json` | `/observed/0/payload` | str |  |
| `results/clean_reproduction/java/b1.certificate.json` | `/` | object | 4 |
| `results/clean_reproduction/java/b1.certificate.json` | `/status` | str |  |
| `results/clean_reproduction/java/b1.certificate.json` | `/orders` | array | 1 |
| `results/clean_reproduction/java/b1.certificate.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/java/b1.certificate.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/java/b1.certificate.json` | `/obstructions` | array | 1 |
| `results/clean_reproduction/java/b1.certificate.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/java/b1.certificate.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/java/b1.certificate.json` | `/obstructions/0/nodes` | array | 2 |
| `results/clean_reproduction/java/b1.certificate.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/java/b1.certificate.json` | `/obstructions/0/reasons` | array | 2 |
| `results/clean_reproduction/java/b1.certificate.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/java/b1.certificate.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/java/b1.certificate.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/java/b1.certificate.json` | `/obstructions/0/reasons/0/row` | int |  |
| `results/clean_reproduction/java/b1.certificate.json` | `/regions` | array | 2 |
| `results/clean_reproduction/java/b1.certificate.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/java/b1.certificate.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/java/b1.certificate.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/java/b1.certificate.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/java/b1.certificate.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/java/b1.certificate.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/java/b1.certificate.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/java/b1.certificate.json` | `/regions/0/excluded` | array | 1 |
| `results/clean_reproduction/java/b1.certificate.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/java/b1.certificate.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/java/b1.certificate.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/java/b1.input.json` | `/` | object | 4 |
| `results/clean_reproduction/java/b1.input.json` | `/kind` | str |  |
| `results/clean_reproduction/java/b1.input.json` | `/providers` | array | 2 |
| `results/clean_reproduction/java/b1.input.json` | `/providers/0` | object | 4 |
| `results/clean_reproduction/java/b1.input.json` | `/providers/0/id` | str |  |
| `results/clean_reproduction/java/b1.input.json` | `/providers/0/owner` | str |  |
| `results/clean_reproduction/java/b1.input.json` | `/providers/0/relocations` | array | 0 |
| `results/clean_reproduction/java/b1.input.json` | `/providers/0/entries` | array | 2 |
| `results/clean_reproduction/java/b1.input.json` | `/providers/0/entries/0` | object | 2 |
| `results/clean_reproduction/java/b1.input.json` | `/providers/0/entries/0/name` | str |  |
| `results/clean_reproduction/java/b1.input.json` | `/providers/0/entries/0/payload` | str |  |
| `results/clean_reproduction/java/b1.input.json` | `/before` | array | 0 |
| `results/clean_reproduction/java/b1.input.json` | `/observed` | array | 2 |
| `results/clean_reproduction/java/b1.input.json` | `/observed/0` | object | 2 |
| `results/clean_reproduction/java/b1.input.json` | `/observed/0/name` | str |  |
| `results/clean_reproduction/java/b1.input.json` | `/observed/0/payload` | str |  |
| `results/clean_reproduction/java_summary.json` | `/` | object | 7 |
| `results/clean_reproduction/java_summary.json` | `/scope` | str |  |
| `results/clean_reproduction/java_summary.json` | `/cases` | array | 2 |
| `results/clean_reproduction/java_summary.json` | `/cases/0` | object | 8 |
| `results/clean_reproduction/java_summary.json` | `/cases/0/case` | str |  |
| `results/clean_reproduction/java_summary.json` | `/cases/0/assembly_order` | array | 2 |
| `results/clean_reproduction/java_summary.json` | `/cases/0/assembly_order/0` | int |  |
| `results/clean_reproduction/java_summary.json` | `/cases/0/runtime_probe_value` | int |  |
| `results/clean_reproduction/java_summary.json` | `/cases/0/marker_byte_candidates` | int |  |
| `results/clean_reproduction/java_summary.json` | `/cases/0/marker_owners` | array | 1 |
| `results/clean_reproduction/java_summary.json` | `/cases/0/marker_owners/0` | str |  |
| `results/clean_reproduction/java_summary.json` | `/cases/0/status` | str |  |
| `results/clean_reproduction/java_summary.json` | `/cases/0/input_bytes` | int |  |
| `results/clean_reproduction/java_summary.json` | `/cases/0/certificate_bytes` | int |  |
| `results/clean_reproduction/java_summary.json` | `/cpu_seconds` | float |  |
| `results/clean_reproduction/java_summary.json` | `/wall_seconds` | float |  |
| `results/clean_reproduction/java_summary.json` | `/parent_peak_rss_kib` | int |  |
| `results/clean_reproduction/java_summary.json` | `/child_peak_rss_kib` | int |  |
| `results/clean_reproduction/java_summary.json` | `/byte_reproduction` | str |  |
| `results/clean_reproduction/oracle_details.csv` | `providers` | CSV column | 69 |
| `results/clean_reproduction/oracle_details.csv` | `precedence_mask` | CSV column | 69 |
| `results/clean_reproduction/oracle_details.csv` | `structures` | CSV column | 69 |
| `results/clean_reproduction/oracle_details.csv` | `labelled_cases` | CSV column | 69 |
| `results/clean_reproduction/oracle_details.csv` | `feasible_labelled_cases` | CSV column | 69 |
| `results/clean_reproduction/oracle_summary.json` | `/` | object | 11 |
| `results/clean_reproduction/oracle_summary.json` | `/structural_cases` | int |  |
| `results/clean_reproduction/oracle_summary.json` | `/labelled_cases` | int |  |
| `results/clean_reproduction/oracle_summary.json` | `/feasible_labelled_cases` | int |  |
| `results/clean_reproduction/oracle_summary.json` | `/region_classifications_checked` | int |  |
| `results/clean_reproduction/oracle_summary.json` | `/mismatches` | int |  |
| `results/clean_reproduction/oracle_summary.json` | `/provider_counts` | array | 3 |
| `results/clean_reproduction/oracle_summary.json` | `/provider_counts/0` | int |  |
| `results/clean_reproduction/oracle_summary.json` | `/region_counts` | array | 3 |
| `results/clean_reproduction/oracle_summary.json` | `/region_counts/0` | int |  |
| `results/clean_reproduction/oracle_summary.json` | `/owner_schemes` | array | 2 |
| `results/clean_reproduction/oracle_summary.json` | `/owner_schemes/0` | str |  |
| `results/clean_reproduction/oracle_summary.json` | `/cpu_seconds` | float |  |
| `results/clean_reproduction/oracle_summary.json` | `/wall_seconds` | float |  |
| `results/clean_reproduction/oracle_summary.json` | `/peak_rss_kib` | int |  |
| `results/clean_reproduction/public/cases.csv` | `build_id` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `pair_id` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `pair_kind` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `first_archive` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `second_archive` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `entry_regions` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `collision_regions` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `admissible_actual_orders` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `ant_matches_first_winner` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `archive_adapters_equal` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `oracle_mismatches` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `local_ambiguous_regions` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `certified_ambiguous_regions` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `global_narrowings` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `equal_regions_resolved_by_coupling` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `witness_orders` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `obstructions` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `certificate_bytes` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `output_bytes` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `output_sha256` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `catalogue_tiebreak_oracle_exact` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `inventory_size_proxy_oracle_exact` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `dependency_oracle_exact` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `local_bytes_oracle_exact` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `certified_oracle_exact` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `trusted_trace_hidden_winner_covered` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `lowering_seconds` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `inference_seconds` | CSV column | 80 |
| `results/clean_reproduction/public/cases.csv` | `checking_seconds` | CSV column | 80 |
| `results/clean_reproduction/public/retained/p001-ab.answer.json` | `/` | object | 2 |
| `results/clean_reproduction/public/retained/p001-ab.answer.json` | `/status` | str |  |
| `results/clean_reproduction/public/retained/p001-ab.answer.json` | `/regions` | array | 2837 |
| `results/clean_reproduction/public/retained/p001-ab.answer.json` | `/regions/0` | object | 3 |
| `results/clean_reproduction/public/retained/p001-ab.answer.json` | `/regions/0/key` | str |  |
| `results/clean_reproduction/public/retained/p001-ab.answer.json` | `/regions/0/owners` | array | 2 |
| `results/clean_reproduction/public/retained/p001-ab.answer.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/public/retained/p001-ab.answer.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/public/retained/p001-ab.certificate.json` | `/` | object | 4 |
| `results/clean_reproduction/public/retained/p001-ab.certificate.json` | `/status` | str |  |
| `results/clean_reproduction/public/retained/p001-ab.certificate.json` | `/orders` | array | 2 |
| `results/clean_reproduction/public/retained/p001-ab.certificate.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/public/retained/p001-ab.certificate.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/public/retained/p001-ab.certificate.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/public/retained/p001-ab.certificate.json` | `/regions` | array | 2837 |
| `results/clean_reproduction/public/retained/p001-ab.certificate.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/public/retained/p001-ab.certificate.json` | `/regions/0/owners` | array | 2 |
| `results/clean_reproduction/public/retained/p001-ab.certificate.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/public/retained/p001-ab.certificate.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/public/retained/p001-ab.certificate.json` | `/regions/0/support` | array | 2 |
| `results/clean_reproduction/public/retained/p001-ab.certificate.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/public/retained/p001-ab.certificate.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/public/retained/p001-ab.certificate.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/public/retained/p001-ab.graph.json` | `/` | object | 4 |
| `results/clean_reproduction/public/retained/p001-ab.graph.json` | `/kind` | str |  |
| `results/clean_reproduction/public/retained/p001-ab.graph.json` | `/owners` | array | 2 |
| `results/clean_reproduction/public/retained/p001-ab.graph.json` | `/owners/0` | str |  |
| `results/clean_reproduction/public/retained/p001-ab.graph.json` | `/before` | array | 0 |
| `results/clean_reproduction/public/retained/p001-ab.graph.json` | `/rows` | array | 2837 |
| `results/clean_reproduction/public/retained/p001-ab.graph.json` | `/rows/0` | object | 3 |
| `results/clean_reproduction/public/retained/p001-ab.graph.json` | `/rows/0/key` | str |  |
| `results/clean_reproduction/public/retained/p001-ab.graph.json` | `/rows/0/present` | array | 2 |
| `results/clean_reproduction/public/retained/p001-ab.graph.json` | `/rows/0/present/0` | int |  |
| `results/clean_reproduction/public/retained/p001-ab.graph.json` | `/rows/0/good` | array | 2 |
| `results/clean_reproduction/public/retained/p001-ab.graph.json` | `/rows/0/good/0` | int |  |
| `results/clean_reproduction/public/retained/p021-ab.answer.json` | `/` | object | 2 |
| `results/clean_reproduction/public/retained/p021-ab.answer.json` | `/status` | str |  |
| `results/clean_reproduction/public/retained/p021-ab.answer.json` | `/regions` | array | 2837 |
| `results/clean_reproduction/public/retained/p021-ab.answer.json` | `/regions/0` | object | 3 |
| `results/clean_reproduction/public/retained/p021-ab.answer.json` | `/regions/0/key` | str |  |
| `results/clean_reproduction/public/retained/p021-ab.answer.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/public/retained/p021-ab.answer.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/public/retained/p021-ab.answer.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/` | object | 4 |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/status` | str |  |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/orders` | array | 1 |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/obstructions` | array | 1 |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/obstructions/0` | object | 3 |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/obstructions/0/kind` | str |  |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/obstructions/0/nodes` | array | 2 |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/obstructions/0/nodes/0` | int |  |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/obstructions/0/reasons` | array | 2 |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/regions` | array | 2837 |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/regions/0/excluded` | array | 1 |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/regions/0/excluded/0` | object | 2 |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/clean_reproduction/public/retained/p021-ab.certificate.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/clean_reproduction/public/retained/p021-ab.graph.json` | `/` | object | 4 |
| `results/clean_reproduction/public/retained/p021-ab.graph.json` | `/kind` | str |  |
| `results/clean_reproduction/public/retained/p021-ab.graph.json` | `/owners` | array | 2 |
| `results/clean_reproduction/public/retained/p021-ab.graph.json` | `/owners/0` | str |  |
| `results/clean_reproduction/public/retained/p021-ab.graph.json` | `/before` | array | 0 |
| `results/clean_reproduction/public/retained/p021-ab.graph.json` | `/rows` | array | 2837 |
| `results/clean_reproduction/public/retained/p021-ab.graph.json` | `/rows/0` | object | 3 |
| `results/clean_reproduction/public/retained/p021-ab.graph.json` | `/rows/0/key` | str |  |
| `results/clean_reproduction/public/retained/p021-ab.graph.json` | `/rows/0/present` | array | 2 |
| `results/clean_reproduction/public/retained/p021-ab.graph.json` | `/rows/0/present/0` | int |  |
| `results/clean_reproduction/public/retained/p021-ab.graph.json` | `/rows/0/good` | array | 2 |
| `results/clean_reproduction/public/retained/p021-ab.graph.json` | `/rows/0/good/0` | int |  |
| `results/clean_reproduction/public/retained/p039-ab.answer.json` | `/` | object | 2 |
| `results/clean_reproduction/public/retained/p039-ab.answer.json` | `/status` | str |  |
| `results/clean_reproduction/public/retained/p039-ab.answer.json` | `/regions` | array | 543 |
| `results/clean_reproduction/public/retained/p039-ab.answer.json` | `/regions/0` | object | 3 |
| `results/clean_reproduction/public/retained/p039-ab.answer.json` | `/regions/0/key` | str |  |
| `results/clean_reproduction/public/retained/p039-ab.answer.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/public/retained/p039-ab.answer.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/public/retained/p039-ab.answer.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/public/retained/p039-ab.certificate.json` | `/` | object | 4 |
| `results/clean_reproduction/public/retained/p039-ab.certificate.json` | `/status` | str |  |
| `results/clean_reproduction/public/retained/p039-ab.certificate.json` | `/orders` | array | 1 |
| `results/clean_reproduction/public/retained/p039-ab.certificate.json` | `/orders/0` | array | 2 |
| `results/clean_reproduction/public/retained/p039-ab.certificate.json` | `/orders/0/0` | int |  |
| `results/clean_reproduction/public/retained/p039-ab.certificate.json` | `/obstructions` | array | 0 |
| `results/clean_reproduction/public/retained/p039-ab.certificate.json` | `/regions` | array | 543 |
| `results/clean_reproduction/public/retained/p039-ab.certificate.json` | `/regions/0` | object | 4 |
| `results/clean_reproduction/public/retained/p039-ab.certificate.json` | `/regions/0/owners` | array | 1 |
| `results/clean_reproduction/public/retained/p039-ab.certificate.json` | `/regions/0/owners/0` | str |  |
| `results/clean_reproduction/public/retained/p039-ab.certificate.json` | `/regions/0/class` | str |  |
| `results/clean_reproduction/public/retained/p039-ab.certificate.json` | `/regions/0/support` | array | 1 |
| `results/clean_reproduction/public/retained/p039-ab.certificate.json` | `/regions/0/support/0` | array | 2 |
| `results/clean_reproduction/public/retained/p039-ab.certificate.json` | `/regions/0/support/0/0` | str |  |
| `results/clean_reproduction/public/retained/p039-ab.certificate.json` | `/regions/0/excluded` | array | 0 |
| `results/clean_reproduction/public/retained/p039-ab.graph.json` | `/` | object | 4 |
| `results/clean_reproduction/public/retained/p039-ab.graph.json` | `/kind` | str |  |
| `results/clean_reproduction/public/retained/p039-ab.graph.json` | `/owners` | array | 2 |
| `results/clean_reproduction/public/retained/p039-ab.graph.json` | `/owners/0` | str |  |
| `results/clean_reproduction/public/retained/p039-ab.graph.json` | `/before` | array | 0 |
| `results/clean_reproduction/public/retained/p039-ab.graph.json` | `/rows` | array | 543 |
| `results/clean_reproduction/public/retained/p039-ab.graph.json` | `/rows/0` | object | 3 |
| `results/clean_reproduction/public/retained/p039-ab.graph.json` | `/rows/0/key` | str |  |
| `results/clean_reproduction/public/retained/p039-ab.graph.json` | `/rows/0/present` | array | 2 |
| `results/clean_reproduction/public/retained/p039-ab.graph.json` | `/rows/0/present/0` | int |  |
| `results/clean_reproduction/public/retained/p039-ab.graph.json` | `/rows/0/good` | array | 1 |
| `results/clean_reproduction/public/retained/p039-ab.graph.json` | `/rows/0/good/0` | int |  |
| `results/clean_reproduction/public/summary.json` | `/` | object | 28 |
| `results/clean_reproduction/public/summary.json` | `/public_provider_archives` | int |  |
| `results/clean_reproduction/public/summary.json` | `/collision_pairs` | int |  |
| `results/clean_reproduction/public/summary.json` | `/actual_ant_builds` | int |  |
| `results/clean_reproduction/public/summary.json` | `/pair_categories` | object | 3 |
| `results/clean_reproduction/public/summary.json` | `/pair_categories/different-only` | int |  |
| `results/clean_reproduction/public/summary.json` | `/pair_categories/equal-only` | int |  |
| `results/clean_reproduction/public/summary.json` | `/pair_categories/mixed` | int |  |
| `results/clean_reproduction/public/summary.json` | `/reversed_pairs_with_identical_output_maps` | int |  |
| `results/clean_reproduction/public/summary.json` | `/indistinguishable_shared_regions_with_owner_flip` | int |  |
| `results/clean_reproduction/public/summary.json` | `/region_observations` | int |  |
| `results/clean_reproduction/public/summary.json` | `/collision_region_observations` | int |  |
| `results/clean_reproduction/public/summary.json` | `/local_byte_ambiguous_regions` | int |  |
| `results/clean_reproduction/public/summary.json` | `/certified_ambiguous_regions` | int |  |
| `results/clean_reproduction/public/summary.json` | `/global_narrowings_over_local_bytes` | int |  |
| `results/clean_reproduction/public/summary.json` | `/equal_byte_regions_resolved_by_global_coupling` | int |  |
| `results/clean_reproduction/public/summary.json` | `/ant_first_winner_mismatches` | int |  |
| `results/clean_reproduction/public/summary.json` | `/independent_archive_adapter_mismatches` | int |  |
| `results/clean_reproduction/public/summary.json` | `/certificate_vs_actual_two_order_oracle_mismatches` | int |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions` | object | 6 |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/catalogue_tiebreak` | object | 6 |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/catalogue_tiebreak/observations` | int |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/catalogue_tiebreak/oracle_exact_count` | int |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/catalogue_tiebreak/oracle_exact_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/catalogue_tiebreak/oracle_conservative_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/catalogue_tiebreak/hidden_winner_coverage_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/catalogue_tiebreak/mean_owner_set_size` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/inventory_size_proxy` | object | 6 |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/inventory_size_proxy/observations` | int |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/inventory_size_proxy/oracle_exact_count` | int |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/inventory_size_proxy/oracle_exact_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/inventory_size_proxy/oracle_conservative_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/inventory_size_proxy/hidden_winner_coverage_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/inventory_size_proxy/mean_owner_set_size` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/dependency` | object | 6 |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/dependency/observations` | int |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/dependency/oracle_exact_count` | int |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/dependency/oracle_exact_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/dependency/oracle_conservative_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/dependency/hidden_winner_coverage_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/dependency/mean_owner_set_size` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/local_bytes` | object | 6 |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/local_bytes/observations` | int |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/local_bytes/oracle_exact_count` | int |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/local_bytes/oracle_exact_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/local_bytes/oracle_conservative_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/local_bytes/hidden_winner_coverage_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/local_bytes/mean_owner_set_size` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/certified` | object | 6 |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/certified/observations` | int |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/certified/oracle_exact_count` | int |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/certified/oracle_exact_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/certified/oracle_conservative_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/certified/hidden_winner_coverage_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/certified/mean_owner_set_size` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/trusted_trace` | object | 6 |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/trusted_trace/observations` | int |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/trusted_trace/oracle_exact_count` | int |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/trusted_trace/oracle_exact_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/trusted_trace/oracle_conservative_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/trusted_trace/hidden_winner_coverage_rate` | float |  |
| `results/clean_reproduction/public/summary.json` | `/baseline_comparison_on_collision_regions/trusted_trace/mean_owner_set_size` | float |  |
| `results/clean_reproduction/public/summary.json` | `/certificate_bytes_min` | int |  |
| `results/clean_reproduction/public/summary.json` | `/certificate_bytes_median` | int |  |
| `results/clean_reproduction/public/summary.json` | `/certificate_bytes_max` | int |  |
| `results/clean_reproduction/public/summary.json` | `/elapsed_seconds` | float |  |
| `results/clean_reproduction/public/summary.json` | `/process_cpu_seconds` | float |  |
| `results/clean_reproduction/public/summary.json` | `/child_user_cpu_seconds` | float |  |
| `results/clean_reproduction/public/summary.json` | `/child_system_cpu_seconds` | float |  |
| `results/clean_reproduction/public/summary.json` | `/child_peak_rss_kib` | int |  |
| `results/clean_reproduction/public/summary.json` | `/workers` | int |  |
| `results/clean_reproduction/public/summary.json` | `/builder` | str |  |
| `results/clean_reproduction/public/summary.json` | `/manifest_handling` | str |  |
| `results/clean_reproduction/public/summary.json` | `/oracle_scope` | str |  |
| `results/clean_reproduction/reproduction_summary.json` | `/` | object | 9 |
| `results/clean_reproduction/reproduction_summary.json` | `/commands` | array | 8 |
| `results/clean_reproduction/reproduction_summary.json` | `/commands/0` | object | 4 |
| `results/clean_reproduction/reproduction_summary.json` | `/commands/0/command` | str |  |
| `results/clean_reproduction/reproduction_summary.json` | `/commands/0/exit_code` | int |  |
| `results/clean_reproduction/reproduction_summary.json` | `/commands/0/wall_seconds` | float |  |
| `results/clean_reproduction/reproduction_summary.json` | `/commands/0/timeout_seconds` | int |  |
| `results/clean_reproduction/reproduction_summary.json` | `/logical_reproduction` | str |  |
| `results/clean_reproduction/reproduction_summary.json` | `/cpu_seconds_children` | float |  |
| `results/clean_reproduction/reproduction_summary.json` | `/wall_seconds` | float |  |
| `results/clean_reproduction/reproduction_summary.json` | `/child_peak_rss_kib` | int |  |
| `results/clean_reproduction/reproduction_summary.json` | `/maximum_workers` | int |  |
| `results/clean_reproduction/reproduction_summary.json` | `/java_requested` | bool |  |
| `results/clean_reproduction/reproduction_summary.json` | `/public_requested` | bool |  |
| `results/clean_reproduction/reproduction_summary.json` | `/scope` | str |  |
| `results/clean_reproduction/scale_summary.json` | `/` | array | 3 |
| `results/clean_reproduction/scale_summary.json` | `/0` | object | 11 |
| `results/clean_reproduction/scale_summary.json` | `/0/case` | str |  |
| `results/clean_reproduction/scale_summary.json` | `/0/providers` | int |  |
| `results/clean_reproduction/scale_summary.json` | `/0/regions` | int |  |
| `results/clean_reproduction/scale_summary.json` | `/0/incidences` | int |  |
| `results/clean_reproduction/scale_summary.json` | `/0/orders` | int |  |
| `results/clean_reproduction/scale_summary.json` | `/0/certificate_bytes` | int |  |
| `results/clean_reproduction/scale_summary.json` | `/0/obstructions` | int |  |
| `results/clean_reproduction/scale_summary.json` | `/0/producer_cpu_seconds` | float |  |
| `results/clean_reproduction/scale_summary.json` | `/0/checker_cpu_seconds` | float |  |
| `results/clean_reproduction/scale_summary.json` | `/0/wall_seconds` | float |  |
| `results/clean_reproduction/scale_summary.json` | `/0/peak_rss_kib` | int |  |
| `results/clean_reproduction_summary.json` | `/` | object | 9 |
| `results/clean_reproduction_summary.json` | `/commands` | array | 8 |
| `results/clean_reproduction_summary.json` | `/commands/0` | object | 4 |
| `results/clean_reproduction_summary.json` | `/commands/0/command` | str |  |
| `results/clean_reproduction_summary.json` | `/commands/0/exit_code` | int |  |
| `results/clean_reproduction_summary.json` | `/commands/0/wall_seconds` | float |  |
| `results/clean_reproduction_summary.json` | `/commands/0/timeout_seconds` | int |  |
| `results/clean_reproduction_summary.json` | `/logical_reproduction` | str |  |
| `results/clean_reproduction_summary.json` | `/cpu_seconds_children` | float |  |
| `results/clean_reproduction_summary.json` | `/wall_seconds` | float |  |
| `results/clean_reproduction_summary.json` | `/child_peak_rss_kib` | int |  |
| `results/clean_reproduction_summary.json` | `/maximum_workers` | int |  |
| `results/clean_reproduction_summary.json` | `/java_requested` | bool |  |
| `results/clean_reproduction_summary.json` | `/public_requested` | bool |  |
| `results/clean_reproduction_summary.json` | `/scope` | str |  |
| `results/java/b0.certificate.json` | `/` | object | 4 |
| `results/java/b0.certificate.json` | `/status` | str |  |
| `results/java/b0.certificate.json` | `/orders` | array | 1 |
| `results/java/b0.certificate.json` | `/orders/0` | array | 2 |
| `results/java/b0.certificate.json` | `/orders/0/0` | int |  |
| `results/java/b0.certificate.json` | `/obstructions` | array | 1 |
| `results/java/b0.certificate.json` | `/obstructions/0` | object | 3 |
| `results/java/b0.certificate.json` | `/obstructions/0/kind` | str |  |
| `results/java/b0.certificate.json` | `/obstructions/0/nodes` | array | 2 |
| `results/java/b0.certificate.json` | `/obstructions/0/nodes/0` | int |  |
| `results/java/b0.certificate.json` | `/obstructions/0/reasons` | array | 2 |
| `results/java/b0.certificate.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/java/b0.certificate.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/java/b0.certificate.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/java/b0.certificate.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/java/b0.certificate.json` | `/regions` | array | 2 |
| `results/java/b0.certificate.json` | `/regions/0` | object | 4 |
| `results/java/b0.certificate.json` | `/regions/0/owners` | array | 1 |
| `results/java/b0.certificate.json` | `/regions/0/owners/0` | str |  |
| `results/java/b0.certificate.json` | `/regions/0/class` | str |  |
| `results/java/b0.certificate.json` | `/regions/0/support` | array | 1 |
| `results/java/b0.certificate.json` | `/regions/0/support/0` | array | 2 |
| `results/java/b0.certificate.json` | `/regions/0/support/0/0` | str |  |
| `results/java/b0.certificate.json` | `/regions/0/excluded` | array | 1 |
| `results/java/b0.certificate.json` | `/regions/0/excluded/0` | object | 2 |
| `results/java/b0.certificate.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/java/b0.certificate.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/java/b0.input.json` | `/` | object | 4 |
| `results/java/b0.input.json` | `/kind` | str |  |
| `results/java/b0.input.json` | `/providers` | array | 2 |
| `results/java/b0.input.json` | `/providers/0` | object | 4 |
| `results/java/b0.input.json` | `/providers/0/id` | str |  |
| `results/java/b0.input.json` | `/providers/0/owner` | str |  |
| `results/java/b0.input.json` | `/providers/0/relocations` | array | 0 |
| `results/java/b0.input.json` | `/providers/0/entries` | array | 2 |
| `results/java/b0.input.json` | `/providers/0/entries/0` | object | 2 |
| `results/java/b0.input.json` | `/providers/0/entries/0/name` | str |  |
| `results/java/b0.input.json` | `/providers/0/entries/0/payload` | str |  |
| `results/java/b0.input.json` | `/before` | array | 0 |
| `results/java/b0.input.json` | `/observed` | array | 2 |
| `results/java/b0.input.json` | `/observed/0` | object | 2 |
| `results/java/b0.input.json` | `/observed/0/name` | str |  |
| `results/java/b0.input.json` | `/observed/0/payload` | str |  |
| `results/java/b1.certificate.json` | `/` | object | 4 |
| `results/java/b1.certificate.json` | `/status` | str |  |
| `results/java/b1.certificate.json` | `/orders` | array | 1 |
| `results/java/b1.certificate.json` | `/orders/0` | array | 2 |
| `results/java/b1.certificate.json` | `/orders/0/0` | int |  |
| `results/java/b1.certificate.json` | `/obstructions` | array | 1 |
| `results/java/b1.certificate.json` | `/obstructions/0` | object | 3 |
| `results/java/b1.certificate.json` | `/obstructions/0/kind` | str |  |
| `results/java/b1.certificate.json` | `/obstructions/0/nodes` | array | 2 |
| `results/java/b1.certificate.json` | `/obstructions/0/nodes/0` | int |  |
| `results/java/b1.certificate.json` | `/obstructions/0/reasons` | array | 2 |
| `results/java/b1.certificate.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/java/b1.certificate.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/java/b1.certificate.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/java/b1.certificate.json` | `/obstructions/0/reasons/0/row` | int |  |
| `results/java/b1.certificate.json` | `/regions` | array | 2 |
| `results/java/b1.certificate.json` | `/regions/0` | object | 4 |
| `results/java/b1.certificate.json` | `/regions/0/owners` | array | 1 |
| `results/java/b1.certificate.json` | `/regions/0/owners/0` | str |  |
| `results/java/b1.certificate.json` | `/regions/0/class` | str |  |
| `results/java/b1.certificate.json` | `/regions/0/support` | array | 1 |
| `results/java/b1.certificate.json` | `/regions/0/support/0` | array | 2 |
| `results/java/b1.certificate.json` | `/regions/0/support/0/0` | str |  |
| `results/java/b1.certificate.json` | `/regions/0/excluded` | array | 1 |
| `results/java/b1.certificate.json` | `/regions/0/excluded/0` | object | 2 |
| `results/java/b1.certificate.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/java/b1.certificate.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/java/b1.input.json` | `/` | object | 4 |
| `results/java/b1.input.json` | `/kind` | str |  |
| `results/java/b1.input.json` | `/providers` | array | 2 |
| `results/java/b1.input.json` | `/providers/0` | object | 4 |
| `results/java/b1.input.json` | `/providers/0/id` | str |  |
| `results/java/b1.input.json` | `/providers/0/owner` | str |  |
| `results/java/b1.input.json` | `/providers/0/relocations` | array | 0 |
| `results/java/b1.input.json` | `/providers/0/entries` | array | 2 |
| `results/java/b1.input.json` | `/providers/0/entries/0` | object | 2 |
| `results/java/b1.input.json` | `/providers/0/entries/0/name` | str |  |
| `results/java/b1.input.json` | `/providers/0/entries/0/payload` | str |  |
| `results/java/b1.input.json` | `/before` | array | 0 |
| `results/java/b1.input.json` | `/observed` | array | 2 |
| `results/java/b1.input.json` | `/observed/0` | object | 2 |
| `results/java/b1.input.json` | `/observed/0/name` | str |  |
| `results/java/b1.input.json` | `/observed/0/payload` | str |  |
| `results/java_summary.json` | `/` | object | 7 |
| `results/java_summary.json` | `/scope` | str |  |
| `results/java_summary.json` | `/cases` | array | 2 |
| `results/java_summary.json` | `/cases/0` | object | 8 |
| `results/java_summary.json` | `/cases/0/case` | str |  |
| `results/java_summary.json` | `/cases/0/assembly_order` | array | 2 |
| `results/java_summary.json` | `/cases/0/assembly_order/0` | int |  |
| `results/java_summary.json` | `/cases/0/runtime_probe_value` | int |  |
| `results/java_summary.json` | `/cases/0/marker_byte_candidates` | int |  |
| `results/java_summary.json` | `/cases/0/marker_owners` | array | 1 |
| `results/java_summary.json` | `/cases/0/marker_owners/0` | str |  |
| `results/java_summary.json` | `/cases/0/status` | str |  |
| `results/java_summary.json` | `/cases/0/input_bytes` | int |  |
| `results/java_summary.json` | `/cases/0/certificate_bytes` | int |  |
| `results/java_summary.json` | `/cpu_seconds` | float |  |
| `results/java_summary.json` | `/wall_seconds` | float |  |
| `results/java_summary.json` | `/parent_peak_rss_kib` | int |  |
| `results/java_summary.json` | `/child_peak_rss_kib` | int |  |
| `results/java_summary.json` | `/byte_reproduction` | str |  |
| `results/oracle_details.csv` | `providers` | CSV column | 69 |
| `results/oracle_details.csv` | `precedence_mask` | CSV column | 69 |
| `results/oracle_details.csv` | `structures` | CSV column | 69 |
| `results/oracle_details.csv` | `labelled_cases` | CSV column | 69 |
| `results/oracle_details.csv` | `feasible_labelled_cases` | CSV column | 69 |
| `results/oracle_summary.json` | `/` | object | 11 |
| `results/oracle_summary.json` | `/structural_cases` | int |  |
| `results/oracle_summary.json` | `/labelled_cases` | int |  |
| `results/oracle_summary.json` | `/feasible_labelled_cases` | int |  |
| `results/oracle_summary.json` | `/region_classifications_checked` | int |  |
| `results/oracle_summary.json` | `/mismatches` | int |  |
| `results/oracle_summary.json` | `/provider_counts` | array | 3 |
| `results/oracle_summary.json` | `/provider_counts/0` | int |  |
| `results/oracle_summary.json` | `/region_counts` | array | 3 |
| `results/oracle_summary.json` | `/region_counts/0` | int |  |
| `results/oracle_summary.json` | `/owner_schemes` | array | 2 |
| `results/oracle_summary.json` | `/owner_schemes/0` | str |  |
| `results/oracle_summary.json` | `/cpu_seconds` | float |  |
| `results/oracle_summary.json` | `/wall_seconds` | float |  |
| `results/oracle_summary.json` | `/peak_rss_kib` | int |  |
| `results/public/cases.csv` | `build_id` | CSV column | 80 |
| `results/public/cases.csv` | `pair_id` | CSV column | 80 |
| `results/public/cases.csv` | `pair_kind` | CSV column | 80 |
| `results/public/cases.csv` | `first_archive` | CSV column | 80 |
| `results/public/cases.csv` | `second_archive` | CSV column | 80 |
| `results/public/cases.csv` | `entry_regions` | CSV column | 80 |
| `results/public/cases.csv` | `collision_regions` | CSV column | 80 |
| `results/public/cases.csv` | `admissible_actual_orders` | CSV column | 80 |
| `results/public/cases.csv` | `ant_matches_first_winner` | CSV column | 80 |
| `results/public/cases.csv` | `archive_adapters_equal` | CSV column | 80 |
| `results/public/cases.csv` | `oracle_mismatches` | CSV column | 80 |
| `results/public/cases.csv` | `local_ambiguous_regions` | CSV column | 80 |
| `results/public/cases.csv` | `certified_ambiguous_regions` | CSV column | 80 |
| `results/public/cases.csv` | `global_narrowings` | CSV column | 80 |
| `results/public/cases.csv` | `equal_regions_resolved_by_coupling` | CSV column | 80 |
| `results/public/cases.csv` | `witness_orders` | CSV column | 80 |
| `results/public/cases.csv` | `obstructions` | CSV column | 80 |
| `results/public/cases.csv` | `certificate_bytes` | CSV column | 80 |
| `results/public/cases.csv` | `output_bytes` | CSV column | 80 |
| `results/public/cases.csv` | `output_sha256` | CSV column | 80 |
| `results/public/cases.csv` | `catalogue_tiebreak_oracle_exact` | CSV column | 80 |
| `results/public/cases.csv` | `inventory_size_proxy_oracle_exact` | CSV column | 80 |
| `results/public/cases.csv` | `dependency_oracle_exact` | CSV column | 80 |
| `results/public/cases.csv` | `local_bytes_oracle_exact` | CSV column | 80 |
| `results/public/cases.csv` | `certified_oracle_exact` | CSV column | 80 |
| `results/public/cases.csv` | `trusted_trace_hidden_winner_covered` | CSV column | 80 |
| `results/public/cases.csv` | `lowering_seconds` | CSV column | 80 |
| `results/public/cases.csv` | `inference_seconds` | CSV column | 80 |
| `results/public/cases.csv` | `checking_seconds` | CSV column | 80 |
| `results/public/retained/p001-ab.answer.json` | `/` | object | 2 |
| `results/public/retained/p001-ab.answer.json` | `/status` | str |  |
| `results/public/retained/p001-ab.answer.json` | `/regions` | array | 2837 |
| `results/public/retained/p001-ab.answer.json` | `/regions/0` | object | 3 |
| `results/public/retained/p001-ab.answer.json` | `/regions/0/key` | str |  |
| `results/public/retained/p001-ab.answer.json` | `/regions/0/owners` | array | 2 |
| `results/public/retained/p001-ab.answer.json` | `/regions/0/owners/0` | str |  |
| `results/public/retained/p001-ab.answer.json` | `/regions/0/class` | str |  |
| `results/public/retained/p001-ab.certificate.json` | `/` | object | 4 |
| `results/public/retained/p001-ab.certificate.json` | `/status` | str |  |
| `results/public/retained/p001-ab.certificate.json` | `/orders` | array | 2 |
| `results/public/retained/p001-ab.certificate.json` | `/orders/0` | array | 2 |
| `results/public/retained/p001-ab.certificate.json` | `/orders/0/0` | int |  |
| `results/public/retained/p001-ab.certificate.json` | `/obstructions` | array | 0 |
| `results/public/retained/p001-ab.certificate.json` | `/regions` | array | 2837 |
| `results/public/retained/p001-ab.certificate.json` | `/regions/0` | object | 4 |
| `results/public/retained/p001-ab.certificate.json` | `/regions/0/owners` | array | 2 |
| `results/public/retained/p001-ab.certificate.json` | `/regions/0/owners/0` | str |  |
| `results/public/retained/p001-ab.certificate.json` | `/regions/0/class` | str |  |
| `results/public/retained/p001-ab.certificate.json` | `/regions/0/support` | array | 2 |
| `results/public/retained/p001-ab.certificate.json` | `/regions/0/support/0` | array | 2 |
| `results/public/retained/p001-ab.certificate.json` | `/regions/0/support/0/0` | str |  |
| `results/public/retained/p001-ab.certificate.json` | `/regions/0/excluded` | array | 0 |
| `results/public/retained/p001-ab.graph.json` | `/` | object | 4 |
| `results/public/retained/p001-ab.graph.json` | `/kind` | str |  |
| `results/public/retained/p001-ab.graph.json` | `/owners` | array | 2 |
| `results/public/retained/p001-ab.graph.json` | `/owners/0` | str |  |
| `results/public/retained/p001-ab.graph.json` | `/before` | array | 0 |
| `results/public/retained/p001-ab.graph.json` | `/rows` | array | 2837 |
| `results/public/retained/p001-ab.graph.json` | `/rows/0` | object | 3 |
| `results/public/retained/p001-ab.graph.json` | `/rows/0/key` | str |  |
| `results/public/retained/p001-ab.graph.json` | `/rows/0/present` | array | 2 |
| `results/public/retained/p001-ab.graph.json` | `/rows/0/present/0` | int |  |
| `results/public/retained/p001-ab.graph.json` | `/rows/0/good` | array | 2 |
| `results/public/retained/p001-ab.graph.json` | `/rows/0/good/0` | int |  |
| `results/public/retained/p021-ab.answer.json` | `/` | object | 2 |
| `results/public/retained/p021-ab.answer.json` | `/status` | str |  |
| `results/public/retained/p021-ab.answer.json` | `/regions` | array | 2837 |
| `results/public/retained/p021-ab.answer.json` | `/regions/0` | object | 3 |
| `results/public/retained/p021-ab.answer.json` | `/regions/0/key` | str |  |
| `results/public/retained/p021-ab.answer.json` | `/regions/0/owners` | array | 1 |
| `results/public/retained/p021-ab.answer.json` | `/regions/0/owners/0` | str |  |
| `results/public/retained/p021-ab.answer.json` | `/regions/0/class` | str |  |
| `results/public/retained/p021-ab.certificate.json` | `/` | object | 4 |
| `results/public/retained/p021-ab.certificate.json` | `/status` | str |  |
| `results/public/retained/p021-ab.certificate.json` | `/orders` | array | 1 |
| `results/public/retained/p021-ab.certificate.json` | `/orders/0` | array | 2 |
| `results/public/retained/p021-ab.certificate.json` | `/orders/0/0` | int |  |
| `results/public/retained/p021-ab.certificate.json` | `/obstructions` | array | 1 |
| `results/public/retained/p021-ab.certificate.json` | `/obstructions/0` | object | 3 |
| `results/public/retained/p021-ab.certificate.json` | `/obstructions/0/kind` | str |  |
| `results/public/retained/p021-ab.certificate.json` | `/obstructions/0/nodes` | array | 2 |
| `results/public/retained/p021-ab.certificate.json` | `/obstructions/0/nodes/0` | int |  |
| `results/public/retained/p021-ab.certificate.json` | `/obstructions/0/reasons` | array | 2 |
| `results/public/retained/p021-ab.certificate.json` | `/obstructions/0/reasons/0` | object | 3 |
| `results/public/retained/p021-ab.certificate.json` | `/obstructions/0/reasons/0/node` | int |  |
| `results/public/retained/p021-ab.certificate.json` | `/obstructions/0/reasons/0/kind` | str |  |
| `results/public/retained/p021-ab.certificate.json` | `/obstructions/0/reasons/0/pred` | int |  |
| `results/public/retained/p021-ab.certificate.json` | `/regions` | array | 2837 |
| `results/public/retained/p021-ab.certificate.json` | `/regions/0` | object | 4 |
| `results/public/retained/p021-ab.certificate.json` | `/regions/0/owners` | array | 1 |
| `results/public/retained/p021-ab.certificate.json` | `/regions/0/owners/0` | str |  |
| `results/public/retained/p021-ab.certificate.json` | `/regions/0/class` | str |  |
| `results/public/retained/p021-ab.certificate.json` | `/regions/0/support` | array | 1 |
| `results/public/retained/p021-ab.certificate.json` | `/regions/0/support/0` | array | 2 |
| `results/public/retained/p021-ab.certificate.json` | `/regions/0/support/0/0` | str |  |
| `results/public/retained/p021-ab.certificate.json` | `/regions/0/excluded` | array | 1 |
| `results/public/retained/p021-ab.certificate.json` | `/regions/0/excluded/0` | object | 2 |
| `results/public/retained/p021-ab.certificate.json` | `/regions/0/excluded/0/provider` | int |  |
| `results/public/retained/p021-ab.certificate.json` | `/regions/0/excluded/0/obstruction` | int |  |
| `results/public/retained/p021-ab.graph.json` | `/` | object | 4 |
| `results/public/retained/p021-ab.graph.json` | `/kind` | str |  |
| `results/public/retained/p021-ab.graph.json` | `/owners` | array | 2 |
| `results/public/retained/p021-ab.graph.json` | `/owners/0` | str |  |
| `results/public/retained/p021-ab.graph.json` | `/before` | array | 0 |
| `results/public/retained/p021-ab.graph.json` | `/rows` | array | 2837 |
| `results/public/retained/p021-ab.graph.json` | `/rows/0` | object | 3 |
| `results/public/retained/p021-ab.graph.json` | `/rows/0/key` | str |  |
| `results/public/retained/p021-ab.graph.json` | `/rows/0/present` | array | 2 |
| `results/public/retained/p021-ab.graph.json` | `/rows/0/present/0` | int |  |
| `results/public/retained/p021-ab.graph.json` | `/rows/0/good` | array | 2 |
| `results/public/retained/p021-ab.graph.json` | `/rows/0/good/0` | int |  |
| `results/public/retained/p039-ab.answer.json` | `/` | object | 2 |
| `results/public/retained/p039-ab.answer.json` | `/status` | str |  |
| `results/public/retained/p039-ab.answer.json` | `/regions` | array | 543 |
| `results/public/retained/p039-ab.answer.json` | `/regions/0` | object | 3 |
| `results/public/retained/p039-ab.answer.json` | `/regions/0/key` | str |  |
| `results/public/retained/p039-ab.answer.json` | `/regions/0/owners` | array | 1 |
| `results/public/retained/p039-ab.answer.json` | `/regions/0/owners/0` | str |  |
| `results/public/retained/p039-ab.answer.json` | `/regions/0/class` | str |  |
| `results/public/retained/p039-ab.certificate.json` | `/` | object | 4 |
| `results/public/retained/p039-ab.certificate.json` | `/status` | str |  |
| `results/public/retained/p039-ab.certificate.json` | `/orders` | array | 1 |
| `results/public/retained/p039-ab.certificate.json` | `/orders/0` | array | 2 |
| `results/public/retained/p039-ab.certificate.json` | `/orders/0/0` | int |  |
| `results/public/retained/p039-ab.certificate.json` | `/obstructions` | array | 0 |
| `results/public/retained/p039-ab.certificate.json` | `/regions` | array | 543 |
| `results/public/retained/p039-ab.certificate.json` | `/regions/0` | object | 4 |
| `results/public/retained/p039-ab.certificate.json` | `/regions/0/owners` | array | 1 |
| `results/public/retained/p039-ab.certificate.json` | `/regions/0/owners/0` | str |  |
| `results/public/retained/p039-ab.certificate.json` | `/regions/0/class` | str |  |
| `results/public/retained/p039-ab.certificate.json` | `/regions/0/support` | array | 1 |
| `results/public/retained/p039-ab.certificate.json` | `/regions/0/support/0` | array | 2 |
| `results/public/retained/p039-ab.certificate.json` | `/regions/0/support/0/0` | str |  |
| `results/public/retained/p039-ab.certificate.json` | `/regions/0/excluded` | array | 0 |
| `results/public/retained/p039-ab.graph.json` | `/` | object | 4 |
| `results/public/retained/p039-ab.graph.json` | `/kind` | str |  |
| `results/public/retained/p039-ab.graph.json` | `/owners` | array | 2 |
| `results/public/retained/p039-ab.graph.json` | `/owners/0` | str |  |
| `results/public/retained/p039-ab.graph.json` | `/before` | array | 0 |
| `results/public/retained/p039-ab.graph.json` | `/rows` | array | 543 |
| `results/public/retained/p039-ab.graph.json` | `/rows/0` | object | 3 |
| `results/public/retained/p039-ab.graph.json` | `/rows/0/key` | str |  |
| `results/public/retained/p039-ab.graph.json` | `/rows/0/present` | array | 2 |
| `results/public/retained/p039-ab.graph.json` | `/rows/0/present/0` | int |  |
| `results/public/retained/p039-ab.graph.json` | `/rows/0/good` | array | 1 |
| `results/public/retained/p039-ab.graph.json` | `/rows/0/good/0` | int |  |
| `results/public/summary.json` | `/` | object | 28 |
| `results/public/summary.json` | `/public_provider_archives` | int |  |
| `results/public/summary.json` | `/collision_pairs` | int |  |
| `results/public/summary.json` | `/actual_ant_builds` | int |  |
| `results/public/summary.json` | `/pair_categories` | object | 3 |
| `results/public/summary.json` | `/pair_categories/different-only` | int |  |
| `results/public/summary.json` | `/pair_categories/equal-only` | int |  |
| `results/public/summary.json` | `/pair_categories/mixed` | int |  |
| `results/public/summary.json` | `/reversed_pairs_with_identical_output_maps` | int |  |
| `results/public/summary.json` | `/indistinguishable_shared_regions_with_owner_flip` | int |  |
| `results/public/summary.json` | `/region_observations` | int |  |
| `results/public/summary.json` | `/collision_region_observations` | int |  |
| `results/public/summary.json` | `/local_byte_ambiguous_regions` | int |  |
| `results/public/summary.json` | `/certified_ambiguous_regions` | int |  |
| `results/public/summary.json` | `/global_narrowings_over_local_bytes` | int |  |
| `results/public/summary.json` | `/equal_byte_regions_resolved_by_global_coupling` | int |  |
| `results/public/summary.json` | `/ant_first_winner_mismatches` | int |  |
| `results/public/summary.json` | `/independent_archive_adapter_mismatches` | int |  |
| `results/public/summary.json` | `/certificate_vs_actual_two_order_oracle_mismatches` | int |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions` | object | 6 |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/catalogue_tiebreak` | object | 6 |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/catalogue_tiebreak/observations` | int |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/catalogue_tiebreak/oracle_exact_count` | int |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/catalogue_tiebreak/oracle_exact_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/catalogue_tiebreak/oracle_conservative_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/catalogue_tiebreak/hidden_winner_coverage_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/catalogue_tiebreak/mean_owner_set_size` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/inventory_size_proxy` | object | 6 |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/inventory_size_proxy/observations` | int |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/inventory_size_proxy/oracle_exact_count` | int |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/inventory_size_proxy/oracle_exact_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/inventory_size_proxy/oracle_conservative_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/inventory_size_proxy/hidden_winner_coverage_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/inventory_size_proxy/mean_owner_set_size` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/dependency` | object | 6 |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/dependency/observations` | int |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/dependency/oracle_exact_count` | int |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/dependency/oracle_exact_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/dependency/oracle_conservative_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/dependency/hidden_winner_coverage_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/dependency/mean_owner_set_size` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/local_bytes` | object | 6 |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/local_bytes/observations` | int |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/local_bytes/oracle_exact_count` | int |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/local_bytes/oracle_exact_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/local_bytes/oracle_conservative_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/local_bytes/hidden_winner_coverage_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/local_bytes/mean_owner_set_size` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/certified` | object | 6 |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/certified/observations` | int |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/certified/oracle_exact_count` | int |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/certified/oracle_exact_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/certified/oracle_conservative_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/certified/hidden_winner_coverage_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/certified/mean_owner_set_size` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/trusted_trace` | object | 6 |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/trusted_trace/observations` | int |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/trusted_trace/oracle_exact_count` | int |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/trusted_trace/oracle_exact_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/trusted_trace/oracle_conservative_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/trusted_trace/hidden_winner_coverage_rate` | float |  |
| `results/public/summary.json` | `/baseline_comparison_on_collision_regions/trusted_trace/mean_owner_set_size` | float |  |
| `results/public/summary.json` | `/certificate_bytes_min` | int |  |
| `results/public/summary.json` | `/certificate_bytes_median` | int |  |
| `results/public/summary.json` | `/certificate_bytes_max` | int |  |
| `results/public/summary.json` | `/elapsed_seconds` | float |  |
| `results/public/summary.json` | `/process_cpu_seconds` | float |  |
| `results/public/summary.json` | `/child_user_cpu_seconds` | float |  |
| `results/public/summary.json` | `/child_system_cpu_seconds` | float |  |
| `results/public/summary.json` | `/child_peak_rss_kib` | int |  |
| `results/public/summary.json` | `/workers` | int |  |
| `results/public/summary.json` | `/builder` | str |  |
| `results/public/summary.json` | `/manifest_handling` | str |  |
| `results/public/summary.json` | `/oracle_scope` | str |  |
| `results/reproduction_summary.json` | `/` | object | 9 |
| `results/reproduction_summary.json` | `/commands` | array | 8 |
| `results/reproduction_summary.json` | `/commands/0` | object | 4 |
| `results/reproduction_summary.json` | `/commands/0/command` | str |  |
| `results/reproduction_summary.json` | `/commands/0/exit_code` | int |  |
| `results/reproduction_summary.json` | `/commands/0/wall_seconds` | float |  |
| `results/reproduction_summary.json` | `/commands/0/timeout_seconds` | int |  |
| `results/reproduction_summary.json` | `/logical_reproduction` | str |  |
| `results/reproduction_summary.json` | `/cpu_seconds_children` | float |  |
| `results/reproduction_summary.json` | `/wall_seconds` | float |  |
| `results/reproduction_summary.json` | `/child_peak_rss_kib` | int |  |
| `results/reproduction_summary.json` | `/maximum_workers` | int |  |
| `results/reproduction_summary.json` | `/java_requested` | bool |  |
| `results/reproduction_summary.json` | `/public_requested` | bool |  |
| `results/reproduction_summary.json` | `/scope` | str |  |
| `results/resource_accounting.json` | `/` | object | 14 |
| `results/resource_accounting.json` | `/accounting_scope` | str |  |
| `results/resource_accounting.json` | `/final_clean_child_cpu_seconds` | float |  |
| `results/resource_accounting.json` | `/final_clean_wall_seconds` | float |  |
| `results/resource_accounting.json` | `/final_clean_child_peak_rss_kib` | int |  |
| `results/resource_accounting.json` | `/maximum_workers` | int |  |
| `results/resource_accounting.json` | `/final_clean_stages` | array | 8 |
| `results/resource_accounting.json` | `/final_clean_stages/0` | str |  |
| `results/resource_accounting.json` | `/public_input_archives` | int |  |
| `results/resource_accounting.json` | `/public_input_archive_bytes` | int |  |
| `results/resource_accounting.json` | `/public_license_records` | int |  |
| `results/resource_accounting.json` | `/public_license_record_bytes` | int |  |
| `results/resource_accounting.json` | `/artifact_bytes_at_accounting` | int |  |
| `results/resource_accounting.json` | `/downloads_during_final_clean_reproduction` | int |  |
| `results/resource_accounting.json` | `/external_compute_or_gpu_used` | bool |  |
| `results/resource_accounting.json` | `/resource_interpretation` | str |  |
| `results/scale_summary.json` | `/` | array | 3 |
| `results/scale_summary.json` | `/0` | object | 11 |
| `results/scale_summary.json` | `/0/case` | str |  |
| `results/scale_summary.json` | `/0/providers` | int |  |
| `results/scale_summary.json` | `/0/regions` | int |  |
| `results/scale_summary.json` | `/0/incidences` | int |  |
| `results/scale_summary.json` | `/0/orders` | int |  |
| `results/scale_summary.json` | `/0/certificate_bytes` | int |  |
| `results/scale_summary.json` | `/0/obstructions` | int |  |
| `results/scale_summary.json` | `/0/producer_cpu_seconds` | float |  |
| `results/scale_summary.json` | `/0/checker_cpu_seconds` | float |  |
| `results/scale_summary.json` | `/0/wall_seconds` | float |  |
| `results/scale_summary.json` | `/0/peak_rss_kib` | int |  |
