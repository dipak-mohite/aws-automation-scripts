import boto3

def create_user(username):
    iam = boto3.client('iam')
    response = iam.create_user(UserName=username)
    print(f'User {username} created:', response)

if __name__ == "__main__":
    create_user('new_user')
