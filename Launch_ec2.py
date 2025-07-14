import boto3

#create Ec2 instance
ec2 = boto3.resource('ec2')

#launch an ec2 instance
instance = ec2.create_instances(
        ImageId='ami-0c2b8ca1dad447f8a',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        TagSpecifications=[
                {
                    'ResourceType':'instance',
                    'Tags': [{'Key':'Name','Value':'Python-Ec2'}]
                }
            ]
        )
print("Launched ec2 instance:", instance[0].id)
