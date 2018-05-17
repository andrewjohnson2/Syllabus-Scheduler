import datefinder
import pyPdf
import textract

import regex as re




def extract_date_strings(self, text, strict=False):
    """
    Scans text for possible datetime strings and extracts them

    source: also return the original date string
    index: also return the indices of the date string in the text
    strict: Strict mode will only return dates sourced with day, month, and year
    """
    for match in self.DATE_REGEX.finditer(text):
        match_str = match.group(0)
        indices = match.span(0)

        ## Get individual group matches
        captures = match.capturesdict()
        time = captures.get('time')
        digits = captures.get('digits')
        digits_modifiers = captures.get('digits_modifiers')
        days = captures.get('days')
        months = captures.get('months')
        timezones = captures.get('timezones')
        delimiters = captures.get('delimiters')
        time = captures.get('time)')
        time_periods = captures.get('time_periods')
        extra_tokens = captures.get('extra_tokens')

        if strict:
            complete = False
            ## 12-05-2015
            if len(digits) == 3:
                complete = True
            ## 19 February 2013 year 09:10
            elif (len(months) == 1) and (len(digits) == 1 or len(digits) == 2):
                complete = True

            if not complete:
                continue

        ## sanitize date string
        ## replace unhelpful whitespace characters with single whitespace
        match_str = re.sub('[\n\t\s\xa0]+', ' ', match_str)
        match_str = match_str.strip(self.STRIP_CHARS)

        ## Save sanitized source string
        yield match_str, indices, captures


datefinder.DateFinder.extract_date_strings = extract_date_strings



# pdf = pyPdf.PdfFileReader(open('syllabus/econ101.pdf', "rb"))
# pdf_text = ''
# for page in pdf.pages:
#     pdf_text += page.extractText()








pdf_text = textract.process("syllabus/PDFPublicHandler.ashx-2.pdf")

print pdf_text


file = open('test_input.txt', 'r')


pdf_text = 'February 14/16 February 8'

dates = datefinder.find_dates(pdf_text, True, False, True)  # text)

for date in dates:
    # if date[0].year == 2018:
        print date

# file.close()
