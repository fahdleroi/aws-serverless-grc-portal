import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Todos')

def lambda_handler(event, context):
    try:
        # Scan de toute la table DynamoDB
        response = table.scan()
        tasks = response.get('Items', [])
        
        # Tri : les plus récentes en premier
        tasks.sort(key=lambda x: x.get('createdAt', ''), reverse=True)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(tasks)
        }
    except Exception as e:
        print(f"ERREUR READ: {str(e)}")
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
