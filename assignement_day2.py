#have a list of 5 AWS services
Services = ["EC2", "S3","DynamoDB", "IAM", "VPC"]
with open("aws_services.txt", "w") as file:
    for svc in Services:
        file.write(svc+"\n")

with open("aws_services.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print("AWS services are:", line.strip())

#Create a dictionary of 2 EC2 instances:
Instances = {
            "instance1": {"id": "i-123", "type": "t2.micro"},
            "instance2": {"id": "i-456", "type": "t3.medium"}
        }

#Loop through that dictionary and print each key and value.
for InstanceName, InstanceInfo in Instances.items():
    print("InstanceName:", InstanceName)
    for key, value in InstanceInfo.items():
        print(f" {key}: {value}")
