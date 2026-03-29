import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Todos')

def lambda_handler(event, context):
    try:
        # Récupération de l'ID depuis l'URL
        todo_id = event['pathParameters']['id']
        
        # Suppression définitive
        table.delete_item(
            Key={'todoId': todo_id}
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'status': 'Tâche supprimée'})
        }
    except Exception as e:
        print(f"ERREUR DELETE: {str(e)}")
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
