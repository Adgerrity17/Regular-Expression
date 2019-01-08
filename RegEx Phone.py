
#Finding patterns in text without regular expressions
import re #import regular expression library

phonenumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #variable now contains a regex object

mo = phonenumberRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group()) #call group to return the match object




