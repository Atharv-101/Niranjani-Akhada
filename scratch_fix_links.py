import os
import re

directory = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

# Known broken links from previous run
broken_links = [
    '404.html', 'blog-single.html', 'blog.html', 'contact.html',
    'faqs.html', 'image-gallery.html', 'index-2.html', 'index-3.html',
    'ministries.html', 'ministry-single.html', 'pastor-single.html', 'pastor.html',
    'sermon-single.html', 'sermons.html', 'service-single.html', 'services.html',
    'tel:123456789', 'tel:75240 42567', 'tel:9219140262', 'testimonials.html', 'video-gallery.html'
]

for file in html_files:
    file_path = os.path.join(directory, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    for broken_link in broken_links:
        # replace exact matches in href
        content = content.replace(f'href="{broken_link}"', 'href="#"')
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed links in {file}")

print("Link fix complete.")
