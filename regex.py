# The "r" at the start of the pattern designates a python "raw" string which
# passes through backslashes without change 
import re

# search for a PATTERN "iii" in string "piiig"
# if the pattern is found match.group() is the matching text
match = re.search(r'iii', 'piiig')
print match.group()

# Search for ANY CHARACTER "."   but \n
match = re.search(r'..g', 'piiig')
print match.group()

# Search for any DIGIT CHARACTER "\d"
match = re.search(r'\d\d\d', 'p123g')
print match.group()

# Search for any WORD CHARACTER "\w" (a word is a letter or a digit)
match = re.search(r'\w\w\w', '@@abcd!!')
print match.group()

# Repetition examples 
# matches ONE OR MORE i's
match = re.search(r'pi+', 'piiig')
print match.group()

# matches ONE OR MORE i's but does not get to second set of i's
match = re.search(r'i+', 'piigiiii')
print match.group()

# match 3 digits that are possibly sepearated by whitespace
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')
print match.group()

# match the START OF A STRING
match = re.search(r'^b\w+', 'bfoobar')
print match.group()

# match an EMAIL ADDRESS inside a string
str = 'alice-b@google.com'
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
  print match.group()    ## alice-b@google.com

# match a PHONE NUMBER 
str = '540-662-7022'
match = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', str)
if match: 
   print match.group()
