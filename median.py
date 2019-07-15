def median(rawlist):
    sortedlist = sorted(rawlist)
    length = len(sortedlist)
    if length % 2 != 0:
       return sortedlist[length/2]
    else: 
       return (sortedlist[length/2] + sortedlist[(length-1)/2])/2.0
    
print median([1,2,3,4,5])
print median([1,2,3,4,5,6])
print median([1,2,3,4,5,9,11,15,21])
print median([21,32,3,4,5,9,11,15,21])
