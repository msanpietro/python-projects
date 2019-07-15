def remove_duplicates(alist):
    processedlist = []
    for item in alist:
        if item not in processedlist:
            processedlist.append(item)
    return processedlist

print remove_duplicates([1,1,2,2,3,4,5,6,7,7,7])
