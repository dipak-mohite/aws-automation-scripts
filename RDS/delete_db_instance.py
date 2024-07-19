import boto3

def delete_db_instance():
    rds = boto3.client('rds')
    response = rds.delete_db_instance(
        DBInstanceIdentifier='mydbinstance',
        SkipFinalSnapshot=True
    )
    print('DB instance deleted:', response)

if __name__ == "__main__":
    delete_db_instance()
