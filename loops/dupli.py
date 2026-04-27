nums = [1, 2, 3, 2, 4, 1,3]
l = []   
for n in nums:
    if(n in l ):
        print(n)
    else:
        l.append(n)
print(l)