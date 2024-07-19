import boto3

def delete_object(bucket_name, object_name):
    s3 = boto3.client('s3')
    response = s3.delete_object(Bucket=bucket_name, Key=object_name)
    print(f'Object {object_name} deleted from bucket {bucket_name}')

if __name__ == "__main__":
    delete_object('my-bucket', 'myfile.txt')
