#!/usr/bin/python

# stringcompression.py

# Assume the string has only uppercase and lowercase letters
# implement a method to perform basic string compression using counts of repeated characters

import os.path
import sys

def compressthestring(uncompressedstring):
    compressedstring = ""
    countConsecutive = 1 
    for i in range (len(uncompressedstring) - 1):
        if uncompressedstring[i] == uncompressedstring[i+1]:
           countConsecutive+=1
        else:
           compressedstring = compressedstring + uncompressedstring[i] 
           compressedstring = compressedstring + str(countConsecutive)
           countConsecutive = 1 
    compressedstring = compressedstring + uncompressedstring[i]
    compressedstring = compressedstring + str(countConsecutive)
    return compressedstring 



## MAIN
fileName = sys.argv[1]

if os.path.isfile(fileName):
    print ("%s is a valid filename" %(fileName) )
else:
    print ("%s is not a valid filename" %(fileName) )

file = open(fileName, "r")

for line in file:
  uncompressedstring = line.rstrip().strip()
  print ( "the compressed string is %s" %( compressthestring(uncompressedstring)  ) )

