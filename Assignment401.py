import boto3
import json

#Create Ec2 resource
ec2 = boto3.resource('ec2')

#Launch Ec2 instance
instances = ec2.create_instances(
            ImageId='ami-0c2b8ca1dad447f8a',
            InstanceType='t2.micro',
            MaxCount=1,
            MinCount=1,
            TagSpecifications=[
                    {
                        'ResourceType':'instance',
                        'Tags':[{'Key': 'Name', 'Value': 'Python2-Ec2'}]
                    }
                ]
            )
#Wait till instance is running
instance = instances[0]
print(f"Launching instance: {instance.id}...")
instance.wait_until_running()
instance.reload()

#collect the required instance info
ec2_info = {
            "InstanceId" : instance.id,
            "State": instance.state['Name'],
            "Type": instance.instance_type,
            "Public IP": instance.public_ip_address,
            "AMI ID": instance.image_id
            }

# write to json file

with open("ec2_info.json", "w") as f:
    json.dump(ec2_info, f, indent=4)

print("Ec2 instance launched and info saved to Ec2_info.json file")



