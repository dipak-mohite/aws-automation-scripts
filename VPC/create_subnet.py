import boto3

def create_subnet(vpc_id):
    ec2 = boto3.client('ec2')
    response = ec2.create_subnet(
        VpcId=vpc_id,
        CidrBlock='10.0.1.0/24'
    )
    print('Subnet created:', response['Subnet']['SubnetId'])

if __name__ == "__main__":
    create_subnet('vpc-id')
