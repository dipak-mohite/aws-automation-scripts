import boto3

def download_file(bucket_name, object_name, file_name):
    s3 = boto3.client('s3')
    response = s3.download_file(bucket_name, object_name, file_name)
    print(f'File {object_name} downloaded from bucket {bucket_name}')

if __name__ == "__main__":
    download_file('my-bucket', 'myfile.txt', 'myfile.txt')
