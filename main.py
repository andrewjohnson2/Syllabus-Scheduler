


import datefinder

# open file name test_input.txt

file = open('test_input.txt', 'r')

text = file.read()

dates = datefinder.find_dates(text)

for date in dates:
    print date


file.close()