import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("ResumeTable")


# test comment
def lambda_handler(event, context):
    response = table.update_item(
        Key={
            "id": "visitors"
        },
        UpdateExpression="ADD #count :increment",
        ExpressionAttributeNames={
            "#count": "count"
        },
        ExpressionAttributeValues={
            ":increment": 1
        },
        ReturnValues="UPDATED_NEW"
    )

    count = response["Attributes"]["count"]

    return {
        "statusCode": 200,
        "body": str(count)
    }