"""PyPDF2 is suitable for survey_2025.pdf type, it recognize computer input text
with two columns of survey, we can convert this pattern to two column dataframe."""

import os
import PyPDF2
import csv

dir = os.getcwd()

# List all PDF files in the current folder
pdf_files = [file for file in os.listdir(dir) if file.endswith('_2025.pdf')]

for pdf in pdf_files:
    print(pdf)
    with open(pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'

print(text)
# Here you would parse text into a structured format depending on the specifics of your PDF
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(text)