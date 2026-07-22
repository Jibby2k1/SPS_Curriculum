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

---

## Workshop 3 — Foundations of Signal Processing 2 *(available)*

Material: [`Foundations_of_Signal_Processing_2.ipynb`](./Foundations_of_Signal_Processing_2.ipynb)

| Session | Focus | Objectives |
|---|---|---|
| **S1 — The z-Transform & ROC** | Theory | ROC geometry, stability vs causality, inversion by residues. |
| **S2 — Multirate** | Application | Decimation/interpolation done honestly; aliasing & images demonstrated. |
| **S3 — Polyphase Structures** | Theory → Application | Never compute what you'll discard; equivalence verified to 1e-15. |
| **S4 — Wavelets, a First Meeting** | Application | Haar from scratch; blocks-signal compression bake-off vs Fourier. |

## Workshop 4 — Statistical Signal Processing *(available)*

Material: [`Statistical_Signal_Processing.ipynb`](./Statistical_Signal_Processing.ipynb)

| Session | Focus | Objectives |
|---|---|---|
| **S1 — Random Processes & Stationarity** | Theory | WSS, autocorrelation, ergodicity. |
| **S2 — The PSD** | Theory → Application | Wiener–Khinchin; why the periodogram lies and Welch converges. |
| **S3 — The Wiener Filter, Derived** | Theory → Application | Wiener–Hopf, orthogonality; a working PSD-only denoiser. |
| **S4 — Matched Filters & Detection** | Application | Neyman–Pearson, ROC curves; matched filter dominates measured. |

## Workshop 5 — Array Processing & Beamforming *(available)*

Material: [`Array_Processing.ipynb`](./Array_Processing.ipynb)

| Session | Focus | Objectives |
|---|---|---|
| **S1 — The Array Manifold** | Theory | Direction as spatial frequency; grating lobes as spatial aliasing. |
| **S2 — Delay-and-Sum & MVDR** | Application | MVDR digs an interferer null by itself (+11 dB SINR measured). |
| **S3 — Subspace Methods: MUSIC** | Theory → Application | Eigen-subspaces resolve sources 8° apart. |

## Workshop 6 — Audio & Speech DSP *(available)*

Material: [`Audio_Speech_DSP.ipynb`](./Audio_Speech_DSP.ipynb)

| Session | Focus | Objectives |
|---|---|---|
| **S1 — Reading Spectrograms** | Application | Sight-read tones, harmonics, percussion, chirps. |
| **S2 — Speech: Source-Filter** | Theory → Application | Synthesize vowels; estimate pitch & formants (LPC) back. |
| **S3 — Effects Are Filters** | Application | Reverb, robot voice, pitch shift as DSP primitives. |

## Workshop 7 — Image Processing as 2-D DSP *(available)*

Material: [`Image_Processing.ipynb`](./Image_Processing.ipynb)

| Session | Focus | Objectives |
|---|---|---|
| **S1 — 2-D Convolution & Spectra** | Theory → Application | Plane waves, reading 2-D spectra. |
| **S2 — Sampling, Aliasing & Moiré** | Application | Zone-plate moiré; anti-alias before subsampling. |
| **S3 — Edges → Learned Features** | Application | Sobel, unsharp masking, the straight line to CNNs. |

## Workshop 8 — Compressed Sensing *(available)*

Material: [`Compressed_Sensing.ipynb`](./Compressed_Sensing.ipynb)

