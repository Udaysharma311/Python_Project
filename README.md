# Python_Project
Integrated various technologies like wit.ai, Telegram botos, Amazon S3, AWS API Gateway , Socket.io with product backend. 

Requirements:
AWS Account
Visual Stdio Code Software for Python

AWS Service:
S3-Bucket - > Store the Data, So I have upload the file to s3 bucket. S3 bucket is pay as you go service. If you want higher storgae then you will pay to S3 machine to add TB data. For Free Account S3 bucket provide 5GB Data we can store.

IAM Service- > AWS Identity and Access Management. I have provide S3 Service. First of all I have crerate the user and provide the Policy. The policy are..
Integrated varous technologies like wit.ai, Telegram botos, Amazon S3, AWS API Gateway , Socket.io woth product backerns 
AmazonDMSRedshiftS3Role
AmazonS3FullAccess	
AmazonS3ObjectLambdaExecutionRolePolicy	
AmazonS3OutpostsFullAccess	
AmazonS3OutpostsReadOnlyAccess	
AmazonS3ReadOnlyAccess	
AWSBackupServiceRolePolicyForS3Backup	
AWSBackupServiceRolePolicyForS3Restore	
QuickSightAccessForS3StorageManagementAnalyticsReadOnly	

After that I have create access key to integrate With Visual stdio code. 


Visual Stdio Code -> I used to Python programing this software where we can write the code. First we configure to the terminal the they ask Access key so I have provide to access key and configure. The Configure is done it is mean that we can create anything that is show to AWS Account. Now I have write the code using boto3 Library

Boto3 Library Library: You use the AWS SDK for Python (Boto3) to create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3). The SDK provides an object-oriented API as well as low-level access to AWS services.

So we write the code create ths S3 bucket, uload the data to S3 bucket and see the data using API Gateway.



