import json
import os

translations = {
  "समाचार": "News",
  "मढ़ियाँ": "Madhiyas",
  "श्री पंचायती अखाड़ा श्री निरंजनी की मढ़ियाँ अखाड़े की प्राचीन गुरु-शिष्य परंपरा, आध्यात्मिक साधना तथा संगठनात्मक व्यवस्था की आधारशिला हैं। प्रत्येक मढ़ी अपनी विशिष्ट परंपरा, मर्यादा एवं आध्यात्मिक पहचान के साथ सनातन धर्म के संरक्षण, संत परंपरा के संवर्धन तथा वैदिक संस्कृति के प्रचार-प्रसार में महत्वपूर्ण योगदान देती है। वर्तमान में श्री निरंजनी अखाड़े में कुल 18 मढ़ियाँ विद्यमान हैं, जो अखाड़े की समृद्ध आध्यात्मिक विरासत का प्रतीक हैं.": "The Madhiyas of Shri Panchayati Akhada Shri Niranjani are the foundation of the Akhada's ancient Guru-disciple tradition, spiritual practice, and organizational structure. Each Madhiya, with its unique tradition, dignity, and spiritual identity, significantly contributes to the preservation of Sanatan Dharma, the promotion of the saint tradition, and the propagation of Vedic culture. Presently, there are a total of 18 Madhiyas in the Shri Niranjani Akhada, symbolizing the rich spiritual heritage of the Akhada.",
  "राजावत मढ़ी": "Rajavat Madhiya",
  "श्री पंचायती अखाड़ा श्री निरंजनी की प्रमुख परंपरागत मढ़ियों में से एक।": "One of the major traditional Madhiyas of Shri Panchayati Akhada Shri Niranjani.",
  "राजावत परंपरा की यह दूसरी मढ़ी अखाड़े की धार्मिक एवं आध्यात्मिक परंपराओं को आगे बढ़ाने तथा संतों के संगठन को सुदृढ़ बनाने में योगदान देती है।": "This second Madhiya of the Rajavat tradition contributes to advancing the religious and spiritual traditions of the Akhada and strengthening the organization of saints.",
  "दुर्गानाथी मढ़ी": "Durganathi Madhiya",
  "गुरु-शिष्य परंपरा एवं संन्यास परंपरा को आगे बढ़ाने वाली प्रतिष्ठित मढ़ी।": "A prestigious Madhiya advancing the Guru-disciple and Sanyas traditions.",
  "रामदत्ती मढ़ी": "Ramdatti Madhiya",
  "धर्म, तप एवं साधना के संरक्षण हेतु समर्पित परंपरागत मढ़ी।": "A traditional Madhiya dedicated to the preservation of Dharma, penance, and spiritual practice.",
  "नृसिंह मढ़ी": "Nrisingh Madhiya",
  "नृसिंह मढ़ी अखाड़े की प्राचीन संन्यासी परंपराओं का प्रतिनिधित्व करती है और धर्मरक्षा की भावना को सुदृढ़ करती है।": "Nrisingh Madhiya represents the ancient ascetic traditions of the Akhada and strengthens the spirit of protecting the Dharma.",
  "मनमुकुन्द मढ़ी": "Manmukund Madhiya",
  "मनमुकुन्द मढ़ी आध्यात्मिक साधना, गुरु सेवा तथा अखाड़े की सांस्कृतिक विरासत के संरक्षण में अपना योगदान देती है।": "Manmukund Madhiya contributes to spiritual practice, Guru service, and the preservation of the Akhada's cultural heritage.",
  "खालसा मढ़ी": "Khalsa Madhiya",
  "खालसा मढ़ी अनुशासन, तप एवं अखाड़े की पारंपरिक व्यवस्था को बनाए रखने वाली प्रमुख मढ़ियों में सम्मिलित है।": "Khalsa Madhiya is included among the major Madhiyas maintaining discipline, penance, and the traditional system of the Akhada.",
  "ब्रह्मनाथी मढ़ी": "Brahmanathi Madhiya",
  "ब्रह्मनाथी मढ़ी वेदांत, गुरु उपासना एवं सनातन धर्म के प्रचार-प्रसार की परंपरा को आगे बढ़ाती है।": "Brahmanathi Madhiya advances the tradition of Vedanta, Guru worship, and the propagation of Sanatan Dharma.",
  "गादी मढ़ी": "Gadi Madhiya",
  "गादी मढ़ी अखाड़े की धार्मिक व्यवस्था एवं गुरु परंपरा से जुड़ी महत्वपूर्ण परंपरागत मढ़ी मानी जाती है।": "Gadi Madhiya is considered an important traditional Madhiya associated with the religious system and Guru tradition of the Akhada.",
  "ॐकारी मढ़ी": "Omkari Madhiya",
  "ॐकारी मढ़ी भगवान शिव के पवित्र प्रणव ‘ॐ’ की आध्यात्मिक भावना से प्रेरित संन्यास परंपरा का प्रतिनिधित्व करती है।": "Omkari Madhiya represents the ascetic tradition inspired by the spiritual spirit of Lord Shiva's sacred Pranava 'Om'.",
  "परमानन्दी मढ़ी": "Parmanandi Madhiya",
  "परमानन्दी मढ़ी साधकों में आध्यात्मिक उन्नति, आत्मज्ञान एवं वैराग्य की भावना को विकसित करने का कार्य करती है।": "Parmanandi Madhiya works to develop spiritual progress, self-realization, and the spirit of renunciation among seekers.",
  "बोडला मढ़ी": "Bodla Madhiya",
  "बोडला मढ़ी अखाड़े की ऐतिहासिक परंपराओं से जुड़ी हुई है तथा संत समाज की एक प्रतिष्ठित शाखा मानी जाती है।": "Bodla Madhiya is associated with the historical traditions of the Akhada and is considered a prestigious branch of the saint community.",
  "मुल्तानी मढ़ी": "Multani Madhiya",
  "मुल्तानी मढ़ी प्राचीन संन्यास परंपरा की एक महत्वपूर्ण कड़ी है, जिसने विभिन्न क्षेत्रों में अखाड़े की परंपरा को आगे बढ़ाया।": "Multani Madhiya is an important link in the ancient ascetic tradition, which has advanced the Akhada's tradition in various fields.",
  "वैकुण्ठी मढ़ी": "Vaikunthi Madhiya",
  "वैकुण्ठी मढ़ी आध्यात्मिक साधना, सेवा एवं धार्मिक संस्कारों के संरक्षण के उद्देश्य से कार्यरत परंपरागत मढ़ी है।": "Vaikunthi Madhiya is a traditional Madhiya working with the objective of spiritual practice, service, and the preservation of religious rites.",
  "सिंहासनी मढ़ी": "Sinhasani Madhiya",
  "सिंहासनी मढ़ी अखाड़े की प्रतिष्ठित मढ़ियों में से एक है, जो शैव संन्यास परंपरा एवं धार्मिक अनुशासन को सुदृढ़ करती है।": "Sinhasani Madhiya is one of the prestigious Madhiyas of the Akhada, which strengthens the Shaiva ascetic tradition and religious discipline.",
  "दरियाव मढ़ी": "Dariyav Madhiya",
  "दरियाव मढ़ी सेवा, समर्पण एवं संत परंपरा के आदर्शों का पालन करते हुए अखाड़े की सांस्कृतिक धरोहर को संरक्षित करती है।": "Dariyav Madhiya preserves the cultural heritage of the Akhada by following the ideals of service, dedication, and the saint tradition.",
  "दस + चार मढ़ी": "Das + Char Madhiya",
  "दस + चार मढ़ी अखाड़े की विशिष्ट पारंपरिक शाखाओं में से एक है, जो गुरु-शिष्य परंपरा एवं संगठनात्मक संरचना का अभिन्न भाग है।": "Das + Char Madhiya is one of the specific traditional branches of the Akhada, which is an integral part of the Guru-disciple tradition and organizational structure.",
  "दस + छः मढ़ी": "Das + Chhah Madhiya",
  "दस + छः मढ़ी श्री पंचायती अखाड़ा श्री निरंजनी की मान्य परंपरागत मढ़ियों में सम्मिलित है और अखाड़े की आध्यात्मिक एवं धार्मिक परंपराओं के संरक्षण में महत्वपूर्ण भूमिका निभाती है।": "Das + Chhah Madhiya is included in the recognized traditional Madhiyas of Shri Panchayati Akhada Shri Niranjani and plays an important role in preserving the spiritual and religious traditions of the Akhada.",
  "इतिहास": "History",
  "स्थापना": "Establishment",
  "गुरु परंपरा": "Guru Tradition",
  "कुंभ पर्व": "Kumbh Parva",
  "नागा संन्यासी": "Naga Sanyasi",
  "वर्तमान स्वरूप": "Present Form",
  "गुरु कृपा ही जीवन का प्रकाश है": "Guru's grace is the light of life",
  "श्री पंचायती अखाड़ा श्री निरंजनी का इतिहास": "History of Shri Panchayati Akhada Shri Niranjani",
  "स्थापना एवं उद्देश्य": "Establishment and Objective",
  "निरंजनी अखाड़ा का मूल उद्देश्य धर्म की रक्षा, साधु-संतों का संगठन, वैदिक ज्ञान का संरक्षण तथा सनातन संस्कृति का प्रचार-प्रसार है। अखाड़े में संन्यासियों को शास्त्र एवं शस्त्र दोनों की शिक्षा प्रदान की जाती रही है, जिससे वे समाज तथा धर्म की रक्षा के लिए सदैव तत्पर रहें।": "The fundamental objective of the Niranjani Akhada is the protection of Dharma, the organization of saints and ascetics, the preservation of Vedic knowledge, and the propagation of Sanatan culture. Ascetics in the Akhada have been imparted education in both scriptures (Shastra) and weapons (Shastra), so they are always ready to protect society and Dharma.",
  "गुरु-शिष्य परंपरा": "Guru-Disciple Tradition",
  "निरंजनी अखाड़े की पहचान उसकी अखंड गुरु-शिष्य परंपरा है। प्रत्येक संन्यासी अपने गुरु से दीक्षा प्राप्त कर वैदिक ज्ञान, योग, तप, संयम तथा सेवा के मार्ग पर अग्रसर होता है। यह परंपरा आज भी उसी श्रद्धा एवं अनुशासन के साथ निरंतर आगे बढ़ रही है।": "The identity of Niranjani Akhada is its unbroken Guru-disciple tradition. Each ascetic, after receiving initiation from their Guru, progresses on the path of Vedic knowledge, yoga, penance, restraint, and service. This tradition continues to move forward today with the same reverence and discipline.",
  "कुंभ पर्व में निरंजनी अखाड़ा": "Niranjani Akhada in Kumbh Parva",
  "महाकुंभ एवं अर्धकुंभ में निरंजनी अखाड़े का शाही स्नान अत्यंत महत्वपूर्ण माना जाता है। लाखों श्रद्धालु अखाड़े के नागा संन्यासियों एवं संतों के दिव्य दर्शन हेतु उपस्थित होते हैं। यह केवल धार्मिक आयोजन नहीं बल्कि सनातन संस्कृति की महान परंपरा का उत्सव है।": "The Shahi Snan (Royal Bath) of Niranjani Akhada in Mahakumbh and Ardhakumbh is considered highly significant. Millions of devotees gather for the divine darshan of the Naga ascetics and saints of the Akhada. It is not just a religious event but a celebration of the great tradition of Sanatan culture.",
  "आध्यात्मिक विरासत": "Spiritual Heritage",
  "निरंजनी अखाड़ा वेद, उपनिषद, पुराण, योग, ध्यान, तपस्या एवं भारतीय आध्यात्मिक संस्कृति की अमूल्य धरोहर को संरक्षित करने का कार्य करता है। इसके आश्रम एवं मढ़ियाँ देशभर में धर्म, शिक्षा, सेवा एवं साधना के केंद्र के रूप में कार्यरत हैं।": "Niranjani Akhada works to preserve the invaluable heritage of Vedas, Upanishads, Puranas, Yoga, Meditation, Penance, and Indian spiritual culture. Its ashrams and Madhiyas operate across the country as centers of religion, education, service, and spiritual practice.",
  "आज श्री पंचायती अखाड़ा श्री निरंजनी आधुनिक युग में भी अपनी प्राचीन परंपराओं को अक्षुण्ण रखते हुए धर्म, संस्कृति, शिक्षा, सेवा एवं आध्यात्मिक जागरण के कार्यों में सक्रिय है। देशभर में स्थित इसकी शाखाएँ, मढ़ियाँ एवं संत समाज सनातन धर्म के प्रचार-प्रसार में निरंतर योगदान दे रहे हैं।": "Today, even in the modern era, Shri Panchayati Akhada Shri Niranjani remains active in the works of religion, culture, education, service, and spiritual awakening while keeping its ancient traditions intact. Its branches, Madhiyas, and saint community located nationwide are continuously contributing to the propagation of Sanatan Dharma.",
  "इतिहास की प्रमुख विशेषताएँ": "Key Features of History",
  "निरंजनी अखाड़े की शक्ति इसकी अखंड गुरु-शिष्य परंपरा में निहित है, जहाँ आध्यात्मिक ज्ञान, अनुशासन एवं सन्यास संस्कार पीढ़ी-दर-पीढ़ी हस्तांतरित होते हैं।": "The strength of Niranjani Akhada lies in its unbroken Guru-disciple tradition, where spiritual knowledge, discipline, and ascetic rites are transferred from generation to generation.",
  "धर्म संरक्षण": "Protection of Dharma",
  "अखाड़े का प्रमुख उद्देश्य सनातन धर्म, वैदिक संस्कृति एवं भारतीय आध्यात्मिक विरासत का संरक्षण तथा समाज में धर्म जागरण करना है।": "The primary objective of the Akhada is the preservation of Sanatan Dharma, Vedic culture, and Indian spiritual heritage, as well as religious awakening in society.",
  "श्री पंचायती अखाड़ा श्री निरंजनी केवल एक संन्यासी संगठन नहीं, बल्कि सनातन धर्म, वैदिक परंपरा, आध्यात्मिक साधना तथा राष्ट्रधर्म की रक्षा का एक जीवंत केंद्र है। इसकी परंपराएँ सदियों से गुरु-शिष्य संबंध, तप, त्याग, सेवा एवं धर्म संरक्षण के आदर्शों पर आधारित हैं।": "Shri Panchayati Akhada Shri Niranjani is not just an ascetic organization but a vibrant center for the protection of Sanatan Dharma, Vedic tradition, spiritual practice, and national duty. Its traditions are based on the ideals of Guru-disciple relationship, penance, renunciation, service, and protection of Dharma established for centuries.",
  "निरंजनी अखाड़े की विशेषताएँ": "Characteristics of Niranjani Akhada",
  "श्री पंचायती अखाड़ा श्री निरंजनी भारतीय सनातन परंपरा के उन महान आध्यात्मिक संस्थानों में से एक है जिसने धर्म, साधना एवं संस्कृति के संरक्षण में अमूल्य योगदान दिया है।": "Shri Panchayati Akhada Shri Niranjani is one of the great spiritual institutions of the Indian Sanatan tradition which has made an invaluable contribution to the preservation of religion, spiritual practice, and culture.",
  "दशनामी संन्यास परंपरा": "Dashanami Sanyas Tradition",
  "आदि शंकराचार्य द्वारा स्थापित दशनामी संन्यास परंपरा के सिद्धांतों का पालन करते हुए अखाड़ा वैदिक ज्ञान एवं आध्यात्मिक अनुशासन का संवाहक है।": "Following the principles of the Dashanami Sanyas tradition established by Adi Shankaracharya, the Akhada is the bearer of Vedic knowledge and spiritual discipline.",
  "कुंभ की गौरवशाली परंपरा": "The Glorious Tradition of Kumbh",
  "महाकुंभ एवं अर्धकुंभ में निरंजनी अखाड़े की शाही पेशवाई और शाही स्नान इसकी प्राचीन परंपरा एवं आध्यात्मिक गौरव का प्रतीक हैं।": "The royal procession (Shahi Peshwai) and royal bath (Shahi Snan) of Niranjani Akhada in Mahakumbh and Ardhakumbh are symbols of its ancient tradition and spiritual pride.",
  "॥ श्री गुरु निरंजन देव ॥": "॥ Shri Guru Niranjan Dev ॥",
  "अखण्डमण्डलाकारं व्याप्तं येन चराचरम् ।तत्पदं दर्शितं येन तस्मै श्रीगुरवे नमः ॥": "Akhanda Mandalakaram Vyaptam Yena Characharam, Tatpadam Darshitam Yena Tasmai Shri Gurave Namah.",
  "अज्ञानतिमिरान्धस्य ज्ञानाञ्जनशलाकया ।चक्षुरुन्मीलितं येन तस्मै श्रीगुरवे नमः ॥": "Agyana Timirandhasya Gyananjana Shalakaya, Chakshurunmilitam Yena Tasmai Shri Gurave Namah.",
  "गुरुर्ब्रह्मा गुरुर्विष्णुः गुरुर्देवो महेश्वरः ।गुरुः साक्षात् परब्रह्म तस्मै श्रीगुरवे नमः ॥": "Gurur Brahma Gurur Vishnu Gurur Devo Maheshwarah, Guruh Sakshat Parambrahma Tasmai Shri Gurave Namah.",
  "श्री पंचायती अखाड़ा श्री निरंजनी की गुरु परंपरा": "Guru Tradition of Shri Panchayati Akhada Shri Niranjani",
  "गुरु परंपरा भारतीय सनातन संस्कृति की आत्मा है। श्री पंचायती\n                                    अखाड़ा श्री निरंजनी में गुरु को ब्रह्मा, विष्णु एवं महेश के स्वरूप के रूप में पूज्य\n                                    माना जाता है। गुरु ही शिष्य को आत्मज्ञान, वैराग्य, तप, योग तथा धर्म के मार्ग पर\n                                    अग्रसर करते हैं। यह अखंड परंपरा सदियों से गुरु से शिष्य तक निरंतर प्रवाहित होती आ\n                                    रही है और आज भी उसी श्रद्धा, अनुशासन एवं समर्पण के साथ जीवित है।": "The Guru tradition is the soul of Indian Sanatan culture. In Shri Panchayati Akhada Shri Niranjani, the Guru is revered as the embodiment of Brahma, Vishnu, and Mahesh. It is the Guru who leads the disciple on the path of self-realization, renunciation, penance, yoga, and religion. This unbroken tradition has been flowing continuously from Guru to disciple for centuries and is alive today with the same reverence, discipline, and dedication.",
  "आध्यात्मिक ज्ञान": "Spiritual Knowledge",
  "गुरु शिष्य को वेद, उपनिषद, शास्त्र एवं आत्मज्ञान का प्रकाश प्रदान करते हैं।": "The Guru bestows upon the disciple the light of the Vedas, Upanishads, scriptures, and self-realization.",
  "संन्यास दीक्षा": "Sanyas Initiation",
  "गुरु के मार्गदर्शन में संन्यास की दीक्षा प्राप्त कर साधक धर्म एवं साधना का जीवन प्रारंभ करता है।": "Under the guidance of the Guru, receiving the initiation of Sanyas, the seeker begins a life of religion and spiritual practice.",
  "अनुशासन एवं साधना": "Discipline and Spiritual Practice",
  "गुरु परंपरा तप, संयम, सेवा और आत्मानुशासन का सर्वोच्च आदर्श प्रस्तुत करती है।": "The Guru tradition presents the highest ideal of penance, restraint, service, and self-discipline."
}

