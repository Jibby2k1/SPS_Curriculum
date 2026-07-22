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

## Workshop 3 — Hardware-Accelerated Scientific Computing *(draft — pending review)*

Material: [`HW_Accelerated_Computing.ipynb`](./HW_Accelerated_Computing.ipynb) — the promised sequel; requires an NVIDIA GPU; carries a review banner.

| Session | Focus | Objectives |
|---|---|---|
| **S1 — Warps, Divergence & Occupancy** | Theory → Application | The 32-thread lockstep unit; aligned vs splitting branches, timed. |
| **S2 — Shared Memory & Tiling** | Application | Tiled matmul: buy CGMA with the on-chip workbench. |
| **S3 — Streams & Overlap** | Application | Pinned memory + streams: hide transfers behind compute. |

## Workshop 4 — CUDA in C++ *(draft — pending review)*

Material: [`CUDA_Cpp.ipynb`](./CUDA_Cpp.ipynb) — needs `nvcc`; carries a review banner.

| Session | Focus | Objectives |
|---|---|---|
| **S1 — First Kernels** | Application | Full lifecycle with CUDA_CHECK discipline. |
| **S2 — Memory Patterns** | Application | Unified vs explicit vs pinned; bandwidth measured with events. |
| **S3 — The Library Ecosystem** | Application | cuBLAS (column-major!), cuFFT; the your-kernel-vs-library ladder. |

