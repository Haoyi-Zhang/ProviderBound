# Implementation-Independence Audit

The literal-permutation information baseline, Info-ZIP validation, and archive-safety audit must not import the certificate producer, checker, or another project-local implementation. This check establishes implementation separation, not formal verification of Python itself.

- `scripts.analyze_information_baselines`: local imports = `none`
- `scripts.validate_infozip_merger`: local imports = `none`
- `scripts.audit_archive_safety`: local imports = `none`

Release-blocking violations: **0**.

The report also records name-based producer/checker/oracle candidates for human review; those labels are not treated as proof of independence.
