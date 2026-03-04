#!/usr/bin/env python3
"""AlpOSS 2026 — Static Site Generator (3 versions)"""
import json, os, re, html as _html

BASE   = os.path.dirname(os.path.abspath(__file__))
AVATAR = "https://avatars.githubusercontent.com/u/238774673"

DISCLAIMER = (
    '<div class="ai-disclaimer">'
    '⚠️ Contenu généré automatiquement par IA à partir des transcriptions audio — '
    'peut contenir des erreurs ou imprécisions. Vérifiez les informations importantes.'
    '</div>'
)
DISCLAIMER_CSS = (
    '.ai-disclaimer { position:fixed; bottom:0; left:0; right:0; z-index:9999; '
    'background:#7c3aed; color:#fff; font-size:11px; text-align:center; '
    'padding:6px 16px; letter-spacing:.2px; opacity:.92; }'
)

SLUGS = [
    # ── Conférences AlpOSS 2026 (originales) ──────────────────────────────────
    "comment-degafamiser-asso-climat", "adieu-windows-bonjour-libre",
    "approche-bottom-up-ngi",          "choisir-logiciel-libre",
    "chronique-journee-open-source",   "coopcircuits",
    "cyber-resilience-act",            "telephonie-digital-workplace",
    "inria-politiques-publiques",      "iam-openldap-active-directory",
    "openxchange-sitpi-claix",         "la-mouette",
    "les-gul",                         "licences-open-source",
    "linux-ecole-nird",                "logiciel-libre-noms-domaine",
    "openstreetmap-nazca",             "p16-ia-souveraine",
    "rag-mutualise-souverain",         "radios-libres",
    "sensibiliser-etudiants",          "mobilizon",
    "table-ronde-migrations",          "teemip",
    "tchap-collectivites",
    # ── Lightning talks (15 min) ───────────────────────────────────────────────
    "alternc-souverainete-donnees",    "vates-ecosystemes-ouverts",
    "postgresql-kubernetes-cloudnativepg", "migrer-messagerie-freins",
    "rag-ia-mutualisee-linagora",      "linux-mac-support-materiel",
    "xwiki-20-ans",                    "files2anywhere-nextcloud-pastell",
    "anct-suite-territoriale",         "lasuite-coop",
    "creme-crm",                       "itop-gestion-services-it",
    "hebergeur-kubernetes",
]

WORKSHOP_SLUGS = [
    "atelier-openrag",          # Donnez une voix à vos documents avec OpenRAG (Linagora)
    "atelier-jupyterhub-wod",   # JupyterHub opérationnel en 1h grâce à WoD (HPE)
    "atelier-openpgp-yubikey",  # OpenPGP avec YubiKey/NitroKey (foopgp / piseb)
    "atelier-silex-web",        # Web Design libre avec Silex (Internet 2000)
    "atelier-wikipedia",        # Wikipedia : comprendre les coulisses (Wikimédia)
    "atelier-rust-cli",         # Découvrir Rust en 2h — CLI de A à Z (Red Hat)
]

DURATIONS = {
    "comment-degafamiser-asso-climat": "6:26",  "adieu-windows-bonjour-libre": "20:44",
    "approche-bottom-up-ngi":          "6:11",  "choisir-logiciel-libre":      "19:33",
    "chronique-journee-open-source":   "6:42",  "coopcircuits":                "6:04",
    "cyber-resilience-act":            "19:45", "telephonie-digital-workplace": "20:18",
    "inria-politiques-publiques":      "6:04",  "iam-openldap-active-directory":"20:43",
    "openxchange-sitpi-claix":         "20:08", "la-mouette":                  "4:38",
    "les-gul":                         "6:06",  "licences-open-source":        "19:59",
    "linux-ecole-nird":                "28:33", "logiciel-libre-noms-domaine": "15:55",
    "openstreetmap-nazca":             "20:59", "p16-ia-souveraine":           "20:01",
    "rag-mutualise-souverain":         "16:55", "radios-libres":               "17:25",
    "sensibiliser-etudiants":          "4:54",  "mobilizon":                   "4:30",
    "table-ronde-migrations":          "43:58", "teemip":                      "2:36",
    "tchap-collectivites":             "19:20",
    # Lightning talks (créneau 15 min)
    "alternc-souverainete-donnees":        "~15:00", "vates-ecosystemes-ouverts":          "~15:00",
    "postgresql-kubernetes-cloudnativepg": "~15:00", "migrer-messagerie-freins":           "~15:00",
    "rag-ia-mutualisee-linagora":          "~15:00", "linux-mac-support-materiel":         "~15:00",
    "xwiki-20-ans":                        "~15:00", "files2anywhere-nextcloud-pastell":   "~15:00",
    "anct-suite-territoriale":             "~15:00", "lasuite-coop":                       "~15:00",
    "creme-crm":                           "~15:00", "itop-gestion-services-it":           "~15:00",
    "hebergeur-kubernetes":                "~15:00",
    # Ateliers (1h ou 2h)
    "atelier-openrag":         "~1h",
    "atelier-jupyterhub-wod":  "~1h",
    "atelier-openpgp-yubikey": "~1h",
    "atelier-silex-web":       "~1h",
    "atelier-wikipedia":       "~1h",
    "atelier-rust-cli":        "~2h",
}

THEMES = {
    "comment-degafamiser-asso-climat":  ("Migrations & Workplace", "#e67e22"),
    "adieu-windows-bonjour-libre":      ("Migrations & Workplace", "#e67e22"),
    "approche-bottom-up-ngi":           ("IA & Souveraineté",      "#9b59b6"),
    "choisir-logiciel-libre":           ("Écosystème libre",       "#2980b9"),
    "chronique-journee-open-source":    ("Écosystème libre",       "#2980b9"),
    "coopcircuits":                     ("Communs & Société",      "#27ae60"),
    "cyber-resilience-act":             ("SSI & Juridique",        "#c0392b"),
    "telephonie-digital-workplace":     ("Infra & Protocoles",     "#16a085"),
    "inria-politiques-publiques":       ("IA & Souveraineté",      "#9b59b6"),
    "iam-openldap-active-directory":    ("SSI & Juridique",        "#c0392b"),
    "openxchange-sitpi-claix":          ("Migrations & Workplace", "#e67e22"),
    "la-mouette":                       ("Écosystème libre",       "#2980b9"),
    "les-gul":                          ("Communs & Société",      "#27ae60"),
    "licences-open-source":             ("SSI & Juridique",        "#c0392b"),
    "linux-ecole-nird":                 ("Migrations & Workplace", "#e67e22"),
    "logiciel-libre-noms-domaine":      ("Infra & Protocoles",     "#16a085"),
    "openstreetmap-nazca":              ("Communs & Société",      "#27ae60"),
    "p16-ia-souveraine":                ("IA & Souveraineté",      "#9b59b6"),
    "rag-mutualise-souverain":          ("IA & Souveraineté",      "#9b59b6"),
    "radios-libres":                    ("Communs & Société",      "#27ae60"),
    "sensibiliser-etudiants":           ("Communs & Société",      "#27ae60"),
    "mobilizon":                        ("Communs & Société",      "#27ae60"),
    "table-ronde-migrations":           ("Migrations & Workplace", "#e67e22"),
    "teemip":                           ("Écosystème libre",       "#2980b9"),
    "tchap-collectivites":              ("Migrations & Workplace", "#e67e22"),
    # Lightning talks
    "alternc-souverainete-donnees":         ("Infra & Protocoles",     "#16a085"),
    "vates-ecosystemes-ouverts":            ("Écosystème libre",       "#2980b9"),
    "postgresql-kubernetes-cloudnativepg":  ("Infra & Protocoles",     "#16a085"),
    "migrer-messagerie-freins":             ("Migrations & Workplace", "#e67e22"),
    "rag-ia-mutualisee-linagora":           ("IA & Souveraineté",      "#9b59b6"),
    "linux-mac-support-materiel":           ("Migrations & Workplace", "#e67e22"),
    "xwiki-20-ans":                         ("Écosystème libre",       "#2980b9"),
    "files2anywhere-nextcloud-pastell":     ("Infra & Protocoles",     "#16a085"),
    "anct-suite-territoriale":              ("Communs & Société",      "#27ae60"),
    "lasuite-coop":                         ("Migrations & Workplace", "#e67e22"),
    "creme-crm":                            ("Écosystème libre",       "#2980b9"),
    "itop-gestion-services-it":             ("Migrations & Workplace", "#e67e22"),
    "hebergeur-kubernetes":                 ("Infra & Protocoles",     "#16a085"),
    # Ateliers
    "atelier-openrag":         ("Atelier", "#1abc9c"),
    "atelier-jupyterhub-wod":  ("Atelier", "#1abc9c"),
    "atelier-openpgp-yubikey": ("Atelier", "#1abc9c"),
    "atelier-silex-web":       ("Atelier", "#1abc9c"),
    "atelier-wikipedia":       ("Atelier", "#1abc9c"),
    "atelier-rust-cli":        ("Atelier", "#1abc9c"),
}


