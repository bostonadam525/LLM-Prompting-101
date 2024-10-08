# Manufacturing Industry LLM Project
* By Adam Lang - Date: 6/12/2024
* This is a use case using Amazon Bedrock and the Cohere Foundation Model "command-light-text-v14".

* The goal of the project was to build an LLM application that can summarize documents from a Manufacturing Company using the foundation model.
* The application uses:
    * 1. AWS Bedrock
    * 2. AWS lambda
    * 3. AWS API Gateway
    * 4. Cohere Command Light Text v14 Foundation Model

* The application was deployed on AWS and tested using POSTMAN.


# Business Use Case
* A manufacturing company will have a Technician out in the field who files a report which is sent back to the company's custom application.
* A subject matter expert (SME) will often have to review the report which could be upwards of 100s of pages of documents.
* The business question is:
1. How can you improve productivity?
2. Can sending the documents to the LLM and the company's employees being able to perform questions and answer queries over the document help improve efficiency?


# Suggested Workflow
<img width="492" alt="image" src="https://github.com/bostonadam525/LLM-Prompting-101/assets/45008475/b2c4e203-9ea1-4ca6-ab6b-cf240929ac59">

# AWS Architecture
![image](https://github.com/bostonadam525/LLM-Prompting-101/assets/45008475/5b45567d-8160-44e0-8331-39b0c2c0d815)

