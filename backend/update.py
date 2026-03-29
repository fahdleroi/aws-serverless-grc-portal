import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Todos')

def lambda_handler(event, context):
    try:
        # Récupération de l'ID depuis l'URL de l'API Gateway
        todo_id = event['pathParameters']['id']
        
        # Mise à jour du booléen isCompleted
        table.update_item(
            Key={'todoId': todo_id},
            UpdateExpression="set isCompleted = :c",
            ExpressionAttributeValues={':c': True}
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'status': 'Tâche mise à jour avec succès'})
        }
    except Exception as e:
        print(f"ERREUR UPDATE: {str(e)}")
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
