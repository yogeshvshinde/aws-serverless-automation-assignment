

Assignment 1 → EC2 Auto Start/Stop (Core AWS skill)
Assignment 2 → S3 Cleanup (Lifecycle automation)
Assignment 3 → Detect Unencrypted Buckets (Security use case)
Assignment 4 → EBS Snapshot + Cleanup (Backup automation)

Compute + Storage + Security + Backup ( All included )

************************************************************

Assignment 1 → EC2 Auto Start/Stop (Core AWS skill)
----------------------------------------------------

Steps:
Created 2 EC2 instances
Added tags:
    Action=Auto-Stop
    Action=Auto-Start
Created IAM role with:
    AmazonEC2FullAccess
Created Lambda function (Python 3.x)
Attached IAM role
Deployed code
Manually triggered Lambda
Verified instance state changes


Assignment 2 → S3 Cleanup (Lifecycle automation)
-----------------------------------------------------

Steps:
Created S3 bucket
Uploaded files (some older than 30 days)
Created IAM role:
    AmazonS3FullAccess
Created Lambda function
Added code
Triggered manually
Verified old files deleted

Assignment 3 → Detect Unencrypted Buckets (Security use case)
-------------------------------------------------------------------

Created multiple S3 buckets
Disabled encryption for some
IAM role:
    AmazonS3ReadOnlyAccess
Created Lambda
Ran manually
Checked logs in CloudWatch


Assignment 4 → EBS Snapshot + Cleanup (Backup automation)
-----------------------------------------------------------------------

Identified EBS Volume ID
IAM Role:
    AmazonEC2FullAccess
Created Lambda
Added code
Ran manually
Verified snapshot creation & deletion