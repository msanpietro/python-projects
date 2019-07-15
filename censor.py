def censor(text, word):
   numstars = len(word)
   sentence = text.split()  # split the string into a python list
   print len(sentence)
   for i in range(len(sentence)): # len() returns number of words in sentence
       if sentence[i]  == word:
           sentence[i] =  numstars * "*"
   newstring = " ".join(sentence)
   return newstring
    
print "The string is --> %s" %( censor("this hack is wack", "hack"))    
print "The string is --> %s" %( censor("how now brow cow how cow", "how"))    


string = "these are the times that try mens souls"
words = string.split()
   
reassemble = "bbb".join(words)
print reassemble
