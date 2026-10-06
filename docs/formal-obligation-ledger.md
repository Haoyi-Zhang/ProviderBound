# Formal obligation ledger

The ledger states what each proof obligation establishes, the assumptions it consumes, and the executable check that can falsify an implementation. It deliberately distinguishes a mathematical argument from finite testing.

| Obligation | Mathematical statement | Required assumptions | Executable falsifier |
|---|---|---|---|
| Normalization determinism | Every accepted raw entry name maps to exactly one canonical name. | Accepted path grammar; unsupported encodings and traversal rejected. | Two accepted spellings map inconsistently, or a rejected spelling enters a provider map. |
| Provider-map well-formedness | A provider has at most one byte string for a canonical entry. | Duplicate normalized entries fail closed. | A JAR with duplicate/colliding normalized names is silently accepted. |
| Order feasibility | A provider order is feasible exactly when it is a linear extension of the supplied precedence relation and reproduces every observed output byte under first-winner merging. | Finite provider list; complete candidate bytes; one global order. | Literal permutation and the graph/reference semantics disagree on a finite instance. |
| Inconsistency separation | No feasible order means inconsistent evidence, not an empty or ambiguous owner result. | Feasibility definition above. | The generator emits an owner classification when the literal feasible-order set is empty. |
| Inclusion soundness | Every label returned as possible has a replayable feasible-order witness whose winning provider carries that label. | Correct label map and normalized inputs. | Checker accepts a witness that violates precedence, output bytes, or label identity. |
| Inclusion completeness | For every feasible winning label there exists a witness accepted by the checker. | Finite orders and exact first-winner semantics. | Literal permutation finds a label omitted by the generated certificate. |
| Exclusion soundness | A counterfactual exclusion certificate demonstrates that forcing a candidate label leaves no feasible order. | Checker reconstructs, rather than trusts, all forced edges and residual obligations. | Checker accepts a mutated exclusion certificate while a literal feasible counterexample exists. |
| Exact projected label set | Accepted inclusion and exclusion evidence yields exactly the image of feasible winning providers under the caller-supplied label function. | Inclusion/exclusion obligations; total label map over providers. | Generator/checker differs from the exhaustive labeled oracle. |
| Label coarsening | Replacing labels by a coarser surjective map can only merge distinctions; the coarse answer is the image of the fine answer. | Same provider/order semantics; only label map changes. | A coarse label appears without a fine preimage or a fine possible label disappears outside its mapped class. |
| Complete-order collapse | If a trusted total provider order is supplied and the evidence is feasible, each entry has at most one winning provider and one projected label. | Total order trusted and all candidates known. | Two different first providers occur under the same total order. |
| Hidden-equal-provider impossibility | Output bytes plus a claimed-complete provider list cannot identify which equal-byte provider historically won when two feasible orders produce the same complete output. | No trace of the historical order beyond the modeled evidence. | An estimator distinguishes the two worlds without consuming additional evidence. |
| Missing-provider impossibility | The output and supplied list cannot prove that an omitted equal-byte provider does not exist. | Open external world; omitted provider observationally duplicates an included provider. | A purported proof excludes the indistinguishable extended world without an external completeness attestation. |

## Evidence hierarchy

1. Mathematical proofs cover all inputs in the formal language if their premises hold.
2. The independently written checker validates one finite certificate without trusting producer classifications.
3. Literal permutation is an exact executable oracle only at manageable provider counts.
4. Exhaustive finite-model enumeration detects implementation/specification disagreement in its bounded domain.
5. Public Ant builds test whether a concrete archive tool conforms on retained cases.
6. Scale probes test resource behavior, not semantic generality.

Passing a lower item never substitutes for a missing higher-level premise.

## Equality relation

Every semantic comparison is over a canonical map from accepted entry paths to uncompressed entry bytes. Raw ZIP/JAR container bytes are intentionally not the equality object: timestamps, compression levels, extra fields, member order, and central-directory layout may differ while the modeled build result is identical. The manifest is excluded by the current Ant configuration. Other retained
metadata entries follow the same first-winner rule; category-specific metadata
transformers are outside the implemented build language.
