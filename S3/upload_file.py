import boto3

def upload_file(bucket_name, file_name, object_name):
    s3 = boto3.client('s3')
    response = s3.upload_file(file_name, bucket_name, object_name)
    print(f'File {file_name} uploaded to bucket {bucket_name}')

if __name__ == "__main__":
    upload_file('my-bucket', 'myfile.txt', 'myfile.txt')
