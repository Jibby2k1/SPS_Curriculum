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

## Workshop 2 — Introduction to Databases *(planned)*

| Session | Focus | Planned content |
|---|---|---|
| **S1 — Relational model & SQL** | Theory → Application | Tables, keys, normalization; SELECT/JOIN/GROUP BY on a sample sensor dataset (SQLite). |
| **S2 — Databases from code** | Application | Python + SQLite/Postgres: parameterized queries, transactions, storing experiment results. |
| **S3 — Beyond relational** | Application | Time-series & columnar stores (Parquet, DuckDB) for signal data; when each wins. |

Contributions welcome — see the [contribution guide](../README.md#contributing).
