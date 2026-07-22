# Analysis

Theory track: rigorous foundations for everything else in the curriculum — the real
numbers, topology, convergence, measure, and probability. Follows the spirit of Rudin's
*Principles of Mathematical Analysis* with interactive visuals.

Consume the material in this order:

1. Real Number Systems
2. Basic Topology
3. Numerical Sequences and Series
4. Measure Theory
5. Random Variables
6. Independence

Each notebook is partitioned into 30–40 minute sessions below.

---

## 1. Real Number Systems *(available)*

Material: [`Real_Number_Systems.ipynb`](./Real_Number_Systems.ipynb)

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — Why ℝ exists** | Theory | Motivation, $\sqrt{2}\notin\mathbb{Q}$, no max/min of rational cuts, notation, Ordered Sets | See the holes in ℚ; define suprema/infima and the least-upper-bound property. |
| **S2 — Fields & the Real Field** | Theory | Fields, The Real Field, Archimedean property, density of ℚ and of irrationals | Build ℝ axiomatically; prove the Archimedean property and density theorems. |

## 2. Basic Topology *(available)*

Material: [`Basic_Topology.ipynb`](./Basic_Topology.ipynb)

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — Cardinality & Metric Spaces** | Theory | Finite/Countable/Uncountable Sets, Metric Spaces (definitions, open/closed sets, relative openness) | Distinguish countable from uncountable; work with neighborhoods, limit points, open/closed sets. |
| **S2 — Compactness** | Theory | Compact Sets (all proofs through Heine–Borel) | Prove the core compactness theorems; understand why compactness is "the next best thing to finiteness." |
| **S3 — Perfect & Connected Sets** | Theory | Perfect Sets, the Cantor Set, Connected Sets | Construct the Cantor set; characterize connected subsets of ℝ. |

## 3. Numerical Sequences and Series *(available)*

Material: [`Numerical_Sequences_and_Series.ipynb`](./Numerical_Sequences_and_Series.ipynb)

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — Sequences & Convergence** | Theory | Convergent sequences, subsequences, Cauchy sequences | Play the ε–N game; prove uniqueness/boundedness; completeness of ℝ via Bolzano–Weierstrass. |
| **S2 — Monotone Sequences, limsup & $e$** | Theory | Monotone convergence, limsup/liminf, $e$ as a limit | Prove convergence without knowing the limit; construct $e$ (feeds [DSP §1.0](../../Intro_DSP/README.md)). |
| **S3 — Series** | Theory | Cauchy criterion, geometric/harmonic series, comparison/root/ratio tests | Interrogate infinite sums; radius of convergence — the $z$-transform's region of convergence. |

## 4. Measure Theory *(draft — pending review)*

Material: [`Measure_Theory.ipynb`](./Measure_Theory.ipynb)

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — σ-algebras & Measures** | Theory | Vitali motivation, σ-algebras, Borel sets, measure axioms, continuity | See why not everything is measurable; prove continuity from below. |
| **S2 — Lebesgue Measure & Integration** | Theory | Outer measure & Carathéodory, null sets, Cantor set, simple functions, MCT/Fatou/DCT | Build the integral; see the escaping-bump counterexample. |
| **S3 — $L^p$ Spaces** | Theory | Norms, Hölder proof via Young, $\ell^1 \subseteq \ell^2$ vs the line | Prove Hölder; cash it in for [DSP §2.0](../../Intro_DSP/README.md). |

## 5. Random Variables *(draft — pending review)*

Material: [`Random_Variables.ipynb`](./Random_Variables.ipynb)

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — Probability Spaces & Random Variables** | Theory | Probability as a measure; RVs as measurable functions; pushforward laws; CDF theorem | Prove the CDF's three properties from measure continuity. |
| **S2 — Distributions, Expectation & Moments** | Theory | Densities, LOTUS, Markov & Chebyshev proofs, sampling vs theory | One-line tail bounds; expectation as the Lebesgue integral. |

## 6. Independence *(draft — pending review)*

Material: [`Independence.ipynb`](./Independence.ipynb)

| Session | Focus | Notebook sections | Objectives |
|---|---|---|---|
| **S1 — Independence & Borel–Cantelli** | Theory | Independence for events/σ-algebras/RVs, product measures, both Borel–Cantelli proofs | The pairwise-vs-mutual trap; the zero–one dichotomy. |
| **S2 — Laws of Large Numbers** | Theory | WLLN via Chebyshev (full proof), SLLN statement, correlated-samples demo | Why averages converge — and what breaks without independence ([Intro to ML](../../Intro_Mach_Learn/README.md)). |

---

**Where next:** the analysis track underpins
[Signal Processing Theory](../../Intro_DSP/README.md) (transforms live in $L^p$ spaces),
[Time Series](../../Intro_Time_Series/README.md) (stochastic processes), and
[Machine Learning](../../Intro_Mach_Learn/README.md) (probability & optimization).
