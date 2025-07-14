#Reverse the list [1, 2, 3] using a method (not slicing or reversed()).

l1 = [1,2,3]
l2 = []
for i in range(len(l1)-1, -1, -1):
    l2.append(l1[i])
print(l2)
