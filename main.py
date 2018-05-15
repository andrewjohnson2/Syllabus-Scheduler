import pyPdf
import datefinder

pdf = pyPdf.PdfFileReader(open('Syllabus-ACC 301 VANCE.pdf', "rb"))
pdf_text = ''
for page in pdf.pages:
    pdf_text += page.extractText()


# open file name test_input.txt

# file = open('test_input.txt', 'r')

# text = file.read()

dates = datefinder.find_dates(pdf_text)  # text)

for date in dates:
    print date

# file.close()
