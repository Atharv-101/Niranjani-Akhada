import re

html_path = '/Users/atharvgangarde/Desktop/OG-files/Akhada-web/Niranjani-Akhada/guru_tradition.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the entire <div class="row service-benefit-item-list" ...> block
# up to <!-- Service Benefit Item List End -->

pattern = re.compile(r'<!-- Service Benefit Item List Start -->.*?<!-- Service Benefit Item List End -->', re.DOTALL)

clean_html = """<!-- Service Benefit Item List Start -->
                                <div class="row guru-tradition-cards-container" style="margin-top: 40px;">
                                    
                                    <!-- Service Benefit Item Start -->
                                    <div class="col-md-4 mb-4">
                                        <div class="guru-card wow fadeInUp" data-wow-delay="0.2s">
                                            <div class="guru-icon-box">
                                                <img src="images/om.svg" alt="">
                                            </div>
                                            <div class="guru-card-content">
                                                <h3 class="guru-card-title">आध्यात्मिक ज्ञान</h3>
                                                <p class="guru-card-text">गुरु शिष्य को वेद, उपनिषद, शास्त्र एवं आत्मज्ञान का प्रकाश प्रदान करते हैं।</p>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- Service Benefit Item End -->

                                    <!-- Service Benefit Item Start -->
                                    <div class="col-md-4 mb-4">
                                        <div class="guru-card wow fadeInUp" data-wow-delay="0.4s">
                                            <div class="guru-icon-box">
                                                <img src="images/om.svg" alt="">
                                            </div>
                                            <div class="guru-card-content">
                                                <h3 class="guru-card-title">संन्यास दीक्षा</h3>
                                                <p class="guru-card-text">गुरु के मार्गदर्शन में संन्यास की दीक्षा प्राप्त कर साधक धर्म एवं साधना का जीवन प्रारंभ करता है।</p>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- Service Benefit Item End -->

                                    <!-- Service Benefit Item Start -->
                                    <div class="col-md-4 mb-4">
                                        <div class="guru-card wow fadeInUp" data-wow-delay="0.6s">
                                            <div class="guru-icon-box">
                                                <img src="images/om.svg" alt="">
                                            </div>
                                            <div class="guru-card-content">
                                                <h3 class="guru-card-title">अनुशासन एवं साधना</h3>
                                                <p class="guru-card-text">गुरु परंपरा तप, संयम, सेवा और आत्मानुशासन का सर्वोच्च आदर्श प्रस्तुत करती है।</p>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- Service Benefit Item End -->
                                    
                                </div>
                                <!-- Service Benefit Item List End -->"""

content = pattern.sub(clean_html, content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("HTML Cleaned")
