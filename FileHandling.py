# Writing to a file

with open("tools.txt", "w") as file:
    file.write("Deployment completed Successfully.\n")
    file.write("All systems are operational.\n")

# Appending to a file

with open("tools.txt", "a") as file:
    file.write("Added more logs..\n")

# Reading to a file , I am doing the reading afterwards as writing or appending steps will not work if I do it first.

with open("tools.txt", "r") as file:
    content = file.read()
    print("content of the file is:\n", content)
