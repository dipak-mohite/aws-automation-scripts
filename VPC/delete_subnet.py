import boto3

def delete_subnet(subnet_id):
    ec2 = boto3.client('ec2')
    response = ec2.delete_subnet(SubnetId=subnet_id)
    print(f'Subnet {subnet_id} deleted:', response)

if __name__ == "__main__":
    delete_subnet('subnet-id')
