# SPS Curriculum Style Guide

House rules for workshop notebooks. The goal: material that is **concise but friendly** —
rigor stays intact, but every hard idea gets its intuition spelled out *before* the
formalism. Sessions are sized for **30–40 minute** live meetings.

## Shared skeleton (all notebooks)

Every notebook, regardless of type, opens and closes the same way:

```
[MD] Content Produced by UF Signal Processing Society
     Authors: <names>
[MD] # <Workshop Title>
[MD] One-paragraph pitch: what you'll be able to do/understand afterward.
[MD] ### Acknowledgements            (optional)
[MD] ## 0. Introduction              — motivation first: why this topic exists
[MD] ## 1. Pre-requisites            — what to know, what to install, links to
                                       prerequisite workshops (relative links)
     ... numbered content sections ...
[MD] ## N. Conclusion                — recap + **Where next** links to related workshops
```

### Session markers

Partition the notebook in-place with a marker cell at each session boundary, matching
the session table in the topic README:

> ---
> ### 🕐 Session 2 of 6 — *Functions & Scope* (~35 min)
> **Goal:** write and declare functions; understand scope, lifetime, and recursion.
> **Builds on:** Session 1. &nbsp; **Feeds into:** Session 3 (pointers).
> ---

Keep the README session table and the in-notebook markers in sync.

### Intuition-first rule

Before every proof, derivation, or dense definition block, add a short plain-language
cell:

> 💡 **Intuition.** <2–5 sentences: what is really going on, what picture to hold in
> your head, why we should expect the result to be true.>

The rigorous cell that follows stays rigorous — the intuition cell is scaffolding, not a
replacement. Where a visual helper exists, the order is: intuition → visual → proof.

## Archetypes

Different content types are organized differently; only the skeleton above is shared.

### 📐 Theory notebooks (e.g. Analysis, DSP Foundations)

- Structure: Motivation → Definitions/Notation → Theorem/Proof sequence → payoff.
- Heading convention: `### Proof: <statement in math>` for each result.
- Each proof gets its 💡 intuition cell; add a runnable **Visual:** cell where a picture
  helps (number lines, spectra, convergence plots). Visual helpers live in one setup
  cell near the top, marked "safe to re-run anytime."
- End sections with a one-line "why we needed this" tying back to the motivation.

### 🛠️ Application notebooks (e.g. Intro_C, Intro_GPU, PyTorch)

- Structure: Motivation → Setup/Install → incremental build-up of one working system →
  benchmark/test it → conclusion.
- Every concept is introduced by *running something*: short code cell, then a markdown
  cell interpreting the output ("what just happened / why it matters").
- Prefer one running example that grows across sessions over many disconnected snippets.
- Include timings or measurable results where relevant; state that numbers vary by
  machine.
- Workshops taught live ship `*_blank_<term><yy>.ipynb` student versions with code cells
  emptied where students fill in.

### 📐+🛠️ Hybrid notebooks (e.g. adaptive filtering, ANN)

- Alternate: theory subsection (with intuition + derivation) → immediately apply it in
  code. Never more than two theory subsections without something runnable.

## Voice

- First-person plural, encouraging, informal but precise ("Let's see how...", "This is
  humbling but fun...").
- Concise: prefer one good sentence over three. Don't pad — friendliness comes from the
  intuition cells and ordering, not word count.
- Cross-reference generously: relative links to other workshops whenever a concept is
  taught elsewhere ("we proved this in [Basic Topology](...)").

## Checklist for a new or revised notebook

- [ ] Shared skeleton (attribution → title → pitch → §0 motivation → §1 prereqs → ... → conclusion)
- [ ] Session markers in-notebook, matching the topic README table
- [ ] 💡 intuition cell before every proof/derivation/dense definition
- [ ] Correct archetype layout (theory / application / hybrid)
- [ ] All code cells run top-to-bottom on a fresh kernel (note any GPU/hardware requirements)
- [ ] "Where next" links, and README links back to the notebook
