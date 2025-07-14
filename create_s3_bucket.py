import boto3

s3=boto3.client('s3')

bucket_name= 'devops-auto-bucket-vais3uiyiuerhnavi9897'
region = 'us-east-1'

s3.create_bucket(
            Bucket = bucket_name
        )

print(f"Bucket created: {bucket_name}")
