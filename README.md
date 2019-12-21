# AWS-Python-Lambda-Git-CI-CD-Example.
  This project will help you to understand how to integrate **GitLab CI/CD** for **AWS**.
  Deploy AWS Lambda functions and create rich **serverless applications.**

Pre-request :
    **AWS account.**
    **Git account.**

**Example**:
In the following example, you will:

   1. Create a basic AWS Lambda Python function.
   2. Link the function to an API Gateway GET endpoint

**Steps**:
The example consists of the following steps:
   1. Creating a Lambda hello function
   2. Creating a serverless.yml file
   3. Crafting the .gitlab-ci.yml file
   4. Setting up your AWS credentials with your GitLab account
   5. Deploying your function
   6. Testing the deployed function

**Creating a Lambda handler function**:

Your Lambda function will be the primary handler of requests. In this case we will create a very simple Python hello function:

    def lambda_handler(event, context):
    """
    Function to return Hello
    """
    message = "Hello ! Your function executed successfully."

    return message

Place this code in the file src/hello.py .
src is the standard location for serverless functions, but is customizable should you desire that.

In our case, lambda_handler defines the hello handler that will be referenced later in the serverless.yml

You can learn more about the AWS Lambda Node.js function handler and all its various options [here](https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model.html)


**Creating a** serverless.yml **file**

In the root of your project, create a serverless.yml file that will contain configuration specifics for the Serverless Framework.

Put the following code in the file:

     service: gitlab-cicd-tutorial
     provider:
     name: aws
     runtime: python3.7

     functions:
       hello:
         handler: src/hello.lambda_handler
         name: hello_function
       events:
         - http:
             path: hello
             method: get
             cors: true

Our function contains a handler and a event.

The handler definition will provision the Lambda function using the source code located src/hello.lambda_handler .

The events declaration will create a AWS API Gateway GET endpoint to receive external requests and hand them over to the Lambda function via a service integration. And we have set up cors true. 
For more information, see the [Your CORS and API Gateway survival guide](https://serverless.com/blog/cors-api-gateway-survival-guide/) blog post written by the Serverless Framework team

You can read more about the available properties and additional configuration possibilities of the Serverless Framework [here](https://serverless.com/examples/aws-python-simple-http-endpoint/)


**Crafting the** .gitlab-ci.yml **file**

In a .gitlab-ci.yml file in the root of your project, place the following code:

    image: "nikolaik/python-nodejs"

    stages:
      - test

    dev:
      stage: test 
      only:
        - master
      before_script:
        - npm config set prefix /usr/local
        - npm install -g serverless
      script:
        - serverless deploy --stage dev --region ap-south-1 --verbose
      environment: dev


This example code does the following:

   Uses the node and python image for all GitLab CI builds.
    As we are deploying python function using serverless framework and serverless framwork is based on npm so we need an image which consist both python and npm configuration. I have used [https://hub.docker.com/r/nikolaik/python-nodej](nikolaik/python-nodejs)image form docker Hub.

    only:
    - master   # it will run pipeline on every push to master branch. If you want to run pipeline on every branch commit you can remove it.
    
   The deploy stage:
       Installs the Serverless Framework.
       Deploys the serverless function to your AWS account using the AWS credentials defined above.
        

**Setting up your AWS credentials with your GitLab account**

In order to interact with your AWS account, the GitLab CI/CD pipelines require both AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to be defined in your GitLab settings under **Settings > CI/CD > Variables**.

   Note : Use variable name as mention above.

**Deploying your function**

git push the changes to your GitLab repository and the GitLab build pipeline will automatically deploy your function.

In your GitLab deploy stage log, there will be output containing your AWS Lambda endpoint URL. The log line will look similar to this:

    endpoints:
        GET - https://5hj381bhg2.execute-api.ap-south-1.amazonaws.com/dev/hello

**Manually testing your function**
Running the following curl command should trigger your function.

    curl https://5hj381bhg2.execute-api.ap-south-1.amazonaws.com/dev/hello

That should output:

    {
        "Hello ! Your function executed successfully."
    }





