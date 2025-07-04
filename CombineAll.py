#List of Tools
Tools = ["Docker", "Kubernetes", "Prometheus"]

#Save tools to a file
with open("tools.txt","w") as file:
    for tool in Tools:
        file.write(tool+"\n")

#Read and Print saved file
with open("tools.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print("Installed:", line.strip())
