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
