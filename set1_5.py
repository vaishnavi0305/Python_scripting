#Print the memory address of two identical strings — do they match?

s1= "hello"
s2= "hello"

id1=id(s1)
id2=id(s2)

print("Memory address of s1", id1," and s2 ", id2, "are same")
