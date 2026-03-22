import boto3
from datetime import datetime, timedelta, timezone

ec2 = boto3.client('ec2')

VOLUME_ID = 'vol-xxxxxxxx'

def lambda_handler(event, context):
    # Create snapshot
    snapshot = ec2.create_snapshot(
        VolumeId=VOLUME_ID,
        Description='Automated snapshot'
    )
    
    print(f"Created snapshot: {snapshot['SnapshotId']}")

    # Delete old snapshots
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']

    for snap in snapshots:
        start_time = snap['StartTime']
        age = datetime.now(timezone.utc) - start_time

        if age > timedelta(days=30):
            ec2.delete_snapshot(SnapshotId=snap['SnapshotId'])
            print(f"Deleted snapshot: {snap['SnapshotId']}")

    return "Snapshot process complete"