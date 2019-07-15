# checkpermutation.rb
# given two strings check if one string is a permutation of the other

def checkpermutation(line1, line2):
    if len(line1) != len(line2):
        print "these 2 lines are not permutations of one another because they are not the same length"
    sortedline1 = sorted(line1)
    sortedline2 = sorted(line2)
 
   # print sortedline1
   # print sortedline2
  
    ## iterate over the characters
    numberofchars = len(line1)
    for i in range (0, numberofchars-1, 1):
        if sortedline1[i] != sortedline2[i]:
            print "these 2 lines are not permutation of one another but they are the same length" 
            return
        
    print "these 2 lines are permutions of one another"


## Read lines in from a file
with open('permutation.txt') as file:
    listarray = []
    for line in file: 
        listarray.append(line.rstrip())

checkpermutation(listarray[0], listarray[1])
