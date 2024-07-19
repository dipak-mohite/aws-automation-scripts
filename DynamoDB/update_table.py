import boto3

def update_table():
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.update_table(
        TableName='MyTable',
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    print('Table updated:', response)

if __name__ == "__main__":
    update_table()
