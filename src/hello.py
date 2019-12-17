import json


def lambda_handler(event, context):
    """
    Function to say Hello
    """
    message = "Hello ! Your function executed successfully."

    return message

if __name__ == '__main__':
    print(lambda_handler('',''))