import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
    if instance.state['Name'] == 'running':
        print("Stopping Instance:", instance.id)
        instance.stop()
