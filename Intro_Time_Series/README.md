# Introduction to Time Series

Signals that evolve — and models that adapt with them. Bridges classical adaptive
filtering and modern recurrent networks.

**Prerequisites:** [DSP Workshop 1](../Intro_DSP/README.md) (convolution, transforms);
[Random Variables](../Intro_Math/Analysis/README.md#5-random-variables-planned) for the
stochastic viewpoint.

---

## Workshop 1 — Adaptive Filtering: Affine Projection *(planned)*

| Session | Focus | Planned content |
|---|---|---|
| **S1 — LMS to APA** | Theory | Wiener filtering recap, steepest descent, LMS; APA as a multi-constraint generalization. |
| **S2 — APA in practice** | Application | Implement NLMS & APA in NumPy; echo-cancellation / system-identification demo; convergence vs step size. |

## Workshop 2 — Adaptive Filtering: Kalman *(planned)*

| Session | Focus | Planned content |
|---|---|---|
| **S1 — State-space models & the Kalman filter** | Theory | State-space form, predict/update cycle, the Kalman gain as optimal blending. |
| **S2 — Tracking in practice** | Application | Implement a Kalman filter for a noisy tracking problem; tune $Q$/$R$; compare to APA from Workshop 1. |

## Workshop 3 — Recurrent Neural Networks *(planned)*

| Session | Focus | Planned content |
|---|---|---|
| **S1 — RNNs as nonlinear state-space models** | Theory | Recurrence, hidden state (the Kalman connection), backprop through time, vanishing gradients, LSTM/GRU. |
| **S2 — Sequence prediction in PyTorch** | Application | Train an LSTM on a real time series; compare against Kalman/APA baselines. Builds on [Intro to PyTorch](../Intro_DL_4_Physics/README.md). |

**Where next:** attention-based sequence models in
[Deep Learning for Physics → Transformers](../Intro_DL_4_Physics/README.md#workshop-2--introduction-to-transformers-available).

Contributions welcome — see the [contribution guide](../README.md#contributing).
