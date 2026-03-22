import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    buckets = s3.list_buckets()

    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']
        
        try:
            s3.get_bucket_encryption(Bucket=bucket_name)
        except Exception:
            print(f"Unencrypted bucket: {bucket_name}")

    return "Scan complete"