import boto3
from notification import send_notification

iam = boto3.client('iam')

def rotate_access_key(username, old_key_id):
    # Create a new access key
    new_key = iam.create_access_key(UserName=username)['AccessKey']
    new_key_id = new_key['AccessKeyId']
    new_secret = new_key['SecretAccessKey']
    
    # Send notification to the user
    send_notification(username, new_key_id, new_secret)
    
    # Deactivate the old key
    iam.update_access_key(UserName=username, AccessKeyId=old_key_id, Status='Inactive')
    print(f"Deactivated old access key {old_key_id} for user {username}.")
