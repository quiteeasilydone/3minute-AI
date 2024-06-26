import boto3
import json

def load_s3_client(env_file_path):
    with open(env_file_path, 'r') as file:
        env_data = json.load(file)

        AWS_ACCESS_KEY_ID = env_data["AWS_ACCESS_KEY_ID"]
        AWS_SECRET_ACCESS_KEY = env_data["AWS_SECRET_ACCESS_KEY"]
        AWS_BUCKET_NAME = env_data["S3_BUCKET_NAME"]
        AWS_DEFAULT_REGION = "ap-northeast-2"
        AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (
            AWS_BUCKET_NAME, AWS_DEFAULT_REGION)
        client = boto3.client('s3',
                            aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                            region_name=AWS_DEFAULT_REGION
                            )
    return client, AWS_BUCKET_NAME