# ─── Shared UI constants ──────────────────────────────────────────────────────

THEME_VARS = """
:root {
  --bg1:#0d1117; --bg2:#161b22; --bg3:#21262d;
  --sb:#1a2332; --sb-brd:#263347; --sb-hov:#233045; --sb-act:#1e3a5f; --acc:#3d7fff;
  --t1:#e6edf3; --t2:#b0bac6; --t2h:#c9d1d9; --t3:#8b949e; --t4:#7a8fa3; --t5:#6b7a8d; --t6:#484f58;
  --brd:#30363d; --brd2:#21262d;
  --link:#58a6ff; --code:#79c0ff; --code-bg:#161b22;
}
[data-theme="light"] {
  --bg1:#ffffff; --bg2:#f6f8fa; --bg3:#eaeef2;
  --sb:#e8ecf1; --sb-brd:#c6cdd5; --sb-hov:#dde3ea; --sb-act:#cad6e8; --acc:#0969da;
  --t1:#1f2328; --t2:#656d76; --t2h:#424a53; --t3:#57606a; --t4:#57606a; --t5:#6e7781; --t6:#818b98;
  --brd:#d0d7de; --brd2:#eaeef2;
  --link:#0969da; --code:#0550ae; --code-bg:#eaeef2;
}
.tt-btn {
  position:fixed; top:14px; right:16px; background:var(--bg2); border:1px solid var(--brd);
  color:var(--t1); width:32px; height:32px; border-radius:6px; cursor:pointer; font-size:16px;
  z-index:1000; transition:background .15s,border-color .15s; line-height:32px; text-align:center; padding:0;
}
.tt-btn:hover { background:var(--bg3); }
"""

THEME_HEAD = '<script>document.documentElement.setAttribute("data-theme",localStorage.getItem("alposs-theme")||"dark");</script>'
TOGGLE_BTN = '<button class="tt-btn" id="tt" onclick="toggleTheme()" title="Changer le thème"></button>'
TOGGLE_JS = """
function toggleTheme() {
  const html = document.documentElement;
  const next = (html.getAttribute('data-theme')||'dark') === 'dark' ? 'light' : 'dark';
  html.setAttribute('data-theme', next);
  document.getElementById('tt').textContent = next === 'dark' ? '\u2600\ufe0f' : '\U0001f319';
  localStorage.setItem('alposs-theme', next);
}
document.getElementById('tt').textContent =
  (document.documentElement.getAttribute('data-theme')||'dark') === 'dark' ? '\u2600\ufe0f' : '\U0001f319';
"""

# CSS for the structured detail view (shared between A and B)
DETAIL_CSS = """
.dv-header { margin-bottom: 24px; padding-bottom: 20px; border-bottom: 2px solid var(--brd); }
.dv-badge { display:inline-block; padding:3px 10px; border-radius:12px; font-size:11px; font-weight:600; text-transform:uppercase; letter-spacing:.6px; color:#fff; margin-bottom:10px; }
.dv-title { font-size:1.85rem; color:var(--t1); line-height:1.3; font-weight:700; margin-bottom:10px; }
.dv-meta { display:flex; align-items:center; gap:10px; flex-wrap:wrap; }
.dv-att { font-size:13px; color:var(--t2); }
.dv-dur { font-size:12px; color:var(--t3); font-family:'JetBrains Mono',monospace; background:var(--bg2); padding:2px 8px; border-radius:4px; }
.dv-spk { font-size:14px; color:var(--t3); line-height:1.55; margin-top:10px; }
.dv-section { margin-bottom:24px; }
.dv-sh { font-size:10px; text-transform:uppercase; letter-spacing:1.2px; color:var(--t5); font-weight:700; margin-bottom:10px; padding-bottom:5px; border-bottom:1px solid var(--brd2); }

.dv-prose h3 { font-size:1rem; color:var(--t2h); font-weight:600; margin:1.1rem 0 .35rem; }
.dv-prose p { color:var(--t2); line-height:1.8; margin-bottom:.75rem; font-size:1rem; }
.dv-prose ul, .dv-prose ol { padding-left:1.3rem; margin-bottom:.75rem; }
.dv-prose li { color:var(--t2); line-height:1.7; margin-bottom:.2rem; font-size:1rem; }
.dv-prose strong { color:var(--t1); }
.dv-prose em { color:var(--t3); }
.dv-prose blockquote { border-left:3px solid var(--brd); padding:6px 14px; color:var(--t3); font-style:italic; margin:.7rem 0; background:var(--bg2); border-radius:0 4px 4px 0; }
.dv-prose code { font-family:'JetBrains Mono',monospace; background:var(--code-bg); padding:1px 5px; border-radius:3px; font-size:.84em; color:var(--code); }
.dv-prose a { color:var(--link); text-decoration:none; }
.dv-prose a:hover { text-decoration:underline; }
.dv-prose table { width:100%; border-collapse:collapse; margin:.75rem 0; }
.dv-prose thead th { background:var(--bg2); color:var(--t1); padding:8px 12px; text-align:left; border-bottom:2px solid var(--brd); font-size:.92rem; font-weight:500; }
.dv-prose tbody td { padding:8px 12px; border-bottom:1px solid var(--brd2); color:var(--t2); font-size:.92rem; }
.dv-prose tbody tr:hover td { background:var(--bg2); }
.dv-prose hr { border:none; border-top:1px solid var(--brd2); margin:1.2rem 0; }

.dv-hlist { list-style:none; display:flex; flex-direction:column; gap:6px; }
.dv-hlist li { padding:10px 14px; background:var(--bg2); border-radius:6px; border-left:3px solid var(--hc,var(--acc)); color:var(--t2); font-size:.98rem; line-height:1.65; }
.dv-hlist li strong { color:var(--t1); }
.dv-hlist li code { font-family:'JetBrains Mono',monospace; background:var(--code-bg); padding:1px 4px; border-radius:3px; font-size:.84em; color:var(--code); }

.dv-tlist { list-style:none; display:flex; flex-direction:column; gap:5px; }
.dv-tlist li { padding:8px 12px; background:var(--bg2); border-radius:6px; font-size:.93rem; line-height:1.6; }
.dv-tname { color:var(--t1); font-weight:600; }
.dv-tsep { color:var(--t5); margin:0 4px; }
.dv-tdesc { color:var(--t2); }
.dv-tdesc a { color:var(--link); text-decoration:none; }
.dv-tdesc a:hover { text-decoration:underline; }
.dv-tdesc code { font-family:'JetBrains Mono',monospace; background:var(--code-bg); padding:1px 4px; border-radius:3px; font-size:.84em; color:var(--code); }

.dv-credits { border-top:1px solid var(--brd2); padding-top:14px; }
.dv-credits p, .dv-credits li { font-size:12px; color:var(--t5); line-height:1.7; }
.dv-credits a { color:var(--link); text-decoration:none; }
.dv-credits ul { list-style:none; padding:0; }

/* ── Search bar ─────────────────────────────────────────────────────────── */
.search-wrap { padding:8px 14px 6px; }
.search-inp {
  width:100%; background:var(--bg1); border:1px solid var(--sb-brd); color:var(--t1);
  padding:6px 10px 6px 30px; border-radius:6px; font-size:13px; font-family:inherit;
  outline:none; background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='%238b949e' stroke-width='2'%3E%3Ccircle cx='11' cy='11' r='8'/%3E%3Cpath d='m21 21-4.35-4.35'/%3E%3C/svg%3E");
  background-repeat:no-repeat; background-position:9px center;
}
.search-inp::placeholder { color:var(--t5); }
.search-inp:focus { border-color:var(--acc); }

/* Version B — search inside filter bar */
.fb-search { background:var(--bg1); border:1px solid var(--brd); color:var(--t1); padding:5px 10px 5px 28px; border-radius:20px; font-size:12px; font-family:inherit; outline:none; width:180px; background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%238b949e' stroke-width='2'%3E%3Ccircle cx='11' cy='11' r='8'/%3E%3Cpath d='m21 21-4.35-4.35'/%3E%3C/svg%3E"); background-repeat:no-repeat; background-position:8px center; }
.fb-search::placeholder { color:var(--t5); }
.fb-search:focus { border-color:var(--acc); }

/* Header external links */
.hdr-links { display:flex; gap:6px; margin-top:10px; flex-wrap:wrap; }
.hdr-link { display:inline-flex; align-items:center; gap:5px; padding:4px 11px; border:1px solid var(--brd); border-radius:6px; color:var(--t3); font-size:12px; text-decoration:none; transition:border-color .15s,color .15s; }
.hdr-link:hover { border-color:var(--acc); color:var(--acc); }
"""

