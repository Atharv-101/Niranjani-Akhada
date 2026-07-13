import json
from deep_translator import GoogleTranslator
import time
import re

with open('translations_template.json', 'r', encoding='utf-8') as f:
    translations = json.load(f)

translator = GoogleTranslator(source='hi', target='en')

# Keep the manually translated ones (from my previous run) intact if they exist
# Actually, the previous ones didn't use `auto_key_` they used `nav_home` etc.
# So I should combine them.
try:
    with open('js/lang.js', 'r', encoding='utf-8') as f:
        existing_js = f.read()
    # Extract the JS object if possible, but it's easier to just merge it here manually.
    # We will just append the new translations to a fresh lang.js structure.
except FileNotFoundError:
    pass

en_dict = {}
hi_dict = {}

print("Translating...")
total = len(translations["hi"].keys())
for i, key in enumerate(translations["hi"].keys()):
    hi_text = translations["hi"][key]
    
    # Strip HTML tags for translation if it's simple, or just translate raw.
    # GoogleTranslator handles basic HTML tags okay sometimes, but let's be careful.
    # The text we extracted with get_text is already somewhat stripped, but decode_contents might have <br>.
    # Wait, in the parse script, I used `tag.decode_contents()`, which includes HTML.
    
    # Let's just translate the text.
    try:
        # If it's pure English (like some links), just copy it
        if not re.search(r'[\u0900-\u097F]', hi_text):
            en_text = hi_text
        else:
            en_text = translator.translate(hi_text)
            time.sleep(0.1) # Be nice to the API
    except Exception as e:
        print(f"Error on {key}: {e}")
        en_text = hi_text # fallback
        
    en_dict[key] = en_text
    hi_dict[key] = hi_text
    if i % 10 == 0:
        print(f"{i}/{total} done")

# The existing translations we added manually earlier
manual_en = {
    "nav_home": "Home",
    "nav_about": "About Us",
    "nav_history": "History",
    "nav_guru_parampara": "Guru Parampara",
    "nav_maths": "Maths/Branches",
    "nav_saints": "Saints & Mahants",
    "nav_mahamandaleshwar": "Mahamandaleshwar",
    "nav_mahant": "Mahant",
    "nav_branches": "Akhada Branches",
    "nav_activities": "Activities",
    "nav_contact": "Contact",
    "hero_subtitle": "॥ Om Guru Niranjan Devay Namah ॥",
    "hero_title": "Panchayati Akhada Shri Niranjani",
    "hero_desc": "Inspired by the great Dashanami tradition of Adi Shankaracharya, Panchayati Akhada Shri Niranjani has been dedicated to the protection of Sanatan Dharma, the spread of spiritual consciousness, the preservation of saint traditions, and human welfare for centuries.",
    "hero_btn_about": "About Us",
    "hero_btn_history": "Know History",
    "hero_counter_1": "Centuries of Spiritual Tradition",
    "hero_counter_2": "Vast Group of Volunteers",
    "hero_counter_3": "Sanatan Dharma Service & Protection",
    "about_subtitle": "Our Story, Faith, Mission, and Vision",
    "about_title": "Panchayati Akhada Shri Niranjani",
    "about_desc": "Panchayati Akhada Shri Niranjani is a very ancient, radiant and prestigious branch of the Dashanami sect established by the great philosopher and religious propagator Adi Shankaracharya. This Akhada was established in Vikram Samvat 1429 (1472 AD).",
    "about_mission_title": "Guru Parampara",
    "about_mission_desc": "Conservation and promotion of the Dashanami Sanyas tradition established by Adi Guru Shankaracharya.",
    "about_vision_title": "Dharma & Social Service",
    "about_vision_desc": "Constantly dedicated to the propagation of Sanatan Dharma, spiritual awakening and public welfare.",
    "about_btn": "Learn More",
    "about_author": "Shri Mahant Ravindrapuri Maharaj",
    "about_author_title": "Secretary - Panchayati Akhada Shri Niranjani<br>President - Mansa Devi Temple Trust",
    "scrolling_text_1": "॥ Om Namah Shivay ॥",
    "scrolling_text_2": "॥ Om Guru Niranjan Dev Namah ॥"
}

