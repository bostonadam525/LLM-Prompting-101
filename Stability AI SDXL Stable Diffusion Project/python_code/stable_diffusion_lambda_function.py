## AWS boto3 SDK - lambda Python Code for prompting the Stability AI SDXL v1.0 Stable Diffusion text to image model
## Code written by Adam Lang
## Date: 6/6/2024
import json
# 1. import boto3
import boto3
import base64
import datetime
# print(boto3.__version__) -- test for boto3 version

# Steps to invoke lambda with AWS Bedrock
# 2. Create client connection with Bedrock and S3 services:
## https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html#BedrockRuntime.Client
client_bedrock = boto3.client('bedrock-runtime')
client_s3 = boto3.client('s3')


def lambda_handler(event, context):
# 3. Store input data (prompt) in a variable
    ##input is JSON event object
    input_prompt = event['prompt']
    print(input_prompt)
# 4. Create a request syntax - details from console and docs (JSON object)
## docs: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/invoke_model.html
    response_bedrock = client_bedrock.invoke_model(contentType='application/json',
                                           accept='application/json',
                                           modelId='stability.stable-diffusion-xl-v1',
                                           body=json.dumps({"text_prompts": [{"text": input_prompt}],
                                           "cfg_scale": 10, #lower num increases randomness
                                           "steps": 30, # num of samples -> more steps -> more accurate
                                           "seed": 0}))# random num -> reproducibility
    print(response_bedrock)

# 5. 5a. Retrieve from dictionary, 5b. Convert streaming body to byte using json load, 5c. print
    response_bedrock_byte=json.loads(response_bedrock['body'].read())
    print(response_bedrock_byte)
# 6. 6a. Retrieve data with artifact key, 6b. Import Base 64, 6c. Decode from Base 64
    response_bedrock_base64 = response_bedrock_byte['artifacts'][0]['base64']
    ## decode response
    response_bedrock_finalimage = base64.b64decode(response_bedrock_base64)
    print(response_bedrock_finalimage)
    
# 7. 7a. Upload the file to S3 bucket using Put object method, 7b. Import datetime, 7c. Generate image name to be stored in Se
    poster_name = 'posterName' + datetime.datetime.today().strftime('%Y-%M-%D-%M-%S')
    
    response_s3=client_s3.put_object(
        Bucket = 'bedrockmovieposterdesign1', #s3 bucket name
        Body = response_bedrock_finalimage,
        Key = poster_name)

# 8. Generate Pre-signed URL
    generate_presigned_url = client_s3.generate_presigned_url(ClientMethod='get_object', 
    Params={'Bucket':'bedrockmovieposterdesign1', 'Key': poster_name}, ExpiresIn=3600,
    HttpMethod=None)
    print(generate_presigned_url)
        
    return {
        'statusCode': 200,
        'body': generate_presigned_url
    }
