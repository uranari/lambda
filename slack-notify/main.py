import create_message
import json
import os
import requests

SLACK_WEBHOOK_URL = os.environ.get('slack_alert_url')


def lambda_handler(event, context):
    content = json.loads(event['Records'][0]['Sns']['Message'])
    event_name = content["eventName"]

    if event_name == "ConsoleLogin":
        user_name = content["userIdentity"]["userName"]
        source_ip = content["sourceIPAddress"]
        result = content["responseElements"]["ConsoleLogin"]
        message = create_message.console_login_message(
            user_name, source_ip, result)

    else:
        message = "Unknown event with " + event_name

        headers = {'Content-Type': 'text/plain'}

        response = requests.post(
            SLACK_WEBHOOK_URL, headers=headers, data=message)
        print(str(response.status_code))
