# Execution environments and evidence scope

The separate retained Windows finite campaign uses CPython 3.12.14, MSC v.1944 64-bit AMD64, on
Windows 11 build 28000. The OS reports 20 logical processors. The runner uses
one scientific process at a time, no third-party Python packages, no network,
and no JVM or Ant execution. Python assertions are enabled; every child uses
`-B`, `PYTHONUTF8=1`, `PYTHONDONTWRITEBYTECODE=1`, and `PYTHONHASHSEED=0`.

`results/local/environment.json` records the actual executable, OS, start time,
and flags. `results/local/reproduction_summary.json` records every command,
duration, exit status, the actual test count, and the complete/failed status.
The six stages are regeneration, passive bundled-input verification, unit tests,
finite oracle, generated/boundary campaign, and scale disk replay. Peak RSS and
child CPU are null because Windows lacks `resource.getrusage`; process CPU and
wall times are measured directly. No resource value is copied from Linux.

The historical Linux capture remains in `docs/environment-capture.json`: Python
3.13.5, x86-64 Linux/glibc 2.41, and OpenJDK 21.0.11. `results/public/summary.json`
records the earlier 80 actual Ant builds (27.954036 s), while the historical
`results/reproduction_summary.json` records a separate full run (68.847405 s,
including a 50.026345 s public stage). `results/java_summary.json` retains two
owned JVM results. These are not new Windows or revised-runner outcomes.

The distributed probe uses 301 orders and 447,688 certificate bytes.
The preserved earlier scale summary used 599 orders and 773,434 bytes. This is
a representation comparison, not a timing speedup claim across machines.
For the historical public case CSV, the conventional even-sample median is
292,845 bytes, averaging 292,719 and 292,971; the prior summary stored the upper
middle value. The table generator recomputes that statistic from raw rows.

The manuscript's complete Linux 6.17 / CPython 3.12.14 / Temurin 21.0.12.1
campaign is in `results/current/`: eight stages, including 80 public Ant builds
and two owned Java builds, completed in 72.17 wall seconds. The table generator
uses these measurements, not `results/local/`.

The retained 74-test suite passes in the separate Windows/Python 3.12.14
execution recorded in `results/unit-tests.json` and `results/unit-tests.txt`.
The retained Linux campaign ran 47 tests; this separate unit execution does
not repeat its external-builder experiment or replace its timing measurements.

`results/owner-granularity.json` is a separate Windows model replay using
retained provider bytes and recorded Debian binary-package labels. It does not
execute Ant or any provider class. Its archive-label counts match all 80 retained
case records; package-labelled local and certified sets are compared under the
same input information. No new timing comparison or downstream analyzer
measurement is attached to this replay.

The complete Ubuntu/Python 3.12 workflow requires the runner's existing JDK;
no dependency installation or toolchain download is performed by the scientific
commands themselves.

The `results/diagnostics/receipt.json` records
Windows-11-10.0.28000-SP0, CPython 3.12.14 MSC v.1944 AMD64, disabled bytecode
writes (`-B`) and hash seed 0. Its UTC times correspond to 2026-10-14 in
Asia/Shanghai. It runs 84 of 85 discovered tests; one retained test that writes
a traversal-name ZIP is explicitly not executed. Temporary owned fixtures stay
inside the selected output and are removed after the run. The full test IDs,
raw log, source/input bindings and provider-byte replay are
retained there. The measured single-run wall time describes this diagnostic
only; no CPU/RSS or comparative speed result is inferred from it.

That execution performs no Ant/JVM build, provider-class execution,
archive extraction, network acquisition or public-output ZIP replay. The same
80 modeled content maps are each evaluated under two label schemes; those 160
count records are neither 160 builds nor additional independent public cases.
Actual ownership labels and downstream analyzer findings remain unmeasured.

The current `results/diagnostics/current/receipt.json` records the fresh
Windows/CPython 3.12.14 execution of 110 selected methods from 111 discovered
methods. The same one retained traversal-ZIP fixture is explicitly excluded.
Its raw log, all 165 input/source bindings and 36 retained-metric comparisons
are included. This run used the unchanged diagnostic driver in a private
extraction, with extended Windows paths after an initial path-length failure;
the receipt preserves its actual paths and times. It ran no Ant/JVM build,
provider code, archive extraction or network acquisition. The earlier receipts
remain historical observations rather than being relabelled as this run.

The separate native replay in `results/native-replay/` uses Temurin OpenJDK
21.0.12.1 on the same Windows/Python host. It actually runs 80 Apache Ant builds
from the 40 retained public pairs and two owned Java assemblies. The probe
returns 11 and 22, and the same-byte marker has the corresponding developer
and library attribution. Localized compiler/builder stdout and stderr are
retained as bytes. Probe stdout is decoded under its ASCII-integer contract.
Unavailable child CPU/RSS and total Java CPU remain null; parent CPU is separate.
Its timings are separate from the Linux table measurements and are not a
cross-platform speed comparison.
