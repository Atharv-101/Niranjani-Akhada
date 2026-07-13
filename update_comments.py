import os
from bs4 import BeautifulSoup, Comment
from deep_translator import GoogleTranslator
import time

def process_html():
    file_path = "index.html"
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")
    translator = GoogleTranslator(source='en', target='hi')
    
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    
    translated_cache = {}
    print(f"Found {len(comments)} comments.")
    
    for i, comment in enumerate(comments):
        original_text = comment.strip()
        
        # Skip empty or already Hindi comments
        if not original_text or any('\u0900' <= c <= '\u097F' for c in original_text):
            continue
            
        if original_text in translated_cache:
            new_text = translated_cache[original_text]
        else:
            try:
                new_text = translator.translate(original_text)
                time.sleep(0.1)
                translated_cache[original_text] = new_text
            except Exception as e:
                print(f"Translation failed for '{original_text}': {e}")
                new_text = original_text
        
        # Replace comment
        comment.replace_with(Comment(f" {new_text} "))
        
        if (i+1) % 20 == 0:
            print(f"Processed {i+1} / {len(comments)}")
            
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(str(soup))
        
    print("Comments updated successfully.")

if __name__ == "__main__":
    process_html()
