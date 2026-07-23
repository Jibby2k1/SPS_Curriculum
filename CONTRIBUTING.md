# Contributing

Thanks for helping build the SPS Curriculum. The bar is simple: **concise, intuition-first,
verified** — and everything below exists to make hitting it easy.

## The workflow

1. Fork, branch (`git switch -c add-my-workshop`) — the
   [Git workshop](./Intro_Host_Prog/Intro_Git/Intro_Git.ipynb) walks this exact loop.
2. Set up the verified environment: `pip install -r requirements.txt`.
3. Write your workshop following the [**Style Guide**](./STYLE_GUIDE.md):
   30–40 min 🕐 session markers, 💡 intuition before rigor, cross-references, Where-next.
4. **Verify before you PR** (this is the house discipline):
   - your notebook runs top-to-bottom on a fresh kernel:
     `python tools/validate.py --execute path/to/Your_Workshop.ipynb`
   - key numerical claims are checked against an **independent oracle** — something you did
     *not* hand-derive (a closed form, a reference solver, a planted ground truth, an
     exhaustive brute force). If a demo's numbers contradict its prose, fix the experiment
     or the prose — never ship them disagreeing.
   - links & anchors resolve repo-wide: `python tools/validate.py`
5. Add your workshop to the topic README's session table and the root README table
   (✅ if executed clean; 📝 with an in-notebook ⚠️ banner if it needs hardware or an
   expert proof-read you can't provide).
6. Open the PR. A reviewer will run the same two commands.

## What makes a good first contribution

- **Clear a 📝 banner**: run a draft workshop on the hardware it needs (GPU, RTL-SDR,
  MATLAB, a microcontroller), fix what breaks, remove the banner.
- **Record a session**: the [Recording guide](./RECORDING.md) maps notebooks → videos.
- **Generate/refresh student blanks** for a teaching term (see existing `*_blank_*` files).
- Improve an intuition cell that didn't land for you — you are the target audience.

## Ground rules

- Notebooks are the unit of content; keep outputs committed (they're the safety net for
  live demos and the evidence of verification).
- Don't commit data files, virtualenvs, or build artifacts.
- Session markers, README tables, and [VIDEO_PLAN.md](./VIDEO_PLAN.md) must agree —
  the plan is *generated* from the markers (`python tools/make_video_plan.py`), so edit
  markers, then regenerate.
