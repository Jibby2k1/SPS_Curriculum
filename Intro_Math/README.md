# Introduction to Mathematics

The theory backbone of the curriculum. Currently one track:

| Track | Status | Description |
|---|---|---|
| [Analysis](./Analysis/README.md) | complete — 3 available + 3 drafts pending review | Real numbers → topology → sequences/series → measure → probability. Rudin-style rigor with interactive visuals. |

## New tracks *(2026)*

| Track | Status | Description |
|---|---|---|
| [Linear Algebra for Signals](./Linear_Algebra/Linear_Algebra.ipynb) | ✅ 5 sessions | Bases → projections/least squares → eigen → SVD → matrix calculus, always with a signal in hand. |
| [Optimization](./Optimization/Optimization.ipynb) | ✅ 4 sessions | Convexity, GD rates (κ!), Lagrange/KKT, SGD noise floors — the theory under every "fit". |
| [Estimation Theory](./Estimation_Theory/Estimation_Theory.ipynb) | ✅ 4 sessions | MLE, Cramér–Rao, Bayesian/MMSE, sufficiency — the missing link to Kalman & ML. |
| [Hilbert Spaces & Fourier, Properly](./Hilbert_Spaces/Hilbert_Spaces.ipynb) | 📝 3 sessions | Inner products, the projection theorem, Parseval as Pythagoras. |
| [Information Theory](./Information_Theory/Information_Theory.ipynb) | ✅ 4 sessions | Entropy, KL/cross-entropy, mutual information, capacity — with every quantity computed live. |
| [Complex Analysis Lite](./Complex_Analysis/Complex_Analysis_Lite.ipynb) | 📝 2 sessions | Poles, ROC, residues → inverse transforms, surgically extracted. |

📝 = draft pending instructor review (banner in notebook).

**Where next:** the math here pays off directly in
[Signal Processing](../Intro_DSP/README.md),
[Time Series](../Intro_Time_Series/README.md), and
[Machine Learning](../Intro_Mach_Learn/README.md).

## Ring 2 tracks *(2026)*

| Track | Status | Description |
|---|---|---|
| [Numerical Linear Algebra](./Numerical_Linear_Algebra/Numerical_Linear_Algebra.ipynb) | ✅ 4 | Conditioning (Läuchli!), QR vs Gram-Schmidt, CG at √κ, randomized SVD — all against LAPACK oracles. |
| [Concentration & Learning Theory](./Concentration/Concentration_Inequalities.ipynb) | 📝 4 | Chernoff → Hoeffding → McDiarmid → Rademacher; an honest generalization bound, computed. |
| [Stochastic Processes II](./Stochastic_Processes/Stochastic_Processes_2.ipynb) | 📝 4 | Conditional expectation as projection, martingales (no free lunch, simulated), Markov mixing = \|λ₂\|, Brownian (dB)²=dt. |
| [Convex Optimization II](./Optimization/Convex_Optimization_2.ipynb) | ✅ 3 | Certified duality gaps, prox/soft-threshold verified by brute force, ADMM == FISTA to 1e-14. |
| [Random Matrix Theory](./Random_Matrix_Theory/Random_Matrix_Theory.ipynb) | ✅ 3 | Semicircle, Marchenko–Pastur (edges verified), the BBP detection threshold. |
| [Manifold Optimization](./Optimization/Manifold_Optimization.ipynb) | ✅ 2 | Sphere/Stiefel descent converging to `eigh`'s answers natively. |
