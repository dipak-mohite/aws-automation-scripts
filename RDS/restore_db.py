import boto3

def restore_db_instance():
    rds = boto3.client('rds')
    response = rds.restore_db_instance_from_db_snapshot(
        DBInstanceIdentifier='mynewdbinstance',
        DBSnapshotIdentifier='mydbsnapshot'
    )
    print('DB instance restored:', response)

if __name__ == "__main__":
    restore_db_instance()
