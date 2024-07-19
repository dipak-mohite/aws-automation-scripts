import boto3

def attach_policy(username, policy_arn):
    iam = boto3.client('iam')
    response = iam.attach_user_policy(UserName=username, PolicyArn=policy_arn)
    print(f'Policy {policy_arn} attached to {username}')

if __name__ == "__main__":
    attach_policy('user_name', 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess')
