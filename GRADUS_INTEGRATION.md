# SPS Curriculum ↔ Gradus Integration Plan

Connecting the **lab** (this repo: 87 executable, oracle-verified workshops) to the
**gym** (Gradus: concept-graph mastery with deterministic grading, `../Gradus`,
live at gradus-dc10e.web.app). The student loop we're building:

```
YouTube video ──► notebook lab (run it) ──► Gradus practice (prove it) ──► next session
      ▲                                                                        │
      └────────────────────────── mastery unlocks ◄────────────────────────────┘
```

## Verified groundwork (2026-07-22)

| Fact | Consequence |
|---|---|
| `dart`/`flutter` available on this machine | course generation can run here, agent-driven (`--manual-chat`) |
| Gradus catalog has **`signals_and_systems_full`** (12 Oppenheim-style chapters) | **do not duplicate** classical S&S; SPS DSP-foundations content *cross-links* to it |
| Gradus catalog has **`machine_learning_theory_placeholder`** | SPS ML track can **fill an existing placeholder** instead of forking a parallel course |
| Gradus pilot is **`rudin_pma`** | skip the SPS Analysis track for generation (already covered, deeper) |
| Deep-link URL format for courses/lessons | ❓ **verify** (`tool/serve_seo_preview.dart` implies SEO routes exist) — blocking Phase 1's Gradus-direction links |

## The content mapping (SPS notebook → Gradus lesson)

The reason this integration is unusually safe: the notebooks were authored *with
verification*, so Gradus generation from them is transcription, not invention.

| SPS structure | Gradus structure |
|---|---|
| Topic (e.g. `Intro_Time_Series/`) | course |
| Workshop notebook | chapter |
| 🕐 session | lesson |
| 💡 intuition cell | concept `body_markdown` (the voice Gradus concepts want) |
| Definitions/theorems/derivations | concepts (`type: definition/theorem/procedure`) |
| Cross-reference links | `prerequisites` / `neighbors` (the concept graph, pre-built) |
| **Oracle checks** (planted truths, closed forms, brute-force comparisons) | **deterministic item families** — exact/numeric answers, rule-gradable, no LLM grading. This is the crown jewel: e.g. "APA with K=4 on colored input converges faster than NLMS because ___", "the Kalman gain when P≫R approaches ___" |
| **Honest-failure demos** (MoE collapse, collider bias, Gaussian-ICA unidentifiability, the RNN losing to linear AR) | `common_confusions` + `non_examples` + author fail points — exactly what Gradus's diagnosis engine feeds on |
| Where-next links | transfer checks across lessons |

## Phases

### Phase 1 — Cross-linking (cheap, ships first)
- **SPS → Gradus:** add "🏋️ Practice on Gradus" to Where-next sections of workshops
  whose material has a live Gradus course (`signals_and_systems` for FoSP 1/2 + Filter
  Design; `rudin_pma` for the Analysis track).
- **Gradus → SPS:** add "🔬 Open the lab" links (GitHub/Colab notebook URLs) in the
  matching Gradus lesson markdown — lessons are markdown-bodied, so this is content-only.
- Blocked on: the deep-link format verification above.

### Phase 2 — Flagship course generation: **"Adaptive Filtering to Mamba"**
The SPS-distinctive course nobody else has, zero catalog collision. Source: the
Time Series track (APA → RLS → Kalman → Beyond-Kalman → ARIMA → RNN → SSM/Mamba →
Online Learning), 8 workshops / 20 sessions.

```bash
cd ../Gradus
dart run tool/generate_course.dart --manual-chat \
  --course-title "Adaptive Filtering to Mamba" \
  --primary-source "UF SPS Curriculum, Time Series track (github.com/Jibby2k1/SPS_Curriculum)" \
  --builder-profile general_textbook \
  --output-dir generated_courses/adaptive_filtering_to_mamba
```
Agent (Claude) answers the prompt files **from the notebooks**, per the mapping table.
- Acceptance: passes `tool/pilot_content_validator.dart`; every lesson links its lab
  notebook; ≥1 deterministic item family per concept sourced from an oracle check;
  publish via `tool/publish_course.dart` to the catalog.
- Success metric for the pipeline itself: hours-per-course; if acceptable, proceed.

### Phase 3 — Fill `machine_learning_theory_placeholder`
Regenerate that existing placeholder from the SPS ML track (ANN → Training Dynamics →
Kernel/RKHS → Concentration → RL → the frontier workshops). Merges SPS content into a
slot Gradus already reserved — no catalog sprawl.

### Phase 4 — Concept-graph export (tooling)
`tools/export_concept_graph.py` in this repo: parse 🕐 markers + Where-next links into
a curriculum-wide prerequisite JSON. Seeds Gradus chapter planning for all later
courses, and doubles as a dependency visualization for START_HERE.md.

### Phase 5 — Catalog completion + the flywheel
- Placeholder roadmaps (`--placeholder-course`) for remaining SPS-distinctive topics
  (Statistical SP / Radar-Comms bundle, GPU/Systems, Quantum) — browse-only until a
  generation pass.
- Steady state: **notebooks are the single source of truth**; a Gradus regeneration
  pass follows each substantive SPS content change; VIDEO_PLAN links land in Gradus
  lessons as videos publish (video → lab → practice, fully closed loop).

## Decisions made (with reasons)
1. **Flagship = Time Series track**, not DSP foundations — avoids `signals_and_systems`
   collision and is the most differentiated course in either product.
2. **Lessons link labs; labs link practice** — neither product absorbs the other; the
   notebook stays canonical.
3. **Items come from oracle checks first** — preserves Gradus's no-runtime-LLM-grading
   thesis with zero invented answers.

## Open questions (resolve before/while Phase 2)
- [ ] Deep-link URL scheme for a course/lesson in the web app
- [ ] Does `general_textbook` or a custom profile better fit lab-flavored engineering
      content? (Inspect one `signals_and_systems_full` lesson for tone before kickoff.)
- [ ] Publish policy: straight to production catalog vs. a beta/staging flag for the
      first SPS-derived course
- [ ] Attribution string for SPS-derived content inside Gradus lessons
