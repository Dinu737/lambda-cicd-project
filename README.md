# Automate CI/CD Pipelines using AWS Lambda

## Purpose
Automatically trigger AWS CodePipeline deployments using AWS Lambda.

## AWS Services Used
- AWS Lambda
- AWS CodePipeline
- IAM

## Workflow
GitHub → Lambda → CodePipeline → Deployment

## Lambda Function
The Lambda function uses Boto3 to start a CodePipeline execution automatically.

## Result
Successful pipeline execution triggered through Lambda.
