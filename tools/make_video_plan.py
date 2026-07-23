#!/usr/bin/env python3
"""Generate VIDEO_PLAN.md from the 🕐 session markers inside the notebooks.

The notebooks are the single source of truth: this script parses every
`### 🕐 Session i of N — *Title* (~MM min)` marker and emits the recording plan
(playlists = topics, videos = sessions, titles per RECORDING.md's convention).

Run from the repository root:  python tools/make_video_plan.py
"""
import glob
import json
import os
import re
from collections import defaultdict

MARKER = re.compile(r"### 🕐 Session (\d+) of (\d+) — \*(.+?)\* \(~(\d+) min\)")

TOPIC_NAMES = {
    "Intro_Math": "Mathematics", "Intro_Programming": "Programming",
    "Intro_Host_Prog": "Host Programming", "Intro_DSP": "DSP",
    "Intro_GPU": "GPU Systems", "Intro_FPGA": "FPGA",
    "Intro_Time_Series": "Time Series", "Intro_Mach_Learn": "Machine Learning",
    "Intro_DL_4_Physics": "DL for Physics", "Intro_SDR": "SDR",
    "Intro_Quantum": "Quantum", "Capstone": "Capstone",
}

def workshop_title(nb):
    for c in nb["cells"][:6]:
        if c["cell_type"] == "markdown":
            for line in "".join(c["source"]).split("\n"):
                if line.startswith("# "):
                    return line[2:].strip()
    return "(untitled)"

def is_draft(nb):
    head = "".join("".join(c["source"]) for c in nb["cells"][:5])
    return "⚠️" in head

def main():
    topics = defaultdict(list)
    for path in sorted(glob.glob("**/*.ipynb", recursive=True)):
        base = os.path.basename(path)
        if any(t in base for t in ("blank", "_sum25", "_fall25", "_summer25")):
            continue
        nb = json.load(open(path, encoding="utf-8"))
        sessions = []
        for c in nb["cells"]:
            if c["cell_type"] != "markdown":
                continue
            m = MARKER.search("".join(c["source"]))
            if m:
                sessions.append((int(m.group(1)), int(m.group(2)), m.group(3), int(m.group(4))))
        topic = path.split(os.sep)[0]
        topics[topic].append((path, workshop_title(nb), is_draft(nb), sorted(sessions)))

    total_videos = total_min = n_draft = 0
    lines = [
        "# Video Plan",
        "",
        "> **Generated file — do not edit by hand.** Regenerate with `python tools/make_video_plan.py`",
        "> after changing any 🕐 session marker. One session = one video; one topic = one playlist.",
        "> Title convention and per-video structure: [RECORDING.md](./RECORDING.md).",
        "> 📝 workshops are **not recorded** until their in-notebook ⚠️ banner is cleared.",
        "",
    ]
    body = []
    for topic in TOPIC_NAMES:
        if topic not in topics:
            continue
        tname = TOPIC_NAMES[topic]
        body.append(f"\n## Playlist: SPS · {tname}\n")
        for path, wtitle, draft, sessions in topics[topic]:
            tag = " 📝 *(draft — do not record yet)*" if draft else ""
            body.append(f"**{wtitle}**{tag} — [`{path}`](./{path})\n")
            if not sessions:
                body.append("- *(no session markers found — add them before recording)*\n")
                continue
            body.append("| # | Video title | ~min |\n|---|---|---|\n")
            for i, n_tot, title, mins in sessions:
                body.append(f"| {i}/{n_tot} | SPS · {tname} · S{i} — {title} | {mins} |\n")
                if not draft:
                    total_videos += 1
                    total_min += mins
                else:
                    n_draft += 1
            body.append("\n")

    lines.append(f"**Recordable now: {total_videos} videos ≈ {total_min/60:.0f} hours of content.** "
                 f"({n_draft} more sessions unlock as 📝 banners are cleared.)")
    lines.append("")
    open("VIDEO_PLAN.md", "w", encoding="utf-8").write("\n".join(lines) + "".join(body))
    print(f"VIDEO_PLAN.md written: {total_videos} recordable videos (~{total_min/60:.0f} h), "
          f"{n_draft} draft sessions pending review")

if __name__ == "__main__":
    main()
