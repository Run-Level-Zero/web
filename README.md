https://runlevelzero.se/

## Where the facts come from

The band's canonical facts – members and their periods, identifiers (Wikidata Q7379514,
MusicBrainz, Discogs, Spotify …), sources and press – live in the band's private admin repo,
`Run-Level-Zero/rlz-admin` (`identity.yaml`, `press/mentions.md`, `wikipedia.md`). Change a fact
there first, then here: the history, the discography, the reviews and the structured data
(the JSON-LD in `index.html`).

## Generated parts

`discography.html` (the tables) and the JSON-LD in `index.html` are generated – edit the data,
not the HTML between the `<!-- musicdata:… -->` markers:

```bash
# with tonsatz and rlz-admin cloned beside this repo
python3 -I build.py      # checks the data first; writes nothing if it disagrees
```
