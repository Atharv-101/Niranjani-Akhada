from bs4 import BeautifulSoup, Comment

file_path = "index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")
comments = soup.find_all(string=lambda text: isinstance(text, Comment))

translations = {
    "प्रारंभ": "Start",
    "समाप्त": "End",
    "समाप्ति": "End",
    "अंत": "End",
    "अनुभाग": "Section",
    
    "हमारा प्रशंसापत्र": "Seven Akhadas",
    "प्रशंसापत्र": "Akhada",
    "हमारा मंत्रालय": "Sanatan Knowledge",
    "मंत्रालय": "Knowledge",
    "हमारा सेवा": "Our Traditions",
    "सेवा": "Tradition",
    "हमारा उपदेश": "Spiritual Heritage",
    "उपदेश": "Heritage",
    "हमारा उद्देश्य": "Guru Niranjan Dev Tradition",
    "उद्देश्य": "Guru Tradition",
    "हमारा मिशन": "Guru Niranjan Dev Tradition",
    "मिशन": "Guru Tradition",
    "हमारा इवेंट": "Quote",
    "इवेंट": "Quote",
    "अभी दान करें": "Donation",
    "दान": "Donation",
    "हमारा ब्लॉग": "Our Blog",
    "ब्लॉग": "Blog",
    "हमारे बारे में": "About Us",
    "अक्सर पूछे जाने वाले प्रश्न": "FAQs",
    "हमारा FAQ": "FAQs",
    
    "स्क्रॉलिंग टिकर": "Scrolling Ticker",
    "अनुभाग शीर्षक": "Section Title",
    "अनुभाग पादलेख पाठ": "Section Footer Text",
    "अनुभाग पाद लेख पाठ": "Section Footer Text",
    "आइटम": "Item",
    "स्लाइड": "Slide",
    "छवि": "Image",
    "बॉक्स": "Box",
    "सामग्री": "Content",
    "बटन": "Button",
    "अकॉर्डियन": "Accordion",
    "हेडर": "Header",
    "हीरो": "Hero",
    "वीडियो": "Video",
    "पूर्वलोडर": "Preloader",
    "लोगो": "Logo",
    "मुख्य मेनू": "Main Menu",
    "सीटीए": "CTA",
    "लेखक": "Author",
    "पाद लेख": "Footer",
    "पादलेख": "Footer",
    "कॉपीराइट": "Copyright",
    "सामाजिक": "Social",
    "लिंक": "Links",
    "जानकारी": "Info",
    "सांख्यिकी": "Statistics",
    "सूची": "List",
    "आइकन": "Icon",
    "काउंटर": "Counter",
    "शरीर": "Body"
}

def translate_comment(text):
    text = text.strip()
    # Sort keys by length descending to replace longest phrases first
    for hi_term in sorted(translations.keys(), key=len, reverse=True):
        if hi_term in text:
            text = text.replace(hi_term, translations[hi_term])
    return text.strip()

count = 0
for comment in comments:
    old_text = comment.strip()
    new_text = translate_comment(old_text)
    
    # If the text was changed or we just want to ensure it's English
    if old_text != new_text or old_text:
        # Also clean up any lingering ' ' around words
        new_text = " ".join(new_text.split())
        comment.replace_with(Comment(f" {new_text} "))
        count += 1

with open("index.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

print(f"Updated {count} comments.")
