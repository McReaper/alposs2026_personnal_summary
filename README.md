# AlpOSS 2026 — Personal Summary

Personal summary, notes, and opinions about the [AlpOSS 2026](https://alposs.fr/) conference, which took place in Échirolles on February 17th, 2026.

**Live site → [mcreaper.github.io/alposs2026_personnal_summary](https://mcreaper.github.io/alposs2026_personnal_summary/)**

> ⚠️ All content in `summaries/` and `slides/` was generated automatically by AI from audio transcriptions. It may contain errors or inaccuracies — always verify important information against the [official replays](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk).

## What's in this repo

| Path | Description |
|---|---|
| `build.py` | Static site generator — produces 3 HTML views from the data |
| `talks.json` | Talk metadata: attendance, personal notes, ESN relevance flags |
| `summaries/` | Full AI-generated summaries per talk (from audio transcriptions) |
| `slides/` | Condensed slide content per talk (used by the diaporama view) |
| `site/` | Generated HTML output (not committed — run `build.py` to generate) |

## The 3 sites

Running `python build.py` generates three static HTML pages in `site/`:

- **Site A** — List + detail view (sidebar navigation, full summaries)
- **Site B** — Card grid view (filterable by theme)
- **Site C** — Slideshow / diaporama (keyboard navigation, personal notes)

## Building

```bash
python build.py
# → site/a/index.html
# → site/b/index.html
# → site/c/index.html
```

No dependencies beyond the Python standard library. Fonts and JS libs are loaded from CDN.

## talks.json flags

Each talk entry carries:

| Field | Type | Description |
|---|---|---|
| `attended` | bool | Whether I was physically present |
| `personal_notes` | string | My personal take on the talk |
| `in_diapo` | bool | Whether the talk appears in the slideshow (site C) |
| `esn_highlight` | bool | Whether I consider this talk relevant for an ESN audience |

## License

GPL-3.0 — see [LICENSE](LICENSE).
