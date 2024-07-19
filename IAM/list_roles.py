import boto3

def list_roles():
    iam = boto3.client('iam')
    response = iam.list_roles()
    roles = [role['RoleName'] for role in response['Roles']]
    print('Roles:', roles)

if __name__ == "__main__":
    list_roles()
