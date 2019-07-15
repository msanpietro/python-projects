#! /usr/bin/python

#zeromatrix.py

# Write an algorithm such that if an element of an MxN matrix is 0, it's entire row and column are set to zero
# This particular algorithm searches for the "zero" element by element
# a more space efficient method would be to check if a row or col contain a 0. If they do then nullify
# the row and column. No need to know exactly the value of each element this way.

# something like if matrix[0].count(0) == 0  or matrix[0].include?(0) then zero out the row

def zeromatrix(matrix):
   row = [0,0,0,0,0]
   column = [0,0,0,0,0]

   ## assuming all rows have same length then use len() which is # of elements per row
   numcolumns = len(matrix[0]) 
   #print ( "numcolumns is %s" %(numcolumns)  )
   numrows = len(matrix)
   #print ( "numrows is %s" %(numrows)  )

   ## find the rows and columns that contain zeros
   # don't forget range (0, 2) does not include 2 so have to extend to numrows even though index starts at 0
   for x in range(0, numrows): 
         for y in range(0, numcolumns):  
             if matrix[x][y] == 0:
                 row[x] = True
                 column[y] = True

   # nullify the rows and columns that are marked "zero"
   for x in range(0, numrows):
         for y in range(0, numcolumns):
                 if row[x] == True:
                    matrix[x][y] = 0
                    
   for y in range(0, numcolumns):
         for x in range(0, numrows):
                 if column[y] == True:
                    matrix[x][y] = 0


#### MAIN
# first define the matrix we are starting with
matrix = [ [1, 0 , 3,  4,  5],
         [5,  6  , 7,  8,  9],
         [9,  10, 11,  0, 13],
         [19, 10, 11, 12, 13],
         [0, 14,  15, 16, 17] ]
print "This is the starting matrix........."
print "---------------------"
print matrix[0]
print "---------------------"
print matrix[1]
print "---------------------"
print matrix[2]
print "---------------------"
print matrix[3]
print "---------------------"
print matrix[4]

print " " 
print "This is the zeroed out matrix........."
zeromatrix(matrix)
print "---------------------"
print matrix[0]
print "---------------------"
print matrix[1]
print "---------------------"
print matrix[2]
print "---------------------"
print matrix[3]
print "---------------------"
print matrix[4]










