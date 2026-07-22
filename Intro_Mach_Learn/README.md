# Introduction to Machine Learning

Theory-and-practice track on learning from data: from single neurons to scaling laws.
The transformer workshop already exists in
[Deep Learning for Physics](../Intro_DL_4_Physics/README.md#workshop-2--introduction-to-transformers-available).

**Prerequisites:** [Intro to Python](../Intro_Func_Prog/README.md#workshop-2--introduction-to-python-planned);
[Random Variables & Independence](../Intro_Math/Analysis/README.md) for the probability
underpinnings.

---

## Workshop 1 — Artificial Neural Networks *(planned)*

| Session | Focus | Planned content |
|---|---|---|
| **S1 — From neuron to network** | Theory | Perceptron, activation functions, universal approximation intuition, loss surfaces. |
| **S2 — Backpropagation** | Theory | Chain rule on the computational graph; gradient descent variants. |
| **S3 — Train an MLP** | Application | NumPy-from-scratch MLP on a small dataset, then the same in PyTorch ([Intro to PyTorch](../Intro_DL_4_Physics/README.md)). |

## Workshop 2 — Convolutional Neural Networks *(planned)*

| Session | Focus | Planned content |
|---|---|---|
| **S1 — Convolution is a filter bank** | Theory | Convolution from [DSP](../Intro_DSP/README.md) → learned kernels; padding, stride, pooling, receptive fields. |
| **S2 — Train a CNN** | Application | Image/spectrogram classification in PyTorch; visualize learned filters. |

## Workshop 3 — Scaling Neural Networks *(planned)*

| Session | Focus | Planned content |
|---|---|---|
| **S1 — Why scale?** | Theory | Scaling laws, compute/data/parameters trade-offs, batching and hardware utilization ([GPU systems](../Intro_GPU/README.md)). |
| **S2 — Scaling in practice** | Application | Mixed precision, data-parallel training, profiling a training loop. |

## Workshop 4 — Transformers *(available, hosted in DL for Physics)*

See [`Intro_DL_4_Physics/intro_transformers`](../Intro_DL_4_Physics/intro_transformers/intro_transformers.ipynb)
and its [session breakdown](../Intro_DL_4_Physics/README.md#workshop-2--introduction-to-transformers-available).

Contributions welcome — see the [contribution guide](../README.md#contributing).
