import json
import re

history_html_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada/history.html'
lang_js_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada/js/lang.js'

with open(history_html_path, 'r', encoding='utf-8') as f:
    html = f.read()

translations = {
    "history_1": {"hi": "इतिहास", "en": "History"},
    "history_2": {"hi": "श्री पंचायती अखाड़ा श्री निरंजनी की गौरवशाली परंपरा", "en": "The Glorious Tradition of Shri Panchayati Akhada Shri Niranjani"},
    "history_3": {"hi": "स्थापना", "en": "Establishment"},
    "history_4": {"hi": "गुरु परंपरा", "en": "Guru Tradition"},
    "history_5": {"hi": "मढ़ियाँ", "en": "Madhiyas"},
    "history_6": {"hi": "कुंभ पर्व", "en": "Kumbh Parv"},
    "history_7": {"hi": "नागा संन्यासी", "en": "Naga Sanyasis"},
    "history_8": {"hi": "वर्तमान स्वरूप", "en": "Present Form"},
    "history_9": {"hi": "गुरु कृपा ही जीवन का प्रकाश है", "en": "Guru's grace is the light of life"},
    "history_10": {"hi": "श्री पंचायती अखाड़ा श्री निरंजनी का इतिहास", "en": "History of Shri Panchayati Akhada Shri Niranjani"},
    "history_11": {"hi": "श्री पंचायती अखाड़ा श्री निरंजनी दशनामी संन्यास परंपरा के प्रमुख एवं प्राचीन अखाड़ों में से एक है। इसकी स्थापना सनातन धर्म की रक्षा, वेद-शास्त्रों के प्रचार, संन्यास परंपरा के संरक्षण तथा समाज में आध्यात्मिक चेतना के प्रसार के उद्देश्य से की गई। यह अखाड़ा आदि शंकराचार्य द्वारा स्थापित दशनामी परंपरा का एक महत्वपूर्ण अंग माना जाता है। <br><br>\n                                सदियों से निरंजनी अखाड़ा धर्म, तप, योग, त्याग एवं गुरु-शिष्य परंपरा का केंद्र रहा है। महाकुंभ, अर्धकुंभ तथा अन्य धार्मिक आयोजनों में इसकी गौरवशाली उपस्थिति सनातन संस्कृति की जीवंत पहचान है।", "en": "Shri Panchayati Akhada Shri Niranjani is one of the prominent and ancient Akhadas of the Dashanami Sanyas tradition. It was established with the objective of protecting Sanatan Dharma, propagating Vedas and Shastras, preserving the Sanyas tradition, and spreading spiritual consciousness in society. This Akhada is considered an important part of the Dashanami tradition established by Adi Shankaracharya. <br><br>\n                                For centuries, Niranjani Akhada has been a center of Dharma, penance, yoga, sacrifice, and the Guru-disciple tradition. Its glorious presence in Mahakumbh, Ardhakumbh, and other religious events is a living identity of Sanatan culture."},
    "history_12": {"hi": "स्थापना एवं उद्देश्य", "en": "Establishment and Objectives"},
    "history_13": {"hi": "निरंजनी अखाड़ा का मूल उद्देश्य धर्म की रक्षा, साधु-संतों का संगठन, वैदिक ज्ञान का संरक्षण तथा सनातन संस्कृति का प्रचार-प्रसार है। अखाड़े में संन्यासियों को शास्त्र एवं शस्त्र दोनों की शिक्षा प्रदान की जाती रही है, जिससे वे समाज तथा धर्म की रक्षा के लिए सदैव तत्पर रहें।", "en": "The main objective of Niranjani Akhada is the protection of Dharma, organization of saints and sages, preservation of Vedic knowledge, and propagation of Sanatan culture. Sanyasis in the Akhada have been imparted education in both Shastras (scriptures) and Shastras (weapons), so that they are always ready to protect society and Dharma."},
    "history_14": {"hi": "गुरु-शिष्य परंपरा", "en": "Guru-Disciple Tradition"},
    "history_15": {"hi": "निरंजनी अखाड़े की पहचान उसकी अखंड गुरु-शिष्य परंपरा है। प्रत्येक संन्यासी अपने गुरु से दीक्षा प्राप्त कर वैदिक ज्ञान, योग, तप, संयम तथा सेवा के मार्ग पर अग्रसर होता है। यह परंपरा आज भी उसी श्रद्धा एवं अनुशासन के साथ निरंतर आगे बढ़ रही है।", "en": "The identity of Niranjani Akhada is its unbroken Guru-disciple tradition. Every Sanyasi, after receiving initiation from his Guru, progresses on the path of Vedic knowledge, yoga, penance, restraint, and service. This tradition continues to move forward with the same reverence and discipline today."},
    "history_16": {"hi": "कुंभ पर्व में निरंजनी अखाड़ा", "en": "Niranjani Akhada in Kumbh Parv"},
    "history_17": {"hi": "महाकुंभ एवं अर्धकुंभ में निरंजनी अखाड़े का शाही स्नान अत्यंत महत्वपूर्ण माना जाता है। लाखों श्रद्धालु अखाड़े के नागा संन्यासियों एवं संतों के दिव्य दर्शन हेतु उपस्थित होते हैं। यह केवल धार्मिक आयोजन नहीं बल्कि सनातन संस्कृति की महान परंपरा का उत्सव है।", "en": "The Shahi Snan of Niranjani Akhada in Mahakumbh and Ardhakumbh is considered extremely important. Millions of devotees attend to have the divine darshan of the Naga Sanyasis and saints of the Akhada. It is not just a religious event but a celebration of the great tradition of Sanatan culture."},
    "history_18": {"hi": "आध्यात्मिक विरासत", "en": "Spiritual Heritage"},
    "history_19": {"hi": "निरंजनी अखाड़ा वेद, उपनिषद, पुराण, योग, ध्यान, तपस्या एवं भारतीय आध्यात्मिक संस्कृति की अमूल्य धरोहर को संरक्षित करने का कार्य करता है। इसके आश्रम एवं मढ़ियाँ देशभर में धर्म, शिक्षा, सेवा एवं साधना के केंद्र के रूप में कार्यरत हैं।", "en": "Niranjani Akhada works to preserve the invaluable heritage of Vedas, Upanishads, Puranas, Yoga, meditation, penance, and Indian spiritual culture. Its ashrams and Madhiyas function as centers of Dharma, education, service, and spiritual practice across the country."},
    "history_20": {"hi": "आज श्री पंचायती अखाड़ा श्री निरंजनी आधुनिक युग में भी अपनी प्राचीन परंपराओं को अक्षुण्ण रखते हुए धर्म, संस्कृति, शिक्षा, सेवा एवं आध्यात्मिक जागरण के कार्यों में सक्रिय है। देशभर में स्थित इसकी शाखाएँ, मढ़ियाँ एवं संत समाज सनातन धर्म के प्रचार-प्रसार में निरंतर योगदान दे रहे हैं।", "en": "Today, Shri Panchayati Akhada Shri Niranjani is active in the works of Dharma, culture, education, service, and spiritual awakening while keeping its ancient traditions intact even in the modern age. Its branches, Madhiyas, and saint society located across the country are continuously contributing to the propagation of Sanatan Dharma."},
    "history_21": {"hi": "इतिहास की प्रमुख विशेषताएँ", "en": "Key Features of History"},
    "history_22": {"hi": "निरंजनी अखाड़े की शक्ति इसकी अखंड गुरु-शिष्य परंपरा में निहित है, जहाँ आध्यात्मिक ज्ञान, अनुशासन एवं सन्यास संस्कार पीढ़ी-दर-पीढ़ी हस्तांतरित होते हैं।", "en": "The strength of Niranjani Akhada lies in its unbroken Guru-disciple tradition, where spiritual knowledge, discipline, and Sanyas rites are transferred from generation to generation."},
    "history_23": {"hi": "धर्म संरक्षण", "en": "Protection of Dharma"},
    "history_24": {"hi": "अखाड़े का प्रमुख उद्देश्य सनातन धर्म, वैदिक संस्कृति एवं भारतीय आध्यात्मिक विरासत का संरक्षण तथा समाज में धर्म जागरण करना है।", "en": "The main objective of the Akhada is the protection of Sanatan Dharma, Vedic culture, and Indian spiritual heritage, and awakening Dharma in society."},
    "history_25": {"hi": "श्री पंचायती अखाड़ा श्री निरंजनी केवल एक संन्यासी संगठन नहीं, बल्कि सनातन धर्म, वैदिक परंपरा, आध्यात्मिक साधना तथा राष्ट्रधर्म की रक्षा का एक जीवंत केंद्र है। इसकी परंपराएँ सदियों से गुरु-शिष्य संबंध, तप, त्याग, सेवा एवं धर्म संरक्षण के आदर्शों पर आधारित हैं।", "en": "Shri Panchayati Akhada Shri Niranjani is not just a Sanyasi organization, but a living center for the protection of Sanatan Dharma, Vedic tradition, spiritual practice, and national duty. Its traditions have been based on the ideals of Guru-disciple relationship, penance, sacrifice, service, and protection of Dharma for centuries."},
    "history_26": {"hi": "निरंजनी अखाड़े की विशेषताएँ", "en": "Features of Niranjani Akhada"},
    "history_27": {"hi": "श्री पंचायती अखाड़ा श्री निरंजनी भारतीय सनातन परंपरा के उन महान आध्यात्मिक संस्थानों में से एक है जिसने धर्म, साधना एवं संस्कृति के संरक्षण में अमूल्य योगदान दिया है।", "en": "Shri Panchayati Akhada Shri Niranjani is one of those great spiritual institutions of the Indian Sanatan tradition that has made an invaluable contribution to the preservation of Dharma, spiritual practice, and culture."},
    "history_28": {"hi": "दशनामी संन्यास परंपरा", "en": "Dashanami Sanyas Tradition"},
    "history_29": {"hi": "आदि शंकराचार्य द्वारा स्थापित दशनामी संन्यास परंपरा के सिद्धांतों का पालन करते हुए अखाड़ा वैदिक ज्ञान एवं आध्यात्मिक अनुशासन का संवाहक है।", "en": "Following the principles of the Dashanami Sanyas tradition established by Adi Shankaracharya, the Akhada is a carrier of Vedic knowledge and spiritual discipline."},
    "history_30": {"hi": "कुंभ की गौरवशाली परंपरा", "en": "Glorious Tradition of Kumbh"},
    "history_31": {"hi": "महाकुंभ एवं अर्धकुंभ में निरंजनी अखाड़े की शाही पेशवाई और शाही स्नान इसकी प्राचीन परंपरा एवं आध्यात्मिक गौरव का प्रतीक हैं।", "en": "The Shahi Peshwai and Shahi Snan of Niranjani Akhada in Mahakumbh and Ardhakumbh are symbols of its ancient tradition and spiritual glory."}
}

