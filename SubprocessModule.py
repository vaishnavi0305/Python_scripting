import subprocess

# Run "ls -l" command and capture output
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

#Print command output
print("Output of ls -l command is :", result.stdout)

#Run "Uptime"
uptime = subprocess.getoutput("uptime")
print("System uptime:", uptime)
