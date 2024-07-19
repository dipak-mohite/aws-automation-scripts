import boto3

def create_security_group(vpc_id):
    ec2 = boto3.client('ec2')
    response = ec2.create_security_group(
        GroupName='MySecurityGroup',
        Description='My security group',
        VpcId=vpc_id
    )
    print('Security group created:', response['GroupId'])

if __name__ == "__main__":
    create_security_group('vpc-id')
