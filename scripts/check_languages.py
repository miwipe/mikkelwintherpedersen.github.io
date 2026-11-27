"""Check translations containing official names and their generated pages."""
from pathlib import Path
from html import escape
import runpy

root = Path(__file__).resolve().parents[1]
site = runpy.run_path(str(root / 'scripts/build.py'))
for english, danish in site['translations'].items():
    assert site['translate'](english) == danish, english

cases = {
    'about.html': 'I am an Associate Professor at the Globe Institute, University of Copenhagen, and lead the Palaeo-Environmental Genomics Group. My work brings together geography, genetics and bioinformatics to reconstruct past ecosystems and explore their responses to climate and human activity.',
    'press.html': site['bio'],
}
for filename, english in cases.items():
    danish = site['translations'][english]
    da_page = (root / filename).read_text(encoding='utf-8')
    en_page = (root / 'en' / filename).read_text(encoding='utf-8')
    assert danish in da_page
    assert english not in da_page
    assert english in en_page
    assert danish not in en_page

for filename in ('index.html', 'about.html', 'group.html', 'talks.html', 'press.html'):
    da_page = (root / filename).read_text(encoding='utf-8')
    en_page = (root / 'en' / filename).read_text(encoding='utf-8')
    assert '__PROPER_NAME_' not in da_page
    assert '<html lang="da">' in da_page
    assert '<html lang="en">' in en_page
    assert 'Københavns Universitet' not in en_page
    for english, danish in site['translations'].items():
        if len(english) > 100 and english != danish:
            assert english not in da_page, (filename, english)
print('Translation checks passed: complete passages, official names and language separation.')
