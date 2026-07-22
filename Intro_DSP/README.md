# Introduction to Digital Signal Processing

Theory-first treatment of signals, transforms, and fast algorithms, followed by an
application-focused series on filter design.

**Prerequisites:** comfort with calculus and complex numbers.
[Real Number Systems](../Intro_Math/Analysis/Real_Number_Systems.ipynb) and
[Basic Topology](../Intro_Math/Analysis/Basic_Topology.ipynb) are helpful but not required.
For the programming side, see [Intro to Python](../Intro_Func_Prog/README.md#workshop-2--introduction-to-python-planned).

---

## Workshop 1 — Foundations of Signal Processing *(available)*

Material: [`Foundations_of_Signal_Processing_1.ipynb`](./Foundations_of_Signal_Processing_1.ipynb)

The notebook is partitioned into six 30–40 minute sessions. Each session lists the
notebook sections it covers.

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — Why transforms?** | Theory | §0 Introduction, §1 Pre-requisites (Euler's $e$), §2.0 ($L_1 \subseteq L_2$, Hölder) | Motivate frequency-domain thinking; establish the function spaces we work in. |
| **S2 — The Laplace Transform** | Theory | §2.1 (history, DT & CT Laplace) | Define the Laplace transform in discrete and continuous time; see it as the parent of everything that follows. |
| **S3 — The Fourier Family** | Theory | §2.2.0–2.2.3 (DTFT, CTFT, DFT) | Derive the Fourier transforms as special cases of Laplace; relate the four transform flavors. |
| **S4 — Sampling & Uncertainty** | Theory | §2.2.4 Sampling Theorem, §2.3 Uncertainty Principle & STFT | State and interpret Nyquist–Shannon; understand time–frequency resolution trade-offs. |
| **S5 — The FFT** | Theory → Application | §2.4.1–2.4.2 (Radix-2 DIT & DIF) | Derive the butterfly; count operations; implement a radix-2 FFT. |
| **S6 — Fast Convolution** | Application | §2.4.3 (Overlap-Add, Overlap-Save) | Filter long/streaming signals with block convolution; benchmark against direct convolution. |

**Where next:** apply these transforms in
[Filter Design](#workshop-2--filter-design-planned) (application),
[Adaptive Filtering](../Intro_Time_Series/README.md) (time series), or accelerate them in
[Intro to GPU Systems](../Intro_GPU/README.md).

---

## Workshop 2 — Filter Design *(planned)*

Application-focused counterpart to Workshop 1. Planned sessions:

| Session | Focus | Planned content | Objectives |
|---|---|---|---|
| **S1 — FIR filters** | Application | Windowed-sinc design, linear phase, `scipy.signal.firwin` | Design and apply an FIR low-pass; read magnitude/phase responses. |
| **S2 — IIR filters** | Application | Butterworth/Chebyshev, bilinear transform, `scipy.signal.iirdesign` | Choose between FIR/IIR; understand stability from pole locations (ties back to Laplace, W1·S2). |
| **S3 — Filter implementation** | Application | Fixed-point effects, biquad cascades, real-time streaming | Implement a robust cascade filter on a real signal (audio or sensor data). |

Contributions welcome — see the [contribution guide](../README.md#contributing).
