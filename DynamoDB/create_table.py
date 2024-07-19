import boto3

def create_table():
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.create_table(
        TableName='MyTable',
        KeySchema=[
            {'AttributeName': 'id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'id', 'AttributeType': 'N'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print('Table created:', response)

if __name__ == "__main__":
    create_table()
