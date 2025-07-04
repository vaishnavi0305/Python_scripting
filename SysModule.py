import sys

print("Script name:", sys.argv[0]) # first argument is always the script name

if len(sys.argv) > 1:
    print("user input from CLI:", sys.argv[1])
else:
    print("No argument passed")