html = html.replace('<h1 class="text-anime-style-3" data-cursor="-opaque">इतिहास</h1>', '<h1 class="text-anime-style-3" data-cursor="-opaque" data-i18n="history_1">इतिहास</h1>')
html = html.replace('<li class="breadcrumb-item"><a href="index.html">श्री पंचायती अखाड़ा श्री निरंजनी की गौरवशाली परंपरा</li>', '<li class="breadcrumb-item"><a href="index.html" data-i18n="history_2">श्री पंचायती अखाड़ा श्री निरंजनी की गौरवशाली परंपरा</a></li>')

html = html.replace('<li><a href="#1">    स्थापना</a></li>', '<li><a href="#1" data-i18n="history_3">स्थापना</a></li>')
html = html.replace('<li><a href="#2">    इतिहास</a></li>', '<li><a href="#2" data-i18n="history_1">इतिहास</a></li>')
html = html.replace('<li><a href="#3">    गुरु परंपरा</a></li>', '<li><a href="#3" data-i18n="history_4">गुरु परंपरा</a></li>')
html = html.replace('<li><a href="#4">    मढ़ियाँ</a></li>', '<li><a href="#4" data-i18n="history_5">मढ़ियाँ</a></li>')
html = html.replace('<li><a href="#5">    कुंभ पर्व</a></li>', '<li><a href="#5" data-i18n="history_6">कुंभ पर्व</a></li>')
html = html.replace('<li><a href="#6">        नागा संन्यासी</a></li>', '<li><a href="#6" data-i18n="history_7">नागा संन्यासी</a></li>')
html = html.replace('<li><a href="#7">        वर्तमान स्वरूप</a></li>', '<li><a href="#7" data-i18n="history_8">वर्तमान स्वरूप</a></li>')

