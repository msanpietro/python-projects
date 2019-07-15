# URLify.py
# given a string replace all spaces with %20

def replacespace(line):
    newline = line.replace(" ", "%20")
    return newline 
  


## Read lines in from a file
with open('RLify.txt') as file:
    for line in file: 
        line = line.rstrip()

print replacespace(line)
