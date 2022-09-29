import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'messages': [{'type': "unstructured", 'unstructured':
            {'text': "Application under development. Search functionality will be implemented in assignment 2!"}}]
    }
