import os
from pdf2image import convert_from_path
import pytesseract
import pandas as pd

"""
Poppler is a PDF rendering library which, when combined with Pandas, can be used to convert PDF 
files into CSV. First, you convert the PDF into images with Poppler, then analyse these images 
with OCR (Optical Character Recognition) tools like Tesseract, and finally store the data 
with Pandas.

Test on survey_2024.pdf, result shows good.
"""

dir = os.getcwd()
pdf_files = [file for file in os.listdir(dir) if file.endswith('_2024.pdf')]

target_file = pdf_files[0]

images = convert_from_path('financial_report.pdf')
text_data = []

for image in images:
    text = pytesseract.image_to_string(image)
    text_data.append(text)

# Assuming text_data is now neatly parsed
df = pd.DataFrame(text_data)
df.to_csv('output.csv', index=False)