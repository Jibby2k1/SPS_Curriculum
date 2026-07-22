# Introduction to Digital Signal Processing

Theory-first treatment of signals, transforms, and fast algorithms, followed by an
application-focused series on filter design.

**Prerequisites:** comfort with calculus and complex numbers.
[Real Number Systems](../Intro_Math/Analysis/Real_Number_Systems.ipynb) and
[Basic Topology](../Intro_Math/Analysis/Basic_Topology.ipynb) are helpful but not required.
For the programming side, see [Intro to Python](../Intro_Programming/README.md#workshop-2--introduction-to-python-available).

---

## Workshop 1 — Foundations of Signal Processing *(available)*

Material: [`Foundations_of_Signal_Processing_1.ipynb`](./Foundations_of_Signal_Processing_1.ipynb)

The notebook is partitioned into eight 30–40 minute sessions (re-cut from six so each
records as one video — see [RECORDING.md](../RECORDING.md)).

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — Why Transforms?** | Theory | §0 Introduction, §1 Pre-requisites (Euler's $e$) | Motivate frequency-domain thinking. |
| **S2 — Function Spaces** | Theory | §2.0 ($\ell_1 \subseteq \ell_2$, Hölder) | Establish the spaces signals live in. |
| **S3 — The Laplace Transform** | Theory | §2.1 (history, DT & CT Laplace) | The parent transform, in both time flavors. |
| **S4 — The DTFT & CTFT** | Theory | §2.2.0–2.2.2 | Fourier as Laplace on the circle/axis. |
| **S5 — The DFT & Sampling** | Theory | §2.2.3–2.2.4 | The computable transform; Nyquist–Shannon. |
| **S6 — Uncertainty & the STFT** | Theory | §2.3 | Time–frequency trade-offs; the spectrogram. |
| **S7 — The FFT** | Theory → Application | §2.4.1–2.4.2 (Radix-2 DIT & DIF) | Derive the butterfly; count operations. |
| **S8 — Fast Convolution** | Application | §2.4.3 (Overlap-Add, Overlap-Save) | Block convolution for long/streaming signals. |

**Where next:** apply these transforms in
[Filter Design](#workshop-2--filter-design-available) (application),
[Adaptive Filtering](../Intro_Time_Series/README.md) (time series), or accelerate them in
[Intro to GPU Systems](../Intro_GPU/README.md).

---

## Workshop 2 — Filter Design *(available)*

Material: [`Filter_Design.ipynb`](./Filter_Design.ipynb) — the application-focused counterpart to Workshop 1.

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — FIR Filters** | Application | §2: windowed-sinc design, windows, linear phase | Design an FIR low-pass with `firwin`; read magnitude/phase; know why linear phase matters. |
| **S2 — IIR Filters** | Application | §3: Butterworth/Chebyshev/elliptic, poles & zeros | Choose between FIR/IIR; verify stability from pole locations (ties back to Laplace, W1·S2). |
| **S3 — Filters in Practice** | Application | §4: notch + low-pass on an ECG-like signal, `filtfilt`, SOS form | Clean a contaminated signal end-to-end; avoid the classic implementation pitfalls. |
