import os

dir_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada'
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

for file in html_files:
    file_path = os.path.join(dir_path, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'js/lang.js' not in content:
        # insert it before </body>
        content = content.replace('</body>', '<script src="js/lang.js"></script>\n</body>')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added lang.js to {file}")
