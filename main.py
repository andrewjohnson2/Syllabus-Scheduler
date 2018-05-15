
import pyPdf
pdf = pyPdf.PdfFileReader(open('test_pdf.pdf', "rb"))
pdf_text = ''
for page in pdf.pages:
    pdf_text += page.extractText()



import datefinder

# open file name test_input.txt

#file = open('test_input.txt', 'r')

#text = file.read()

dates = datefinder.find_dates(pdf_text)#text)

for date in dates:
    print date


#file.close()