#!/usr/bin/env python3
"""Generate the data-driven parts of runlevelzero.se from the music data.

  discography.html   the release tables      <- rlz-admin/discography.yaml
  index.html         the schema.org JSON-LD  <- rlz-admin/identity.yaml

Needs the repos cloned side by side: tonsatz (the tools) and rlz-admin (the data), e.g.
~/code/tonsatz, ~/code/rlz-admin, ~/code/runlevelzero.se – or set MUSICDATA_ROOT.
Run: python3 -I build.py  (checks first; writes nothing if the data disagrees). Commit the result.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get("MUSICDATA_ROOT") or os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "tonsatz", "tools"))
import musicdata  # noqa: E402

data = musicdata.load()
problems = musicdata.check(data)
if problems:
    print("musicdata problems – nothing written:", *problems, sep="\n - ")
    sys.exit(1)

for name, fn, block in [("discography.html", "discography", musicdata.rlz_discography_html(data)),
                        ("index.html", "jsonld", musicdata.jsonld_script(musicdata.band_jsonld(data), "  "))]:
    path = os.path.join(HERE, name)
    text = open(path, encoding="utf-8").read()
    new = musicdata.replace_block(text, fn, block)
    if new != text:
        open(path, "w", encoding="utf-8").write(new)
        print("wrote", name)
print(f"runlevelzero.se: {len(data['rlz']['releases'])} releases, {len(data['identity']['members'])} members; 0 problems")
