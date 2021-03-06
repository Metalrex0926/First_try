# Import libraries 
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path
import os 

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# Path of the pdf 
PDF_file = "E:\Codes\PDF\DL_0197_18-19.pdf"

# Store all the pages of the PDF in a variable 
pages = convert_from_path(PDF_file, 500) 

# Counter to store images of each page of PDF to image 
image_counter = 1

# Iterate through all the pages stored above 
for page in pages: 
    filename = "page_"+str(image_counter)+".jpg"
    page.save(filename, 'JPEG',)
    image_counter = image_counter + 1

filelimit = image_counter-1


outfile = "E:\Codes\PDF\DL_0197_18-19.txt"


f = open(outfile, "a") 


for i in range(1, filelimit + 1):
    filename = "page_"+str(i)+".jpg"
    text = str(((pytesseract.image_to_string(Image.open(filename)))))
    text = text.replace('-\n', '')
    f.write(text) 

f.close() 


