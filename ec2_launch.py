import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
        ImageId='ami-0c2b8ca1dad447f8a',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [{'Key': 'Name', 'Value': 'Python-EC2'}]
                }
            ]
        )

print(f"Launched Ec2: {instance[0].id}")
