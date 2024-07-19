import boto3

def list_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    instances = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
    print('Instances:', instances)

if __name__ == "__main__":
    list_instances()
