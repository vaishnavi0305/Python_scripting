#create a dictionary of at least 5 DevOps tools with:
#Tool name as the key
#Description/purpose as the value
Devops_tools = {
            "Kubernetes" : "Container Orchestration tool",
            "Jenkins" : "CiCD Tool",
            "Ansible" : "Configuration Management",
            "Terraform" : "Infrastructure as a code",
            "Github" : "Version control"
        }
with open("devops_tools.txt", "w") as file:
    for name, purpose in Devops_tools.items():
        file.write(f"{name} - {purpose}\n")

with open("devops_tools.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        name, purpose = line.strip().split(" - ")
        print(f"Tool: {name}")
        print(f"Purpose: {purpose}\n")
