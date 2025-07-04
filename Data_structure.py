#Create a List
tools = ["terraform", "Ansible", "Jenkins"]

# Access the items in the list
print("Fist tool:", tools[0])

# Add item in the list
tools.append("GithubActions")

# Remove an item in the list
tools.remove("Ansible")

# Loop through list
for tool in tools:
    print("Tools:", tool)
