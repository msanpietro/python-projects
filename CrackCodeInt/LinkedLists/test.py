#!/usr/bin/python

x = 0 

for i in range ( 1 , 5 , 1):
    print ( "the value of i is %s" %(i) ) 
    print ( "the value of x is %s" %(x) ) 
    for j in range ( 6 , 10, 1):
        print ( "the value of j is %s" %(j) ) 
    x = x + 3  ## obviously this line is NOT IN THE LOOP. It executes wht the for loop ends
      

