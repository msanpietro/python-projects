def is_prime(x):
  count = 0 
  for n in range(2, x):
    if (x % n) == 0:
          count += 1
   
  if count == 0: 
       return True

for i in range(3,20):
  if is_prime(i) == True:
     print "%s is a prime number" %(i)
  else:
     print "%s is not a prime number" %(i)

