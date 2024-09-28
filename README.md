## Overview
This project automates the process of rotating AWS IAM user access keys. It identifies old or unused access keys, generates new ones, and notifies users to update their configurations.

### Key Features
1. **Automatic Detection**: Identifies IAM access keys older than 90 days or unused for 30 days.
2. **Key Rotation**: Automatically rotates the keys, deactivates old keys, and securely stores the new ones.
3. **User Notifications**: Sends alerts to users via AWS SNS or SES to update their systems with new keys.
4. **Grace Period**: Old keys are completely deleted after a 7-day grace period if not updated.

## Setup and Installation

### Prerequisites
1. **AWS Account**: You need access to an AWS account with the necessary IAM permissions.
2. **AWS Lambda and SNS**: The solution is implemented as a Lambda function triggered on a schedule using CloudWatch Events.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/IAM-Access-Key-Rotation.git
    cd IAM-Access-Key-Rotation
    ```

2. Install the necessary Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure the following environment variables in AWS Lambda:
    - `AWS_REGION`: Your AWS region.
    - `SNS_TOPIC_ARN`: The ARN of the SNS topic to notify users.

### How It Works

1. **Lambda Function**: The Lambda function is triggered by an EventBridge rule, checking IAM access keys for each user.
2. **Key Rotation**: For keys older than 90 days, the Lambda function creates a new access key, deactivates the old one, and sends a notification.
3. **Notification**: Users receive a message with the new access key details and are given a 7-day grace period before the old key is deleted.

### Example Usage

To run the Lambda function locally, you can test with:
```bash
python lambda_function.py
