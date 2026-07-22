# Introduction to Machine Learning

Theory-and-practice track on learning from data: from single neurons to scaling laws.
The transformer workshop already exists in
[Deep Learning for Physics](../Intro_DL_4_Physics/README.md#workshop-2--introduction-to-transformers-available).

**Prerequisites:** [Intro to Python](../Intro_Programming/README.md#workshop-2--introduction-to-python-available);
[Random Variables & Independence](../Intro_Math/Analysis/README.md) for the probability
underpinnings.

---

## Workshop 1 — Artificial Neural Networks *(available)*

Material: [`Intro_ANN/Intro_ANN.ipynb`](./Intro_ANN/Intro_ANN.ipynb) — from scratch in NumPy, every gradient by hand.

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — From Neuron to Network** | Theory | §2: the spiral dataset, activations, why nonlinearity is non-negotiable | Understand what stacking + folding buys. |
| **S2 — Backpropagation** | Theory → Application | §3: chain-rule derivation, implementation, gradient checking | Derive and *verify* every gradient. |
| **S3 — Training the Network** | Application | §4: full training loop, decision-boundary visualization | Train to 100% on the spiral; run the width/nonlinearity/learning-rate experiments. |

## Workshop 2 — Convolutional Neural Networks *(available)*

Material: [`Intro_CNN/Intro_CNN.ipynb`](./Intro_CNN/Intro_CNN.ipynb)

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — Convolution as a Learned Filter Bank** | Theory | §2: the CNN↔DSP dictionary, hand-made edge detector | Map conv/pool/stride/receptive field onto [DSP](../Intro_DSP/README.md) concepts. |
| **S2 — Train a CNN on Spectrograms** | Application | §3: chirp/tone/noise classification, kernel & feature-map visualization | Train a classifier and *open the hood* on what it learned. |

## Workshop 3 — Scaling Neural Networks *(available)*

Material: [`Scale_NN/Scale_NN.ipynb`](./Scale_NN/Scale_NN.ipynb) — all benchmarks CPU-runnable; GPU-scale tools covered as a map.

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — Why Scale? Accounting & Scaling Laws** | Theory → Application | §2–§3: param/FLOP counting, a laptop-scale scaling study | Count before optimizing; watch loss power-law onto the noise floor. |
| **S2 — Making Training Fast** | Application | §4–§7: throughput-vs-batch knee, profiler, gradient accumulation (proved exact), GPU toolbox map | Find the binding constraint; spend the cheap resource ([GPU systems](../Intro_GPU/README.md)). |

## Workshop 4 — Transformers *(available — hosted in DL for Physics by design)*

[Deep Learning for Physics](../Intro_DL_4_Physics/README.md) is the curriculum's applied-DL
home: hands-on PyTorch workshops with student blank versions. This ML track owns the *theory*
(ANN → CNN → Scaling); the applied transformer sessions live there on purpose.

See [`Intro_DL_4_Physics/intro_transformers`](../Intro_DL_4_Physics/intro_transformers/intro_transformers.ipynb)
and its [session breakdown](../Intro_DL_4_Physics/README.md#workshop-2--introduction-to-transformers-available).

## Workshop 5 — Training Dynamics *(available)*

Material: [`Training_Dynamics.ipynb`](./Training_Dynamics.ipynb)

| Session | Focus | Objectives |
|---|---|---|
| **S1 — Optimizers** | Theory → Application | SGD → momentum → Adam, raced fairly on one testbed. |
| **S2 — Schedules & Warmup** | Application | Cosine + warmup, with an honest small-task reading. |
| **S3 — Regularization** | Application | Weight decay, dropout, early stopping; watch the val-gap yawn. |

## Workshop 6 — LLMs from the Ground Up *(available)*

Material: [`LLMs_from_the_Ground_Up.ipynb`](./LLMs_from_the_Ground_Up.ipynb)

| Session | Focus | Objectives |
|---|---|---|
| **S1 — Tokens & Embeddings** | Theory → Application | Char vocab + a working mini-BPE. |
| **S2 — Pretraining** | Application | Train a nano-GPT to 0.07 nats (vs 2.76 unigram); sample coherent text. |
| **S3 — Finetuning & Alignment** | Theory → Application | SFT in miniature — voice change + catastrophic forgetting, live. |
| **S4 — Inference** | Application | Temperature/top-k; measure the quadratic cost the KV cache kills. |

## Workshop 7 — Representation Learning *(available)*

Material: [`Representation_Learning.ipynb`](./Representation_Learning.ipynb)

| Session | Focus | Objectives |
|---|---|---|
| **S1 — Autoencoders** | Application | 2-D bottleneck audited against the true generative factors. |
| **S2 — VAEs** | Theory → Application | KL glue; decode a latent grid into novel signals. |
| **S3 — Contrastive Learning** | Application | InfoNCE; invariance as a design choice. |

## Workshop 8 — Diffusion Models *(available)*

Material: [`Diffusion_Models.ipynb`](./Diffusion_Models.ipynb)

| Session | Focus | Objectives |
|---|---|---|
| **S1 — Forward Process & Denoising** | Theory → Application | Noise schedules; train the ε-predictor. |
| **S2 — Sampling** | Application | Noise crystallizes into two moons; stats verified against data. |

## Workshop 9 — Kernel Methods & RKHS *(available)*

Material: [`Kernel_Methods.ipynb`](./Kernel_Methods.ipynb)

| Session | Focus | Objectives |
|---|---|---|
| **S1 — The Kernel Trick** | Theory → Application | Representer theorem; kernel ridge in one solve. |
| **S2 — Gaussian Processes** | Application | Closed-form error bars, calibration audited (92% in ±2σ). |
| **S3 — KLMS** | Application | LMS in the RKHS beats any linear filter on a nonlinear system. |

## Workshop 10 — Model Compression & Edge AI *(available)*

Material: [`Model_Compression.ipynb`](./Model_Compression.ipynb)

| Session | Focus | Objectives |
|---|---|---|
| **S1 — Quantization** | Application | int8/int4 free, int2 collapses — measured, and tied to FPGA Q-format. |
| **S2 — Pruning** | Application | 95% pruned: 92% → 97% after fine-tune. |
| **S3 — Distillation** | Application | 1.6k-param student learns more from the teacher than from labels. |

## Workshop 11 — Uncertainty in ML *(available)*

Material: [`Uncertainty_in_ML.ipynb`](./Uncertainty_in_ML.ipynb)

| Session | Focus | Objectives |
|---|---|---|
| **S1 — Calibration** | Application | Reliability diagrams, ECE, temperature scaling. |
| **S2 — Ensembles & OOD** | Application | Bootstrap ensembles flag some off-map regions — with honest area numbers on what still fools everything. |

Contributions welcome — see the [contribution guide](../README.md#contributing).
