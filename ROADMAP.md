# Curriculum Roadmap

The build-out plan. Priorities: ⭐ = fills a gap other workshops depend on; 🎥 = strong
YouTube material. Statuses move ✅ as content lands (see the [README](./README.md) table
for the live view). Sizing rule everywhere: **one session = 30–40 minutes = one video**
(see [RECORDING.md](./RECORDING.md)).

## A. Mathematics
- ⭐ **Linear Algebra for Signals** (5) — bases · projections/least squares · eigen · SVD · matrix calculus
- ⭐ **Optimization** (4) — convexity · GD + rates · Lagrange/KKT · SGD
- ⭐ **Estimation Theory** (4) — MLE · CRLB · Bayes/MMSE · sufficiency
- **Hilbert Spaces & Fourier, Properly** (3) — inner products · projection theorem · the Fourier basis
- 🎥 **Information Theory** (4) — entropy · KL/cross-entropy · mutual information · coding at a glance
- **Complex Analysis Lite** (2) — poles · residues → inverse transforms

## B. DSP
- ⭐ **Foundations of Signal Processing 2** (4) — z-transform/ROC · multirate · polyphase · wavelets teaser
- ⭐ **Statistical Signal Processing** (4) — random processes · PSD/Welch · Wiener · matched filters & detection
- 🎥 **Array Processing & Beamforming** (3) — manifold · delay-and-sum · MVDR/MUSIC
- 🎥 **Audio & Speech DSP** (3) — spectrograms · pitch/formants · effects as filters
- **Image Processing as 2-D DSP** (3) — 2-D conv/FFT · aliasing/moiré · edges → CNN bridge
- 🎥 **Compressed Sensing** (2) — undersampling · L1 reconstruction
- **Digital Communications** (4) — modulation · matched filter/eye diagrams · sync · OFDM

## C. Time Series
- ⭐ **RLS & Recursive Estimation** (2) — EW least squares · RLS ↔ Kalman
- **Beyond Kalman** (3) — EKF · UKF · 🎥 particle filters
- **Classical Forecasting** (2) — AR/MA + ACF/PACF · ARIMA fit & diagnose

## D. Machine Learning
- ⭐ **Training Dynamics** (3) — optimizers · schedules/warmup · regularization & double descent
- ⭐🎥 **LLMs from the Ground Up** (4) — tokens/embeddings · pretraining · finetuning/RLHF glance · inference
- 🎥 **Physics-Informed Neural Networks** (2) — PDE losses · solve a real problem
- **Representation Learning** (3) — autoencoders · VAEs · contrastive
- 🎥 **Diffusion Models** (2) — noising intuition · tiny 2-D diffusion
- **Kernel Methods & RKHS** (3) — kernel trick · GPs · KLMS bridge to adaptive filters
- **Model Compression & Edge AI** (3) — quantization · pruning · distillation
- **Uncertainty in ML** (2) — calibration · ensembles

## E. Systems
- ⭐ **Hardware-Accelerated Scientific Computing** (3) — warps/occupancy/shared memory · streams · CGMA-driven optimization *(promised in Intro_GPU)*
- ⭐ **Real-Time Signal Processing** (3) — fixed point · buffers/latency budgets · a real-time pipeline *(promised in Intro_GPU)*
- 🎥 **Software-Defined Radio** (3) — RTL-SDR · receive FM · decode something
- **Git & Collaboration** (2) — commits/branches/merges · PRs on this repo
- **Containers & Reproducibility** (2) — envs → Docker · package a workshop
- **CUDA in C++** (3) — raw kernels · memory · cuBLAS/cuFFT

## F. Structural
1. ✅ Split DSP Foundations 6 → 8 sessions
2. ✅ Split `Intro_C` §6 → `Data_Structures_in_C`
3. ✅ Rename `Intro_Func_Prog` → `Intro_Programming`
4. ✅ Transformers dual-home resolved: `Intro_DL_4_Physics` is the applied-DL home; ML README points there
5. ✅ [RECORDING.md](./RECORDING.md) house format
6. `_blank_` student versions for new workshops (rolling, per teaching term)
7. ✅ [START_HERE.md](./START_HERE.md) learning paths