html = html.replace('<h2>गुरु कृपा ही जीवन का प्रकाश है</h2>', '<h2 data-i18n="history_9">गुरु कृपा ही जीवन का प्रकाश है</h2>')

html = html.replace('<h2 class="text-anime-style-3" id="1">श्री पंचायती अखाड़ा श्री निरंजनी का इतिहास</h2>', '<h2 class="text-anime-style-3" id="1" data-i18n="history_10">श्री पंचायती अखाड़ा श्री निरंजनी का इतिहास</h2>')
html = html.replace('<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;">श्री पंचायती अखाड़ा श्री निरंजनी दशनामी संन्यास परंपरा के प्रमुख एवं प्राचीन अखाड़ों में से एक है। इसकी स्थापना सनातन धर्म की रक्षा, वेद-शास्त्रों के प्रचार, संन्यास परंपरा के संरक्षण तथा समाज में आध्यात्मिक चेतना के प्रसार के उद्देश्य से की गई। यह अखाड़ा आदि शंकराचार्य द्वारा स्थापित दशनामी परंपरा का एक महत्वपूर्ण अंग माना जाता है। <br><br>\n                                सदियों से निरंजनी अखाड़ा धर्म, तप, योग, त्याग एवं गुरु-शिष्य परंपरा का केंद्र रहा है। महाकुंभ, अर्धकुंभ तथा अन्य धार्मिक आयोजनों में इसकी गौरवशाली उपस्थिति सनातन संस्कृति की जीवंत पहचान है।\n                                </p>', '<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;" data-i18n="history_11">श्री पंचायती अखाड़ा श्री निरंजनी दशनामी संन्यास परंपरा के प्रमुख एवं प्राचीन अखाड़ों में से एक है। इसकी स्थापना सनातन धर्म की रक्षा, वेद-शास्त्रों के प्रचार, संन्यास परंपरा के संरक्षण तथा समाज में आध्यात्मिक चेतना के प्रसार के उद्देश्य से की गई। यह अखाड़ा आदि शंकराचार्य द्वारा स्थापित दशनामी परंपरा का एक महत्वपूर्ण अंग माना जाता है। <br><br>\n                                सदियों से निरंजनी अखाड़ा धर्म, तप, योग, त्याग एवं गुरु-शिष्य परंपरा का केंद्र रहा है। महाकुंभ, अर्धकुंभ तथा अन्य धार्मिक आयोजनों में इसकी गौरवशाली उपस्थिति सनातन संस्कृति की जीवंत पहचान है।\n                                </p>')

