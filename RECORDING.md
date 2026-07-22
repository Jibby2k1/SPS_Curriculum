# Recording Guide

House format for turning sessions into YouTube videos. **One session = one video**; one
topic README = one playlist. Everything below keeps videos in the 30–40 minute window.

## Video structure (mirrors the notebook)

| Segment | Length | Source in notebook |
|---|---|---|
| **Hook** | 30–60 s | The workshop pitch cell, or the session's most surprising demo result shown *first* |
| **Session card** | 15 s | The 🕐 session marker — read the goal, name the prereqs |
| **Intuition** | 3–5 min | The 💡 cells — deliver these *before* any formalism, verbatim spirit |
| **Rigor / build** | 15–25 min | The proof or live-coding cells, in notebook order |
| **Demo payoff** | 3–5 min | The executed cell whose output proves the point (race condition, spectrum peak, learning curve) |
| **Recap card** | 60 s | Session goal restated + "Where next" links as end-screen |

## Conventions

- **Title:** `SPS · <Track> · S<n> — <Session Title>` (e.g. `SPS · DSP · S7 — The FFT`).
- **Chapters:** the notebook's `##`/`###` headings inside the session become YouTube
  chapter timestamps — keep headings short for this reason.
- **Playlists** mirror topic READMEs; playlist description links the README.
- **Run everything live** from a fresh kernel; the committed outputs are your safety net
  if a live demo misbehaves ("here's what it produced earlier").
- **Draft-banner rule:** 📝 workshops are not recorded until an instructor clears the
  ⚠️ banner.
- **Slides are optional** — the notebook *is* the visual. Zoom the font
  (`Ctrl/Cmd +` twice), hide the toolbar, use a dark or light theme consistently per
  track.

## Recording checklist

- [ ] Fresh kernel, all cells pre-run once (warm caches, download datasets)
- [ ] Session fits 30–40 min in a dry run — if not, split the session in the notebook
      *first* (update marker + README), never speed-talk
- [ ] Mic check with a spectrogram — we teach DSP; our audio should survive our own tools
- [ ] End screen: "Where next" links → next video in playlist
