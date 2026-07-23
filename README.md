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
    Math[📐 Mathematics<br>Analysis · LinAlg · Optimization<br>Estimation · Info Theory] --> DSP[📐 DSP<br>Transforms · Filters · Statistical SP<br>Arrays · Audio · Images · Comms]
    Prog[🛠️ Programming<br>Python · C · MATLAB] --> DSP
    Prog --> Host[🛠️ Host Programming<br>OS · Databases · Git · Containers]
    Prog --> GPU[🛠️ GPU Systems<br>CuPy · CUDA · RAPIDS]
    DSP --> TS[Time Series<br>Adaptive Filters · Kalman+ · ARIMA · RNNs]
    DSP --> SDR[🛠️ SDR<br>real antennas]
    DSP --> FPGA[🛠️ FPGA Systems]
    Math --> ML[Machine Learning<br>ANN→CNN→LLMs · Diffusion<br>Kernels · Compression · Uncertainty]
    GPU --> DL[🛠️ DL for Physics<br>PyTorch · Transformers · PINNs]
    ML --> DL
    TS --> DL
    Math --> RMT[📐 Ring 2 math<br>NLA · RMT · Martingales · OT]
    ML --> Frontier[📐+🛠️ ML frontier<br>RL · Diffusion II · Causal<br>MechInterp · Architectures]
    DSP --> R2DSP[📐+🛠️ Ring 2 DSP<br>Graphs · Coding · Radar · MIMO<br>ICA · Sparse · Cyclo]
    GPU --> Sys2[🛠️ Systems II<br>Roofline · Distributed · Triton]
    R2DSP --> Cap[🏁 Capstone<br>full pipeline]
    Frontier --> Cap
    Sys2 --> Cap
