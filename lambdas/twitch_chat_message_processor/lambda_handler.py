import json
import boto3
import os

from twitch_chat_message_processor.get_gcode_from_message import get_gcode_from_message
sqs_message_url = os.environ["sqs_message_url"]

def lambda_handler(event: dict, _context):
    message = event["Records"][0]["body"]
    receiptHandle = event["Records"][0]["receiptHandle"]

    # Get gcode
    commands = get_gcode_from_message(message)
    if commands:
        try:
            send_message(json.dumps(commands))
            # delete_message(receiptHandle) # deleted automatically by sqs when sent to lambda
        except Exception as e:
            print(f"Could not send message: {e}")
    else:
        print("Not enough valid commands in message.")

    return {
        "statusCode": 200,
        "body": json.dumps(f"Successfully posted record to command queue '{message}'"),
    }


def send_message(commands: str):
    sqs = boto3.client("sqs")
    sqs.send_message(QueueUrl=sqs_message_url, MessageBody=commands)


def delete_message(receiptHandle: str):
    sqs = boto3.client("sqs")
    sqs.delete_message(
        QueueUrl=sqs_message_url, ReceiptHandle=receiptHandle
    )
