# SPS Curriculum Style Guide

House rules for workshop notebooks. The goal: material that is **concise but friendly** —
rigor stays intact, but every hard idea gets its intuition spelled out *before* the
formalism. Sessions are sized for **30–40 minute** live meetings.

## Shared skeleton (all notebooks)

Every notebook, regardless of type, opens and closes the same way:

```
[MD] [![Open in Colab](...)](https://colab.research.google.com/github/Jibby2k1/SPS_Curriculum/blob/main/<path to this file>)
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

**The Colab badge is the very first cell, before attribution.** It always points at *this exact
file's* path in `main` — copy-paste the badge markdown from any existing notebook and just swap
the path. `sync_blanks.py` copies it into blanks automatically (it's ordinary markdown, not a
🎓 teacher note), so a blank's badge opens the parent notebook in Colab — that's expected, not a
bug. Notebooks with no runnable code (Verilog/MATLAB/HLS drafts) still get the badge: it's free
one-click reading access even when there's nothing to execute.

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

### Debrief rule

Every code cell that *produces a result worth looking at* — a number, a plot, an oracle
check, a timing — is followed by a markdown cell that reads the output back to the
reader:

> **What just happened.** The learned score matches the closed-form one to cosine
> 0.998 — 'predict the noise' really was score estimation. The arrows disagree only far
> from the data, where no training samples ever landed.

Three sentences is plenty. Name the actual number, say what it proves, and — where the
result has a limitation — say where it breaks down. A student reading alone should never
meet an output they can't interpret.

Cells that only set up (imports, helper definitions, data loading) need no debrief; the
rule is about results, not lines of code.

### Teacher notes

Session markers and 💡 cells are what the instructor *says*. Teacher notes are how the
session is *run*, and they live in the main notebook — the `*_blank_*` student copies
omit them — inside a collapsed block so a student browsing the notebook sees a tidy page:

```html
<details>
<summary>🎓 <b>Teacher notes — §3 Langevin dynamics</b></summary>

**Timing:** ~12 min. Don't rush the noise term; it is the whole point of the section.

**Board first:** sketch the compass field by hand before running the cell — students who
see the arrows drawn never confuse the score with gradient descent on a loss.

**Misconception:** "score = ∇loss." It is the gradient of the *log-density*, taken with
respect to $x$, not the parameters. Ask someone to say aloud which variable we
differentiate.

**Ask the room:** "why inject noise at all?" — let them argue before you answer.

**If the demo misbehaves:** cosine below 0.9 usually means too few training steps; bump
to 5000 and keep talking while it runs.
</details>
```

One block per session at minimum, placed just after the 🕐 session marker; add
section-level blocks wherever a specific section is hard to deliver. Draw on the fields
that apply — don't pad a block to hit all of them:

- **Timing** — minutes for the section, and what to cut when running late.
- **Board first / analogy** — what to draw or say before any formalism appears.
- **Misconception** — the specific wrong idea students arrive with, and the question that
  surfaces it.
- **Ask the room** — a question to hand back to students instead of answering.
- **If the demo misbehaves** — the failure you should expect live, and the recovery.
- **Prereq check** — what to re-derive on the spot if the room looks lost.

Write them to a colleague who knows the subject but has never taught this session.

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
- Narration earns its place by carrying *information* — a number, a caveat, a reason, a
  connection to another workshop. A sentence that only restates the heading, or a teacher
  note that says "explain this clearly," is padding: cut it. When revising a thin
  notebook, the test is not "is it longer" but "can a student who missed the meeting
  follow it alone."

## Checklist for a new or revised notebook

- [ ] Colab badge as the first cell, linking to this file's own path
- [ ] Shared skeleton (attribution → title → pitch → §0 motivation → §1 prereqs → ... → conclusion)
- [ ] Session markers in-notebook, matching the topic README table
- [ ] 💡 intuition cell before every proof/derivation/dense definition
- [ ] Debrief cell after every result-producing code cell (names the actual number)
- [ ] 🎓 teacher-note block after every session marker (main notebook only, not blanks)
- [ ] Correct archetype layout (theory / application / hybrid)
- [ ] All code cells run top-to-bottom on a fresh kernel (note any GPU/hardware requirements)
- [ ] "Where next" links, and README links back to the notebook
