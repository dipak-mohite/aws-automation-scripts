import boto3

def create_vpc():
    ec2 = boto3.client('ec2')
    response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    print('VPC created:', response['Vpc']['VpcId'])

if __name__ == "__main__":
    create_vpc()
