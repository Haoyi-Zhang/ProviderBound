# Security and Tamper-Test Evidence

The artifact contains **40** statically discoverable test functions. Clean reproduction executes the project test stage; this file indexes tests relevant to the untrusted-input and untrusted-certificate boundary.

## Schema Malleability

Matched tests: **5**

- `tests/test_boundary.py:59` — `test_shared_obligation_round_trip`
- `tests/test_boundary.py:73` — `test_duplicate_region_omission`
- `tests/test_boundary.py:120` — `test_every_stored_input`
- `tests/test_boundary.py:140` — `test_json_duplicates_and_file_bounds`
- `tests/test_boundary.py:188` — `test_seeded_larger_models_against_literal_orders`

## Path Canonicalization

Matched tests: **4**

- `tests/test_boundary.py:120` — `test_every_stored_input`
- `tests/test_boundary.py:140` — `test_json_duplicates_and_file_bounds`
- `tests/test_boundary.py:160` — `test_concrete_archive_adapters_and_safety`
- `tests/test_boundary.py:245` — `test_concrete_archive_output_union_rejected`

## Order And Inconsistency

Matched tests: **12**

- `tests/test_boundary.py:24` — `test_ambiguity_not_inconsistency`
- `tests/test_boundary.py:28` — `test_all_equal_payload_orders_are_valid`
- `tests/test_boundary.py:63` — `test_wrong_order`
- `tests/test_boundary.py:65` — `test_repeated_provider_order`
- `tests/test_boundary.py:67` — `test_bool_is_not_index`
- `tests/test_boundary.py:79` — `test_empty_witness_bank`
- `tests/test_boundary.py:81` — `test_cannot_certify_all_orders_from_one_witness`
- `tests/test_boundary.py:84` — `test_false_inconsistency`
- `tests/test_boundary.py:86` — `test_missing_candidate_is_inconsistent`
- `tests/test_boundary.py:89` — `test_self_cycle`
- `tests/test_boundary.py:112` — `test_total_order_collapses_or_rejects`
- `tests/test_boundary.py:188` — `test_seeded_larger_models_against_literal_orders`

## Certificate Mutation

Matched tests: **4**

- `tests/test_boundary.py:75` — `test_witness_for_wrong_owner`
- `tests/test_boundary.py:79` — `test_empty_witness_bank`
- `tests/test_boundary.py:81` — `test_cannot_certify_all_orders_from_one_witness`
- `tests/test_boundary.py:188` — `test_seeded_larger_models_against_literal_orders`

## Unsupported Semantics

Matched tests: **6**

- `tests/test_boundary.py:51` — `test_obstruction_index_out_of_range`
- `tests/test_boundary.py:53` — `test_obstruction_index_boolean`
- `tests/test_boundary.py:67` — `test_bool_is_not_index`
- `tests/test_boundary.py:120` — `test_every_stored_input`
- `tests/test_boundary.py:136` — `test_unsupported_input_is_not_ambiguous`
- `tests/test_boundary.py:160` — `test_concrete_archive_adapters_and_safety`

## Implementation Separation

Matched tests: **6**

- `tests/test_boundary.py:102` — `test_missing_inventory_is_not_detectable_in_general`
- `tests/test_boundary.py:129` — `test_no_checker_inference_import`
- `tests/test_boundary.py:140` — `test_json_duplicates_and_file_bounds`
- `tests/test_boundary.py:160` — `test_concrete_archive_adapters_and_safety`
- `tests/test_boundary.py:188` — `test_seeded_larger_models_against_literal_orders`
- `tests/test_boundary.py:245` — `test_concrete_archive_output_union_rejected`

## Interpretation

- This is a static evidence index; passing behavior is established by the clean release reproduction.
- Token-based categorization is conservative and is not itself a proof of test adequacy.
- The archive-safety audit separately checks duplicate names, path aliases, encryption, and symbolic links in the retained frame.
