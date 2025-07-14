#Count how many times "S3" appears in the list: ["EC2", "S3", "S3", "RDS"]

l1= ["EC2", "S3", "S3", "RDS", "S3"]

find = "S3"
count = 0
for i in range(len(l1)):
    if find == l1[i]:
        count += 1
print(f"{find} appeared {count} times")

