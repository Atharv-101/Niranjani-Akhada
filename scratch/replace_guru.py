import re
import json

guru_html_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada/guru_tradition.html'
history_html_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada/history.html'
lang_js_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada/js/lang.js'

with open(guru_html_path, 'r', encoding='utf-8') as f:
    guru_content = f.read()

with open(history_html_path, 'r', encoding='utf-8') as f:
    history_content = f.read()

# Extract the header and footer from guru_tradition.html
header_match = re.search(r'(.*?)<!-- Page Header Section Start -->', guru_content, re.DOTALL)
footer_match = re.search(r'(<!-- Main Footer Start -->.*)', guru_content, re.DOTALL)

if not header_match or not footer_match:
    print("Could not find header or footer in guru_tradition.html")
    exit(1)

guru_header = header_match.group(1)
guru_footer = footer_match.group(1)

# Now extract the page content from history.html as a base template
content_match = re.search(r'(<!-- Page Header Section Start -->.*?)<!-- Main Footer Start -->', history_content, re.DOTALL)
if not content_match:
    print("Could not find content in history.html")
    exit(1)

page_content = content_match.group(1)

# Now we need to modify page_content to fit Guru Tradition
# 1. Update Breadcrumb and Header
page_content = page_content.replace('data-i18n="history_1">इतिहास</h1>', 'data-i18n="guru_1">गुरु परंपरा</h1>')

# 2. Update the main headings and paragraphs
# history_10 -> guru_2
page_content = page_content.replace('data-i18n="history_10">श्री पंचायती अखाड़ा श्री निरंजनी का इतिहास</h2>', 'data-i18n="guru_2">निरंजनी अखाड़े की गुरु-शिष्य परंपरा</h2>')

# history_11 -> guru_3
page_content = re.sub(
    r'<p class="wow fadeInUp" style="[^"]*" data-i18n="history_11">.*?</p>',
    '<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;" data-i18n="guru_3">सनातन धर्म में गुरु का स्थान सर्वोच्च माना गया है। गुरु वह प्रकाश है जो शिष्य के जीवन से अज्ञान का अंधकार दूर कर उसे आत्मज्ञान की ओर ले जाता है। श्री पंचायती अखाड़ा श्री निरंजनी में अखंड गुरु-शिष्य परंपरा सदियों से चली आ रही है, जो अखाड़े की आध्यात्मिक शक्ति का मूल स्रोत है।<br><br>इस परंपरा के अंतर्गत, एक संन्यासी अपना सर्वस्व त्याग कर गुरु की शरण में जाता है और गुरु उसे सन्यास धर्म, तपस्या एवं वैदिक ज्ञान की दीक्षा प्रदान करते हैं।</p>',
    page_content, flags=re.DOTALL
)

# history_12 -> guru_4
page_content = page_content.replace('data-i18n="history_12">स्थापना एवं उद्देश्य</h2>', 'data-i18n="guru_4">दीक्षा और संस्कार</h2>')

# history_13 -> guru_5
page_content = re.sub(
    r'<p class="wow fadeInUp" style="[^"]*" data-i18n="history_13">.*?</p>',
    '<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;" data-i18n="guru_5">निरंजनी अखाड़े में संन्यास दीक्षा का विशेष महत्व है। गुरु अपने शिष्य को महावाक्यों का उपदेश देते हैं और उसे धर्म रक्षा तथा समाज कल्याण के प्रति समर्पित होने का संकल्प दिलाते हैं। यह दीक्षा संस्कार शिष्य के पुनर्जन्म के समान माना जाता है, जहाँ वह अपने पूर्व जीवन और मोह को त्याग कर एक नया आध्यात्मिक जीवन प्रारंभ करता है।</p>',
    page_content, flags=re.DOTALL
)

# history_14 -> guru_6
page_content = page_content.replace('data-i18n="history_14">गुरु-शिष्य परंपरा</h2>', 'data-i18n="guru_6">वर्तमान आचार्य और नेतृत्व</h2>')

# history_15 -> guru_7
page_content = re.sub(
    r'<p class="wow fadeInUp" style="[^"]*" data-i18n="history_15">.*?</p>',
    '<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;" data-i18n="guru_7">अखाड़े की संपूर्ण आध्यात्मिक और प्रशासनिक व्यवस्था आचार्य महामंडलेश्वर के मार्गदर्शन में संचालित होती है। वर्तमान में, परमहंस परिव्राजकाचार्य श्रीमद् ब्रह्मनिष्ठ पूज्यपाद श्री निरंजन पीठाधीश्वर श्री श्री 1008 आचार्य महामण्डलेश्वर स्वामी श्री कैलाशानन्द गिरि जी महाराज अखाड़े का नेतृत्व कर रहे हैं। उनके सानिध्य में अखाड़ा निरंतर प्रगति के पथ पर अग्रसर है।</p>',
    page_content, flags=re.DOTALL
)

# history_16 -> guru_8
page_content = page_content.replace('data-i18n="history_16">कुंभ पर्व में निरंजनी अखाड़ा</h2>', 'data-i18n="guru_8">तप, ज्ञान और सेवा का मार्ग</h2>')

# history_17 -> guru_9
page_content = re.sub(
    r'<p class="wow fadeInUp" style="[^"]*" data-i18n="history_17">.*?</p>',
    '<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;" data-i18n="guru_9">अखाड़े की गुरु परंपरा केवल वेद-शास्त्रों के अध्ययन तक सीमित नहीं है, बल्कि यह कठोर तपस्या, हठयोग और मानव सेवा का भी एक व्यावहारिक मार्ग है। गुरु अपने शिष्यों को अखाड़े की मढ़ियों, आश्रमों और कुंभ जैसे महापर्वों के दौरान धर्म के प्रचार-प्रसार के लिए तैयार करते हैं।</p>',
    page_content, flags=re.DOTALL
)

# Remove the extra sections (history_18, history_19, history_8, history_20)
# We will just cut them out using regex
page_content = re.sub(r'<br><br><br>\s*<h2 class="text-anime-style-3" id="5" data-i18n="history_18">.*?</div>', '</div>', page_content, flags=re.DOTALL)
# The above regex might be too greedy, let\'s be careful.
# Let's just string replace the HTML we don't want, or construct a fresh string.
# Actually, the page structure is:
# <h2 id="5">...</h2> <p>...</p> <br><br><br> <h2 id="6">...</h2> <p>...</p> <br><br><br><br>
# Let's write a targeted regex.