# JS: inline markdown renderer + structured detail builder (raw string — JS backticks are fine)
RENDER_JS = r"""
function inlineMd(s) {
  return (s||'')
    .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
    .replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>')
    .replace(/`([^`]+)`/g,'<code>$1</code>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g,'<a href="$2">$1</a>');
}

function renderDetail(talk) {
  var pm = function(t) { return t ? marked.parse(t) : ''; };
  var h = '';

  // ── Header ──────────────────────────────────────────────────────────────────
  h += '<div class="dv-header">';
  h +=   `<div class="dv-badge" style="background:${talk.theme_color}">${talk.theme}</div>`;
  h +=   `<h1 class="dv-title">${talk.title}</h1>`;
  h +=   '<div class="dv-meta">';
  if (talk.attended) h += '<span class="dv-att">✅ Présent</span>';
  h +=     `<span class="dv-dur">${talk.duration}</span>`;
  h +=   '</div>';
  if (talk.speakers) h += `<div class="dv-spk">${talk.speakers}</div>`;
  h += '</div>';

  // ── Intervenants ────────────────────────────────────────────────────────────
  if (talk.about_md) {
    h += '<div class="dv-section">';
    h +=   '<div class="dv-sh">Intervenants</div>';
    h +=   `<div class="dv-prose">${pm(talk.about_md)}</div>`;
    h += '</div>';
  }

  // ── Résumé ──────────────────────────────────────────────────────────────────
  if (talk.resume_md) {
    h += '<div class="dv-section">';
    h +=   '<div class="dv-sh">Résumé</div>';
    h +=   `<div class="dv-prose">${pm(talk.resume_md)}</div>`;
    h += '</div>';
  }

  // ── Points marquants ────────────────────────────────────────────────────────
  if (talk.highlights && talk.highlights.length) {
    h += '<div class="dv-section">';
    h +=   '<div class="dv-sh">Points marquants</div>';
    h +=   '<ul class="dv-hlist">';
    talk.highlights.forEach(function(item) {
      h += `<li style="--hc:${talk.theme_color}">${inlineMd(item)}</li>`;
    });
    h +=   '</ul>';
    h += '</div>';
  }

  // ── Technologies & outils ───────────────────────────────────────────────────
  if (talk.tech_items && talk.tech_items.length) {
    h += '<div class="dv-section">';
    h +=   '<div class="dv-sh">Technologies &amp; outils</div>';
    h +=   '<ul class="dv-tlist">';
    talk.tech_items.forEach(function(t) {
      h += '<li>';
      h +=   `<span class="dv-tname">${t.name}</span>`;
      if (t.desc) h += `<span class="dv-tsep">—</span><span class="dv-tdesc">${inlineMd(t.desc)}</span>`;
      h += '</li>';
    });
    h +=   '</ul>';
    h += '</div>';
  }

  // ── Crédits ─────────────────────────────────────────────────────────────────
  if (talk.credits_md) {
    h += `<div class="dv-section dv-credits">${pm(talk.credits_md)}</div>`;
  }

  return h;
}
"""


# ─── Section parsing ──────────────────────────────────────────────────────────

def parse_sections(md_text):
    """Split a summary markdown file into a dict of section_name → content."""
    sections = {}
    for part in re.split(r'^## ', md_text, flags=re.MULTILINE)[1:]:
        name, _, content = part.partition('\n')
        sections[name.strip()] = content.strip()
    return sections


def parse_tech_items(content):
    """Parse '- **Name** — desc' bullet list into [{name, desc}]."""
    items = []
    for line in content.splitlines():
        line = line.strip()
        if not line.startswith('- '):
            continue
        body = line[2:]
        m = re.match(r'\*\*(.+?)\*\*\s*[—–-]\s*(.*)', body)
        if m:
            items.append({'name': m.group(1).strip(), 'desc': m.group(2).strip()})
        elif body.startswith('**'):
            m2 = re.match(r'\*\*(.+?)\*\*(.*)', body)
            if m2:
                items.append({'name': m2.group(1).strip(), 'desc': m2.group(2).lstrip('—– ').strip()})
    return items


def parse_bullets(content):
    """Extract plain bullet list items, skipping blockquotes and placeholders."""
    items = []
    for line in content.splitlines():
        line = line.strip()
        if not line.startswith('- '):
            continue
        text = line[2:].strip()
        if text and not text.startswith('*('):
            items.append(text)
    return items


# ─── Data loading ─────────────────────────────────────────────────────────────

def _make_item(slug, entry, summary_md):
    """Build a unified talk/workshop dict from a JSON entry and its summary markdown."""
    title = re.sub(r"^AlpOSS 2026\s*[-–:]\s*", "", entry["title"]).strip()
    theme, color = THEMES.get(slug, ("Autre", "#7f8c8d"))
    sections = parse_sections(summary_md)
    about_key = next((k for k in sections if k.startswith('À propos')), None)
    return {
        "id":            slug,
        "title":         title,
        "speakers":      entry.get("description", ""),
        "duration":      DURATIONS.get(slug, "?"),
        "attended":      entry.get("attended", False),
        "official_link": entry.get("official_link", ""),
        "theme":         theme,
        "theme_color":   color,
        "kind":          "atelier" if slug.startswith("atelier-") else "talk",
        "about_md":      sections.get(about_key, '') if about_key else '',
        "resume_md":     sections.get('Résumé', ''),
        "tech_items":    parse_tech_items(sections.get('Technologies & outils mentionnés', '')),
        "highlights":    parse_bullets(sections.get('Points marquants', '')),
        "credits_md":    sections.get('Crédits', ''),
        "summary_md":    summary_md,
        "esn_highlight":  entry.get("esn_highlight", False),
        "in_diapo":       entry.get("in_diapo", False),
        "personal_notes": entry.get("personal_notes", ""),
    }


