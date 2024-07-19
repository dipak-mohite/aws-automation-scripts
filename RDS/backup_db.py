import boto3

def create_db_snapshot():
    rds = boto3.client('rds')
    response = rds.create_db_snapshot(
        DBInstanceIdentifier='mydbinstance',
        DBSnapshotIdentifier='mydbsnapshot'
    )
    print('DB snapshot created:', response)

if __name__ == "__main__":
    create_db_snapshot()
