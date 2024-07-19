import boto3

def delete_security_group(group_id):
    ec2 = boto3.client('ec2')
    response = ec2.delete_security_group(GroupId=group_id)
    print(f'Security group {group_id} deleted:', response)

if __name__ == "__main__":
    delete_security_group('sg-id')