def load_talks():
    with open(os.path.join(BASE, "talks.json"), encoding="utf-8") as f:
        raw = json.load(f)
    talks = []
    missing = []

    for slug, entry in zip(SLUGS, raw["talks"]):
        md_path = os.path.join(BASE, "summaries", f"{slug}.md")
        if not os.path.exists(md_path):
            missing.append(slug)
            continue
        with open(md_path, encoding="utf-8") as f:
            summary_md = f.read()
        talks.append(_make_item(slug, entry, summary_md))

    for slug, entry in zip(WORKSHOP_SLUGS, raw.get("workshops", [])):
        md_path = os.path.join(BASE, "summaries", f"{slug}.md")
        if not os.path.exists(md_path):
            missing.append(slug)
            continue
        with open(md_path, encoding="utf-8") as f:
            summary_md = f.read()
        talks.append(_make_item(slug, entry, summary_md))

    if missing:
        print(f"  ⚠️  Résumés manquants (ignorés) : {', '.join(missing)}")
    return talks


def load_slides():
    """Load talks/workshops where attended==True OR personal_notes, reading slides/*.md."""
    with open(os.path.join(BASE, "talks.json"), encoding="utf-8") as f:
        raw = json.load(f)

    all_slugs   = SLUGS + WORKSHOP_SLUGS
    all_entries = raw["talks"] + raw.get("workshops", [])

    result, missing = [], []
    for slug, entry in zip(all_slugs, all_entries):
        if not entry.get("in_diapo"):
            continue
        slide_path = os.path.join(BASE, "slides", f"{slug}.md")
        if not os.path.exists(slide_path):
            missing.append(slug)
            continue
        with open(slide_path, encoding="utf-8") as f:
            slide_md = f.read()

        # Title from H1
        first_line = slide_md.split("\n")[0]
        title = re.sub(r"^#+\s*", "", first_line).strip()

        sections = parse_sections(slide_md)

        # "Prénom Nom · Société"
        intervenant = sections.get("Intervenant", "").strip()
        speaker_name, company_short = intervenant, ""
        if "·" in intervenant:
            parts = intervenant.split("·", 1)
            speaker_name  = parts[0].strip()
            company_short = parts[1].strip()

        theme, color = THEMES.get(slug, ("Autre", "#7f8c8d"))
        result.append({
            "id":             slug,
            "title":          title,
            "speaker_name":   speaker_name,
            "company_short":  company_short,
            "company_tip":    sections.get("Société", ""),
            "resume":         sections.get("Résumé", ""),
            "highlights":     parse_bullets(sections.get("Points marquants", "")),
            "tech_items":     parse_tech_items(sections.get("Technologies", "")),
            "personal_notes": entry.get("personal_notes", "").strip(),
            "attended":       entry.get("attended", False),
            "theme":          theme,
            "theme_color":    color,
            "duration":       DURATIONS.get(slug, "?"),
        })

    if missing:
        print(f"  ⚠️  Slides manquants (ignorés) : {', '.join(missing)}")
    print(f"Loaded {len(result)} slides.")
    return result


def data_js(talks):
    """Embed talk data as JS. Exclude summary_md (not needed at runtime)."""
    slim = [{k: v for k, v in t.items() if k != 'summary_md'} for t in talks]
    return "const TALKS = " + json.dumps(slim, ensure_ascii=False) + ";\nconst AVATAR = " + json.dumps(AVATAR) + ";"


# ─── Version A — Le Rapport de Mission ───────────────────────────────────────

def version_a(talks):
    themes_unique = list(dict.fromkeys(t["theme"] for t in talks))
    theme_color_map = {t["theme"]: t["theme_color"] for t in talks}

    filter_btns = '<button class="fbtn active" data-theme="all" onclick="filterTheme(this,\'all\')">Tous</button>\n'
    for th in themes_unique:
        c = theme_color_map[th]
        filter_btns += f'<button class="fbtn" data-theme="{th}" onclick="filterTheme(this,\'{th}\')" style="--tc:{c}">{th}</button>\n'

    items = ""
    for i, t in enumerate(talks):
        av   = f'<img src="{AVATAR}" class="mini-av" />' if t["attended"] else ""
        star = '<span class="esn-star" title="À retenir pour une ESN">★</span>' if t["esn_highlight"] else ""
        active = " active" if i == 0 else ""
        search_data = f"{t['title']} {t['speakers']}".lower().replace('"', '&quot;')
        items += f"""<li class="ti{active}" data-id="{t['id']}" data-theme="{t['theme']}" data-search="{search_data}" onclick="selectTalk('{t['id']}')">
  <span class="dot" style="background:{t['theme_color']}"></span>
  <span class="it">{t['title']}</span>
  <span class="im">{star}{av}<span class="dur">{t['duration']}</span></span>
</li>\n"""

    css = THEME_VARS + DETAIL_CSS + """
* { box-sizing:border-box; margin:0; padding:0; }
body { font-family:'Inter',system-ui,sans-serif; display:flex; height:100vh; overflow:hidden; background:var(--bg1); }

.sb { width:300px; min-width:300px; background:var(--sb); display:flex; flex-direction:column; height:100vh; }
.sbh { padding:20px; border-bottom:1px solid var(--sb-brd); }
.sbh img { width:44px; height:44px; border-radius:50%; border:2px solid var(--acc); margin-bottom:10px; display:block; }
.sbh h1 { color:var(--t1); font-size:16px; font-weight:700; }
.sbh .sub { color:var(--t4); font-size:12px; margin-top:2px; }
.stats { display:flex; gap:18px; margin-top:12px; }
.stat .n { color:var(--t1); font-size:22px; font-weight:700; line-height:1; }
.stat .l { color:var(--t4); font-size:10px; text-transform:uppercase; letter-spacing:.5px; }

.filters { padding:10px 16px; border-bottom:1px solid var(--sb-brd); display:flex; flex-wrap:wrap; gap:5px; }
.fbtn { background:transparent; border:1px solid var(--sb-brd); color:var(--t4); padding:3px 9px; border-radius:10px; font-size:10px; cursor:pointer; transition:all .15s; font-family:inherit; }
.fbtn:hover { border-color:var(--tc,var(--acc)); color:var(--tc,var(--acc)); }
.fbtn.active { background:var(--tc,var(--acc)); border-color:var(--tc,var(--acc)); color:#fff; }

.tl { flex:1; overflow-y:auto; padding:6px 0; }
.tl::-webkit-scrollbar { width:3px; }
.tl::-webkit-scrollbar-thumb { background:var(--sb-brd); border-radius:2px; }

.ti { display:flex; align-items:center; gap:8px; padding:9px 16px; cursor:pointer; transition:background .1s; border-left:3px solid transparent; }
.ti:hover { background:var(--sb-hov); }
.ti.active { background:var(--sb-act); border-left-color:var(--acc); }
.ti.hidden { display:none; }
.dot { width:7px; height:7px; border-radius:50%; flex-shrink:0; }
.it { flex:1; color:var(--t2h); font-size:14px; line-height:1.4; overflow:hidden; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; }
.ti.active .it { color:var(--t1); }
.im { display:flex; align-items:center; gap:5px; flex-shrink:0; }
.mini-av { width:18px; height:18px; border-radius:50%; opacity:.85; }
.mini-av-ph { width:18px; height:18px; }
.dur { color:var(--t4); font-size:11px; font-family:'JetBrains Mono',monospace; }

.ct { flex:1; overflow-y:auto; background:var(--bg1); }
.ct-inner { max-width:780px; margin:0 auto; padding:40px 48px 80px; }
.esn-star { color:#f1c40f; font-size:11px; flex-shrink:0; }
"""

    js = """
let _themeA = 'all';

function selectTalk(id) {
  document.querySelectorAll('.ti').forEach(el => el.classList.toggle('active', el.dataset.id === id));
  const talk = TALKS.find(t => t.id === id);
  if (!talk) return;
  document.getElementById('detail').innerHTML = renderDetail(talk);
  document.querySelector('.ct').scrollTop = 0;
}

function applyFiltersA() {
  const q = document.getElementById('srch-a').value.toLowerCase().trim();
  document.querySelectorAll('.ti').forEach(el => {
    const themeOk = _themeA === 'all' || el.dataset.theme === _themeA;
    const searchOk = !q || el.dataset.search.includes(q);
    el.classList.toggle('hidden', !themeOk || !searchOk);
  });
}

function filterTheme(btn, theme) {
  document.querySelectorAll('.fbtn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  _themeA = theme;
  applyFiltersA();
}

marked.setOptions({ breaks: true });
selectTalk(TALKS[0].id);
""" + TOGGLE_JS

    total    = len(talks)
    attended = sum(1 for t in talks if t["attended"])

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  {THEME_HEAD}
  <title>AlpOSS 2026 — Rapport de mission</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>{css}{DISCLAIMER_CSS}</style>
