def count (sequence, item):
    count = 0 
    for i in range(len(sequence)):
        if sequence[i] == item:
            count+=1
    return count
print "how many times does it occur? => %s" %(count( [1,2,2,2,3,4,5,6,2,2] , 2 ))
print "how many times does it occur? => %s" %(count( ["one", "two", "three", "two", "two", "two", "two", "five"] , "two" ))


