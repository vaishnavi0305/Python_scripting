import os
import sys
import subprocess

#current working directory
print("CWD:", os.getcwd())

# Run as Shell command
subprocess.run(["ls", "-l"])

# Script Arguments
print("Args:", sys.argv)
