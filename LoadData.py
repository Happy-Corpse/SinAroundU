import json
# import the AWS SDK (for Python the package name is boto3)
import boto3
from boto3.dynamodb.conditions import Key

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb')
s3 = boto3.client('s3')
bucket = 'sinaroundu-bucket'


def lambda_handler(event, context):
    # load files from s3
    file_name = 'median_rent.json'
    response = s3.get_object(Bucket=bucket, Key=file_name)

    body = json.load(response["Body"])
    # get item
    table_name = "MedianRent"
    count = 0
    for item in body:
        count += 1
        # put item
        response = dynamodb_client.put_item(
            TableName=table_name,
            Item={"district_id": {"N": str(item["district_id"])},
                  "uuid": {"N": str(count)},
                  "town": {"S": item["town"]},
                  "flat_type": {"S": item["flat_type"]},
                  "quarter": {"S": item["quarter"]},
                  "median_rent": {"S": str(item["median_rent"])},
                  }
        )
    return {
        'statusCode': 200,
        'body': json.dumps("success"),
    }