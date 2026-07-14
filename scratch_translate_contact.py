import json
import re
import os

translations = {
    "Contact us": "संपर्क करें",
    "home": "मुख्य पृष्ठ",
    "Contact Us": "संपर्क करें",
    "Get in touch": "संपर्क में रहें",
    "Contact Our Church For Prayer Support": "श्री निरंजनी अखाड़े से संपर्क करें",
    "We would love to hear from you. Whether you have prayer requests, questions about our services, or want to get involved in our ministries,": "अखाड़े से संबंधित किसी भी जानकारी, धार्मिक आयोजनों अथवा अन्य आध्यात्मिक कार्यों के लिए आप हमसे संपर्क कर सकते हैं।",
    "Email Address": "ईमेल आईडी",
    "Phone Number": "फ़ोन नंबर",
    "Our Location": "हमारा पता",
    "123 Faith Avenue, Near Peace GardenJubilee Road,": "श्री पंचायती अखाड़ा निरंजनी, दारागंज, प्रयागराज",
    "Share Your Prayer Requests Here": "अपना संदेश हमें भेजें",
    "First Name": "पहला नाम",
    "Last Name": "अंतिम नाम",
    "Message": "संदेश",
    "Send Message": "संदेश भेजें",
    "Where We Locateda": "हमारा स्थान",
    "Find Our Church Location Easily": "आसानी से हमारा अखाड़ा खोजें",
    "Our church is conveniently located in a peaceful and easily accessible area, making it simple for individuals and families to join us for worship, fellowship": "हमारा अखाड़ा एक शांतिपूर्ण और सुलभ क्षेत्र में स्थित है, जहाँ आकर आप आध्यात्मिक शांति और संत समागम का लाभ उठा सकते हैं।"
}

file_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada/contact.html'
with open(file_path, 'r', encoding='utf-8') as fh:
    html = fh.read()

# Replace texts
for en_text, hi_text in translations.items():
    if en_text in html:
        html = html.replace(en_text, hi_text)

# Fix placeholders
html = html.replace('placeholder="First Name"', 'placeholder="पहला नाम"')
html = html.replace('placeholder="Last Name"', 'placeholder="अंतिम नाम"')
html = html.replace('placeholder="Phone Number"', 'placeholder="फ़ोन नंबर"')
html = html.replace('placeholder="Email Address"', 'placeholder="ईमेल आईडी"')
html = html.replace('placeholder="Message"', 'placeholder="संदेश"')

with open(file_path, 'w', encoding='utf-8') as fh:
    fh.write(html)

print("contact.html translated to Hindi.")
