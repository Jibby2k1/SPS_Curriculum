# Deep Learning for Physics

Application track — **the curriculum's applied-DL home**: build and train neural networks in
PyTorch on physics-flavored data (theory lives in [Intro to ML](../Intro_Mach_Learn/README.md)).
Each workshop ships a completed instructor notebook plus fill-in-the-blank student
versions (`*_blank_*.ipynb`) used in live sessions.

**Prerequisites:** [Intro to Python](../Intro_Programming/README.md#workshop-2--introduction-to-python-available).
[Intro to GPU Systems](../Intro_GPU/README.md) explains the hardware these models train on;
[Intro to ML](../Intro_Mach_Learn/README.md) covers the underlying theory.

---

## Workshop 1 — Introduction to PyTorch *(available)*

Material: [`intro_pytorch/intro_pytorch.ipynb`](./intro_pytorch/intro_pytorch.ipynb)
· student versions: [fall25](./intro_pytorch/intro_pytorch_blank_fall25.ipynb), [summer25](./intro_pytorch/intro_pytorch_blank_summer25.ipynb)

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — Tensors & Data** | Application | §0–2: tensors, indexing/slicing, vectorization, Datasets & Dataloaders | Manipulate tensors fluently; wrap a custom dataset in a Dataloader. |
| **S2 — Build & Train** | Application | §3–4 + testing: `nn.Module`, training loop, evaluation | Define a network, run the train/eval loop, inspect a saved model (`model.pth`). |

## Workshop 2 — Introduction to Transformers *(available)*

Material: [`intro_transformers/intro_transformers.ipynb`](./intro_transformers/intro_transformers.ipynb)
· student versions: [fall25](./intro_transformers/intro_transformers_blank_fall25.ipynb), [summer25](./intro_transformers/intro_transformers_blank_sum25.ipynb)

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — Attention & Data** | Theory → Application | §0–1: setup, data generation | Understand the attention mechanism; generate the training dataset. |
| **S2 — Build & Train a Transformer** | Application | §2–3 + testing | Assemble a transformer from PyTorch primitives; train and evaluate it. |

## Workshop 3 — Physics-Informed Neural Networks *(available)*

Material: [`PINNs.ipynb`](./PINNs.ipynb) — arguably this track's flagship.

| Session | Focus | Objectives |
|---|---|---|
| **S1 — The PDE-as-Loss Idea** | Theory → Application | Autograd w.r.t. inputs; solve an ODE with zero data (max err 6e-3). |
| **S2 — The Oscillator from 6 Points** | Application | Physics as a prior: RMSE 0.68 (plain) → 0.03 (PINN). |

**Where next:** sequence models from a signals perspective in
[Time Series → RNNs](../Intro_Time_Series/README.md); scaling questions in
[ML → Scaling Neural Networks](../Intro_Mach_Learn/README.md).
