import boto3

def lambda_handler(event, context):
    
    codepipeline = boto3.client('codepipeline')

    response = codepipeline.start_pipeline_execution(
        name='CloudPizzaPipeline'   # Replace with your pipeline name
    )

    return {
        'statusCode': 200,
        'message': 'Pipeline triggered successfully',
        'executionId': response['pipelineExecutionId']
    }
