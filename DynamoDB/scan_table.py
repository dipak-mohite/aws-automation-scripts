import boto3

def scan_table():
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.scan(TableName='MyTable')
    print('Scan results:', response['Items'])

if __name__ == "__main__":
    scan_table()
