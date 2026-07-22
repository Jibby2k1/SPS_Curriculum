# SPS Curriculum

**Educational workshops in Signal Processing & Machine Learning Systems** — taught at the
University of Florida since 2024.

Every workshop is partitioned into **30–40 minute sessions** sized for a live meeting,
tagged as **Theory** 📐 (proofs, derivations, why it works) or **Application** 🛠️
(runnable code, real data, how to build it). Each topic README lists its session
breakdown, objectives, and cross-references.

## Curriculum Map

```mermaid
flowchart LR
    Math[📐 Mathematics<br>Analysis] --> DSP[📐 DSP<br>Transforms & Filters]
    Prog[🛠️ Programming<br>Python · C · MATLAB] --> DSP
    Prog --> Host[🛠️ Host Programming<br>OS · Databases]
    Prog --> GPU[🛠️ GPU Systems]
    DSP --> TS[Time Series<br>Adaptive Filters · RNNs]
    DSP --> FPGA[🛠️ FPGA Systems]
    Math --> ML[Machine Learning<br>ANN · CNN · Scaling]
    GPU --> DL[🛠️ DL for Physics<br>PyTorch · Transformers]
    ML --> DL
    TS --> DL
```

## Workshops

| Topic | Workshop | Focus | Status | Contributors |
|---|---|---|---|---|
| [**Mathematics**](./Intro_Math/README.md) | [Real Number Systems](./Intro_Math/Analysis/Real_Number_Systems.ipynb) | 📐 Theory | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Basic Topology](./Intro_Math/Analysis/Basic_Topology.ipynb) | 📐 Theory | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Numerical Sequences and Series](./Intro_Math/Analysis/README.md#3-numerical-sequences-and-series-planned) | 📐 Theory | 🚧 Planned | — |
| | [Measure Theory](./Intro_Math/Analysis/README.md#4-measure-theory-planned) | 📐 Theory | 🚧 Planned | — |
| | [Random Variables](./Intro_Math/Analysis/README.md#5-random-variables-planned) | 📐 Theory | 🚧 Planned | — |
| | [Independence](./Intro_Math/Analysis/README.md#6-independence-planned) | 📐 Theory | 🚧 Planned | — |
| [**Programming**](./Intro_Func_Prog/README.md) | [Introduction to C](./Intro_Func_Prog/Intro_C.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Introduction to Python](./Intro_Func_Prog/README.md#workshop-2--introduction-to-python-planned) | 🛠️ Application | 🚧 Planned | — |
| | [Introduction to MATLAB](./Intro_Func_Prog/README.md#workshop-3--introduction-to-matlab-planned) | 🛠️ Application | 🚧 Planned | — |
| [**Host Programming**](./Intro_Host_Prog/README.md) | [Operating Systems](./Intro_Host_Prog/README.md#workshop-1--introduction-to-operating-systems-planned) | 📐+🛠️ | 🚧 Planned | — |
| | [Databases](./Intro_Host_Prog/README.md#workshop-2--introduction-to-databases-planned) | 🛠️ Application | 🚧 Planned | — |
| [**DSP**](./Intro_DSP/README.md) | [Foundations of Signal Processing](./Intro_DSP/Foundations_of_Signal_Processing_1.ipynb) | 📐 Theory | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Filter Design](./Intro_DSP/README.md#workshop-2--filter-design-planned) | 🛠️ Application | 🚧 Planned | — |
| [**GPU Systems**](./Intro_GPU/README.md) | [GPU-Accelerated Computing (Numba & CuPy)](./Intro_GPU/Intro_GPU.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [RAPIDS](./Intro_GPU/README.md#workshop-2--introduction-to-rapids-planned) | 🛠️ Application | 🚧 Planned | — |
| [**FPGA Systems**](./Intro_FPGA/README.md) | [Introduction to FPGA](./Intro_FPGA/README.md#workshop-1--introduction-to-fpga-planned) | 🛠️ Application | 🚧 Planned | — |
| [**Time Series**](./Intro_Time_Series/README.md) | [Adaptive Filtering (APA)](./Intro_Time_Series/README.md#workshop-1--adaptive-filtering-affine-projection-planned) | 📐+🛠️ | 🚧 Planned | — |
| | [Adaptive Filtering (Kalman)](./Intro_Time_Series/README.md#workshop-2--adaptive-filtering-kalman-planned) | 📐+🛠️ | 🚧 Planned | — |
| | [Recurrent Neural Networks](./Intro_Time_Series/README.md#workshop-3--recurrent-neural-networks-planned) | 📐+🛠️ | 🚧 Planned | — |
| [**Machine Learning**](./Intro_Mach_Learn/README.md) | [Artificial Neural Networks](./Intro_Mach_Learn/README.md#workshop-1--artificial-neural-networks-planned) | 📐+🛠️ | 🚧 Planned | — |
| | [Convolutional Neural Networks](./Intro_Mach_Learn/README.md#workshop-2--convolutional-neural-networks-planned) | 📐+🛠️ | 🚧 Planned | — |
| | [Scaling Neural Networks](./Intro_Mach_Learn/README.md#workshop-3--scaling-neural-networks-planned) | 📐+🛠️ | 🚧 Planned | — |
| [**DL for Physics**](./Intro_DL_4_Physics/README.md) | [Introduction to PyTorch](./Intro_DL_4_Physics/intro_pytorch/intro_pytorch.ipynb) | 🛠️ Application | ✅ Available | [Awwab](https://github.com/kaddu341) |
| | [Introduction to Transformers](./Intro_DL_4_Physics/intro_transformers/intro_transformers.ipynb) | 🛠️ Application | ✅ Available | [Awwab](https://github.com/kaddu341) |

## Getting Started

1. **Pick a session**, not a whole notebook — each topic README maps its notebooks into
   30–40 minute sessions with objectives and prerequisites.
2. **Run the notebooks** in [Jupyter](https://jupyter.org/) or
   [Google Colab](https://colab.research.google.com/) (upload the `.ipynb`, or open via
   `File → Open notebook → GitHub` and paste this repo's URL).
3. **Theory or application?** 📐 sessions are lecture/whiteboard-friendly; 🛠️ sessions
   are live-coding-friendly. Most workshops interleave both and cross-reference each
   other.

## Contributing

🚧 **Planned** workshops have full session outlines in their topic READMEs waiting for an
author. To contribute:

1. Fork the repo and create a feature branch.
2. Pick a planned workshop (or improve an existing one) — follow its session outline, or
   propose changes to it.
3. Match the house style: sessions sized 30–40 minutes, tagged theory/application, with
   cross-references to related workshops.
4. Submit a PR.

## Acknowledgements

Built by the SPS community at the University of Florida. Special thanks to all
[contributors](https://github.com/Jibby2k1/SPS_Curriculum/graphs/contributors).
