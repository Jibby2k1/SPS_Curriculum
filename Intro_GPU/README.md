# Introduction to GPU Systems

How to make scientific code fast: from CPU vectorization to GPU architecture and
CUDA-backed Python. Pairs theory (what the hardware actually does) with application
(porting NumPy code to the GPU).

**Prerequisites:** [Intro to Python](../Intro_Func_Prog/README.md#workshop-2--introduction-to-python-available);
[Intro to C](../Intro_Func_Prog/Intro_C.ipynb) helps for the memory model.

---

## Workshop 1 — GPU-Accelerated Scientific Computing *(available)*

Material: [`Intro_GPU.ipynb`](./Intro_GPU.ipynb)

Partitioned into two 30–40 minute sessions:

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — From CPU to GPU** | Theory | §2 CPU (regular vs vectorized), §3.1–3.2 GPU hardware architecture & system structure | Understand SIMD, why GPUs exist, and how host & device fit together. |
| **S2 — Memory, Kernels & CuPy** | Application | §3.3–3.5 GPU memory & kernels, §4 Minimizing latency, §5 NumPy vs CuPy | Move data host↔device deliberately; port NumPy code to CuPy and benchmark it. |

**Where next:** train neural networks on the GPU in
[Deep Learning for Physics](../Intro_DL_4_Physics/README.md), or scale dataframes with
RAPIDS below.

---

## Workshop 2 — Introduction to RAPIDS *(planned)*

| Session | Focus | Planned content |
|---|---|---|
| **S1 — cuDF** | Application | pandas → cuDF: GPU dataframes, when transfers dominate, benchmarking honestly. |
| **S2 — cuML & cuSignal** | Application | GPU-accelerated ML primitives and signal processing; ties to [DSP](../Intro_DSP/README.md) and [ML](../Intro_Mach_Learn/README.md). |

Contributions welcome — see the [contribution guide](../README.md#contributing).
