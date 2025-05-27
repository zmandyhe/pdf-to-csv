import os
from pdf2image import convert_from_path
import pytesseract
import pandas as pd

"""
pdf2image is a python module that wraps the pdftoppm and pdftocairo utilities to convert PDF into images.
to install: `pip install pdf2image`

pytesseract is a Python wrapper for Google's Tesseract-OCR Engine, enabling developers to convert 
images containing text into string formats that can be processed further.
to install: 
`sudo apt install tesseract-ocr` then `sudo apt install libtesseract-dev`

Poppler is a PDF rendering library based on the xpdf-3.0 code base.
to install (linux): `sudo apt-get install poppler-utils` 

Test on survey_2024.pdf, result shows good.
"""

dir = os.getcwd()
pdf_files = [file for file in os.listdir(dir) if file.endswith('_2024.pdf')]

target_file = pdf_files[0]
print(target_file)

images = convert_from_path(target_file)
text_data = []

for image in images:
    text = pytesseract.image_to_string(image)
    text_data.append(text)

# Assuming text_data is now neatly parsed
df = pd.DataFrame(text_data)
df.to_csv('output2.csv', index=False)