# Source relation, closest-work delta, and attribution

This document records the substantive lineage of the research question.  It is
not a claim that prior Android library identification, certificate checking, or
Horn-rule feasibility is new.  The 22-paper narrative calibration is recorded
separately in `literature-calibration.csv` and `literature-calibration.md`; the
full bibliography used by the manuscript is in `paper/references.bib` in the
complete project package.

## Historical Android-library source

AndroLibZoo constructs a large dependency-derived catalogue intended to support
Android static analysis.  Its reported unit is a refined set of library/package
identifiers extracted from public dependency evidence, not a proof object for a
particular output region.  This project changes the trust boundary: it assumes a
finite per-build inventory and asks what exact owner conclusion follows for each
output path, including when the evidence permits several owners or no feasible
build world.

The project does not use AndroLibZoo as ground truth, does not claim that package
catalogues are useless, and does not present a direct recent-work extension on
behalf of any prior author.  A catalogue can be an upstream source of candidate
provider labels; the certificate answers a different, build-specific question.

## Established algorithmic foundation

The feasibility construction specializes known Horn-rule/antimatroid accessible-
set membership.  A provider may be selected only when every active row containing
it has another remaining admissible candidate.  Greedily removing eligible
providers either constructs an order or leaves a closed residual trap.  The
project proves the specialization and certificate obligations in its notation,
but does not claim invention of the general queue algorithm or antimatroid
representation.

## Prior proof and checking traditions

Proof-carrying code, program checking, translation validation, verified
compilation, and certificate-enhanced Android data-flow analysis establish the
broader producer/checker pattern.  The delta here is property-specific: the
certificate proves an exact set-valued projection over all first-winner provider
orders admitted by a frozen inventory and observed bytes.  It is not a new
origin story for proof-carrying systems, nor a mechanized proof of the Python
implementation.

## Stronger practical library-identification systems

LibRadar, LibScout, LibD, LibID, ATVHunter, LibHunter, LibDB, OSSPolice, CENTRIS,
LibAM, and related systems address candidate discovery, version identification,
obfuscation resilience, component or area matching, and vulnerable-library
analysis.  Many tolerate transformations that the current exact-byte model
rejects.  The current experiment therefore does not claim higher detection
accuracy or broader applicability.

The complementary value is an auditable boundary after candidate extraction:
when exact consumed archives and a supported build composition are available,
the checker states which ownership conclusions are forced, which remain
ambiguous, and which input/output combinations are inconsistent.  A practical
pipeline may use a mature detector upstream, but its matching assumptions must
be translated into a separately justified observation relation before the
certificate can rely on them.

## Build and supply-chain systems

Build Systems à la Carte clarifies that build semantics should be explicit rather
than inferred from tool names.  in-toto and The Update Framework show how signed
supply-chain metadata can strengthen provenance claims.  Maven ecosystem studies
show that dependency declarations, repository structure, bloat, versioning, and
runtime semantic conflicts are distinct concerns.  The present model isolates a
small duplicate-path fragment so that all possible orders can be characterized
exactly; it does not replace general build provenance or dependency resolution.

## Why real Ant builds matter

The first-winner rule could otherwise be dismissed as a purely synthetic toy.
The public study executes Apache Ant's Zip task on 40 collision-bearing pairs in
both orders.  Ant output, direct archive reading, the independent adapters, and
the certificate oracle agree on every observation.  Thirty reversed pairs have
identical output byte maps while 3,471 shared paths change hidden winner, showing
that output bytes alone may not identify provenance.  The single mixed pair
shows the converse: one differing shared path constrains the global order and
resolves 100 equal-byte observations that are locally ambiguous.

These are real archive-composition facts for the frozen corpus.  They do not
establish the prevalence of first-winner ambiguity in Android apps, nor do they
cover class rewriting performed by Maven Shade, D8/R8, or other build plugins.

## Defensible contribution boundary

The manuscript's defensible claims are:

1. an explicit closed-world first-winner ownership semantics with inconsistency
   and set-valued ambiguity separated;
2. replayable positive orders and counterfactual obstructions for exact owner
   projection;
3. a separate checker whose obligations do not require rerunning producer
   search;
4. complete ordinary proofs for the frozen semantics plus exhaustive tiny-model
   checking; and
5. exact external validation on both orders of 40 public collision pairs.

It does not claim an end-to-end Android build model, discovery of all libraries,
legal authorship attribution, a new general Horn algorithm, a subset-minimal
ambiguity core, a mechanized implementation proof, or empirical superiority to
published detectors.
