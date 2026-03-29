import json
import boto3
import uuid
from datetime import datetime

# Initialisation de la ressource DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Todos')

def lambda_handler(event, context):
    try:
        # On récupère les données envoyées par le portail
        body = json.loads(event['body'])
        todo_id = str(uuid.uuid4()) # Génération d'un ID unique
        
        item = {
            'todoId': todo_id,
            'title': body['title'],
            'isCompleted': False,
            'createdAt': datetime.utcnow().isoformat()
        }
        
        # Insertion dans DynamoDB
        table.put_item(Item=item)
        
        return {
            'statusCode': 201,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(item)
        }
    except Exception as e:
        print(f"ERREUR CREATE: {str(e)}") # Log automatique vers CloudWatch
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
