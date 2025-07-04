import json

#Example data
server_info = {
            "name" : "Dev-server",
            "Ip" : "10.34.6.5",
            "Status" : "Running"
        }

# write to json file
with open("server.json", "w") as f:
    json.dump(server_info, f)

# read it back
with open("server.json", "r") as f:
    data = json.load(f)
    print("Server Name:", data["name"])
