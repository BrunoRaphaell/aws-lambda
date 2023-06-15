import json
from log import mensagem_log

def lambda_handler(event, context):
    
    print('teste inicial')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'mensagem': mensagem_log('teste inicial')
    }
