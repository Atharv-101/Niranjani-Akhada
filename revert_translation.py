from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Remove all data-i18n and data- i18n attributes
for tag in soup.find_all(True):
    if tag.has_attr('data-i18n'):
        del tag['data-i18n']
    if tag.has_attr('data- i18n'):
        del tag['data- i18n']

# Remove the language toggle button
# <a href="#" id="lang-toggle-btn" ...>
btn = soup.find(id="lang-toggle-btn")
if btn:
    # Also remove its parent <div class="header-btn" style="margin-left: 10px;"> if it's there
    parent = btn.parent
    if parent and parent.name == 'div' and 'header-btn' in parent.get('class', []):
        parent.decompose()
    else:
        btn.decompose()

# Remove the script tag for js/lang.js
script = soup.find("script", src="js/lang.js")
if script:
    script.decompose()

with open("index_reverted.html", "w", encoding="utf-8") as f:
    f.write(str(soup))