| Session | Focus | Objectives |
|---|---|---|
| **S1 — Why Undersampling Can Work** | Theory | Sparsity + incoherence + the L1 diamond geometry. |
| **S2 — Reconstruction Lab** | Application | ISTA from scratch: exact support recovery from 15% of samples (25.8 dB vs L2's 0.8 dB). |

## Workshop 9 — Digital Communications *(available)*

Material: [`Digital_Communications.ipynb`](./Digital_Communications.ipynb)

| Session | Focus | Objectives |
|---|---|---|
| **S1 — Modulation** | Theory → Application | Constellations; the energy/rate trade at fixed SNR. |
| **S2 — Pulse Shaping & Eye Diagrams** | Application | RRC link, matched filter, reading the eye. |
| **S3 — Synchronization** | Application | One preamble correlation finds frame AND phase (0 errors after sync). |
| **S4 — OFDM in 40 Minutes** | Application | IFFT modem + cyclic prefix: equalization becomes division. |

## Workshop 10 — Real-Time Signal Processing *(available)*

Material: [`Real_Time_DSP.ipynb`](./Real_Time_DSP.ipynb) — the workshop Intro_GPU promised.

| Session | Focus | Objectives |
|---|---|---|
| **S1 — Fixed-Point Arithmetic** | Theory → Application | Q-format, 6 dB/bit measured, the overflow trap demonstrated. |
| **S2 — Latency Budgets** | Application | Latency ≥ one block; compute < one block-duration; measured deadlines. |
| **S3 — A Real-Time Pipeline** | Application | Threaded producer/consumer with headroom histograms and miss counts. |


---

# Ring 2 Workshops *(2026)*

## Workshop 11 — Graph Signal Processing & GNNs *(available)*

Material: [`Graph_Signal_Processing.ipynb`](./Graph_Signal_Processing.ipynb)

| Session | Objectives |
|---|---|
| **S1 — Laplacian & Graph Fourier** | Graph harmonics; ring graph reduces to the DFT (1e-15). |
| **S2 — Filtering on Graphs** | Spectral & polynomial (local) filters; sensor-field denoising. |
| **S3 — Sampling on Graphs** | Bandlimited recovery from K nodes, exact; graph aliasing shown. |
| **S4 — Message Passing = Learned Filters** | GCN from scratch: 10 labels → 89% of 80 nodes; MLP ablation 41%. |

## Workshop 12 — Channel Coding *(available)*

Material: [`Channel_Coding.ipynb`](./Channel_Coding.ipynb)

| Session | Objectives |
|---|---|
| **S1 — Hamming** | Syndrome decoding; all 112 single-error cases corrected, exhaustively. |
| **S2 — Convolutional + Viterbi** | Trellis DP == brute-force ML decode, verified. |
| **S3 — LDPC & Polar at a Glance** | Survey session: belief propagation, polarization, the map. |

## Workshop 13 — Sparse Coding & Dictionary Learning *(available)*

Material: [`Sparse_Dictionary_Learning.ipynb`](./Sparse_Dictionary_Learning.ipynb)

| Session | Objectives |
|---|---|
| **S1 — OMP** | Planted support recovered exactly; the sparsity cliff mapped. |
| **S2 — K-SVD** | 20/20 planted atoms recovered (|cos|>0.98). |
| **S3 — Denoising with Learned Atoms** | Learned dictionary +2.5 dB where DCT loses ground. |

## Workshop 14 — Blind Source Separation & ICA *(available)*

Material: [`ICA_Blind_Source_Separation.ipynb`](./ICA_Blind_Source_Separation.ipynb)

| Session | Objectives |
|---|---|
| **S1 — Why Correlation Isn't Enough** | Whitening reaches a rotation and goes silent. |
| **S2 — FastICA** | Unmix 3 sources blind: |corr| ≥ 0.999 vs planted truth. |
| **S3 — Limits & Practice** | Gaussian unidentifiability demonstrated; field guide. |

## Workshop 15 — Time–Frequency II *(available)*

Material: [`Time_Frequency_2.ipynb`](./Time_Frequency_2.ipynb)

| Session | Objectives |
|---|---|
| **S1 — Wigner–Ville** | Razor concentration and its cross-term ghosts, both shown. |
| **S2 — Synchrosqueezing** | Ridge width 9.1 Hz → one bin, no ghosts. |
| **S3 — EMD** | Planted fast/slow/trend recovered at |corr| = 1.000. |

## Workshop 16 — Cyclostationarity & HOS *(available)*

Material: [`Cyclostationary_HOS.ipynb`](./Cyclostationary_HOS.ipynb)

| Session | Objectives |
|---|---|
| **S1 — Cyclic Statistics** | BPSK's spikes at symbol rate and 2f_c. |
| **S2 — Detection Below the Floor** | Under level uncertainty: energy 0.8σ vs cyclic 8.8σ at −10 dB. |
| **S3 — Higher-Order Statistics** | Bicoherence 0.98 vs 0.11: phase coupling the PSD can't see. |

## Workshop 17 — Radar Signal Processing *(available)*

Material: [`Radar_Signal_Processing.ipynb`](./Radar_Signal_Processing.ipynb)

| Session | Objectives |
|---|---|
| **S1 — Pulse Compression** | 30 m resolution from a 3 km pulse; both targets recovered exactly. |
| **S2 — Doppler** | Range-Doppler map; both movers extracted to planted R and v. |
| **S3 — CFAR** | 1 false alarm vs 109 across a 9× noise step. |
| **S4 — SAR at a Glance** | A flown 205 m aperture resolves ±40 m scatterers. |

## Workshop 18 — MIMO Communications *(available)*

Material: [`MIMO_Communications.ipynb`](./MIMO_Communications.ipynb)

| Session | Objectives |
|---|---|
| **S1 — Capacity** | log-det scaling ~linear in antennas, simulated. |
| **S2 — Diversity** | BER slopes steepen with branches (MRC). |
| **S3 — SVD Precoding** | UᴴHV = diag(σ) at 1e-15; verified-independent pipes; water-filling +23% at low SNR. |

## Workshop 19 — Sigma-Delta & Quantization *(available)*

Material: [`Sigma_Delta_Quantization.ipynb`](./Sigma_Delta_Quantization.ipynb)

| Session | Objectives |
|---|---|
| **S1 — Quantization Noise** | 6 dB/bit and +3 dB/octave, measured. |
| **S2 — Noise Shaping** | 1 bit → 11.3 effective bits at 64×, second-order loop. |


