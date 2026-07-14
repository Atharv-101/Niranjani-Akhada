import re

file_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada/gallery.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's extract the start index of <div class="row gallery-items page-gallery-box">
start_tag = '<div class="row gallery-items page-gallery-box">'
end_tag = '<!-- gallery section end -->'

start_idx = content.find(start_tag)
# The end might be <!-- gallery section end --> or something similar. Let's just find the next <!-- Pagination Start --> or similar, since this is a gallery page.
# Wait, let's find the closing </div> of the row.
