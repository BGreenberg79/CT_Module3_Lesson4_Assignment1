# Task 1 Email Extract Enhancement

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)

eliminate = r"\b[A-Za-z0-9._%+-]+@[exclude]+\.[A-Z|a-z]{2,}[,]{1}\s{1}"

modified_text = re.sub(eliminate,"", text,1)
print(modified_text)

'''
I removed the exclude email from the original text by making a second regular expression that I assigned to the variable eliminate.
I used most of the same formatting from the original find all but specified exclude inside the brackets after the at symbol.
I also included a single comma and white space each at the end of the expression to make the ensuing re.sub and print statements fucntion correctly.
The re.sub() I used worked by taking the eliminate variable (regular expression that I wrote), and replacing that occurance with ean empty string shown to be "".
I then identified that I was using the string found in text for modification and would be making this modification once.
I assigned this re.sub() to the variable modified_text and then printed modified_text to show the substitution/removal was successful.
'''