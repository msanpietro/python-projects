vowels = "aeiouAEIOU"
text = "this is a test"

def anti_vowel(text):
    new_word = ""
    for char in text:
       if char in vowels:
          new_word += ""
       else: 
          new_word += char
    return new_word

print "The string is \"%s\"" %(text)
print "the new string is \"%s\"" %(anti_vowel("this is a test"))
