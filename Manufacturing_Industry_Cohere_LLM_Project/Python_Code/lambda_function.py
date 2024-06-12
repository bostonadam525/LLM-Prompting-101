import json

# 1. import boto3 and check version

import boto3 #python SDK
#print(boto3.__version__) #check boto3 version

# 1b. create client connection with bedrock
client_bedrock = boto3.client('bedrock-runtime')


## lambda handler function -- event, context
def lambda_handler(event, context):
    #2a. store input in a variable, b. print event
    input_prompt = event['prompt']
    print(input_prompt)
    
    #3. create request syntax - get details from console & body should be JSON object - use json dmps for body
    
    client_bedrockrequest = client_bedrock.invoke_model(
        contentType = 'application/json',
        accept = 'application/json',
        modelId = 'cohere.command-light-text-v14',
        body = json.dumps({
            "prompt": input_prompt,
            "temperature": 0.9,
            "p": 0.75,
            "k": 0,
            "max_tokens": 100}))
    #print(client_bedrockrequest)
    
    
    
    #4. convert streaming body to Byte(.read method) and then Byte to String using json.loads
    
    client_bedrock_byte = client_bedrockrequest['body'].read()
    print(client_bedrock_byte)
    #print(type(client_bedrock_byte))
    
    
    #5a. print event and type, b. store input in a variable
    
    client_bedrock_string = json.loads(client_bedrock_byte)
    #print(client_bedrock_string)
    
    
    
    #6. update 'return' by changing the 'body'
    client_final_response = client_bedrock_string['generations'][0]['text']
    print(client_final_response)
    
    # TODO implement
    
    return {
        'statusCode': 200,
        'body': json.dumps(client_final_response)
    }
