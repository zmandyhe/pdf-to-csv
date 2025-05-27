**Using different Python libraries to convert pdf to csv files**


Two methods:
1. Use PyPDF2 (good for computer generated text input, not good with PDF files containing handwriting)
- `python convert_pypdf2.py`
- test file: survey_2025.pdf
- Result: 4.8 (scale: 1-5), see output.txt
- TO-DO: convert this txt file to DataFrame file (based on patterns \n for new line, ? separate qestion and answer)


2. Use pdf2image & pytesseract (goal is to use it for OCR for recognizing handwriting on PDF files)
- `python convert_pdf2image.py`
- test file: survey_2024.pdf
- Result: 0.1 (scale: 1-5), see output2.csv
- TO-DO: improve the OCR recognization or use other libraries.