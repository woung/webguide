import json, sys
sys.path.insert(0, '.')
from scaffold_langs import TITLES, LANG_META

manifest = json.load(open('manifest.json'))

NAV_LABELS = {
  'fr': {'lang_menu': 'Langue', 'en': 'English', 'fr': 'Français', 'es': 'Español', 'ar': 'العربية'},
  'es': {'lang_menu': 'Idioma', 'en': 'English', 'fr': 'Français', 'es': 'Español', 'ar': 'العربية'},
  'ar': {'lang_menu': 'اللغة', 'en': 'English', 'fr': 'Français', 'es': 'Español', 'ar': 'العربية'},
}

TEMPLATE = """project:
  type: book
  output-dir: ../_site/{lang}

lang: {lang}
dir: {dir}

book:
  title: "{book_title}"
  subtitle: "{book_sub}"
  author: "WHO Health Emergencies Programme"
  date: last-modified
  page-footer:
    left: "© World Health Organization, 2026"
    right: "Built with Quarto"
  favicon: ../en/media/image1.png
  search: true
  page-navigation: true
  back-to-top-navigation: true
  sidebar:
    style: floating
    collapse-level: 1
    pinned: true
  navbar:
    left: []
    right:
      - text: "🌐 {lang_menu}"
        menu:
          - text: "{t_en}"
            file: ../en/index.qmd
          - text: "{t_fr}"
            file: ../fr/index.qmd
          - text: "{t_es}"
            file: ../es/index.qmd
          - text: "{t_ar}"
            file: ../ar/index.qmd
  chapters:
    - index.qmd
{chapters_yaml}

format:
  html:
    theme:
      light: [cosmo, ../shared/theme.scss]
    css: ../shared/styles.css
    toc: true
    toc-depth: 3
    number-sections: true
    number-depth: 2
    code-copy: true
    smooth-scroll: true
    highlight-style: github
    mainfont: "Inter"
    monofont: "JetBrains Mono"
    fontsize: 1rem
    linkcolor: "#0B6E4F"
    grid:
      sidebar-width: 300px
      body-width: 850px
      margin-width: 250px
"""

for lang in ('fr', 'es', 'ar'):
    lines = []
    in_part = False
    for entry in manifest:
        if entry['type'] == 'part':
            title_l = TITLES[lang].get(entry['title'], entry['title'])
            lines.append(f'    - part: "{title_l}"')
            lines.append('      chapters:')
            in_part = True
        else:
            fname = entry['file']  # e.g. chapters/04-xxx.qmd
            prefix = '        - ' if in_part else '    - '
            lines.append(prefix + fname)
    chapters_yaml = '\n'.join(lines)

    meta = LANG_META[lang]
    nl = NAV_LABELS[lang]
    yml = TEMPLATE.format(
        lang=lang,
        dir=meta['dir'],
        book_title=meta['book_title'],
        book_sub=meta['book_sub'],
        lang_menu=nl['lang_menu'],
        t_en=nl['en'], t_fr=nl['fr'], t_es=nl['es'], t_ar=nl['ar'],
        chapters_yaml=chapters_yaml,
    )
    with open(f'{lang}/_quarto.yml', 'w', encoding='utf-8') as f:
        f.write(yml)
    print(f'--- {lang}/_quarto.yml chapters block ---')
    print(chapters_yaml[:500])
