def lambda_handler(event, context):
    """
    Function to return Hello
    """
    message = "Hello ! Your function executed successfully."

    return message

if __name__ == '__main__':
    print(lambda_handler('',''))