```

Start with [**START_HERE.md**](./START_HERE.md) for guided learning paths; see the
[**ROADMAP**](./ROADMAP.md) for what's next, [**RECORDING.md**](./RECORDING.md) for the
video format, and [**VIDEO_PLAN.md**](./VIDEO_PLAN.md) for the full generated recording plan.
Contributors: [**CONTRIBUTING.md**](./CONTRIBUTING.md) + `pip install -r requirements.txt` +
`python tools/validate.py`.

## Workshops

| Topic | Workshop | Focus | Status | Contributors |
|---|---|---|---|---|
| [**Mathematics**](./Intro_Math/README.md) | [Real Number Systems](./Intro_Math/Analysis/Real_Number_Systems.ipynb) | 📐 Theory | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Basic Topology](./Intro_Math/Analysis/Basic_Topology.ipynb) | 📐 Theory | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Numerical Sequences and Series](./Intro_Math/Analysis/Numerical_Sequences_and_Series.ipynb) | 📐 Theory | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Measure Theory](./Intro_Math/Analysis/Measure_Theory.ipynb) | 📐 Theory | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| | [Random Variables](./Intro_Math/Analysis/Random_Variables.ipynb) | 📐 Theory | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| | [Independence](./Intro_Math/Analysis/Independence.ipynb) | 📐 Theory | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| | [Linear Algebra for Signals](./Intro_Math/Linear_Algebra/Linear_Algebra.ipynb) | 📐 Theory | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Optimization](./Intro_Math/Optimization/Optimization.ipynb) | 📐 Theory | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Estimation Theory](./Intro_Math/Estimation_Theory/Estimation_Theory.ipynb) | 📐 Theory | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Hilbert Spaces & Fourier](./Intro_Math/Hilbert_Spaces/Hilbert_Spaces.ipynb) | 📐 Theory | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| | [Information Theory](./Intro_Math/Information_Theory/Information_Theory.ipynb) | 📐 Theory | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Complex Analysis Lite](./Intro_Math/Complex_Analysis/Complex_Analysis_Lite.ipynb) | 📐 Theory | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| | [Numerical Linear Algebra](./Intro_Math/Numerical_Linear_Algebra/Numerical_Linear_Algebra.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Concentration & Learning Theory](./Intro_Math/Concentration/Concentration_Inequalities.ipynb) | 📐 Theory | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| | [Stochastic Processes II](./Intro_Math/Stochastic_Processes/Stochastic_Processes_2.ipynb) | 📐 Theory | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| | [Convex Optimization II](./Intro_Math/Optimization/Convex_Optimization_2.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Random Matrix Theory](./Intro_Math/Random_Matrix_Theory/Random_Matrix_Theory.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Manifold Optimization](./Intro_Math/Optimization/Manifold_Optimization.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| [**Programming**](./Intro_Programming/README.md) | [Introduction to C](./Intro_Programming/Intro_C.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Data Structures in C](./Intro_Programming/Data_Structures_in_C.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Introduction to Python](./Intro_Programming/Intro_Python/Intro_Python.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Introduction to MATLAB](./Intro_Programming/Intro_MATLAB/Intro_MATLAB.ipynb) | 🛠️ Application | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| [**Host Programming**](./Intro_Host_Prog/README.md) | [Operating Systems](./Intro_Host_Prog/Intro_OS/Intro_OS.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Databases](./Intro_Host_Prog/Intro_Databases/Intro_Databases.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Git & Collaboration](./Intro_Host_Prog/Intro_Git/Intro_Git.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Containers & Reproducibility](./Intro_Host_Prog/Intro_Containers/Intro_Containers.ipynb) | 🛠️ Application | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| [**DSP**](./Intro_DSP/README.md) | [Foundations of Signal Processing](./Intro_DSP/Foundations_of_Signal_Processing_1.ipynb) | 📐 Theory | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Filter Design](./Intro_DSP/Filter_Design.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Foundations of Signal Processing 2](./Intro_DSP/Foundations_of_Signal_Processing_2.ipynb) | 📐 Theory | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Statistical Signal Processing](./Intro_DSP/Statistical_Signal_Processing.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Array Processing & Beamforming](./Intro_DSP/Array_Processing.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Audio & Speech DSP](./Intro_DSP/Audio_Speech_DSP.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Image Processing as 2-D DSP](./Intro_DSP/Image_Processing.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Compressed Sensing](./Intro_DSP/Compressed_Sensing.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Digital Communications](./Intro_DSP/Digital_Communications.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Real-Time Signal Processing](./Intro_DSP/Real_Time_DSP.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Graph Signal Processing & GNNs](./Intro_DSP/Graph_Signal_Processing.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Channel Coding](./Intro_DSP/Channel_Coding.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Sparse Coding & Dictionary Learning](./Intro_DSP/Sparse_Dictionary_Learning.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Blind Source Separation & ICA](./Intro_DSP/ICA_Blind_Source_Separation.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Time–Frequency II](./Intro_DSP/Time_Frequency_2.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Cyclostationarity & HOS](./Intro_DSP/Cyclostationary_HOS.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Radar Signal Processing](./Intro_DSP/Radar_Signal_Processing.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [MIMO Communications](./Intro_DSP/MIMO_Communications.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Sigma-Delta & Quantization](./Intro_DSP/Sigma_Delta_Quantization.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| [**GPU Systems**](./Intro_GPU/README.md) | [GPU-Accelerated Computing (Numba & CuPy)](./Intro_GPU/Intro_GPU.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [RAPIDS](./Intro_GPU/Intro_RAPIDS.ipynb) | 🛠️ Application | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| | [Hardware-Accelerated Computing](./Intro_GPU/HW_Accelerated_Computing.ipynb) | 📐+🛠️ | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| | [CUDA in C++](./Intro_GPU/CUDA_Cpp.ipynb) | 🛠️ Application | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| | [Performance Engineering & Roofline](./Intro_GPU/Performance_Engineering.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Distributed Training II](./Intro_GPU/Distributed_Training_2.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Triton: GPU Kernels in Python](./Intro_GPU/Triton_Kernels.ipynb) | 🛠️ Application | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| [**FPGA Systems**](./Intro_FPGA/README.md) | [Introduction to FPGA](./Intro_FPGA/Intro_FPGA.ipynb) | 🛠️ Application | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| | [HLS for FPGA: C to Gates](./Intro_FPGA/HLS_for_FPGA.ipynb) | 🛠️ Application | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| [**Time Series**](./Intro_Time_Series/README.md) | [Adaptive Filtering (APA)](./Intro_Time_Series/Intro_AdFilt_APA.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Adaptive Filtering (Kalman)](./Intro_Time_Series/Intro_AdFilt_KF.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Recurrent Neural Networks](./Intro_Time_Series/Intro_RNN.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [RLS & Recursive Estimation](./Intro_Time_Series/Intro_RLS.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Beyond Kalman (EKF/UKF/Particle)](./Intro_Time_Series/Beyond_Kalman.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Classical Forecasting (ARIMA)](./Intro_Time_Series/Classical_Forecasting.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [State-Space Models: Kalman → S4 → Mamba](./Intro_Time_Series/State_Space_Models_Kalman_to_Mamba.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Online Learning & Regret](./Intro_Time_Series/Online_Learning_and_Regret.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| [**Machine Learning**](./Intro_Mach_Learn/README.md) | [Artificial Neural Networks](./Intro_Mach_Learn/Intro_ANN/Intro_ANN.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Convolutional Neural Networks](./Intro_Mach_Learn/Intro_CNN/Intro_CNN.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Scaling Neural Networks](./Intro_Mach_Learn/Scale_NN/Scale_NN.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Training Dynamics](./Intro_Mach_Learn/Training_Dynamics.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [LLMs from the Ground Up](./Intro_Mach_Learn/LLMs_from_the_Ground_Up.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Representation Learning](./Intro_Mach_Learn/Representation_Learning.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Diffusion Models](./Intro_Mach_Learn/Diffusion_Models.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Kernel Methods & RKHS](./Intro_Mach_Learn/Kernel_Methods.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Model Compression & Edge AI](./Intro_Mach_Learn/Model_Compression.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Uncertainty in ML](./Intro_Mach_Learn/Uncertainty_in_ML.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Reinforcement Learning](./Intro_Mach_Learn/Reinforcement_Learning.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Optimal Transport](./Intro_Mach_Learn/Optimal_Transport.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Diffusion II: Score & SDEs](./Intro_Mach_Learn/Diffusion_Score_SDE.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Causal Inference](./Intro_Mach_Learn/Causal_Inference.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Modern Architectures](./Intro_Mach_Learn/Modern_Architectures.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Variational Inference & Flows](./Intro_Mach_Learn/Variational_Inference_Flows.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Mechanistic Interpretability](./Intro_Mach_Learn/Mechanistic_Interpretability.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [Federated Learning & Privacy](./Intro_Mach_Learn/Federated_Learning_Privacy.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| | [TinyML](./Intro_Mach_Learn/TinyML.ipynb) | 🛠️ Application | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| [**DL for Physics**](./Intro_DL_4_Physics/README.md) | [Introduction to PyTorch](./Intro_DL_4_Physics/intro_pytorch/intro_pytorch.ipynb) | 🛠️ Application | ✅ Available | [Awwab](https://github.com/kaddu341) |
| | [Introduction to Transformers](./Intro_DL_4_Physics/intro_transformers/intro_transformers.ipynb) | 🛠️ Application | ✅ Available | [Awwab](https://github.com/kaddu341) |
| | [Physics-Informed Neural Networks](./Intro_DL_4_Physics/PINNs.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| [**SDR**](./Intro_SDR/README.md) | [Software-Defined Radio](./Intro_SDR/Software_Defined_Radio.ipynb) | 🛠️ Application | 📝 Draft¹ | [Raul](https://github.com/Jibby2k1) |
| [**Quantum**](./Intro_Quantum/README.md) | [Quantum for Signal Processors](./Intro_Quantum/Quantum_for_Signal_Processors.ipynb) | 📐+🛠️ | ✅ Available | [Raul](https://github.com/Jibby2k1) |
| [**Capstone**](./Capstone/README.md) | [Build a Full System](./Capstone/Full_System_Capstone.ipynb) | 🛠️ Application | ✅ Available | [Raul](https://github.com/Jibby2k1) |

¹ **📝 Draft** = complete but pending instructor verification (math proofs, or code needing MATLAB/FPGA/GPU hardware to run). Each draft carries a ⚠️ banner in the notebook; it is removed once an instructor signs off.

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

📝 **Draft** workshops need an instructor verification pass — a great first contribution. To contribute:

1. Fork the repo and create a feature branch.
2. Pick a planned workshop (or improve an existing one) — follow its session outline, or
   propose changes to it.
3. Match the house style — see the [**Style Guide**](./STYLE_GUIDE.md): sessions sized 30–40
   minutes, tagged theory/application, intuition spelled out before rigor, with cross-references
   to related workshops.
4. Submit a PR.

## Acknowledgements

Built by the SPS community at the University of Florida. Special thanks to all
[contributors](https://github.com/Jibby2k1/SPS_Curriculum/graphs/contributors).
