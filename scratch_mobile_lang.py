import os
import re

dir_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada'
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

css_to_add = """
    /* Mobile Language Button */
    .mobile-lang-wrapper {
        display: none;
        align-items: center;
    }
    @media (max-width: 991px) {
        .mobile-lang-wrapper {
            display: flex !important;
        }
        .main-header .navbar-toggle {
            margin-left: 10px;
        }
    }
"""

html_to_add = """                    <!-- Main Menu End -->
                    <div class="mobile-lang-wrapper">
                        <a class="btn-default" style="padding: 6px 12px; font-size: 13px;" href="#" onclick="toggleLanguage(); return false;">EN/HI</a>
                    </div>
                    <div class="navbar-toggle"></div>"""

for file in html_files:
    file_path = os.path.join(dir_path, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Add CSS before </style>
    if "/* Mobile Language Button */" not in content:
        content = content.replace("</style>", f"{css_to_add}\n</style>")
        
    # 2. Add Mobile Button next to navbar-toggle
    if "mobile-lang-wrapper" not in content:
        # Some files might have spaces or newlines between Main Menu End and navbar-toggle
        pattern = re.compile(r'<!-- Main Menu End -->\s*<div class="navbar-toggle"></div>')
        content = pattern.sub(html_to_add, content)
        
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

print("Mobile language button added to all pages.")
