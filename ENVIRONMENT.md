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

The expanded 55-test suite also passes in a separate Windows/Python 3.12.14
execution recorded in `results/unit-tests.json` and `results/unit-tests.txt`.
This test run does not repeat the external builder campaign.

The complete Ubuntu/Python 3.12 workflow requires the runner's existing JDK;
no dependency installation or toolchain download is performed by the scientific
commands themselves.
