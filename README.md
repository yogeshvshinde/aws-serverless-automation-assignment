

Assignment 1 → EC2 Auto Start/Stop (Core AWS skill)
Assignment 2 → S3 Cleanup (Lifecycle automation)
Assignment 3 → Detect Unencrypted Buckets (Security use case)
Assignment 4 → EBS Snapshot + Cleanup (Backup automation)

Compute + Storage + Security + Backup ( All included )

************************************************************



Assignment 1 → EC2 Auto Start/Stop

Step 1: Create EC2 Instances
1.	Go to AWS Console → EC2 
2.	Click Launch Instance 
Instance 1:
•	Name: auto-stop-instance 
•	Instance type: t2.micro 
•	Click Launch 
Instance 2:
•	Name: auto-start-instance 
•	Instance type: t2.micro 
•	Click Launch

 ![alt text](image-2.png)


 

Step 2: Add Tags
1.	Go to Instances 
2.	Select first instance → Click Tags tab 
3.	Click Manage tags
Key: Action
Value: Auto-Stop

 ![alt text](image-1.png)

Repeat for second instance:
Key: Action
Value: Auto-Start

Step 3: Create IAM Role for Lambda
1.	Go to IAM → Roles 
2.	Click Create role 
Select:
•	Trusted entity → AWS service 
•	Use case → Lambda 
Click Next
Attach policy:
•	Select: AmazonEC2FullAccess 
Click:
•	Next → Name role: lambda-ec2-role → Create

 ![alt text](image-3.png)




Step 4: Create Lambda Function
1.	Go to AWS Lambda 
2.	Click Create function 
Fill:
•	Function name: ec2-auto-manager 
•	Runtime: Python 3.x 
•	Execution role: Use existing role → lambda-ec2-role 
Click Create function

Step 4: Add Code


![alt text](image-4.png)


![alt text](image-5.png)

 ![alt text](image-6.png)

 
![alt text](image-7.png)



 

Step 6: Test Lambda
1.	Click Test 
2.	Create test event → Name: test 
3.	Click Test

 
![alt text](image-8.png)
 


 ![alt text](image-9.png)

 
![alt text](image-10.png)


![alt text](image-11.png)





Assignment 2 (S3 Cleanup)
________________________________________
Step 1: Create S3 Bucket
1.	Go to S3 
2.	Click Create bucket 
•	Name: my-cleanup-bucket-123 
•	Keep defaults → Create 
________________________________________
Step 2: Upload Files
1.	Open bucket 
2.	Click Upload 
3.	Upload some files



![alt text](image-12.png)


![alt text](image-13.png)



 

 

Step 3: IAM Role
Create new role:
•	Service: Lambda 
•	Policy: AmazonS3FullAccess 
•	Name: lambda-s3-role 



 ![alt text](image-14.png)

 
________________________________________
Step 4: Create Lambda
•	Name: s3-cleanup 
•	Runtime: Python 
•	Role: lambda-s3-role
 

![alt text](image-15.png)





Add the code 
Click Deploy

Step 6: Test
Click Test
Check bucket → old files removed


 
![alt text](image-16.png)

![alt text](image-17.png)


![alt text](image-18.png)


![alt text](image-19.png)
 

 

 ![alt text](image-20.png)




 

Assignment 3 (Unencrypted Buckets)
________________________________________
Step 1: Create Buckets
Create:
•	1 with encryption 
•	1 without encryption 
 

 
![alt text](image-21.png)


![alt text](image-22.png)



________________________________________
 Step 2: IAM Role
•	Policy: AmazonS3ReadOnlyAccess 
•	Name: lambda-s3-read-role 


![alt text](image-23.png)

  ________________________________________
Step 3: Lambda
•	Name: s3-encryption-check
Step 4: Code

Step 5: Test
•	Click Test 

 
![alt text](image-24.png)




Assignment 4 (EBS Snapshot)
________________________________________
Step 1: Find Volume ID
1.	Go to EC2 → Volumes 
2.	Copy volume ID 
 

 ![alt text](image-25.png)



________________________________________
Step 2: IAM Role
•	Policy: AmazonEC2FullAccess 
•	Name: lambda-ec2-role 
 

 ![alt text](image-26.png)


________________________________________
Step 3: Lambda
•	Name: ebs-backup 


![alt text](image-27.png)



 
________________________________________
Step 4: Code
 

![alt text](image-28.png)




Click deploy

Step 5: Test
•	Run Lambda 
•	Go to EC2 → Snapshots



![alt text](image-29.png)
 



