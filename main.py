import datefinder
import pyPdf
import parsedatetime



pdf = pyPdf.PdfFileReader(open('Syllabus-ACC 301 VANCE.pdf', "rb"))
pdf_text = ''
for page in pdf.pages:
    pdf_text += page.extractText()


# open file name test_input.txt

# file = open('test_input.txt', 'r')

# text = file.read()

# print pdf_text
dates = datefinder.find_dates(pdf_text, False, True, False)  # text)

p = parsedatetime.Calendar();
print p.parse("Monday, April 23, from 10:30 a.m. to 12:30 p.m.")


# file.close()
