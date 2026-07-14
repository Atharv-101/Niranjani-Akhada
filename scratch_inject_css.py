import os
import re

directory = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada'
html_files = ['index.html', 'about.html', 'history.html', 'guru_tradition.html', 'madhiyas.html', 'mahant.html']

css_to_inject = """
<!-- Modern Typography and Styling Overrides -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
    :root {
        --primary-font: 'Outfit', sans-serif !important;
        --secondary-font: 'Inter', sans-serif !important;
        --text-color: #333;
        --shadow-soft: 0 10px 30px rgba(0, 0, 0, 0.08);
    }
    body, p, span, li, a {
        font-family: var(--secondary-font) !important;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: var(--primary-font) !important;
        font-weight: 600;
        letter-spacing: -0.3px;
    }
    /* Page Header Enhancement */
    .page-header-box h1 {
        font-size: 2.8rem;
        color: #ffffff !important;
        text-shadow: 2px 2px 15px rgba(0,0,0,0.8);
        letter-spacing: -0.5px;
        margin-bottom: 20px;
    }
    .page-header-box h1 .line, .page-header-box h1 .word, .page-header-box h1 .char {
        color: #ffffff !important;
    }
    /* Fix messy headings generally */
    .section-title h2 {
        line-height: 1.3;
        margin-bottom: 15px;
    }
    /* Clean up general typography */
    p {
        line-height: 1.7;
        color: #555;
    }
</style>
"""

for file in html_files:
    file_path = os.path.join(directory, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "Modern Typography and Styling Overrides" not in content:
        # Inject just before </head>
        content = content.replace('</head>', f'{css_to_inject}\n</head>')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected modern CSS into {file}")

print("CSS injection complete.")