html = html.replace('<h2 class="text-anime-style-3" id="2">स्थापना एवं उद्देश्य</h2>', '<h2 class="text-anime-style-3" id="2" data-i18n="history_12">स्थापना एवं उद्देश्य</h2>')
html = html.replace('<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;">निरंजनी अखाड़ा का मूल उद्देश्य धर्म की रक्षा, साधु-संतों का संगठन, वैदिक ज्ञान का संरक्षण तथा सनातन संस्कृति का प्रचार-प्रसार है। अखाड़े में संन्यासियों को शास्त्र एवं शस्त्र दोनों की शिक्षा प्रदान की जाती रही है, जिससे वे समाज तथा धर्म की रक्षा के लिए सदैव तत्पर रहें。\n                                </p>', '<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;" data-i18n="history_13">निरंजनी अखाड़ा का मूल उद्देश्य धर्म की रक्षा, साधु-संतों का संगठन, वैदिक ज्ञान का संरक्षण तथा सनातन संस्कृति का प्रचार-प्रसार है। अखाड़े में संन्यासियों को शास्त्र एवं शस्त्र दोनों की शिक्षा प्रदान की जाती रही है, जिससे वे समाज तथा धर्म की रक्षा के लिए सदैव तत्पर रहें।\n                                </p>')

