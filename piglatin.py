original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print "the word entered was %s" %(original)
else:
    print 'empty'
    
word = original.lower()    
pyg = "ay"  # create the suffix

first = original[0]
second = original[1]
third = original[2]

new_word = word[1:len(new_word)] + first + pyg
print new_word

# other possible solutions below
#1st2letters = word[0:2]
#piglatin = word[1:] + 1st2letters
#print "the piglatin word is %s" %(piglatin)
