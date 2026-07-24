#!/usr/bin/env python3
"""Refresh student blanks from their teaching notebooks.

Run from the repository root:  python tools/sync_blanks.py [--apply] [PATTERN]

Blanks (`X_blank_<term><yy>.ipynb`) are hand-made copies of `X.ipynb` with the
teaching code cells emptied down to a comment header and `# YOUR CODE HERE`. That
makes their *prose* a duplicate of the parent's, which drifts every time a notebook
is revised — students then read last term's narration.

This tool re-derives each blank from its parent:

  markdown cells  <- copied from the parent, except 🎓 teacher-note blocks, which are
                     instructor-only and never ship to students
  code cells      <- taken from the existing blank, untouched, in order

So the editorial decision of *which* cells students fill in stays where it belongs —
in the blank — while the narration always matches the notebook it came from.

Cells are matched positionally, which is only sound when both files hold the same
number of code cells. A pair that fails that check is skipped and reported rather
than guessed at; fix it by hand, then re-run.

Default is a dry run. Pass --apply to write.
"""
import argparse
import glob
import json
import os
import re
import sys

TEACHER_NOTE = "🎓"

def parent_of(blank_path):
    p = re.sub(r"_blank_[A-Za-z0-9]+\.ipynb$", ".ipynb", blank_path)
    return p if p != blank_path and os.path.exists(p) else None

def pairs(pattern=None):
    out = []
    for b in sorted(glob.glob("**/*blank*.ipynb", recursive=True)):
        if pattern and pattern not in b:
            continue
        p = parent_of(b)
        if p:
            out.append((p, b))
    return out

def is_teacher_note(cell):
    return cell["cell_type"] == "markdown" and TEACHER_NOTE in "".join(cell["source"])

def rebuild(parent_cells, blank_cells):
    """Parent's structure, parent's prose, blank's code. None if unalignable."""
    blank_code = [c for c in blank_cells if c["cell_type"] == "code"]
    parent_code = [c for c in parent_cells if c["cell_type"] == "code"]
    if len(blank_code) != len(parent_code):
        return None
    out, i = [], 0
    for cell in parent_cells:
        if cell["cell_type"] == "code":
            out.append(blank_code[i])
            i += 1
        elif not is_teacher_note(cell):
            out.append(cell)
    return out

def words(cells):
    return sum(len("".join(c["source"]).split())
               for c in cells if c["cell_type"] == "markdown")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pattern", nargs="?", help="only sync blanks whose path contains this")
    ap.add_argument("--apply", action="store_true", help="write the files (default: dry run)")
    args = ap.parse_args()

    if not os.path.exists("README.md"):
        sys.exit("run from the repository root")

    changed = skipped = 0
    for parent, blank in pairs(args.pattern):
        pnb = json.load(open(parent, encoding="utf-8"))
        bnb = json.load(open(blank, encoding="utf-8"))
        rebuilt = rebuild(pnb["cells"], bnb["cells"])
        if rebuilt is None:
            pc = sum(1 for c in pnb["cells"] if c["cell_type"] == "code")
            bc = sum(1 for c in bnb["cells"] if c["cell_type"] == "code")
            print(f"SKIP  {blank}  ({pc} code cells in parent, {bc} in blank — align by hand)")
            skipped += 1
            continue
        if rebuilt == bnb["cells"]:
            continue
        before, after = words(bnb["cells"]), words(rebuilt)
        print(f"SYNC  {blank}  {before} -> {after} words")
        changed += 1
        if args.apply:
            bnb["cells"] = rebuilt
            with open(blank, "w", encoding="utf-8") as fh:
                json.dump(bnb, fh, indent=1, ensure_ascii=False)
                fh.write("\n")

    verb = "synced" if args.apply else "would sync (dry run — pass --apply)"
    print(f"\n{changed} blank(s) {verb}, {skipped} skipped")
    return 0

if __name__ == "__main__":
    sys.exit(main())
