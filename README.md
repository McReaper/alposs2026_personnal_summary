# AlpOSS 2026 — Rapport de mission Kaizen

Résumé, notes et points de vue sur la conférence [AlpOSS 2026](https://alposs.fr/), qui s'est tenue à Échirolles le 17 février 2026. Produit par Victor Malod pour [Kaizen Solutions](https://kaizen-solutions.net/).

**Site en ligne → [victormalod.pages.forge.kaizen-solutions.net/alposs2026_personnal_summary](https://victormalod.pages.forge.kaizen-solutions.net/alposs2026_personnal_summary/)**

> ⚠️ Le contenu de `summaries/` et `slides/` a été généré automatiquement par IA à partir de transcriptions audio. Il peut contenir des erreurs — vérifiez toujours les informations importantes contre les [replays officiels](https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk).

## What's in this repo

| Path | Description |
|---|---|
| `build.py` | Static site generator — produces 3 HTML views from the data |
| `talks.json` | Talk metadata: attendance, personal notes, relevance flags |
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
| `esn_highlight` | bool | Whether I consider this talk relevant for Kaizen's clients and activity |

## License

GPL-3.0 — see [LICENSE](LICENSE).
