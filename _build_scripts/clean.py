import re, glob

FN_TEXT = "[^1]: Emergency response framework (ERF), second edition. Geneva: World Health Organization; 2017 (https://apps.who.int/iris/handle/10665/258604, accessed 4 April 2022).\n"

for path in glob.glob('en/chapters/*.qmd'):
    with open(path, encoding='utf-8') as f:
        t = f.read()

    orig = t

    # remove the misplaced footnote def from wherever it landed
    t = re.sub(r'\n\[\^1\]:.*\n?', '\n', t)

    # strip invisible LTR/RTL marks left over from Word
    t = t.replace('\u200e', '').replace('\u200f', '')

    # unwrap {.mark} and {.underline} spans -> plain text
    t = re.sub(r'\[([^\]]*?)\]\{\.mark\}', r'\1', t)
    t = re.sub(r'\[([^\]]*?)\]\{\.underline\}', r'\1', t)

    # unescape common pandoc-escaped punctuation
    t = t.replace('\\[', '[').replace('\\]', ']')
    t = t.replace('\\%', '%').replace('\\$', '$').replace('\\_', '_')

    # collapse excess blank lines again after edits
    t = re.sub(r'\n{3,}', '\n\n', t)

    if path.endswith('04-overview-of-ewars-in-a-box.qmd'):
        t = t.rstrip() + '\n\n' + FN_TEXT

    if t != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(t)
        print('cleaned', path)
