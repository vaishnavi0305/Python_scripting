
# 🐍 Python Scripting for DevOps Engineers

This repo covers basic to intermediate Python scripting essentials tailored for DevOps Engineers. From variables to file handling and system automation, each section includes examples and mini-assignments for hands-on learning.

---

## 1️⃣ Variables & Data Types

```python
# Variables
name = "Vaishnavi"
age = 25
is_devops_engineer = True
rating = 4.9

print("Name:", name)
print("Age:", age)
print("DevOps Engineer:", is_devops_engineer)
print("Rating:", rating)
```

### 🧠 Data Types in Python:
- `str` → Text
- `int` → Whole numbers
- `float` → Decimal numbers
- `bool` → `True` / `False`

---

## 2️⃣ Input & Output

```python
user_name = input("Enter your name: ")
print("Hello,", user_name)

num = input("Enter a number: ")
print("Your number times 2 is:", int(num) * 2)
```

📌 `input()` always returns a string. Use `int()`, `float()` to cast as needed.

---

## 3️⃣ Conditional Statements

```python
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
```

🧠 Indentation is mandatory in Python (use 4 spaces).

---

## 4️⃣ Loops

```python
# For loop
for i in range(1, 6):
    print("Count:", i)

# While loop
n = 3
while n > 0:
    print("n =", n)
    n -= 1
```

📌 `range(start, end)` goes from `start` to `end - 1`.

---

## 5️⃣ Functions

```python
def greet(name):
    print("Hello,", name)

greet("Vaishnavi")

def add(a, b):
    return a + b

print("Sum:", add(5, 10))
```

🧠 Functions promote reusable code. Use `return` to return values.

---

## ✅ Day 1 Assignment

Create a file `assignment_day1.py` that:
- Takes user name and age
- Checks if age >= 18
- Prints welcome message if eligible
- Loops from 1 to 5 printing DevOps skill level

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print("Welcome", name, "you are eligible to vote")
else:
    print("Sorry", name, "you are not eligible to vote")

for level in range(1, 6):
    print("DevOps Skill Level:", level)
```

---

## 6️⃣ Lists

```python
tools = ["Terraform", "Ansible", "Jenkins"]
print("First tool:", tools[0])

tools.append("GitHub Actions")
tools.remove("Jenkins")

for tool in tools:
    print("Tool:", tool)
```

---

## 7️⃣ Dictionaries

```python
server = {
    "name": "web-server-1",
    "ip": "192.168.1.10",
    "status": "running"
}

print("Server IP:", server["ip"])
server["os"] = "Ubuntu"

for key, value in server.items():
    print(key, ":", value)
```

---

## 8️⃣ File Handling

**Reading a file:**

```python
with open("tools.txt", "r") as file:
    content = file.read()
    print("File content:
", content)
```

**Writing to a file:**

```python
with open("my_log.txt", "w") as file:
    file.write("Deployment completed successfully.
")
```

**Appending to a file:**

```python
with open("my_log.txt", "a") as file:
    file.write("Added more logs...
")
```

---

## 🧪 Bonus: Combine Lists and Files

```python
tools = ["Docker", "Kubernetes", "Prometheus"]

# Write to file
with open("tools.txt", "w") as file:
    for tool in tools:
        file.write(tool + "\n")

# Read and print
with open("tools.txt", "r") as file:
    for line in file:
        print("Installed:", line.strip())
```

---

## ✅ Assignment: DevOps Tools Dictionary

```python
Devops_tools = {
    "Kubernetes": "Container Orchestration tool",
    "Jenkins": "CI/CD Tool",
    "Ansible": "Configuration Management",
    "Terraform": "Infrastructure as Code",
    "GitHub": "Version Control"
}

with open("devops_tools.txt", "w") as file:
    for name, purpose in Devops_tools.items():
        file.write(f"{name} - {purpose}\n")

with open("devops_tools.txt", "r") as file:
    for line in file.readlines():
        name, purpose = line.strip().split(" - ")
        print(f"Tool: {name}")
        print(f"Purpose: {purpose}\n")
```

---

## 9️⃣ OS Module

```python
import os

print("Current Directory:", os.getcwd())
print("Files:", os.listdir())

os.mkdir("logs")

with open("logs/status.txt", "w") as f:
    f.write("Server is up\n")

print("Path exists?", os.path.exists("logs/status.txt"))
```

---

## 🔟 sys Module

```python
import sys

print("Script name:", sys.argv[0])

if len(sys.argv) > 1:
    print("CLI Argument:", sys.argv[1])
else:
    print("No argument passed")
```

Usage:
```bash
python3 day3_sys_os_subprocess.py DevOps
```

---

## 🔁 subprocess Module

```python
import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print("Output:\n", result.stdout)

uptime = subprocess.getoutput("uptime")
print("System Uptime:", uptime)
```

---

## 🔢 json Module

```python
import json

server_info = {
    "name": "dev-server",
    "ip": "192.168.0.1",
    "status": "running"
}

with open("server.json", "w") as f:
    json.dump(server_info, f)

with open("server.json", "r") as f:
    data = json.load(f)
    print("Server name:", data["name"])
```

---

## ✅ Day 3 Assignment – Directory Inspector

Write a script `directory_inspector.py` to:
- Take directory path from CLI
- If exists, list all files/folders
- Get size (in KB) using `os.path.getsize()`
- Save output in `directory_report.json`

```python
import os
import json
import sys

if len(sys.argv) < 2:
    print("usage: python3 directory_inspector.py <directoryPath>")
    sys.exit(1)

path = sys.argv[1]

if os.path.exists(path) and os.path.isdir(path):
    report = {}

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            size = round(os.path.getsize(full_path)/1024, 2)
            report[item] = {"type": "file", "size_kb": size}
        elif os.path.isdir(full_path):
            report[item] = {"type": "directory", "size_kb": 0.0}

    with open("directory_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print(f"Found {len(report)} items. Saved to directory_report.json")
else:
    print("Path does not exist.")
```

---

## 📚 Summary

This covers:
- ✅ Python basics for DevOps
- ✅ Files, JSON, CLI, and automation
- ✅ Real-world style assignments

Perfect for scripting tasks, automation, and interview readiness.

---

## 🚀 Author

**Vaishnavi Buradkar**  
Cloud & DevOps Engineer | AWS | Terraform | Jenkins | Python  
🔗 [GitHub](https://github.com/vaishnavi0305)
