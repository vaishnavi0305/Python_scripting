import boto3

ec2=boto3.resource('ec2')

print("Running Ec2 Instances:")
for instance in ec2.instances.all():
    if instance.state['Name'] == 'running':
        print(f"{instance.id} -> {instance.instance_type}, {instance.public_ip_address}")