html = html.replace('<h2 class="text-anime-style-3" id="3">गुरु-शिष्य परंपरा</h2>', '<h2 class="text-anime-style-3" id="3" data-i18n="history_14">गुरु-शिष्य परंपरा</h2>')
html = html.replace('<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;">निरंजनी अखाड़े की पहचान उसकी अखंड गुरु-शिष्य परंपरा है। प्रत्येक संन्यासी अपने गुरु से दीक्षा प्राप्त कर वैदिक ज्ञान, योग, तप, संयम तथा सेवा के मार्ग पर अग्रसर होता है। यह परंपरा आज भी उसी श्रद्धा एवं अनुशासन के साथ निरंतर आगे बढ़ रही है。\n                                </p>', '<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;" data-i18n="history_15">निरंजनी अखाड़े की पहचान उसकी अखंड गुरु-शिष्य परंपरा है। प्रत्येक संन्यासी अपने गुरु से दीक्षा प्राप्त कर वैदिक ज्ञान, योग, तप, संयम तथा सेवा के मार्ग पर अग्रसर होता है। यह परंपरा आज भी उसी श्रद्धा एवं अनुशासन के साथ निरंतर आगे बढ़ रही है।\n                                </p>')

html = html.replace('<h2 class="text-anime-style-3" id="4">कुंभ पर्व में निरंजनी अखाड़ा</h2>', '<h2 class="text-anime-style-3" id="4" data-i18n="history_16">कुंभ पर्व में निरंजनी अखाड़ा</h2>')
html = html.replace('<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;">महाकुंभ एवं अर्धकुंभ में निरंजनी अखाड़े का शाही स्नान अत्यंत महत्वपूर्ण माना जाता है। लाखों श्रद्धालु अखाड़े के नागा संन्यासियों एवं संतों के दिव्य दर्शन हेतु उपस्थित होते हैं। यह केवल धार्मिक आयोजन नहीं बल्कि सनातन संस्कृति की महान परंपरा का उत्सव है。\n                                </p>', '<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;" data-i18n="history_17">महाकुंभ एवं अर्धकुंभ में निरंजनी अखाड़े का शाही स्नान अत्यंत महत्वपूर्ण माना जाता है। लाखों श्रद्धालु अखाड़े के नागा संन्यासियों एवं संतों के दिव्य दर्शन हेतु उपस्थित होते हैं। यह केवल धार्मिक आयोजन नहीं बल्कि सनातन संस्कृति की महान परंपरा का उत्सव है।\n                                </p>')

html = html.replace('<h2 class="text-anime-style-3" id="5">आध्यात्मिक विरासत</h2>', '<h2 class="text-anime-style-3" id="5" data-i18n="history_18">आध्यात्मिक विरासत</h2>')
html = html.replace('<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;">निरंजनी अखाड़ा वेद, उपनिषद, पुराण, योग, ध्यान, तपस्या एवं भारतीय आध्यात्मिक संस्कृति की अमूल्य धरोहर को संरक्षित करने का कार्य करता है। इसके आश्रम एवं मढ़ियाँ देशभर में धर्म, शिक्षा, सेवा एवं साधना के केंद्र के रूप में कार्यरत हैं。\n                                </p>', '<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;" data-i18n="history_19">निरंजनी अखाड़ा वेद, उपनिषद, पुराण, योग, ध्यान, तपस्या एवं भारतीय आध्यात्मिक संस्कृति की अमूल्य धरोहर को संरक्षित करने का कार्य करता है। इसके आश्रम एवं मढ़ियाँ देशभर में धर्म, शिक्षा, सेवा एवं साधना के केंद्र के रूप में कार्यरत हैं।\n                                </p>')


