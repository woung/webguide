# EWARS in a Box — Web User Guide (Quarto)

Converted from `Web_User_Guide_2026_Version.docx` into a multi-language
Quarto **book** (sidebar table of contents, search, numbered chapters).

## Structure

```
webguide/
├── en/                  ← English edition (complete — 30 chapters + landing page)
│   ├── _quarto.yml
│   ├── index.qmd
│   ├── chapters/        ← one .qmd per chapter
│   └── media/           ← 878 extracted images
├── fr/                  ← French edition (scaffolded, pending translation)
├── es/                  ← Spanish edition (scaffolded, pending translation)
├── ar/                  ← Arabic edition (scaffolded, pending translation, RTL)
├── shared/
│   ├── theme.scss       ← color palette, type, sidebar styling
│   └── styles.css       ← abbreviation grid, language cards, RTL overrides
└── _build_scripts/      ← the scripts used to split/clean the source docx (reference only)
```

Each language is its **own Quarto book project** with a matching chapter/file
layout, so filenames line up 1:1 across `en/`, `fr/`, `es/`, `ar/` — a
translator can open e.g. `fr/chapters/06-locations.qmd` and translate the
English `en/chapters/06-locations.qmd` content directly into it. A language
switcher (🌐) sits in the top navbar of every edition, and each landing page
has language cards showing what's complete vs. pending.

## Rendering

This sandbox doesn't have the Quarto CLI installed (and has no network
access to install it), so I wasn't able to render a live preview here. The
project has been validated as far as possible without Quarto itself — all
`_quarto.yml` files parse as valid YAML, every chapter file referenced in
each book config exists on disk, and all 1,469 image references resolve to
real extracted files.

On your machine, with [Quarto installed](https://quarto.org/docs/get-started/):

```bash
cd en
quarto preview        # live-reload local preview
# or
quarto render         # static site build → ../_site/en
```

Do the same inside `fr/`, `es/`, or `ar/` for those editions.

## What was done to the source

- Converted via `pandoc` with `--extract-media` (878 images).
- Split the ~17,000-line document into 30 chapter files at each
  `Chapter N.` / `PART` / front-matter heading.
- Removed Word-conversion artifacts: empty TOC-placeholder headings, stray
  bold/line-break remnants, escaped brackets, `{.mark}`/`{.underline}`
  spans, invisible LTR/RTL marks.
- Reflowed the Abbreviations list into a styled two-column definition grid.
- Fixed a footnote whose definition had landed in the wrong chapter after
  splitting.
- Grid tables (from Word tables) convert cleanly to Pandoc grid-table
  markdown and didn't need manual rework.

## Design

Teal/emerald palette (`#0B3D3A` / `#0B6E4F`) instead of default Quarto blue,
`Newsreader` serif for headings paired with `Inter` for body text and
`JetBrains Mono` for code/UI labels, a floating sidebar with an emerald
active-item indicator, responsive images with a subtle card treatment, and
amber-accented callout blockquotes. `shared/styles.css` includes RTL
overrides (`html[dir="rtl"]`) so the Arabic edition mirrors correctly.

## Adding a translation

1. Open a chapter in `fr/`, `es/`, or `ar/` (same filename as its `en/`
   counterpart).
2. Replace the placeholder banner and title with the translated content,
   keeping the same `# Heading` levels so the sidebar TOC and
   cross-references stay intact.
3. Image paths can point back at `../en/media/...` (already used in the
   placeholders) since the source images aren't language-specific.
# webguide1
