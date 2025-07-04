#Takes your name and age as input
name = input("Enter your name:")
age = int(input("Enter your age:"))

#Check if you are eligible to vote "age>=18"
if age>=18:
# print Welcome message if eligible
    print("Welcome ",name, "you are eligible to vote")
else:
    print("Sorry", name, "you are not eligible to vote")

# Loops from 1 to 5 and prints "Devops skill level: X" for each
for X in range(1,5):
    print("Devops Skill Level:", X)

