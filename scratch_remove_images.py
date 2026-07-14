import re

file_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada/Swami-Kailashanand-Giri-Jii.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for the gallery items
# We want to match:
# <div class="col-lg-4 col-6">\s*<div class="photo-gallery wow fadeInUp" data-wow-delay="[0-9.]+s">\s*<a href="images/SKG/(1[8-9]|2[0-5])\.jpg".*?</div>\s*</div>

pattern = re.compile(r'<div class="col-lg-4 col-6">\s*<div class="photo-gallery wow fadeInUp"[^>]*>\s*<a href="images/SKG/(?:18|19|20|21|22|23|24|25)\.jpg"[\s\S]*?</div>\s*</div>')

new_content = re.sub(pattern, '', content)

if content != new_content:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Removed missing images 18-25 from gallery.")
else:
    print("Pattern not found or already removed.")
