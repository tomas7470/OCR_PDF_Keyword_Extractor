import os
import re
import csv
import pytesseract
from PIL import Image

# Function to use the pytesseract for OCRing an image
def ocr_text_extraction(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Function to search for keywords after OCR is applied, 
def search_keywords_in_pdf(keywords, pdf_file):
    results = []
    with fitz.open(pdf_file) as doc:
        for page_num, page in enumerate(doc, start=1):
            images = page.get_images(full=True)
            for img_num, img in enumerate(images, start=1):
                image = Image.frombytes("RGB", [img["width"], img["height"]], img["image"])
                image_path = f"temp_img_{page_num}_{img_num}.png"
                image.save(image_path)
                text = ocr_text_extraction(image_path)
                os.remove(image_path)
                for keyword in keywords:
                    matches = re.finditer(r"(?i)(\b" + re.escape(keyword) + r"\b)", text, flags=re.IGNORECASE)
                    for match in matches:
                        start = max(0, match.start() - 20)
                        end = min(len(text), match.end() + 20)
                        result = {
                            'Keyword': keyword,
                            'Context': text[start:end],
                            'PDF File': os.path.basename(pdf_file)
                        }
                        results.append(result)
    return results

def search_keywords_in_folder(keywords, folder_path, output_file):
    results = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(folder_path, file_name)
            results += search_keywords_in_pdf(keywords, file_path)

    fieldnames = ['Keyword', 'Context', 'PDF File']
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

# Define the keywords to search
keywords = ['keyword1','keyword2','keyword3','keyword4','keyword5','keyword6']

# Specify the folder path containing the PDF files
folder_path = '/path/to/pdf.pdf'

# Specify the output CSV file path
output_file = 'output.csv'

# Set the path to the Tesseract executable (if not in the system PATH)
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

# Call the function to search for keywords in the PDF files and generate the CSV file
search_keywords_in_folder(keywords, folder_path, output_file)
