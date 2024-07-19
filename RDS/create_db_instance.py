import boto3

def create_db_instance():
    rds = boto3.client('rds')
    response = rds.create_db_instance(
        DBInstanceIdentifier='mydbinstance',
        AllocatedStorage=20,
        DBInstanceClass='db.t2.micro',
        Engine='mysql',
        MasterUsername='admin',
        MasterUserPassword='password',
        BackupRetentionPeriod=7
    )
    print('DB instance created:', response)

if __name__ == "__main__":
    create_db_instance()
