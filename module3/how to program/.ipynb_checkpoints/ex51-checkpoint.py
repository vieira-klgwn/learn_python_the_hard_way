# NOW YOU CAN WRITE THE ACTUAL CODE BY CHANGING THE PSEUDO CODE INTO ACTUAL PYTHON CODE

#import modules I need
import pdftotext
import re
import sys

#open the pdf
infile = open(sys.argv[1], "rb")

# convert it to text
pdf = pdftotext.PDF(infile)
print(pdf.read())

lines = "".join(pdf).split("\n")# FYI, this splits each start of newline into another element of an array. 
# it means that each other line become a array member

num = 1
# find Reporting Period
for line in lines:
    if line.startswith("Reporting Period"):
        # print it
        print(f"[{num}]",line)
        num += 1
    else:
        pass
# other optional codes of using regular expressions
numbers = re.compile(r"^[,\d\s]+$")
ignore = re.compile(r"^\s*$")

for line in lines:
    if numbers.match(line):
        print("Line much number:", line)
    elif numbers.match(line):
        print("Line match ignore:", line)
    else:
        pass