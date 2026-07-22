# Introduction to GPU Systems

How to make scientific code fast: from CPU vectorization to GPU architecture and
CUDA-backed Python. Pairs theory (what the hardware actually does) with application
(porting NumPy code to the GPU).

**Prerequisites:** [Intro to Python](../Intro_Programming/README.md#workshop-2--introduction-to-python-available);
[Intro to C](../Intro_Programming/Intro_C.ipynb) helps for the memory model.

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

## Workshop 2 — Introduction to RAPIDS *(draft — pending review)*

Material: [`Intro_RAPIDS.ipynb`](./Intro_RAPIDS.ipynb) — requires an NVIDIA GPU (Colab works); carries a review banner.

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — cuDF** | Application | §2: pandas → cuDF port, the honest end-to-end benchmark, the crossover | Charge the transfer; find where the GPU actually wins. |
| **S2 — cuML** | Application | §3: KMeans bake-off, the three-condition decision rule | Know when RAPIDS earns its keep vs sklearn ([ML](../Intro_Mach_Learn/README.md)). |
