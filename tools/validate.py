#!/usr/bin/env python3
"""Repository validation battery for the SPS Curriculum.

Run from the repository root:  python tools/validate.py [--execute NOTEBOOK.ipynb]

Checks (fast, no execution):
  1. every relative link in .md and notebook markdown resolves to a real file
  2. every #anchor resolves against the target's headings (GitHub slug rules)
  3. no corrupted LaTeX escapes (raw control characters) in notebook markdown
  4. every draft-tier notebook (📝 in the root README) carries its ⚠️ banner
  5. every teaching notebook is linked from the root README table

Optionally (--execute): run one notebook top-to-bottom on a fresh kernel and
report any cell errors — the check every new/edited workshop must pass.

Exit code 0 = clean; 1 = problems found (CI-friendly).
"""
import argparse
import glob
import json
import os
import re
import sys

def slug(heading: str) -> str:
    h = re.sub(r"[^\w\s-]", "", heading.strip().lstrip("#").strip().lower())
    return re.sub(r"\s", "-", h)

def md_texts(path: str):
    if path.endswith(".ipynb"):
        nb = json.load(open(path, encoding="utf-8"))
        return ["".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "markdown"]
    return [open(path, encoding="utf-8").read()]

def collect_files():
    return sorted(glob.glob("**/*.md", recursive=True) + glob.glob("**/*.ipynb", recursive=True))

def check_links(files):
    heads, problems = {}, []
    for m in files:
        hs = set()
        for txt in md_texts(m):
            for line in txt.split("\n"):
                if re.match(r"#{1,6}\s", line.strip()):
                    hs.add(slug(line.strip()))
        heads[os.path.normpath(m)] = hs
    for md in files:
        for txt in md_texts(md):
            for path, anc in re.findall(r"\]\(([^)#\s]*)(#[^)]*)?\)", txt):
                if path.startswith(("http", "data:", "attachment:")) or path == "...":
                    continue
                p = os.path.normpath(os.path.join(os.path.dirname(md), path)) if path else os.path.normpath(md)
                if path and not os.path.exists(p):
                    problems.append(f"BROKEN FILE LINK  {md}: {path}")
                elif anc and p in heads and anc[1:] not in heads[p]:
                    problems.append(f"BROKEN ANCHOR     {md}: {path}{anc}")
    return problems

def check_control_chars(files):
    problems = []
    for f in files:
        if not f.endswith(".ipynb") or "blank" in f:
            continue
        nb = json.load(open(f, encoding="utf-8"))
        for i, c in enumerate(nb["cells"]):
            if c["cell_type"] != "markdown":
                continue
            bad = [ord(ch) for ch in "".join(c["source"]) if ord(ch) < 32 and ch not in "\n\t"]
            if bad:
                problems.append(f"CONTROL CHARS     {f} cell {i}: {bad[:6]} (corrupted LaTeX escape?)")
    return problems

def check_banners_and_index():
    problems = []
    readme = open("README.md", encoding="utf-8").read()
    # 4: every 📝 row's notebook must carry a ⚠️ banner near the top
    for m in re.finditer(r"\[([^\]]+)\]\((\./[^)#\s]+\.ipynb)\)[^|]*\|[^|]*\| 📝 Draft", readme):
        path = m.group(2)[2:]
        if not os.path.exists(path):
            continue  # caught by check_links
        nb = json.load(open(path, encoding="utf-8"))
        head = "".join("".join(c["source"]) for c in nb["cells"][:5])
        if "⚠️" not in head:
            problems.append(f"MISSING BANNER    {path} is 📝 in README but has no ⚠️ banner")
    # 5: every teaching notebook appears in the root README
    for nb_path in glob.glob("**/*.ipynb", recursive=True):
        base = os.path.basename(nb_path)
        if any(tag in base for tag in ("blank", "_sum25", "_fall25", "_summer25")):
            continue
        if nb_path not in readme and "./" + nb_path not in readme:
            problems.append(f"NOT IN README     {nb_path}")
    return problems

def execute_notebook(path):
    import nbformat
    from nbclient import NotebookClient
    nb = nbformat.read(path, as_version=4)
    NotebookClient(nb, timeout=900, kernel_name="python3").execute()
    errs = [o for c in nb.cells if c.cell_type == "code"
            for o in c.get("outputs", []) if o.get("output_type") == "error"]
    return errs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--execute", metavar="NOTEBOOK", help="also execute one notebook on a fresh kernel")
    args = ap.parse_args()

    if not os.path.exists("README.md"):
        sys.exit("run from the repository root")

    files = collect_files()
    problems = check_links(files) + check_control_chars(files) + check_banners_and_index()

    for p in problems:
        print(p)
    print(f"\n{len(files)} files scanned — {'CLEAN' if not problems else f'{len(problems)} problem(s)'}")

    if args.execute:
        print(f"\nexecuting {args.execute} ...")
        errs = execute_notebook(args.execute)
        if errs:
            for e in errs:
                print("CELL ERROR:", e.get("ename"), e.get("evalue"))
            problems.append("execution errors")
        else:
            print("executed clean, no cell errors")

    sys.exit(1 if problems else 0)

if __name__ == "__main__":
    main()
