import boto3

def query_table():
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.query(
        TableName='MyTable',
        KeyConditionExpression='id = :id',
        ExpressionAttributeValues={
            ':id': {'N': '1'}
        }
    )
    print('Query results:', response['Items'])

if __name__ == "__main__":
    query_table()
