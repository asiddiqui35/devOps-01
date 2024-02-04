import json
import boto3
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# dynamodb_client = boto3.client('dynamodb')
dynamodb_client = boto3.resource('dynamodb')
table_name = "b2302-test"

# event = {
#     "FirstName": "John",
#     "LastName": "Dow",
#     "Department": "IT",
#     "Location": "New York",
#     "email": "john@gmail.com"
# }


def lambda_handler(event, context):

    logging.info(f"Input I received: {event}")
    response = create_item(table_name=table_name,
                           partition_key_name="email",
                           additional_data=event
                           )
    logging.info(f"DB Response {response}")

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }


def create_item(table_name, partition_key_name, additional_data):
    """
    Insert data into a DynamoDB table with only a partition key and additional data.

    Args:
    table_name (str): The name of the DynamoDB table.
    partition_key_name (str): The name of the partition key.
    partition_key_value (str): The value of the partition key.
    additional_data (dict): Additional attributes to be added to the item.

    Returns:
    dict: The response from DynamoDB on successful insert, or an error message.
    """

    try:
        # Select your DynamoDB table
        table = dynamodb_client.Table(table_name)

        # Prepare the data item
        item_data = {"PartitionKeyName": partition_key_name}
        item_data.update(additional_data)

        # Insert the data
        response = table.put_item(Item=item_data)
        logging.info(f"Item Created Response: {response}")
        return response

    except ClientError as e:
        # Handle specific DynamoDB client errors
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        logging.info(f"Error Message {error_message}")
        return {'Error': {'Code': error_code, 'Message': error_message}}

    except Exception as e:
        # Handle any other exceptions
        return {'Error': {'Message': str(e)}}


# lambda_handler(event)
