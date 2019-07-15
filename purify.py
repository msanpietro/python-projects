def purify(numbers):
    purelist = []
    for i in numbers:
        if i % 2 == 0:
            purelist.append(i)
    return purelist
    
print purify([1,2,3,4,5,6,7,8,9,10])
