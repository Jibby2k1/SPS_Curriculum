# Introduction to Machine Learning

Theory-and-practice track on learning from data: from single neurons to scaling laws.
The transformer workshop already exists in
[Deep Learning for Physics](../Intro_DL_4_Physics/README.md#workshop-2--introduction-to-transformers-available).

**Prerequisites:** [Intro to Python](../Intro_Func_Prog/README.md#workshop-2--introduction-to-python-available);
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

## Workshop 3 — Scaling Neural Networks *(planned)*

| Session | Focus | Planned content |
|---|---|---|
| **S1 — Why scale?** | Theory | Scaling laws, compute/data/parameters trade-offs, batching and hardware utilization ([GPU systems](../Intro_GPU/README.md)). |
| **S2 — Scaling in practice** | Application | Mixed precision, data-parallel training, profiling a training loop. |

## Workshop 4 — Transformers *(available, hosted in DL for Physics)*

See [`Intro_DL_4_Physics/intro_transformers`](../Intro_DL_4_Physics/intro_transformers/intro_transformers.ipynb)
and its [session breakdown](../Intro_DL_4_Physics/README.md#workshop-2--introduction-to-transformers-available).

Contributions welcome — see the [contribution guide](../README.md#contributing).
