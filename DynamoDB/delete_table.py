import boto3

def delete_table():
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.delete_table(TableName='MyTable')
    print('Table deleted:', response)

if __name__ == "__main__":
    delete_table()
