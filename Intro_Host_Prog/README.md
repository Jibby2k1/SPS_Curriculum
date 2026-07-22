# Introduction to Host Programming

Application track: the systems software that surrounds your signal chain — the OS your
code runs on and the databases your data lands in.

**Prerequisites:** [Intro to C](../Intro_Func_Prog/Intro_C.ipynb) (memory model, files,
command line).

---

## Workshop 1 — Introduction to Operating Systems *(planned)*

| Session | Focus | Planned content |
|---|---|---|
| **S1 — Processes & the kernel** | Theory | What an OS does; processes vs threads; syscalls; observing them with `ps`/`strace`. |
| **S2 — Memory & scheduling** | Theory | Virtual memory, paging, the scheduler — why your benchmark numbers wobble ([GPU latency](../Intro_GPU/README.md) callback). |
| **S3 — Concurrency in practice** | Application | Threads, locks, race conditions; a small producer/consumer pipeline in C or Python. |
| **S4 — The shell & automation** | Application | Bash, pipes, cron, environment; packaging an experiment so it reruns cleanly. |

## Workshop 2 — Introduction to Databases *(available)*

Material: [`Intro_Databases/Intro_Databases.ipynb`](./Intro_Databases/Intro_Databases.ipynb) — runs on `sqlite3`, zero installation.

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — Relational Model & SQL Basics** | Application | §2: tables, keys, constraints, SELECT | Design a sensor-logging schema; watch constraints reject bad data. |
| **S2 — Joins, Aggregation & Transactions** | Application | §3–§4: JOIN, GROUP BY, atomicity | Reassemble entities; summarize per-sensor; make multi-step changes all-or-nothing. |
| **S3 — Databases from Python** | Application | §5: parameterized queries, an experiment logger, beyond SQLite | Query safely (no injection); log training runs; know when to reach for Postgres/DuckDB. |

Contributions welcome — see the [contribution guide](../README.md#contributing).
