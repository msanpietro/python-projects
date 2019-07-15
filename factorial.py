def factorial(x):
  if x == 0:
        return 0
  if x == 1:
        return 1
  return x * factorial(x-1)

print "factorial(10) is equal to %s" %(factorial(10))
print "factorial(5) is equal to %s" %(factorial(5))
