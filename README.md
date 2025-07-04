Python Scripting or Python Notes 

 

1️⃣ Variables & Data Types 

# Variables 
name = "Vaishnavi" 
age = 25 
is_devops_engineer = True 
rating = 4.9 
 
print("Name:", name) 
print("Age:", age) 
print("DevOps Engineer:", is_devops_engineer) 
print("Rating:", rating) 
 

🧠 Types in Python: 

str → text 

int → whole numbers 

float → decimals 

bool → True/False 

========================================================================= 

2️⃣ Input & Output 

user_name = input("Enter your name: ") 
print("Hello,", user_name) 
 
num = input("Enter a number: ") 
print("Your number times 2 is:", int(num) * 2) 
 

📌 input() always returns a string. You must cast it using int(), float(), etc. 

==================================================================== 

3️⃣ Conditional Statements 

marks = int(input("Enter your marks: ")) 
 
if marks >= 90: 
    print("Grade: A") 
elif marks >= 75: 
    print("Grade: B") 
elif marks >= 60: 
    print("Grade: C") 
else: 
    print("Grade: F") 
 

🧠 Indentation is mandatory in Python (4 spaces or 1 tab). 

======================================================================== 

4️⃣ Loops 

# For loop 
for i in range(1, 6): 
    print("Count:", i) 
 
# While loop 
n = 3 
while n > 0: 
    print("n =", n) 
    n -= 1 
 

📌 range(start, end) generates numbers up to but not including end. 

========================================================================= 

 5️⃣ Functions 

def greet(name): 
    print("Hello,", name) 
 
greet("Vaishnavi") 
 
def add(a, b): 
    return a + b 
 
sum_result = add(5, 10) 
print("Sum:", sum_result) 
 

🧠 Functions help you reuse code. Use return to send back results. 

======================================================================== 

✅ Day 1 Assignment for You 

Create a script assignment_day1.py that: 

Takes your name and age as input 

Checks if you’re eligible to vote (age >= 18) 

Prints a welcome message if eligible 

Loops from 1 to 5 and prints "DevOps Skill Level: X" for each 

Script: 

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

 

======================================================================== 

6️⃣ Python List 

Lists store ordered sequences of values. You can add, remove, or modify them. 

# Create a list 
tools = ["Terraform", "Ansible", "Jenkins"] 
 
# Access elements 
print("First tool:", tools[0])  # Index starts at 0 
 
# Add item 
tools.append("GitHub Actions") 
 
# Remove item 
tools.remove("Jenkins") 
 
# Loop through list 
for tool in tools: 
    print("Tool:", tool) 

 

======================================================================== 

2️⃣ Python Dictionaries 

Dictionaries store key-value pairs (like JSON). 

# Create a dictionary 
server = { 
    "name": "web-server-1", 
    "ip": "192.168.1.10", 
    "status": "running" 
} 
 
# Access values 
print("Server IP:", server["ip"]) 
 
# Add new key 
server["os"] = "Ubuntu" 
 
# Loop through keys & values 
for key, value in server.items(): 
    print(key, ":", value) 

======================================================================== 

3️⃣ File Handling in Python 

Python uses the open() function for reading/writing files. 

📖 Reading a File 

with open("tools.txt", "r") as file: 
    content = file.read() 
    print("File content:\n", content) 

📝 Writing to a File 

with open("my_log.txt", "w") as file: 
    file.write("Deployment completed successfully.\n") 

file.write("All systems are operational.\n") 
 

➕ Appending to a File 

with open("my_log.txt", "a") as file: 
    file.write("Added more logs...\n") 
 

====================================================================== 

🧪 Bonus: Combine All 

# List of tools 
tools = ["Docker", "Kubernetes", "Prometheus"] 
 
# Save tools to a file 
with open("tools.txt", "w") as file: 
    for tool in tools: 
        file.write(tool + "\n") 
 
# Read and print saved file 
with open("tools.txt", "r") as file: 
    lines = file.readlines() 
    for line in lines: 
        print("Installed:", line.strip()) 
 

======================================================================= 

✅ Assignment Requirements 

Create a dictionary of at least 5 DevOps tools with: 

Tool name as the key 