</head>
<body>
{TOGGLE_BTN}
<aside class="sb">
  <div class="sbh">
    <img src="{AVATAR}" alt="Victor" />
    <h1>AlpOSS 2026</h1>
    <div class="sub">17 février 2026 · Grenoble</div>
    <div class="stats">
      <div class="stat"><div class="n">{total}</div><div class="l">talks</div></div>
      <div class="stat"><div class="n">{attended}</div><div class="l">assistés</div></div>
      <div class="stat"><div class="n">{total - attended}</div><div class="l">non assistés</div></div>
    </div>
    <div class="hdr-links">
      <a class="hdr-link" href="https://alposs.fr/" target="_blank">🏔 alposs.fr</a>
      <a class="hdr-link" href="https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk" target="_blank">▶ Replays</a>
    </div>
  </div>
  <div class="search-wrap">
    <input id="srch-a" class="search-inp" type="search" placeholder="Rechercher…" oninput="applyFiltersA()" />
  </div>
  <div class="filters">{filter_btns}</div>
  <ul class="tl">{items}</ul>
</aside>
<main class="ct">
  <div class="ct-inner">
    <div id="detail"></div>
  </div>
</main>
<script>
{data_js(talks)}
{RENDER_JS}
{js}
</script>
{DISCLAIMER}
</body>
</html>"""


# ─── Version B — La Journée en Cartes ────────────────────────────────────────

def version_b(talks):
    themes_unique = list(dict.fromkeys(t["theme"] for t in talks))
    theme_color_map = {t["theme"]: t["theme_color"] for t in talks}

    filter_btns = '<button class="fbtn active" data-theme="all" onclick="filterB(this,\'all\')">Tous</button>\n'
    for th in themes_unique:
        c = theme_color_map[th]
        filter_btns += f'<button class="fbtn" data-theme="{th}" onclick="filterB(this,\'{th}\')" style="--tc:{c}">{th}</button>\n'

    total    = len(talks)
    attended = sum(1 for t in talks if t["attended"])

    css = THEME_VARS + DETAIL_CSS + """
* { box-sizing:border-box; margin:0; padding:0; }
body { font-family:'Inter',system-ui,sans-serif; background:var(--bg1); min-height:100vh; }

header { background:var(--bg2); color:var(--t1); padding:28px 40px; border-bottom:1px solid var(--brd); }
header h1 { font-size:1.6rem; font-weight:700; }
header .sub { color:var(--t3); font-size:14px; margin-top:4px; }
header .stats { display:flex; gap:32px; margin-top:16px; }
.stat .n { font-size:28px; font-weight:700; line-height:1; color:var(--t1); }
.stat .l { color:var(--t3); font-size:11px; text-transform:uppercase; letter-spacing:.5px; }

