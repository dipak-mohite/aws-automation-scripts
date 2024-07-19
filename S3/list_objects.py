import boto3

def list_objects(bucket_name):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name)
    objects = [obj['Key'] for obj in response.get('Contents', [])]
    print('Objects:', objects)

if __name__ == "__main__":
    list_objects('my-bucket')