html = html.replace('वर्तमान स्वरूप</h2>', 'वर्तमान स्वरूप</h2>')
html = html.replace('<h2 class="text-anime-style-3" id="6">\n                                    वर्तमान स्वरूप</h2>', '<h2 class="text-anime-style-3" id="6" data-i18n="history_8">\n                                    वर्तमान स्वरूप</h2>')


html = html.replace('<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;">आज श्री पंचायती अखाड़ा श्री निरंजनी आधुनिक युग में भी अपनी प्राचीन परंपराओं को अक्षुण्ण रखते हुए धर्म, संस्कृति, शिक्षा, सेवा एवं आध्यात्मिक जागरण के कार्यों में सक्रिय है। देशभर में स्थित इसकी शाखाएँ, मढ़ियाँ एवं संत समाज सनातन धर्म के प्रचार-प्रसार में निरंतर योगदान दे रहे हैं。\n                                </p>', '<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;" data-i18n="history_20">आज श्री पंचायती अखाड़ा श्री निरंजनी आधुनिक युग में भी अपनी प्राचीन परंपराओं को अक्षुण्ण रखते हुए धर्म, संस्कृति, शिक्षा, सेवा एवं आध्यात्मिक जागरण के कार्यों में सक्रिय है। देशभर में स्थित इसकी शाखाएँ, मढ़ियाँ एवं संत समाज सनातन धर्म के प्रचार-प्रसार में निरंतर योगदान दे रहे हैं।\n                                </p>')

html = html.replace('<h2 class="text-anime-style-3">इतिहास की प्रमुख विशेषताएँ</h2>', '<h2 class="text-anime-style-3" data-i18n="history_21">इतिहास की प्रमुख विशेषताएँ</h2>')

html = html.replace('<h3>गुरु-शिष्य परंपरा</h3>', '<h3 data-i18n="history_14">गुरु-शिष्य परंपरा</h3>')
html = html.replace('<p>निरंजनी अखाड़े की शक्ति इसकी अखंड गुरु-शिष्य परंपरा में निहित है, जहाँ आध्यात्मिक ज्ञान, अनुशासन एवं सन्यास संस्कार पीढ़ी-दर-पीढ़ी हस्तांतरित होते हैं।</p>', '<p data-i18n="history_22">निरंजनी अखाड़े की शक्ति इसकी अखंड गुरु-शिष्य परंपरा में निहित है, जहाँ आध्यात्मिक ज्ञान, अनुशासन एवं सन्यास संस्कार पीढ़ी-दर-पीढ़ी हस्तांतरित होते हैं।</p>')

html = html.replace('<h3>धर्म संरक्षण</h3>', '<h3 data-i18n="history_23">धर्म संरक्षण</h3>')
html = html.replace('<p>अखाड़े का प्रमुख उद्देश्य सनातन धर्म, वैदिक संस्कृति एवं भारतीय आध्यात्मिक विरासत का संरक्षण तथा समाज में धर्म जागरण करना है।</p>', '<p data-i18n="history_24">अखाड़े का प्रमुख उद्देश्य सनातन धर्म, वैदिक संस्कृति एवं भारतीय आध्यात्मिक विरासत का संरक्षण तथा समाज में धर्म जागरण करना है।</p>')

