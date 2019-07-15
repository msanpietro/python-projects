# Read a string from a file and determine if it is entirely made of Unique characters
filename = "hello.txt"
file = open('is_unique.txt', "r")
for line in file:
    inputstring = line
    #print inputstring

checklist = list(inputstring)
checkset  = set(inputstring)

lenlist = len(checklist)
lenset  = len(checkset)

if lenlist == lenset:
   print "the string contains only unique values"
else:
   print "the string does not contain unique values"