manual_hi = {
    "nav_home": "मुख्यपृष्ठ",
    "nav_about": "हमारे बारे में",
    "nav_history": "इतिहास",
    "nav_guru_parampara": "गुरु परंपरा",
    "nav_maths": "मढ़ियाँ",
    "nav_saints": "संत एवं महंत",
    "nav_mahamandaleshwar": "महामंडलेश्वर",
    "nav_mahant": "महंत",
    "nav_branches": "अखाड़े की शाखाएँ",
    "nav_activities": "गतिविधियाँ",
    "nav_contact": "संपर्क",
    "hero_subtitle": "॥ ॐ गुरु निरंजन देवाय नमः ॥",
    "hero_title": "पंचायती अखाड़ा श्री निरंजनी",
    "hero_desc": "आदि शंकराचार्य की महान दशनामी परंपरा से प्रेरित, पंचायती अखाड़ा श्री निरंजनी सदियों से सनातन धर्म की रक्षा, आध्यात्मिक चेतना के प्रसार, संत परंपरा के संरक्षण तथा मानव कल्याण के लिए समर्पित है।",
    "hero_btn_about": "हमारे बारे में",
    "hero_btn_history": "इतिहास जानें",
    "hero_counter_1": "सदियों की आध्यात्मिक परंपरा",
    "hero_counter_2": "स्वयंसेवकों का विशाल समूह",
    "hero_counter_3": "सनातन धर्म सेवा एवं संरक्षण",
    "about_subtitle": "हमारी कहानी, आस्था, मिशन और विजन",
    "about_title": "पंचायती अखाड़ा श्री निरंजनी",
    "about_desc": "पंचायती अखाड़ा श्री निरंजनी, महान दार्शनिक एवं धर्मप्रवर्तक आदि शंकराचार्य द्वारा स्थापित दशनामी संप्रदाय की एक अत्यंत प्राचीन, तेजस्वी और प्रतिष्ठित शाखा है। इस अखाड़े की स्थापना विक्रम संवत १४२९ (ईस्वी १४७२) में हुई थी।",
    "about_mission_title": "गुरु परंपरा",
    "about_mission_desc": "आदि गुरु शंकराचार्य द्वारा स्थापित दशनामी संन्यास परंपरा का संरक्षण एवं संवर्धन।",
    "about_vision_title": "धर्म एवं समाज सेवा",
    "about_vision_desc": "सनातन धर्म के प्रचार, आध्यात्मिक जागरण एवं जनकल्याण के लिए निरंतर समर्पित।",
    "about_btn": "और अधिक जानें",
    "about_author": "श्री महंत रविन्द्रपुरी महाराज",
    "about_author_title": "सचिव – पंचायती अखाड़ा श्री निरंजनी <br> अध्यक्ष – मनसा देवी मंदिर ट्रस्ट",
    "scrolling_text_1": "॥ ॐ नमः शिवाय ॥",
    "scrolling_text_2": "॥ ॐ गुरु निरंजन देव नमः ॥"
}

en_dict.update(manual_en)
hi_dict.update(manual_hi)

combined_translations = {
    "en": en_dict,
    "hi": hi_dict
}

lang_js_content = "const translations = " + json.dumps(combined_translations, ensure_ascii=False, indent=2) + """;

document.addEventListener("DOMContentLoaded", () => {
    // Determine language from localStorage or default to hi
    let currentLang = localStorage.getItem('language') || 'hi';
    
    // Function to apply translation
    window.setLanguage = function(lang) {
        currentLang = lang;
        localStorage.setItem('language', lang);
        
        // Find all elements with data-i18n attribute
        const elements = document.querySelectorAll('[data-i18n]');
        
        elements.forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (translations[lang] && translations[lang][key]) {
                if(el.tagName === 'INPUT' && (el.type === 'submit' || el.type === 'button')) {
                    el.value = translations[lang][key];
                } else if (el.tagName === 'INPUT' && el.type === 'text') {
                    el.placeholder = translations[lang][key];
                } else {
                    el.innerHTML = translations[lang][key];
                }
            }
        });
        
        // Update toggle button text if exists
        const toggleBtn = document.getElementById('lang-toggle-btn');
        if (toggleBtn) {
            toggleBtn.textContent = lang === 'hi' ? 'EN' : 'HI';
        }
    };
    
    // Function to toggle language
    window.toggleLanguage = function() {
        const newLang = currentLang === 'hi' ? 'en' : 'hi';
        setLanguage(newLang);
    };
    
    // Initial call
    setLanguage(currentLang);
});
"""

with open('js/lang.js', 'w', encoding='utf-8') as f:
    f.write(lang_js_content)

print("Translations written to lang.js.")

# Now replace index.html with index_new.html
import os
os.replace('index_new.html', 'index.html')
print("index.html replaced.")
