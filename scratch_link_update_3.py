import os
import re

dir_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada'
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

# List of tuples: (regex pattern for the data-i18n anchor, new href)
replacements = [
    # auto_key_20 -> history.html
    (r'(<a[^>]*data-i18n="auto_key_20"[^>]*)href="[^"]*"', r'\1href="history.html"'),
    # auto_key_21 -> guru_tradition.html
    (r'(<a[^>]*data-i18n="auto_key_21"[^>]*)href="[^"]*"', r'\1href="guru_tradition.html"'),
    # auto_key_24 -> madhiyas.html
    (r'(<a[^>]*data-i18n="auto_key_24"[^>]*)href="[^"]*"', r'\1href="madhiyas.html"'),
    # auto_key_31 -> contact.html
    (r'(<a[^>]*data-i18n="auto_key_31"[^>]*)href="[^"]*"', r'\1href="contact.html"')
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

print("Comprehensive interlink check and update complete.")
