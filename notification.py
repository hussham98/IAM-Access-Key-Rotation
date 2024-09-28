import boto3

def send_notification(username, access_key_id, secret_access_key):
    sns = boto3.client('sns')
    message = f"""
    Hi {username},

    Your IAM access key has been rotated. Please update your systems with the new credentials:

    Access Key ID: {access_key_id}
    Secret Access Key: {secret_access_key}

    The old key will be permanently deleted in 7 days.

    Regards,
    Security Team
    """
    sns.publish(
        TopicArn='arn:aws:sns:your-region:your-account-id:access-key-rotation',
        Message=message,
        Subject='Your IAM Access Key Has Been Rotated'
    )
