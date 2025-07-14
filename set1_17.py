#Check if "S3" is in the list ["EC2", "S3", "RDS"]

l1= ["EC2", "S3", "RDS"]
find="S3"
for i in l1:
    if i == find:
        print("Found")
        break
else:
    print("Not found")


