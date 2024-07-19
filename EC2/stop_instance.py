import boto3

def stop_instance(instance_id):
    ec2 = boto3.client('ec2')
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f'Stopped instance {instance_id}')

if __name__ == "__main__":
    instance_id = 'your-instance-id'
    stop_instance(instance_id)
