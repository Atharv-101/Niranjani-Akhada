import os
import re

dir_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada'
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

# More robust replacements focusing on the data-i18n keys
replacements = [
    (r'(<a[^>]*data-i18n="auto_key_7"[^>]*)href="[^"]*"', r'\1href="Swami-Kailashanand-Giri-Jii.html"'),
    (r'(<a[^>]*data-i18n="auto_key_8"[^>]*)href="[^"]*"', r'\1href="Mahant-Ravinder-Puri.html"'),
    (r'(<a[^>]*data-i18n="auto_key_28"[^>]*)href="[^"]*"', r'\1href="gallery.html"'),
    (r'(<a[^>]*data-i18n="auto_key_29"[^>]*)href="[^"]*"', r'\1href="news.html"')
]

for file in html_files:
    file_path = os.path.join(dir_path, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
        
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated links in {file}")

print("Interlink check and update complete.")
