import json
import os
import re

translations = {
    "संपर्क करें": "Contact us",
    "मुख्य पृष्ठ": "home",
    "संपर्क में रहें": "Get in touch",
    "श्री निरंजनी अखाड़े से संपर्क करें": "Contact Our Church For Prayer Support",
    "अखाड़े से संबंधित किसी भी जानकारी, धार्मिक आयोजनों अथवा अन्य आध्यात्मिक कार्यों के लिए आप हमसे संपर्क कर सकते हैं।": "We would love to hear from you. Whether you have prayer requests, questions about our services, or want to get involved in our ministries,",
    "ईमेल आईडी": "Email Address",
    "फ़ोन नंबर": "Phone Number",
    "हमारा पता": "Our Location",
    "श्री पंचायती अखाड़ा निरंजनी, दारागंज, प्रयागराज": "123 Faith Avenue, Near Peace GardenJubilee Road,",
    "अपना संदेश हमें भेजें": "Share Your Prayer Requests Here",
    "पहला नाम": "First Name",
    "अंतिम नाम": "Last Name",
    "संदेश": "Message",
    "संदेश भेजें": "Send Message",
    "हमारा स्थान": "Where We Locateda",
    "आसानी से हमारा अखाड़ा खोजें": "Find Our Church Location Easily",
    "हमारा अखाड़ा एक शांतिपूर्ण और सुलभ क्षेत्र में स्थित है, जहाँ आकर आप आध्यात्मिक शांति और संत समागम का लाभ उठा सकते हैं।": "Our church is conveniently located in a peaceful and easily accessible area, making it simple for individuals and families to join us for worship, fellowship"
}

dir_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada'
lang_file = os.path.join(dir_path, 'js/lang.js')

with open(lang_file, 'r', encoding='utf-8') as f:
    lang_content_fresh = f.read()

en_json_str = ""
hi_json_str = ""
custom_keys = {}

start_idx = 100
for hi_text, en_text in translations.items():
    key = f"auto_page_content_contact_{start_idx}"
    custom_keys[hi_text] = key
    en_json_str += f'    "{key}": {json.dumps(en_text, ensure_ascii=False)},\n'
    hi_json_str += f'    "{key}": {json.dumps(hi_text, ensure_ascii=False)},\n'
    start_idx += 1

lang_content_fresh = lang_content_fresh.replace('en: {', 'en: {\n' + en_json_str)
lang_content_fresh = lang_content_fresh.replace('hi: {', 'hi: {\n' + hi_json_str)

with open(lang_file, 'w', encoding='utf-8') as f:
    f.write(lang_content_fresh)

# Update contact.html
contact_file = os.path.join(dir_path, 'contact.html')
with open(contact_file, 'r', encoding='utf-8') as fh:
    html = fh.read()

for hi_text, key in custom_keys.items():
    # Only wrap if not already wrapped
    if f'data-i18n="{key}"' not in html:
        # Avoid wrapping placeholders because placeholder attributes can't contain HTML tags.
        # So we skip placeholders.
        if hi_text in ['पहला नाम', 'अंतिम नाम', 'संदेश', 'ईमेल आईडी', 'फ़ोन नंबर']:
            # For these, they might be inside placeholder="" OR they might be in text (like labels).
            # We will ignore placeholders for data-i18n injection for now to avoid breaking HTML.
            html = html.replace(f'>{hi_text}<', f'><span data-i18n="{key}">{hi_text}</span><')
        else:
            html = html.replace(hi_text, f'<span data-i18n="{key}">{hi_text}</span>')

# Add lang.js and mobile menu to contact.html if missing
if 'js/lang.js' not in html:
    html = html.replace('</body>', '<script src="js/lang.js"></script>\n</body>')
    
if 'mobile-lang-wrapper' not in html:
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
                    
    html = html.replace("</style>", f"{css_to_add}\n</style>")
    pattern = re.compile(r'<!-- Main Menu End -->\s*<div class="navbar-toggle"></div>')
    html = pattern.sub(html_to_add, html)

with open(contact_file, 'w', encoding='utf-8') as fh:
    fh.write(html)

print("Contact page wrapped in data-i18n and updated with lang.js")
