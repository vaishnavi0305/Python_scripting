#create a Dictionary
server = {
        "name": "Server01",
        "IP": "10.0.78.99",
        "status": "Running"
         }

#Access values
print("Server IP:", server["IP"])

#Add new key
server["os"] = "ubuntu"

# Loops through keys and values
for key, value in server.items():
    print(key, ":", value)

print("dictionary:", server.items())
