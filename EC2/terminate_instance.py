import boto3

def terminate_instance(instance_id):
    ec2 = boto3.client('ec2')
    ec2.terminate_instances(InstanceIds=[instance_id])
    print(f'Terminated instance {instance_id}')

if __name__ == "__main__":
    instance_id = 'your-instance-id'
    terminate_instance(instance_id)
