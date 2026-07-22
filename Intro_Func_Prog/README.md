# Introduction to Programming

Application track: the languages used throughout the curriculum. Start with Python if
you're new to programming; take C before the
[GPU](../Intro_GPU/README.md) and [FPGA](../Intro_FPGA/README.md) series.

---

## Workshop 1 — Introduction to C *(available)*

Material: [`Intro_C.ipynb`](./Intro_C.ipynb)

Partitioned into six 30–40 minute sessions:

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — Setup, Syntax & Control** | Application | §1 Pre-requisites, §2 Syntax and Structure | Install GCC, compile & run; use types, operators, and control structures. |
| **S2 — Functions & Scope** | Application | §3 Functions | Write and declare functions; understand scope, lifetime, static variables, recursion. |
| **S3 — Memory & Pointers** | Theory → Application | §4 Arrays & Structures, §5 Pointers | Model memory as an address space; use `malloc`/`realloc`/`free` correctly. |
| **S4 — Linked Structures** | Application | §6.1 Linked Lists, Stacks, Queues | Implement singly/doubly linked lists and static/dynamic stacks & queues. |
| **S5 — Trees & Heaps** | Theory → Application | §6.2 Trees (BST, Max/Min Heap) | Implement a BST and a heap; reason about their invariants and complexity. |
| **S6 — Files & the Command Line** | Application | §7 Files, §8 Command Line | Read/write files; build a small CLI program with `argc`/`argv`. |

**Where next:** C-level memory reasoning carries into
[GPU kernels](../Intro_GPU/README.md) and
[Operating Systems](../Intro_Host_Prog/README.md).

---

## Workshop 2 — Introduction to Python *(available)*

Material: [`Intro_Python/Intro_Python.ipynb`](./Intro_Python/Intro_Python.ipynb) — the entry point of the programming track.

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — Language Core** | Application | §2: types, strings, control flow, functions, comprehensions | Write and run real Python; use the core idioms. |
| **S2 — Data & Objects** | Application | §3: lists/dicts/sets/tuples, classes, modules | Organize data and code; build a small `Signal` class. |
| **S3 — Scientific Python** | Application | §4–§5: NumPy vectorization, broadcasting, Matplotlib | Compute and plot the way [DSP](../Intro_DSP/README.md) and [ML](../Intro_Mach_Learn/README.md) workshops assume. |

## Workshop 3 — Introduction to MATLAB *(planned)*

| Session | Focus | Planned content |
|---|---|---|
| **S1 — MATLAB fundamentals** | Application | Matrices as the native type, indexing, scripts vs functions, plotting. |
| **S2 — Signal processing in MATLAB** | Application | Signal Processing Toolbox: `fft`, `filter`, `freqz` — mirrors [DSP Workshop 1](../Intro_DSP/README.md) in MATLAB idiom. |

Contributions welcome — see the [contribution guide](../README.md#contributing).
