import boto3

def create_bucket(bucket_name):
    s3 = boto3.client('s3')
    response = s3.create_bucket(Bucket=bucket_name)
    print(f'Bucket {bucket_name} created:', response)

if __name__ == "__main__":
    create_bucket('my-bucket')
