import subprocess
status = subprocess.run(["systemctl", "is-active", "java"], capture_output=True, text=True)
print(status)
if status.stdout.strip() == "active":
    result = print("running")
    print(result)
