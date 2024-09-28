import boto3
from datetime import datetime, timedelta
from key_rotation import rotate_access_key

iam = boto3.client('iam')

def lambda_handler(event, context):
    # Define the time limits
    age_limit = timedelta(days=90)
    now = datetime.utcnow()

    # List all IAM users
    users = iam.list_users()['Users']
    
    for user in users:
        username = user['UserName']
        
        # List all access keys for the user
        access_keys = iam.list_access_keys(UserName=username)['AccessKeyMetadata']
        
        for key in access_keys:
            key_id = key['AccessKeyId']
            create_date = key['CreateDate']
            age = now - create_date.replace(tzinfo=None)
            
            # Check if the key is older than 90 days
            if age > age_limit:
                print(f"Access key {key_id} for user {username} is older than 90 days.")
                rotate_access_key(username, key_id)
