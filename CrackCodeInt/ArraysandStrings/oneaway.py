# oneaway.py
# there are 3 types of edits that are possible
# insert, remove  or replace character

# Given two strings decide if they are one edit, or zero edits away from each other
# assume we will read the strings from a file

# Replacement - if two strings are one replacement away it means they only differ in one place and they are the same length
# Insertion - if two strings are one insertion away it means they are identical except for a shift at some point
# Removal - if two strings are one removal away it is the same as the insertion case 
# write a method(s) that returns a boolean value for each case

# python oneaway.py oneaway.txt
import os.path
import sys

def oneeditreplace(firststring, secondstring):
    count = 0 
    for i in range(len(firststring)):
        if firststring[i] != secondstring[i]:
           count = count + 1 
    if count == 1: return True
    else:
        return False

def oneeditinsertdelete(firststring, secondstring):
    index1 = 0 
    index2 = 0
   
    while ( index1 < len(firststring) and index2 < len(secondstring) ):
        if firststring[index1] != secondstring[index2]:
            if index1 != index2:
               return False  ## this would mean a 2nd difference was found
            else:
               index2 = index2 + 1 ## then loop around  
            index1 = index1 + 1
            index2 = index2 + 1 
        else:
            return True


## MAIN
fileName = sys.argv[1]

if os.path.isfile(fileName):
    print ("%s is a valid filename" %(fileName) )
else:
    print ("%s is not a valid filename" %(fileName) )

file = open(fileName, "r")
print "The strings are one edit away (True or False):"
for line in file:
    words = line.split(",") # split the line into a list of two string
    words[0] = words[0].rstrip().strip() # remove the newline (\n) rstrip() and whitespace string
    words[1] = words[1].rstrip().strip() 
  #  print ("the strings are %s and %s" %(words[0], words[1]) )
   
# first deal with the corner case where the two strings are identical
    if words[0] == words[1]:
        print "the two strings are identical"

# next determine the length of each string in order to choose the correct method
    if len(words[0]) == len(words[1]):              ## if strings have identical length they may be one replacement away from each other 
        print ( "The strings %s and %s are ==> %s" %( words[0], words[1], oneeditreplace(words[0], words[1])  )  )
    elif len(words[0]) + 1 == len(words[1]):
        print ( "The strings %s and %s are ==> %s" %( words[0], words[1], oneeditinsertdelete(words[0], words[1]) ) )
    elif len(words[0]) - 1 == len(words[1]):
        print ( "The strings %s and %s are ==> %s" %( words[0], words[1], oneeditinsertdelete(words[0], words[1]) ) )
    else:
        print ""
