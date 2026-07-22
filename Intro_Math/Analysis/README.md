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

## 3. Numerical Sequences and Series *(planned)*

| Session | Focus | Planned content |
|---|---|---|
| **S1 — Sequences & convergence** | Theory | Convergent sequences, subsequences, Cauchy sequences, completeness of ℝ (uses compactness from Topology S2). |
| **S2 — Limits superior/inferior & special sequences** | Theory | limsup/liminf, monotone convergence, $e$ as a limit (feeds [DSP §1.0](../../Intro_DSP/README.md)). |
| **S3 — Series** | Theory | Comparison/root/ratio tests, power series, absolute convergence — groundwork for transforms as infinite sums. |

## 4. Measure Theory *(planned)*

| Session | Focus | Planned content |
|---|---|---|
| **S1 — σ-algebras & measures** | Theory | Motivation (non-measurable sets), σ-algebras, Borel sets, measure axioms. |
| **S2 — Lebesgue measure & integration** | Theory | Lebesgue vs Riemann, simple functions, convergence theorems (MCT/DCT). |
| **S3 — $L^p$ spaces** | Theory | $L^1, L^2, L^\infty$, Hölder & Minkowski — direct payoff in [DSP §2.0](../../Intro_DSP/README.md). |

## 5. Random Variables *(planned)*

| Session | Focus | Planned content |
|---|---|---|
| **S1 — Probability spaces** | Theory | Probability as a measure; random variables as measurable functions. |
| **S2 — Distributions & expectation** | Theory | CDFs, densities, expectation as Lebesgue integral, moments. |

## 6. Independence *(planned)*

| Session | Focus | Planned content |
|---|---|---|
| **S1 — Independence & product measures** | Theory | Independent events/σ-algebras/variables; Borel–Cantelli. |
| **S2 — Laws of large numbers** | Theory | WLLN/SLLN — the foundation for statistical learning ([Intro to ML](../../Intro_Mach_Learn/README.md)). |

---

**Where next:** the analysis track underpins
[Signal Processing Theory](../../Intro_DSP/README.md) (transforms live in $L^p$ spaces),
[Time Series](../../Intro_Time_Series/README.md) (stochastic processes), and
[Machine Learning](../../Intro_Mach_Learn/README.md) (probability & optimization).
