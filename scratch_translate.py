import re
import os

directory = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada'
lang_file = os.path.join(directory, 'js/lang.js')

# Content to translate and its English version
translations = {
    # Kailashanand Giri
    "भूमिका एवं जिम्मेदारियाँ": "Roles & Responsibilities",
    "आचार्य महामण्डलेश्वर — श्री पंचायती अखाड़ा श्री निरंजनी": "Acharya Mahamandaleshwar - Shri Panchayati Akhada Shri Niranjani",
    "निरंजन पीठाधीश्वर": "Niranjan Peethadhishwar",
    "सर्वोच्च आध्यात्मिक गुरु — श्री पंचायती अखाड़ा श्री निरंजनी": "Supreme Spiritual Guru - Shri Panchayati Akhada Shri Niranjani",
    "सिद्धपीठ श्री दक्षिण काली मंदिर, हरिद्वार के पीठाधीश्वर": "Peethadhishwar of Siddhapeeth Shri Dakshin Kali Temple, Haridwar",
    "नागा संन्यास परंपरा के आध्यात्मिक मार्गदर्शक": "Spiritual Guide of Naga Sanyas Tradition",
    "सनातन धर्म एवं वेदांत के प्रचारक": "Preacher of Sanatan Dharma and Vedanta",
    "प्रेम का अर्थ सेवा है, और सेवा का अर्थ है ईश्वर को प्रसन्न करना।": "Love means service, and service means pleasing God.",
    
    # Ravinder Puri
    "सचिव — श्री पंचायती अखाड़ा श्री निरंजनी": "Secretary - Shri Panchayati Akhada Shri Niranjani",
    "अध्यक्ष — मनसा देवी मंदिर ट्रस्ट, हरिद्वार": "President - Mansa Devi Temple Trust, Haridwar",
    "अखिल भारतीय अखाड़ा परिषद के पूर्व अध्यक्ष": "Former President of All India Akhada Parishad",
    "सनातन धर्म और संस्कृति के प्रमुख संरक्षक": "Chief Patron of Sanatan Dharma and Culture",
    "हरिद्वार में धार्मिक और सामाजिक कार्यों के प्रमुख मार्गदर्शक": "Chief Guide of Religious and Social Works in Haridwar",
    "कुंभ मेले और धार्मिक आयोजनों के प्रमुख व्यवस्थापक": "Chief Organizer of Kumbh Mela and Religious Events",
    "नर सेवा ही नारायण सेवा है। सेवा वह है जिसमें न कोई अपेक्षा हो और न कोई स्वार्थ।": "Service to humanity is service to God. True service is one with no expectation and no selfishness."
}

# 1. Update lang.js
with open(lang_file, 'r', encoding='utf-8') as f:
    lang_content = f.read()

# We need to insert keys into "en: {" and "hi: {"
# Let's use custom keys like "new_custom_X"
custom_keys = {}
for i, (hi_text, en_text) in enumerate(translations.items(), 1):
    key = f"new_custom_{i}"
    custom_keys[hi_text] = key

en_additions = ""
hi_additions = ""
for hi_text, key in custom_keys.items():
    en_text = translations[hi_text]
    en_additions += f'    "{key}": "{en_text}",\n'
    hi_additions += f'    "{key}": "{hi_text}",\n'

# Insert into lang.js
lang_content = re.sub(r'(en: {)', r'\1\n' + en_additions, lang_content)
lang_content = re.sub(r'(hi: {)', r'\1\n' + hi_additions, lang_content)

with open(lang_file, 'w', encoding='utf-8') as f:
    f.write(lang_content)

# 2. Update HTML files
html_files = ['Swami-Kailashanand-Giri-Jii.html', 'Mahant-Ravinder-Puri.html']
for file in html_files:
    file_path = os.path.join(directory, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    for hi_text, key in custom_keys.items():
        # Replace occurrences in HTML with span wrapped version if not already wrapped
        # We assume it's just plain text inside h2, h3, or p.
        if hi_text in html and f'data-i18n="{key}"' not in html:
            html = html.replace(hi_text, f'<span data-i18n="{key}">{hi_text}</span>')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Translations successfully integrated!")
