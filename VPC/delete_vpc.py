import boto3

def delete_vpc(vpc_id):
    ec2 = boto3.client('ec2')
    response = ec2.delete_vpc(VpcId=vpc_id)
    print(f'VPC {vpc_id} deleted:', response)

if __name__ == "__main__":
    delete_vpc('vpc-id')
