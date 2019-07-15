def reverse(text):
  length = len(text)
  index = length
  newstring = ""
  for i in range(0, length):
     newstring = newstring + text[index-1]
     index -= 1
  return newstring

print "the reversed string is %s " %(reverse("abcd"))
