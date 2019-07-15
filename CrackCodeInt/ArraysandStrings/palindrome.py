# palindrone.py
## check if a string is a permuation of a palindrome

# read the string in from a file
# assume an ASCII string ie. 128 characters ( 7 bit )

# Break the Algorithm down into even and odd length strings
# Even length String: 
# only pairs of characters in an even length palindrome

# Odd length String:
# Strings of odd length must have exactly one character with an odd count
# "a man a plan a canal panama"
# madam, elle, 
# so for both cases there can be no more than 1 character in the string with an odd count

##########################################################

def check_palindrome(line):
  # make a dictionary aka hash
  numofoccurances = {}
  count = 0 

  for i in range( ord('a') , ord('z')+1 ):
      numofoccurances[chr(i)] = line.count(chr(i))
      #print numofoccurances[chr(i)]

  for i in range( ord('a') , ord('z')+1 ):
      if numofoccurances[chr(i)] % 2 == 1:
         count = count + 1
  
  if count == 1:
     print("%s is a palindrome permutation." %(line) )
  else:
     print ("%s can't be a palindrome permutation." %(line) ) 
 

#### Main
with open('datapalindrome.txt') as file:
    for line in file:
        check_palindrome(line)


