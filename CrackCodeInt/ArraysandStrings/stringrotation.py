#! /usr/bin/python

#stringrotation,py

# Give two strings check if s2 is a rotation of s1
# e.g. waterbottle is a rotation of erbottlewat
# To solve we double s1 since if s2 is a rotation of s1 then s2 must be contained in s1 + s1
import os.path
import sys

def isSubstring(string1, string2):
   n = len(string1)
   if len(string1) != len(string2) or n == 0:
      return False


   # if string2 is a substring of string1 it will be contained in string1 + string1
   # saving us the need to wrap indexes or cut the string
   dblstring1 = string1 + string1

   if string2 in dblstring1:
   	 return True
   else:
   	 return False

## Main
# initialize a list of 10 elements since we don't know the size yet
strings = range(10)

n = 0
fileName = sys.argv[1] 

if os.path.isfile(fileName):
   print ("%s is a valid filename" %(fileName) ) 
else:
   print ("%s is not a valid filename" %(fileName) ) 

file = open(fileName, "r")

for line in file:
    strings[n] = line.rstrip().strip()
    print ( "the string is %s" %(strings[n])  ) 
    n = n + 1 

string1 = strings[0]
string2 = strings[1]

if isSubstring(string1, string2):
   print ("%s is a substring of %s" %(string2, string1) ) 