.filters { padding:16px 40px; background:var(--bg2); border-bottom:1px solid var(--brd); display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
.filters span { color:var(--t3); font-size:13px; margin-right:4px; }
.fbtn { background:transparent; border:1px solid var(--brd); color:var(--t3); padding:5px 14px; border-radius:20px; font-size:12px; cursor:pointer; transition:all .15s; font-family:inherit; }
.fbtn:hover { border-color:var(--tc,var(--link)); color:var(--tc,var(--link)); }
.fbtn.active { background:var(--tc,var(--link)); border-color:var(--tc,var(--link)); color:#fff; }

.grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:16px; padding:24px 40px 60px; }

.card { background:var(--bg2); border-radius:8px; border-left:4px solid var(--tc,var(--link)); padding:18px 20px; cursor:pointer;
  transition:transform .15s,box-shadow .15s; box-shadow:0 1px 4px rgba(0,0,0,.15); position:relative;
  display:flex; flex-direction:column; }
.card:hover { transform:translateY(-2px); box-shadow:0 6px 24px rgba(0,0,0,.2); }
.card.hidden { display:none; }
.esn-badge { position:absolute; top:10px; right:12px; color:#f1c40f; font-size:16px; line-height:1; }

.card-top { display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:10px; }
.badge { font-size:10px; font-weight:600; color:var(--tc,var(--link)); text-transform:uppercase; letter-spacing:.5px; }
.mini-av { width:20px; height:20px; border-radius:50%; }
.dur { font-size:12px; color:var(--t6); font-family:'JetBrains Mono',monospace; }
.card-foot { display:flex; align-items:center; justify-content:flex-end; gap:6px; margin-top:auto; padding-top:10px; }

.card h3 { font-size:15px; font-weight:600; color:var(--t1); line-height:1.45; margin-bottom:8px; }
.card .speakers { font-size:13px; color:var(--t3); line-height:1.4; }

.modal-bg { display:none; position:fixed; inset:0; background:rgba(0,0,0,.6); z-index:100; align-items:center; justify-content:center; }
.modal-bg.open { display:flex; }
.modal { background:var(--bg2); border:1px solid var(--brd); border-radius:12px; width:min(760px,92vw); max-height:85vh; overflow-y:auto; padding:36px 40px; position:relative; }
.modal::-webkit-scrollbar { width:5px; }
.modal::-webkit-scrollbar-thumb { background:var(--brd); border-radius:3px; }
.modal-close { position:absolute; top:16px; right:20px; background:none; border:none; font-size:22px; cursor:pointer; color:var(--t3); }
.modal-close:hover { color:var(--t1); }
"""

    js = """
marked.setOptions({ breaks: true });

let _themeB = 'all';

function applyFiltersB() {
  const q = document.getElementById('srch-b').value.toLowerCase().trim();
  document.querySelectorAll('.card').forEach(el => {
    const themeOk = _themeB === 'all' || el.dataset.theme === _themeB;
    const searchOk = !q || el.dataset.search.includes(q);
    el.classList.toggle('hidden', !themeOk || !searchOk);
  });
}

function filterB(btn, theme) {
  document.querySelectorAll('.fbtn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  _themeB = theme;
  applyFiltersB();
}

function openCard(id) {
  const talk = TALKS.find(t => t.id === id);
  if (!talk) return;
  document.getElementById('modal-content').innerHTML = renderDetail(talk);
  document.getElementById('modal-bg').classList.add('open');
  document.querySelector('.modal').scrollTop = 0;
}

function closeModal() {
  document.getElementById('modal-bg').classList.remove('open');
}

document.addEventListener('keydown', e => { if (e.key === 'Escape') closeModal(); });
""" + TOGGLE_JS

    cards = ""
    for t in talks:
        av   = f'<img src="{AVATAR}" class="mini-av" title="Présent" />' if t["attended"] else ""
        esn  = '<span class="esn-badge" title="À retenir pour une ESN">★</span>' if t["esn_highlight"] else ""
        search_data = f"{t['title']} {t['speakers']}".lower().replace('"', '&quot;')
        cards += f"""<div class="card" data-id="{t['id']}" data-theme="{t['theme']}" data-search="{search_data}" style="--tc:{t['theme_color']}" onclick="openCard('{t['id']}')">
  {esn}
  <div class="card-top">
    <span class="badge">{t['theme']}</span>
  </div>
  <h3>{t['title']}</h3>
  <div class="speakers">{t['speakers']}</div>
  <div class="card-foot">{av}<span class="dur">{t['duration']}</span></div>
</div>\n"""

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  {THEME_HEAD}
  <title>AlpOSS 2026 — La Journée en Cartes</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>{css}{DISCLAIMER_CSS}</style>
</head>
<body>
{TOGGLE_BTN}
<header>
  <h1><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 28" style="height:.9em;width:auto;vertical-align:middle;margin-right:.3em" aria-hidden="true">
    <line x1="2" y1="14" x2="58" y2="2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <g transform="rotate(-10,14,11)">
      <line x1="14" y1="11" x2="14" y2="15" stroke="currentColor" stroke-width="1.5"/>
      <circle cx="14" cy="20" r="5" fill="none" stroke="currentColor" stroke-width="2"/>
    </g>
    <g transform="rotate(-10,30,8)">
      <line x1="30" y1="8" x2="30" y2="12" stroke="currentColor" stroke-width="1.5"/>
      <circle cx="30" cy="17" r="5" fill="none" stroke="currentColor" stroke-width="2"/>
    </g>
    <g transform="rotate(-10,46,5)">
      <line x1="46" y1="5" x2="46" y2="9" stroke="currentColor" stroke-width="1.5"/>
      <circle cx="46" cy="14" r="5" fill="none" stroke="currentColor" stroke-width="2"/>
    </g>
  </svg>AlpOSS 2026</h1>
  <div class="sub">Grenoble · 17 février 2026 · Compte-rendu de participation</div>
  <div class="stats">
    <div class="stat"><div class="n">{total}</div><div class="l">conférences</div></div>
    <div class="stat"><div class="n">{attended}</div><div class="l">assistées</div></div>
    <div class="stat"><div class="n">{total - attended}</div><div class="l">non assistées</div></div>
  </div>
  <div class="hdr-links">
    <a class="hdr-link" href="https://alposs.fr/" target="_blank">🏔 alposs.fr</a>
    <a class="hdr-link" href="https://video.echirolles.fr/w/p/7CPFbyKwNmwZBVbnMo2rmk" target="_blank">▶ Replays</a>
  </div>
</header>
<div class="filters">
  <input id="srch-b" class="fb-search" type="search" placeholder="Rechercher…" oninput="applyFiltersB()" />
  <span>Filtrer :</span>
  {filter_btns}
</div>
<div class="grid" id="grid">{cards}</div>

<div class="modal-bg" id="modal-bg" onclick="if(event.target===this)closeModal()">
  <div class="modal">
    <button class="modal-close" onclick="closeModal()">✕</button>
    <div id="modal-content"></div>
  </div>
</div>

<script>
{data_js(talks)}
{RENDER_JS}
{js}
</script>
{DISCLAIMER}
</body>
</html>"""


# ─── Version C — Le Diaporama Web ────────────────────────────────────────────

def version_c(slides, all_talks=None):
    # Partition into attended (main) and non-attended with notes (extra)
    main_slides  = [s for s in slides if s["attended"]]
    extra_slides = [s for s in slides if not s["attended"]]

    # Truly missed: not in slides at all, not a workshop
    slide_ids = {s["id"] for s in slides}
    missed = [t for t in (all_talks or [])
              if t["id"] not in slide_ids and t.get("kind") != "atelier"]

    # Excluded: attended or noted, but deliberately not in diapo
    excluded = [t for t in (all_talks or [])
                if not t.get("in_diapo")
                and (t.get("attended") or t.get("personal_notes", "").strip())
                and t.get("kind") != "atelier"]

    # Structural slides injected between talk groups
    intro      = {"type": "intro",    "id": "_intro",     "theme_color": "#3d7fff"}
    sec_main   = {"type": "section",  "id": "_sec_main",  "theme_color": "#3d7fff",
                  "label": "Partie principale",
                  "num": "01", "sub": f"{len(main_slides)} talks assistés en direct"}
    sec_ext    = {"type": "section",  "id": "_sec_ext",   "theme_color": "#7f8c8d",
                  "label": "Mentions rapides",
                  "num": "02", "sub": f"{len(extra_slides)} talks couverts à distance"}
    sec_excl   = {"type": "section",  "id": "_sec_excl",  "theme_color": "#484f58",
                  "label": "Autres talks vus",
                  "num": "03", "sub": f"{len(excluded)} talks vus, non présentés"}
    excl_slide = {"type": "excluded", "id": "_excluded",  "theme_color": "#484f58",
                  "items": excluded}
    rate       = {"type": "rate",     "id": "_rate",      "theme_color": "#e67e22",
                  "missed": missed}

    all_items = [intro, sec_main] + main_slides + [sec_ext] + extra_slides + [sec_excl, excl_slide, rate]
    total = len(all_items)

    css = THEME_VARS + """
html { zoom: 1.75; }
* { box-sizing:border-box; margin:0; padding:0; }
body { font-family:'Space Grotesk',system-ui,sans-serif; background:var(--bg1); color:var(--t1);
       height:100vh; overflow:hidden; user-select:none; }
/* Disable fixed banner in zoomed context — disclaimer shown in controls bar */
.ai-disclaimer { display: none; }

/* ── Slides ─────────────────────────────────────────────────────────────── */
.slide { position:absolute; inset:0; display:flex; flex-direction:column;
         padding:44px 72px 88px; opacity:0; transition:opacity .3s; pointer-events:none; }
.slide.active { opacity:1; pointer-events:all; }

.slide-top { display:flex; justify-content:space-between; align-items:center; margin-bottom:24px; }
.theme-badge { display:inline-block; padding:4px 14px; border-radius:20px; font-size:11px;
               font-weight:700; text-transform:uppercase; letter-spacing:.8px; color:#fff; }
.slide-counter { font-size:13px; color:var(--t5); font-family:'JetBrains Mono',monospace; }

.slide-title { font-size:clamp(1.55rem,3.2vw,2.6rem); font-weight:700; color:var(--t1);
               line-height:1.25; margin-bottom:12px; }
.slide-speaker { font-size:16px; color:var(--t3); margin-bottom:24px; line-height:1.5;
                 display:flex; align-items:center; gap:10px; flex-wrap:wrap; }
.company-btn { background:none; border:none; color:var(--t4); font-family:inherit; font-size:15px;
               cursor:pointer; padding:0; display:inline-flex; align-items:center; gap:3px;
               transition:color .15s; }
.company-btn:hover { color:var(--acc); }
.company-btn::after { content:"▾"; font-size:11px; }

/* ── Body layout ────────────────────────────────────────────────────────── */
.slide-body { display:flex; gap:36px; flex:1; min-height:0; }
.slide-left { flex:1; display:flex; flex-direction:column; gap:18px; min-width:0; }
.slide-resume { font-size:clamp(14px,1.4vw,17px); color:var(--t2); line-height:1.8; }
.slide-bullets ul { list-style:none; display:flex; flex-direction:column; gap:11px; }
.slide-bullets li { font-size:clamp(15px,1.55vw,18px); color:var(--t2h); line-height:1.5;
                    padding-left:22px; position:relative; }
.slide-bullets li::before { content:"▸"; position:absolute; left:0; color:var(--tc,var(--acc));
                             font-size:12px; top:4px; }
.slide-chips { display:flex; flex-wrap:wrap; gap:7px; margin-top:auto; padding-top:14px; }
.chip { background:var(--bg2); border:1px solid var(--brd); border-radius:20px; padding:4px 12px;
        font-size:12px; color:var(--t3); cursor:pointer; transition:all .15s; font-family:inherit; }
.chip:hover { border-color:var(--tc,var(--acc)); color:var(--tc,var(--acc)); }

/* ── Right column ───────────────────────────────────────────────────────── */
.slide-right { width:200px; flex-shrink:0; display:flex; flex-direction:column;
               align-items:center; justify-content:flex-end; gap:20px; }
.slide-avatar { width:96px; height:96px; border-radius:50%;
                border:3px solid var(--tc,var(--acc)); opacity:.9; }
.thought-bubble { width:96px; height:96px; color:var(--t5); opacity:.45; }

/* ── Note bubble (Caveat) ───────────────────────────────────────────────── */
.note-bubble { font-family:'Caveat',cursive; font-size:17px; font-weight:500;
               background:var(--bg3); border:1px solid var(--brd); border-radius:12px;
               padding:14px 16px; line-height:1.55; color:var(--t2);
               width:200px; text-align:left; position:relative; }
.note-bubble::after  { content:""; position:absolute; bottom:-10px; left:28px;
                        border:5px solid transparent; border-top-color:var(--brd); }
.note-bubble::before { content:""; position:absolute; bottom:-8px; left:28px;
                        border:5px solid transparent; border-top-color:var(--bg3); z-index:1; }
.note-bubble--no-ptr::after, .note-bubble--no-ptr::before { display:none; }
.note-bubble.note-bubble--dashed { border-color:transparent;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Crect width='100%25' height='100%25' rx='12' ry='12' fill='none' stroke='%23888' stroke-width='2' stroke-dasharray='8 6'/%3E%3C/svg%3E"); }

/* ── Tooltip ────────────────────────────────────────────────────────────── */
#tip { display:none; position:fixed; z-index:500; background:var(--bg2); border:1px solid var(--brd);
       border-radius:10px; padding:14px 16px; max-width:340px; font-size:14px; color:var(--t2);
       line-height:1.65; box-shadow:0 8px 32px rgba(0,0,0,.35); }
#tip.open { display:block; }
#tip .tip-close { float:right; background:none; border:none; color:var(--t4); cursor:pointer;
                  font-size:16px; margin:-4px -4px 0 8px; line-height:1; }

/* ── Controls ───────────────────────────────────────────────────────────── */
.controls { position:fixed; bottom:0; left:0; right:0; background:var(--bg2); border-top:1px solid var(--brd2); }
.progress-bar { height:3px; background:var(--acc); transition:width .3s; }
.ctrl-inner { display:flex; align-items:center; justify-content:space-between; padding:10px 72px; }
.ctrl-btn { background:none; border:1px solid var(--brd); color:var(--t3); padding:6px 18px;
            border-radius:6px; cursor:pointer; font-family:inherit; font-size:13px; transition:all .15s; }
.ctrl-btn:hover { background:var(--bg3); color:var(--t1); }
.ctrl-hint { font-size:12px; color:var(--t6); }

/* ── Structural slides ──────────────────────────────────────────── */
/* Intro */
.slide-intro .intro-body { display:flex; flex-direction:column; gap:32px; flex:1; justify-content:center; }
.intro-title { font-size:clamp(2.8rem,6vw,5rem); font-weight:900; color:var(--t1); line-height:1.1; }
.intro-date  { font-size:16px; color:var(--t4); margin-top:6px; }
.intro-cols  { display:grid; grid-template-columns:1fr 1fr; gap:20px; }
.intro-col   { background:var(--bg2); border-radius:10px; padding:18px 22px; border-top:3px solid var(--tc,var(--acc)); }
.intro-col-title { font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:var(--tc,var(--acc)); margin-bottom:10px; }
.intro-col p { font-size:14px; color:var(--t2); line-height:1.75; }
.intro-stats { display:flex; gap:40px; }
.isn { font-size:clamp(2rem,4vw,3rem); font-weight:800; color:var(--t1); line-height:1; }
.isl { font-size:11px; text-transform:uppercase; letter-spacing:.8px; color:var(--t4); margin-top:4px; }
/* Section divider */
.slide-section .section-body { display:flex; flex-direction:column; align-items:center; justify-content:center; flex:1; text-align:center; gap:16px; }
.section-num   { font-size:clamp(5rem,12vw,9rem); font-weight:900; color:var(--brd); line-height:1; font-family:'JetBrains Mono',monospace; }
.section-label { font-size:clamp(2rem,4.5vw,3.5rem); font-weight:700; color:var(--t1); }
.section-sub   { font-size:16px; color:var(--t4); }
/* Excluded listing */
.slide-excluded .excl-grid { display:grid; grid-template-columns:1fr 1fr; gap:0 20px; flex:1; align-content:start; overflow:hidden; }
.excl-row { display:flex; align-items:baseline; gap:7px; padding:5px 0; border-bottom:1px solid var(--brd2); }
.excl-dot { width:6px; height:6px; border-radius:50%; flex-shrink:0; margin-top:5px; }
.excl-title { flex:1; font-size:13px; color:var(--t2); line-height:1.4; overflow:hidden; white-space:nowrap; text-overflow:ellipsis; min-width:0; }
.excl-sp { font-size:11px; color:var(--t5); white-space:nowrap; flex-shrink:0; }
.excl-dur { font-size:11px; color:var(--t6); font-family:'JetBrains Mono',monospace; flex-shrink:0; }
/* Rate slide */
.slide-rate .rate-body { display:flex; flex-direction:column; gap:20px; flex:1; }
.rate-title { font-size:clamp(1.6rem,3vw,2.4rem); font-weight:700; color:var(--t1); }
.rate-intro { font-size:15px; color:var(--t3); line-height:1.7; max-width:700px; }
.rate-grid  { display:grid; grid-template-columns:repeat(auto-fill,minmax(220px,1fr)); gap:10px; }
.rate-item  { background:var(--bg2); border-radius:8px; padding:12px 16px; border-left:3px solid var(--t6); }
.rate-name  { font-size:14px; font-weight:600; color:var(--t2h); line-height:1.4; }
.rate-sp    { font-size:12px; color:var(--t5); margin-top:4px; }
"""

    slides_colors_js = json.dumps(
        [{"id": it["id"], "theme_color": it["theme_color"]} for it in all_items],
        ensure_ascii=False
    )

    js = f"""
const SLIDES = {slides_colors_js};
let cur = 0;
const total = {total};

function showSlide(n) {{
  cur = Math.max(0, Math.min(total - 1, n));
  document.querySelectorAll('.slide').forEach((el, i) => el.classList.toggle('active', i === cur));
  const pct = ((cur + 1) / total * 100).toFixed(1);
  const tc = SLIDES[cur].theme_color;
  document.querySelector('.progress-bar').style.width = pct + '%';
  document.querySelector('.progress-bar').style.background = tc;
  document.getElementById('ctrl-prev').disabled = cur === 0;
  document.getElementById('ctrl-next').disabled = cur === total - 1;
  hideTip();
}}

document.addEventListener('keydown', e => {{
  if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') showSlide(cur + 1);
  if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')                    showSlide(cur - 1);
  if (e.key === 'Escape') hideTip();
}});

// ── Tooltip singleton ────────────────────────────────────────────────────
const tip = document.getElementById('tip');
tip._src = '';

function showTip(el, text) {{
  const id = el.dataset.tipId || el.className;
  if (tip._src === id && tip.classList.contains('open')) {{ hideTip(); return; }}
  tip.querySelector('.tip-body').innerHTML = text.replace(/\\n\\n/g,'</p><p>').replace(/\\n/g,'<br>');
  tip._src = id;
  tip.style.left = '-9999px'; tip.style.top = '-9999px';
  tip.classList.add('open');
  const r = el.getBoundingClientRect();
  const zoom = parseFloat(getComputedStyle(document.documentElement).zoom) || 1;
  const tw = tip.offsetWidth, th = tip.offsetHeight;
  const vw = window.innerWidth / zoom, vh = window.innerHeight / zoom;
  let left = r.left / zoom, top = r.bottom / zoom + 8;
  if (left + tw > vw - 12) left = vw - tw - 12;
  if (top + th > vh - 12) top = r.top / zoom - th - 8;
  tip.style.left = Math.max(12, left) + 'px';
  tip.style.top  = Math.max(8,  top)  + 'px';
}}

function hideTip() {{ tip.classList.remove('open'); tip._src = ''; }}

document.addEventListener('click', e => {{
  if (!tip.contains(e.target) && !e.target.closest('[data-tip]')) hideTip();
}});

showSlide(0);
""" + TOGGLE_JS

    def make_intro_html(i):
        n_main, n_extra = len(main_slides), len(extra_slides)
        return f"""<div class="slide slide-intro" style="--tc:#3d7fff">
  <div class="slide-top">
    <span class="theme-badge" style="background:#3d7fff">Introduction</span>
    <span class="slide-counter">{i+1} / {total}</span>
  </div>
  <div class="intro-body">
    <div>
      <div class="intro-title">AlpOSS 2026</div>
      <div class="intro-date">Alpine Open Source Summit · Grenoble · 17 février 2026</div>
    </div>
    <div class="intro-cols">
      <div class="intro-col">
        <div class="intro-col-title">L'événement</div>
        <p>AlpOSS est une journée de conférences et ateliers autour du logiciel libre, organisée à Grenoble. En 2026 : 44 talks, 6 ateliers, une seule journée.</p>
      </div>
      <div class="intro-col">
        <div class="intro-col-title">Pourquoi j'y étais</div>
        <p>Développeur dans une ESN, je suis venu en éclaireur : identifier les technologies et tendances open source pertinentes pour nos clients et notre offre de service.</p>
      </div>
    </div>
    <div class="intro-stats">
      <div><div class="isn">44</div><div class="isl">talks</div></div>
      <div><div class="isn">6</div><div class="isl">ateliers</div></div>
      <div><div class="isn">{n_main}</div><div class="isl">assistés</div></div>
      <div><div class="isn">{n_extra}</div><div class="isl">mentions</div></div>
    </div>
  </div>
</div>"""

    def make_section_html(i, item):
        return f"""<div class="slide slide-section" style="--tc:{item['theme_color']}">
  <div class="slide-top">
    <span></span>
    <span class="slide-counter">{i+1} / {total}</span>
  </div>
  <div class="section-body">
    <div class="section-num">{item['num']}</div>
    <div class="section-label">{_html.escape(item['label'])}</div>
    <div class="section-sub">{_html.escape(item['sub'])}</div>
  </div>
</div>"""

    def make_excluded_html(i, item):
        rows = "".join(
            f'<div class="excl-row">'
            f'<span class="excl-dot" style="background:{t["theme_color"]}"></span>'
            f'<span class="excl-title" title="{_html.escape(t["title"])}">{_html.escape(t["title"])}</span>'
            + (f'<span class="excl-sp">{_html.escape(t.get("speakers","").strip())}</span>'
               if t.get("speakers","").strip() else "")
            + f'<span class="excl-dur">{_html.escape(t.get("duration",""))}</span>'
            + '</div>'
            for t in item.get("items", [])
        )
        return f"""<div class="slide slide-excluded" style="--tc:#484f58">
  <div class="slide-top">
    <span class="theme-badge" style="background:#484f58">Autres talks vus</span>
    <span class="slide-counter">{i+1} / {total}</span>
  </div>
  <div class="excl-grid">{rows}</div>
</div>"""

    def make_rate_html(i, item):
        items_html = "".join(
            f'<div class="rate-item">'
            f'<div class="rate-name">{_html.escape(t["title"])}</div>'
            + (f'<div class="rate-sp">{_html.escape(t.get("speakers","").strip())}</div>'
               if t.get("speakers","").strip() else "")
            + '</div>'
            for t in item.get("missed", [])
        )
        grid = f'<div class="rate-grid">{items_html}</div>' if items_html else ""
        return f"""<div class="slide slide-rate" style="--tc:#e67e22">
  <div class="slide-top">
    <span class="theme-badge" style="background:#e67e22">Regrets</span>
    <span class="slide-counter">{i+1} / {total}</span>
  </div>
  <div class="rate-body">
    <div class="rate-title">Ce que j'ai raté...</div>
    <div class="rate-intro">AlpOSS proposait plusieurs salles en simultané. Voici les talks que je n'ai pas pu suivre, faute d'être au bon endroit au bon moment.</div>
    {grid}
  </div>
</div>"""

    def make_talk_html(i, s):
        # Company tooltip button
        company_html = ""
        if s["company_short"]:
            co_tip = _html.escape(json.dumps(s.get("company_tip", "")))
            company_html = (
                f'<button class="company-btn" data-tip data-tip-id="co_{s["id"]}"'
                f' onclick="showTip(this,{co_tip})">{_html.escape(s["company_short"])}</button>'
            )

        # Tech chips
        chips_html = ""
        for j, t in enumerate(s["tech_items"]):
            tip_text = _html.escape(json.dumps(t.get("desc", "")))
            chips_html += (
                f'<button class="chip" data-tip data-tip-id="t_{s["id"]}_{j}"'
                f' onclick="showTip(this,{tip_text})">{_html.escape(t["name"])}</button>\n'
            )

        # Note bubble (Caveat font) — pointer only when avatar is present
        note_html = ""
        if s.get("personal_notes"):
            extra = "" if s["attended"] else " note-bubble--no-ptr note-bubble--dashed"
            note_html = f'<div class="note-bubble{extra}">{_html.escape(s["personal_notes"])}</div>'

        # Avatar (only if attended)
        av_html = f'<img src="{AVATAR}" class="slide-avatar" />' if s["attended"] else ""

        # Right column
        right_html = f'<div class="slide-right">{note_html}{av_html}</div>'

        # Bullets (max 4)
        bullets_html = "".join(
            f"<li>{_html.escape(b)}</li>" for b in s["highlights"][:4]
        ) or "<li>Voir le résumé complet.</li>"

        # Resume (inline, single paragraph)
        resume = _html.escape(s.get("resume", "").replace("\n", " ").strip())

        # Speaker line
        sep = ' <span style="color:var(--t5)">·</span> '
        speaker_line = _html.escape(s["speaker_name"])
        if company_html:
            speaker_line += sep + company_html

        return f"""<div class="slide" style="--tc:{s['theme_color']}">
  <div class="slide-top">
    <span class="theme-badge" style="background:{s['theme_color']}">{_html.escape(s['theme'])}</span>
    <span class="slide-counter">{i+1} / {total}</span>
  </div>
  <div class="slide-title">{_html.escape(s['title'])}</div>
  <div class="slide-speaker">{speaker_line}</div>
  <div class="slide-body">
    <div class="slide-left">
      <div class="slide-resume">{resume}</div>
      <div class="slide-bullets"><ul>{bullets_html}</ul></div>
      <div class="slide-chips">{chips_html}</div>
    </div>
    {right_html}
  </div>
</div>"""

    def make_slide_html(i, item):
        t = item.get("type", "talk")
        if t == "intro":    return make_intro_html(i)
        if t == "section":  return make_section_html(i, item)
        if t == "excluded": return make_excluded_html(i, item)
        if t == "rate":     return make_rate_html(i, item)
        return make_talk_html(i, item)

    slides_html = "\n".join(make_slide_html(i, it) for i, it in enumerate(all_items))

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  {THEME_HEAD}
  <title>AlpOSS 2026 — Diaporama</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Caveat:wght@500&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
  <style>{css}{DISCLAIMER_CSS}</style>
</head>
<body>
{TOGGLE_BTN}
{slides_html}
<div id="tip">
  <button class="tip-close" onclick="hideTip()">✕</button>
  <div class="tip-body"></div>
</div>
<div class="controls">
  <div class="progress-bar" style="width:0%"></div>
  <div class="ctrl-inner">
    <button class="ctrl-btn" id="ctrl-prev" onclick="showSlide(cur-1)">← Précédent</button>
    <span class="ctrl-hint">⚠️ Contenu généré par IA · peut contenir des erreurs &nbsp;|&nbsp; ← → ou Espace</span>
    <button class="ctrl-btn" id="ctrl-next" onclick="showSlide(cur+1)">Suivant →</button>
  </div>
</div>
<script>
{js}
</script>
{DISCLAIMER}
</body>
</html>"""


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    talks  = load_talks()
    slides = load_slides()

    for version, fn, data in [
        ("a", version_a, talks),
        ("b", version_b, talks),
        ("c", lambda d: version_c(d, talks), slides),
    ]:
        out_dir = os.path.join(BASE, "site", version)
        os.makedirs(out_dir, exist_ok=True)
        html_out = fn(data)
        out_path = os.path.join(out_dir, "index.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_out)
        size = os.path.getsize(out_path)
        print(f"  site/{version}/index.html  ({size // 1024} KB)")

    print("Done.")

if __name__ == "__main__":
    main()
