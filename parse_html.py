from bs4 import BeautifulSoup, NavigableString
import json

with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

translatable_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'a', 'li', 'button']
translations = {"hi": {}, "en": {}}
count = 1

# Only process body elements, skip the ones already processed
body = soup.find('body')
if body:
    for tag in body.find_all(translatable_tags):
        if not tag.has_attr('data-i18n'):
            text = tag.get_text(strip=True)
            if len(text) > 2 and text not in ["EN", "HI"]: # Ignore short meaningless strings or current language toggle
                key = f"auto_key_{count}"
                tag['data-i18n'] = key
                translations["hi"][key] = tag.decode_contents() # Keep inner html like <br>
                translations["en"][key] = "" # Empty for now, to be translated
                count += 1

with open("index_new.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

with open("translations_template.json", "w", encoding="utf-8") as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"Extracted {count-1} strings.")
