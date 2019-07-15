#! /usr/bin/python

## rotate a NxN matrix 90 degrees
# Give an image represented by an NxN matrix where each pixel in the image is 4 bytes
# write a method to rotate the image by 90 degrees
# Note that an integer value is 4 bytes long so we will use integer values
# We will only be rotating the outer "shell" of the matrix
# The inner values will not be touched
# Consider a 4x4 matrix when we rotate the 1st row we also rotate the last row
# When we rotate the 2nd row we also rotate the 2nd to last row
# For this reason we need only rotate n/2 rows not all rows

# rotatematrix.py
## use a list of a list as a matrix

def rotatematrix( matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
       return False
    layer = 0 
    j = 0 
    length = len(matrix)
    
    ## start the outer loop which increments the layer 
    for layer in range(0, length/2  , 1 ):  # the length is 4 but we only need to rotate 2 rows ( row 0 and row1)
        print ( "the value of layer is %s" %(layer) ) 
        last = length - 1 - layer 
        print "im in the outer loop"

        for j in range(layer, last, 1):
            offset = j - layer
            print ( "j is %s" %(j) )
            print (  "layer is %s" %(layer) ) 
            print (  "last is %s" %(last) ) 
            print (  "offset is %s" %(offset) ) 

            temp = matrix[layer][j]   ## save the top corner
  
            # shift the left column to the top 
            matrix[layer][j] = matrix[last-offset][layer]

            # shift the bottom to the left
            matrix[last-offset][layer] = matrix[last][last - offset]

            # shift right to the bottom
            matrix[last][last-offset] = matrix[j][last]

            # shift top to the right
            matrix[j][last] = temp

    return  matrix 



## MAIN
matrix = [[1 ,2 , 3 , 4],
         [5 ,6  , 7 , 8],
         [9,10,11,12],
         [13,14,15,16]]
print matrix[0]
print "---------------------"
print matrix[1]
print "---------------------"
print matrix[2]
print "---------------------"
print matrix[3]
print "---------------------"

length = len(matrix)

rotated_matrix = rotatematrix(matrix)

for i in range(0, length, 1):
   print rotated_matrix[i]
   print "---------------"
