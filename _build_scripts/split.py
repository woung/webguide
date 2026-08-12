import re, os, json

with open('full.md', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

# --- Pass 1: strip junk artifact lines ---
cleaned = []
skip_next_blank_dupe = False
for i, ln in enumerate(lines):
    stripped = ln.strip()
    # drop empty/decorative headings like "#   {#section .TOC-Heading}", "# ", "## "
    if re.match(r'^#+\s*(\{#section \.TOC-Heading\})?\s*$', stripped):
        continue
    # drop stray bold-backslash line-break artifacts
    if stripped in ('**\\', '**'):
        continue
    # drop the lone big cover image at very top (image1.png is the WHO cover graphic)
    if 'media/image1.png' in ln and i < 5:
        continue
    cleaned.append(ln)

text = '\n'.join(cleaned)
# collapse 3+ blank lines to 1
text = re.sub(r'\n{3,}', '\n\n', text)
lines = text.split('\n')

# --- Pass 2: identify top-level split points ---
# Patterns: "# PART <roman>. <Title>", "# Chapter <n>. <Title>", "# Acknowledgments",
# "# Abbreviations", "# Executive summary", "# Chapter 26. Glossary", "# Chapter 27. Help and support"
section_re = re.compile(r'^# (PART [IVX]+\.\s*.+|Chapter \d+\.\s*.+|Acknowledgments|Abbreviations|Executive summary)\s*$')

sections = []  # list of dicts: {type, title, start_line}
for i, ln in enumerate(lines):
    m = section_re.match(ln.strip())
    if m:
        sections.append({'line': i, 'heading': ln.strip()})

# slice content
pieces = []
for idx, sec in enumerate(sections):
    start = sec['line']
    end = sections[idx+1]['line'] if idx+1 < len(sections) else len(lines)
    pieces.append({'heading': sec['heading'], 'content': lines[start:end]})

def slugify(s):
    s = re.sub(r'^(PART [IVX]+\.\s*|Chapter \d+\.\s*)', '', s)
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s

manifest = []
order = 0
part_title = None
os.makedirs('en/chapters', exist_ok=True)

for p in pieces:
    heading = p['heading']
    if heading.startswith('# PART'):
        part_title = re.sub(r'^# PART [IVX]+\.\s*', '', heading).strip()
        manifest.append({'type': 'part', 'title': part_title})
        continue
    order += 1
    slug = slugify(heading.replace('# ', ''))
    fname = f'{order:02d}-{slug}.qmd'
    body = '\n'.join(p['content']).strip() + '\n'
    with open(f'en/chapters/{fname}', 'w', encoding='utf-8') as f:
        f.write(body)
    disp_title = re.sub(r'^# ', '', heading)
    manifest.append({'type': 'chapter', 'file': f'chapters/{fname}', 'title': disp_title})

with open('manifest.json', 'w') as f:
    json.dump(manifest, f, indent=2)

print(f"Wrote {order} chapter files")
for m in manifest:
    print(m)
