import boto3
import os
from dotenv import load_dotenv

# Load environment variables from a .env file for local development
load_dotenv()

def get_bedrock_client():
    # Check if the AWS_PROFILE environment variable is set
    if 'AWS_PROFILE' in os.environ:
        # Use profile-based authentication for local development
        boto3.setup_default_session(profile_name=os.getenv('AWS_PROFILE'))
    
    # If AWS_PROFILE is not set, boto3 will automatically use IAM role credentials in AWS environments
    bedrock = boto3.client('bedrock-runtime')
    return bedrock