with open('/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada/extracted_hindi.json', 'r', encoding='utf-8') as fh:
    extracted = json.load(fh)

dir_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada'
lang_file = os.path.join(dir_path, 'js/lang.js')

with open(lang_file, 'r', encoding='utf-8') as f:
    lang_content_fresh = f.read()

en_json_str = ""
hi_json_str = ""
custom_keys = {}

for i, (hi_text, _) in enumerate(extracted.items(), 1):
    key = f"auto_page_content_{i}"
    en_text = translations.get(hi_text, hi_text)
    custom_keys[hi_text] = key
    en_json_str += f'    "{key}": {json.dumps(en_text, ensure_ascii=False)},\n'
    hi_json_str += f'    "{key}": {json.dumps(hi_text, ensure_ascii=False)},\n'

lang_content_fresh = lang_content_fresh.replace('en: {', 'en: {\n' + en_json_str)
lang_content_fresh = lang_content_fresh.replace('hi: {', 'hi: {\n' + hi_json_str)

with open(lang_file, 'w', encoding='utf-8') as f:
    f.write(lang_content_fresh)

# Update HTML files
files = ['news.html', 'madhiyas.html', 'history.html', 'guru_tradition.html']
for f in files:
    path = os.path.join(dir_path, f)
    if not os.path.exists(path): continue
    with open(path, 'r', encoding='utf-8') as fh:
        html = fh.read()
    
    for hi_text, key in custom_keys.items():
        if hi_text in html:
            if f'data-i18n="{key}"' not in html:
                html = html.replace(hi_text, f'<span data-i18n="{key}">{hi_text}</span>')
                
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(html)

print("Translation successfully applied to HTML files and lang.js!")
