import os
import re

dir_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada'
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

# Let's check the links present in index.html
with open(os.path.join(dir_path, 'index.html'), 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract all href attributes
hrefs = re.findall(r'href="([^"]+)"', index_content)
linked_htmls = set([h for h in hrefs if h.endswith('.html')])

print("Available HTML files:")
print(sorted(html_files))
print("\nHTML files linked in index.html:")
print(sorted(list(linked_htmls)))

print("\nMissing from index.html links:")
missing = set(html_files) - linked_htmls - set(['index.html'])
print(sorted(list(missing)))
