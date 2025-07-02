#Write to file

with open("log.txt", "w") as f:
    f.write("Deployment started...\n" )

# Read from file
with open("log.txt", "r") as f:
    content = f.read()
    print("Log content:\n", content)
