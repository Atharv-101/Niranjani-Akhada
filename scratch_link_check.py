import os
import re

directory = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

links = set()
for file in html_files:
    with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
        content = f.read()
        found = re.findall(r'href="([^"]+)"', content)
        for link in found:
            if not link.startswith('http') and not link.startswith('#') and not link.startswith('mailto:'):
                links.add(link)

print("Local links found in HTML files:")
for link in sorted(links):
    if '#' in link: link = link.split('#')[0]
    if link == '': continue
    
    path = os.path.join(directory, link)
    if os.path.exists(path):
        print(f"[OK] {link}")
    else:
        print(f"[BROKEN] {link}")