Description/purpose as the value 
 Example: 

{ 
  "Terraform": "Infrastructure as Code", 
  "Jenkins": "CI/CD Pipeline", } 
 

Write each tool and its purpose to a file called devops_tools.txt in this format: 

Terraform - Infrastructure as Code 
Jenkins - CI/CD Pipeline 
 

Read the file and display the tools in this format: 

Tool: Terraform 
Purpose: Infrastructure as Code 

 

Script: 

 

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

 

========================================================================= 

1️⃣ os Module – Interact with System/Files 

import os 

# Current working directory 

print("Current Directory:", os.getcwd()) 

  

# List files in current dir 

print("Files:", os.listdir()) 

  

# Create a new folder 

os.mkdir("logs") 

  

# Create a file inside that folder 

with open("logs/status.txt", "w") as f: 

    f.write("Server is up\n") 

  

# Check if a path exists 

print("Does logs/status.txt exist?", os.path.exists("logs/status.txt")) 

 

====================================================================== 

2️⃣ sys Module – Command-Line Arguments 

import sys 
 
print("Script name:", sys.argv[0])  # First arg is always the script name 
 
if len(sys.argv) > 1: 
    print("User Input from CLI:", sys.argv[1]) 
else: 
    print("No argument passed") 
 

Try it like this: 

python3 day3_sys_os_subprocess.py DevOps 

===================================================================== 

3️⃣ subprocess – Run Shell Commands from Python 

import subprocess 
 
# Run 'ls -l' and capture output 
result = subprocess.run(["ls", "-l"], capture_output=True, text=True) 
 
# Print command output 
print("Output of ls -l:\n", result.stdout) 
 
# Run 'uptime' 
uptime = subprocess.getoutput("uptime") 
print("System Uptime:", uptime) 
 

✅ This is super useful for DevOps to run bash/terraform/awscli inside Python scripts. 

====================================================================== 

4️⃣ json – Read & Write JSON Files 

import json 
 
# Example data 
server_info = { 
    "name": "dev-server", 
    "ip": "192.168.0.1", 
    "status": "running" 
} 
 
# Write to JSON file 
with open("server.json", "w") as f: 
    json.dump(server_info, f) 
 
# Read it back 
with open("server.json", "r") as f: 
    data = json.load(f) 
    print("Server name:", data["name"]) 
 

======================================================================== 

🧪 Day 3 Mini Assignment 

✅ Assignment Requirements 

Take a directory path as a command-line argument (e.g., python3 dir_inspector.py /etc) 

If the directory exists: 

Use os.listdir() to list files/folders 

For each file: 

Use os.path.getsize() to get its size (in KB) 

Use os.path.isfile() to check if it's a file or directory 

Save details in a JSON file called directory_report.json 

 

JSON Format: 

{ 
  "filename1.txt": {"type": "file", "size_kb": 1.2}, 
  "subfolder": {"type": "directory", "size_kb": 0.0} 
} 
 

If the directory doesn’t exist, print an error and exit. 

🧠 Hints 

Use os.path.join() to get full file paths 

Convert bytes to KB: size / 1024 

 

Script:- 

import os 

import subprocess 

import json 

import sys 

  

if len(sys.argv) < 2: 

    print("usage: python3 Assignment3.py <directoryPath>") 

    sys.exit(1) 

  

Path = sys.argv[1] 

  

if os.path.exists(Path) and os.path.isdir(Path): 

    listFileFolder = os.listdir(Path) 

    report = {} 

  

    for list in listFileFolder: 

        full_path = os.path.join(Path, list) # Get absolute path 

        if os.path.isfile(full_path): 

            size = round(os.path.getsize(full_path)/1024, 2) 

            report[list] = {"type":"file", "size": size} 

        elif os.path.isdir(full_path): 

            report[list] = {"type": "directory", "size": 0.0} 

     

    #Save to json 

    with open("directory_report.json", "w") as f: 

        json.dump(report, f, indent=4) 

    print(f"Found {len(listFileFolder)} items.") 

    print("report saved to directory_report.json file") 

else: 

    print("Path doesnot exists") 

 

================================================================== 

 

 

 
 

 
