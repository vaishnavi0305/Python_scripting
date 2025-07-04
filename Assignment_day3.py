import os
import subprocess
import json
import sys

file = sys.argv[1]
print("check file size of",file, "if exists")

if os.path.exists(file):
    detail = subprocess.run(["ls", "-lsh", file], capture_output=True, text=True)
    print("file detail is:\n", detail.stdout)
    
    #Extract size from ls output
    output_lines = detail.stdout.splitlines()
    if output_lines:
        size = output_lines[0].split()[0] #Get the 5th column (size)
        # Prepare JSON structure
        file_info = {
            "filename": file,
            "size": size,
            "status": "exists"
        }
        #Save to file
        with open("file_info.json", "w") as f:
            json.dump(file_info, f, indent=4)
        print("File info saved to file_info.json")
else:
    print("file ", file, "does not exists.")

