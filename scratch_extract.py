from bs4 import BeautifulSoup, NavigableString
import json
import re
import os

files = ['news.html', 'madhiyas.html', 'history.html', 'guru_tradition.html']
extracted = {}

for f in files:
    path = os.path.join('/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada', f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as fh:
            soup = BeautifulSoup(fh, 'html.parser')
            # Extract text from tags that don't have data-i18n
            for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'span', 'a']):
                # skip if already translated or inside header/footer which is already translated
                if tag.has_attr('data-i18n') or tag.find_parent('header') or tag.find_parent('footer') or tag.find_parent('nav'):
                    continue
                text = tag.get_text(strip=True)
                # If contains hindi
                if re.search(r'[\u0900-\u097F]', text):
                    # We only want leaf nodes (tags that contain the text directly)
                    if len(tag.find_all()) == 0 or (len(tag.find_all()) == 1 and tag.find('br')):
                        extracted[text] = ""

with open('/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada/extracted_hindi.json', 'w', encoding='utf-8') as fh:
    json.dump(extracted, fh, ensure_ascii=False, indent=2)

print(f"Extracted {len(extracted)} unique strings.")