html = html.replace('<p class="wow fadeInUp" data-wow-delay="0.8s" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;">श्री पंचायती अखाड़ा श्री निरंजनी केवल एक संन्यासी संगठन नहीं, बल्कि सनातन धर्म, वैदिक परंपरा, आध्यात्मिक साधना तथा राष्ट्रधर्म की रक्षा का एक जीवंत केंद्र है। इसकी परंपराएँ सदियों से गुरु-शिष्य संबंध, तप, त्याग, सेवा एवं धर्म संरक्षण के आदर्शों पर आधारित हैं।</p>', '<p class="wow fadeInUp" data-wow-delay="0.8s" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;" data-i18n="history_25">श्री पंचायती अखाड़ा श्री निरंजनी केवल एक संन्यासी संगठन नहीं, बल्कि सनातन धर्म, वैदिक परंपरा, आध्यात्मिक साधना तथा राष्ट्रधर्म की रक्षा का एक जीवंत केंद्र है। इसकी परंपराएँ सदियों से गुरु-शिष्य संबंध, तप, त्याग, सेवा एवं धर्म संरक्षण के आदर्शों पर आधारित हैं।</p>')


html = html.replace('<h2 class="text-anime-style-3">निरंजनी अखाड़े की विशेषताएँ</h2>', '<h2 class="text-anime-style-3" data-i18n="history_26">निरंजनी अखाड़े की विशेषताएँ</h2>')
html = html.replace('<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;">श्री पंचायती अखाड़ा श्री निरंजनी भारतीय सनातन परंपरा के उन महान आध्यात्मिक संस्थानों में से एक है जिसने धर्म, साधना एवं संस्कृति के संरक्षण में अमूल्य योगदान दिया है।</p>', '<p class="wow fadeInUp" style="text-align: justify; font-size: 18px; line-height: 1.8; font-weight: 500; color: #555; font-family: \'Tiro Devanagari Marathi\', serif;" data-i18n="history_27">श्री पंचायती अखाड़ा श्री निरंजनी भारतीय सनातन परंपरा के उन महान आध्यात्मिक संस्थानों में से एक है जिसने धर्म, साधना एवं संस्कृति के संरक्षण में अमूल्य योगदान दिया है।</p>')

html = html.replace('<h3>दशनामी संन्यास परंपरा</h3>', '<h3 data-i18n="history_28">दशनामी संन्यास परंपरा</h3>')
html = html.replace('<p>आदि शंकराचार्य द्वारा स्थापित दशनामी संन्यास परंपरा के सिद्धांतों का पालन करते हुए अखाड़ा वैदिक ज्ञान एवं आध्यात्मिक अनुशासन का संवाहक है।</p>', '<p data-i18n="history_29">आदि शंकराचार्य द्वारा स्थापित दशनामी संन्यास परंपरा के सिद्धांतों का पालन करते हुए अखाड़ा वैदिक ज्ञान एवं आध्यात्मिक अनुशासन का संवाहक है।</p>')

html = html.replace('<h3>कुंभ की गौरवशाली परंपरा</h3>', '<h3 data-i18n="history_30">कुंभ की गौरवशाली परंपरा</h3>')
html = html.replace('<p>महाकुंभ एवं अर्धकुंभ में निरंजनी अखाड़े की शाही पेशवाई और शाही स्नान इसकी प्राचीन परंपरा एवं आध्यात्मिक गौरव का प्रतीक हैं।</p>', '<p data-i18n="history_31">महाकुंभ एवं अर्धकुंभ में निरंजनी अखाड़े की शाही पेशवाई और शाही स्नान इसकी प्राचीन परंपरा एवं आध्यात्मिक गौरव का प्रतीक हैं।</p>')

with open(history_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(lang_js_path, 'r', encoding='utf-8') as f:
    lang_content = f.read()

# Parse the js to inject translations
import json
import re

for lang in ['en', 'hi']:
    for k, v in translations.items():
        val = v[lang].replace('"', '\\"').replace('\n', '\\n')
        # Insert before the closing brace of the respective language
        # We need a robust way to insert it.
        pass

