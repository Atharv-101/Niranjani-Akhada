import re
import os

file_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada/gallery.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

items = []
for i in range(1, 156):
    num_str = f"{i:02d}"  # 01, 02 ... 99, 100 ... 155
    delay = ((i - 1) % 3) * 0.2
    delay_str = f' data-wow-delay="{delay:.1f}s"' if delay > 0 else ''
    
    item = f"""                <div class="col-lg-4 col-6">
                    <!-- Image Gallery start -->
                    <div class="photo-gallery wow fadeInUp"{delay_str}>
                        <a href="images/gallary/{num_str}.jpg" data-cursor-text="View">
                            <figure class="image-anime">
                                <img src="images/gallary/{num_str}.jpg" alt="">
                            </figure>
                        </a>
                    </div>
                    <!-- Image Gallery end -->
                </div>"""
    items.append(item)

gallery_html = "\n".join(items)

# The pattern looks for the container and everything up to <!-- gallery section end -->
pattern = re.compile(r'(<div class="row gallery-items page-gallery-box">\s*).*?(</div>\s*<!-- gallery section end -->)', re.DOTALL)

new_content = pattern.sub(r'\1' + gallery_html + r'\n            \2', content)

if new_content != content:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Gallery successfully updated with 155 items.")
else:
    print("Could not find the target section to replace.")
