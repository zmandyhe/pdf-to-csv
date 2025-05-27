"""PyPDF2 is suitable for survey_2025.pdf type, it recognize computer input text
with two columns of survey, we can convert this pattern to two column dataframe."""

import os
import PyPDF2
import csv

dir = os.getcwd()

# List all PDF files in the current folder
pdf_files = [file for file in os.listdir(dir) if file.endswith('_2025.pdf')]

# read line by line
text = []
for pdf in pdf_files:
    print(pdf)
    with open(pdf, 'rb') as file:
        # Creating a pdf reader object
        pdfReader = PyPDF2.PdfReader(file)
        # Getting number of pages in pdf file
        pages = len(pdfReader.pages)

        # Loop for reading all the Pages
        for i in range(pages):
            # Creating a page object
            pageObj = pdfReader.pages[i]
        
            # Printing Page Number
            print("Page No: ",i)
        
            # Extracting text from page
            # And splitting it into chunks of lines
            text = pageObj.extract_text().split("  ")
        
            # Finally the lines are stored into list
            # For iterating over list a loop is used
            for i in range(len(text)):
        
                # Printing the line
                # Lines are seprated using "\n"
                print(text[i],end="\n\n")
        
                # For Seprating the Pages
                print()
        
    # closing the pdf file object
    file.close()

print(text)

with open("output.txt", "w") as file:
    file.write(text[0])

# Here you would parse text into a structured format depending on the specifics of your PDF
# with open('output1.csv', 'w', newline='') as file:
    # writer = csv.writer(file)
    # writer.writerows(text)

