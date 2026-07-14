import re

guru_html_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada/guru_tradition.html'
history_html_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada/history.html'

with open(guru_html_path, 'r', encoding='utf-8') as f:
    guru_content = f.read()

with open(history_html_path, 'r', encoding='utf-8') as f:
    history_content = f.read()

header_match = re.search(r'(<!-- Header Start -->.*?<!-- Header End -->)', history_content, re.DOTALL)
if header_match:
    header_content = header_match.group(1)
    
    # In guru content, replace the empty header block
    guru_content = re.sub(r'<!-- Header Start -->\s*<!-- Header End -->', header_content, guru_content, flags=re.DOTALL)
    
    # Now let's fix the grid to use Bootstrap classes and make text center-aligned.
    # The grid was: <div class="service-benefit-item-list" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 40px;">
    # Let's replace it with: <div class="row service-benefit-item-list" style="margin-top: 40px;">
    
    grid_start = '<div class="service-benefit-item-list" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 40px;">'
    new_grid_start = '<div class="row service-benefit-item-list" style="margin-top: 40px;">'
    guru_content = guru_content.replace(grid_start, new_grid_start)
    
    # Now replace the <div class="service-benefit-item wow fadeInUp"... with <div class="col-md-4 mb-4"><div class="service-benefit-item wow fadeInUp"...
    # We will use regex
    
    item_pattern = r'(<!-- Service Benefit Item Start -->\s*)(<div class="service-benefit-item wow fadeInUp".*?</div>\s*<!-- Service Benefit Item End -->)'
    # We need to wrap group 2 in <div class="col-md-4 mb-4"></div>
    # Let's do it carefully
    
    def wrap_item(match):
        return match.group(1) + '<div class="col-md-4 mb-4">\n' + match.group(2) + '\n</div>'
    
    # Actually, the regex needs to capture the whole div. The div has nested divs. 
    # Let's just string replace the known starting tags.
    
    item_start = '<div class="service-benefit-item wow fadeInUp"'
    new_item_start = '<div class="col-md-4 mb-4">\n<div class="service-benefit-item wow fadeInUp"'
    
    item_end = '</div>\n                                    <!-- Service Benefit Item End -->'
    new_item_end = '</div>\n</div>\n                                    <!-- Service Benefit Item End -->'
    
    guru_content = guru_content.replace(item_start, new_item_start)
    guru_content = guru_content.replace(item_end, new_item_end)

    # Make the main paragraph center-aligned
    old_p = '<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;">गुरु परंपरा भारतीय सनातन संस्कृति की आत्मा है।'
    new_p = '<p class="wow fadeInUp" style="text-align: center; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;">गुरु परंपरा भारतीय सनातन संस्कृति की आत्मा है।'
    guru_content = guru_content.replace(old_p, new_p)

    with open(guru_html_path, 'w', encoding='utf-8') as f:
        f.write(guru_content)
    print("Success")
else:
    print("Failed to find header")
