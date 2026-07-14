import os
import re

dir_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada'
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

# We want to replace href="#" with the correct links in the navbar.
replacements = [
    (r'<a class="nav-link" data-i18n="auto_key_7"\s*href="[^"]*">महामंडलेश्वर</a>', r'<a class="nav-link" data-i18n="auto_key_7" href="Swami-Kailashanand-Giri-Jii.html">महामंडलेश्वर</a>'),
    (r'<a class="nav-link" data-i18n="auto_key_8"\s*href="[^"]*">महंत</a>', r'<a class="nav-link" data-i18n="auto_key_8" href="Mahant-Ravinder-Puri.html">महंत</a>'),
    (r'<a class="nav-link" data-i18n="auto_key_28"\s*href="[^"]*">चित्रावली</a>', r'<a class="nav-link" data-i18n="auto_key_28" href="gallery.html">चित्रावली</a>'),
    (r'<a class="nav-link" data-i18n="auto_key_29"\s*href="[^"]*">समाचार</a>', r'<a class="nav-link" data-i18n="auto_key_29" href="news.html">समाचार</a>')
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
