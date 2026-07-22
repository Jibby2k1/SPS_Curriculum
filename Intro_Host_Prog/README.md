# Introduction to Host Programming

Application track: the systems software that surrounds your signal chain — the OS your
code runs on and the databases your data lands in.

**Prerequisites:** [Intro to C](../Intro_Programming/Intro_C.ipynb) (memory model, files,
command line).

---

## Workshop 1 — Introduction to Operating Systems *(available)*

Material: [`Intro_OS/Intro_OS.ipynb`](./Intro_OS/Intro_OS.ipynb) — requires Linux/macOS/WSL or Colab.

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — Processes & the Kernel** | Theory → Application | §2: PIDs, the process tree via /proc, strace | See what a process is; watch syscalls happen. |
| **S2 — Memory & Scheduling** | Theory → Application | §3–§4: /proc/self/maps, lazy allocation demo, scheduler jitter | Understand virtual memory & why benchmarks wobble ([GPU latency](../Intro_GPU/README.md) callback). |
| **S3 — Concurrency in Practice** | Application | §5: a real race condition, locks, GIL, multiprocessing, producer/consumer | Cause a race, fix it twice (lock, queue); get true parallelism. |
| **S4 — The Shell & Automation** | Application | §6: pipes, redirection, environment, reproducibility checklist | Compose tools; package experiments that rerun cleanly. |

## Workshop 2 — Introduction to Databases *(available)*

Material: [`Intro_Databases/Intro_Databases.ipynb`](./Intro_Databases/Intro_Databases.ipynb) — runs on `sqlite3`, zero installation.

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — Relational Model & SQL Basics** | Application | §2: tables, keys, constraints, SELECT | Design a sensor-logging schema; watch constraints reject bad data. |
| **S2 — Joins, Aggregation & Transactions** | Application | §3–§4: JOIN, GROUP BY, atomicity | Reassemble entities; summarize per-sensor; make multi-step changes all-or-nothing. |
| **S3 — Databases from Python** | Application | §5: parameterized queries, an experiment logger, beyond SQLite | Query safely (no injection); log training runs; know when to reach for Postgres/DuckDB. |

## Workshop 3 — Git & Collaboration *(available)*

Material: [`Intro_Git/Intro_Git.ipynb`](./Intro_Git/Intro_Git.ipynb) — builds its own sandbox repo; every cell runs.

| Session | Focus | Objectives |
|---|---|---|
| **S1 — Commits, Branches & Merges** | Application | The snapshot DAG; cause and resolve a real conflict. |
| **S2 — The Collaboration Loop** | Application | Fork → branch → PR → review, plus the five rescue commands. |

## Workshop 4 — Containers & Reproducibility *(draft — pending review)*

Material: [`Intro_Containers/Intro_Containers.ipynb`](./Intro_Containers/Intro_Containers.ipynb) — needs Docker; carries a review banner.

| Session | Focus | Objectives |
|---|---|---|
| **S1 — Environments, Pinned** | Application | requirements → lockfiles: declare intent, lock reality. |
| **S2 — Docker** | Application | Containerize a workshop; layer-cache discipline; volumes for data. |

Contributions welcome — see the [contribution guide](../README.md#contributing).
