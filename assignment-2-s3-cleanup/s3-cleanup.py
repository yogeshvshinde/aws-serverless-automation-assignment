import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')

BUCKET_NAME = 'your-bucket-name'

def lambda_handler(event, context):
    objects = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if 'Contents' not in objects:
        return "No files found"

    for obj in objects['Contents']:
        last_modified = obj['LastModified']
        age = datetime.now(timezone.utc) - last_modified

        if age > timedelta(days=30):
            s3.delete_object(Bucket=BUCKET_NAME, Key=obj['Key'])
            print(f"Deleted: {obj['Key']}")

    return "Cleanup complete"