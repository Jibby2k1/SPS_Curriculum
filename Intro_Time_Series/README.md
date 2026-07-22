# Introduction to Time Series

Signals that evolve — and models that adapt with them. Bridges classical adaptive
filtering and modern recurrent networks.

**Prerequisites:** [DSP Workshop 1](../Intro_DSP/README.md) (convolution, transforms);
[Random Variables](../Intro_Math/Analysis/README.md#5-random-variables-draft--pending-review) for the
stochastic viewpoint.

---

## Workshop 1 — Adaptive Filtering: Affine Projection *(available)*

Material: [`Intro_AdFilt_APA.ipynb`](./Intro_AdFilt_APA.ipynb)

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — From Steepest Descent to LMS** | Theory → Application | §2: Wiener solution, LMS derivation & implementation | Derive $\mathbf{w}_o = R^{-1}\mathbf{p}$; watch LMS discover an unknown system. |
| **S2 — NLMS & APA** | Theory → Application | §3–§4: normalization, affine projection, the colored-input race | Fix LMS's power sensitivity; see projection order buy convergence speed on correlated input. |

## Workshop 2 — Adaptive Filtering: Kalman *(available)*

Material: [`Intro_AdFilt_KF.ipynb`](./Intro_AdFilt_KF.ipynb)

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — State-Space Models & the Kalman Equations** | Theory | §2: predict/update cycle, the gain as a trust dial, scalar sanity check | Understand the five equations and why the innovation drives everything. |
| **S2 — Tracking in Practice** | Application | §3: constant-velocity tracker, estimating unmeasured velocity, tuning $Q$/$R$ | Build a real tracker; see both mistuning failure modes. |

## Workshop 3 — Recurrent Neural Networks *(available)*

Material: [`Intro_RNN.ipynb`](./Intro_RNN.ipynb)

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — RNNs as Learned State-Space Models** | Theory | §2: recurrence, BPTT, vanishing/exploding gradients (demo), LSTM gating | Connect RNN ↔ Kalman; see *why* plain RNNs forget and how gates fix it. |
| **S2 — Sequence Prediction in Practice** | Application | §3: LSTM forecaster vs persistence & linear AR baselines | Train honestly, clip gradients, and respect the linear baseline. Builds on [Intro to PyTorch](../Intro_DL_4_Physics/README.md). |

## Workshop 4 — RLS & Recursive Estimation *(available)*

Material: [`Intro_RLS.ipynb`](./Intro_RLS.ipynb) — the rung between APA and Kalman.

| Session | Focus | Objectives |
|---|---|---|
| **S1 — Exponentially-Weighted LS** | Theory → Application | Matrix inversion lemma → O(M²) exact recursion; near-immune to colored input. |
| **S2 — RLS ↔ Kalman** | Theory | The identification verified to machine precision; the family cost/robustness table. |

## Workshop 5 — Beyond Kalman *(available)*

Material: [`Beyond_Kalman.ipynb`](./Beyond_Kalman.ipynb)

| Session | Focus | Objectives |
|---|---|---|
| **S1 — The EKF** | Application | Track a large-swing pendulum from sin(θ) alone. |
| **S2 — The UKF** | Theory → Application | Sigma points beat the tangent line on the banana problem. |
| **S3 — Particle Filters** | Application | Honestly bimodal belief in a corridor; resampling and its costs. |

## Workshop 6 — Classical Forecasting *(available)*

Material: [`Classical_Forecasting.ipynb`](./Classical_Forecasting.ipynb)

| Session | Focus | Objectives |
|---|---|---|
| **S1 — AR & MA Fingerprints** | Theory → Application | ACF/PACF identification; Yule-Walker recovers [1.1, −0.5] exactly. |
| **S2 — ARIMA & Honest Forecasts** | Application | Difference, fit, forecast with a widening 95% cone. |

**Where next:** attention-based sequence models in
[Deep Learning for Physics → Transformers](../Intro_DL_4_Physics/README.md#workshop-2--introduction-to-transformers-available).

Contributions welcome — see the [contribution guide](../README.md#contributing).
