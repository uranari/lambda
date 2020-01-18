import create_message
import os
import requests

SLACK_WEBHOOK_URL = os.environ.get('slack_alert_url')


def lambda_handler(event, context):
    event_name = event['Records'][0]['Sns']['Message']["eventName"]

    if event_name == "ConsoleLogin":
        user_name = event['Records'][0]['Sns']['Message']["userIdentity"]["userName"]
        source_ip = event['Records'][0]['Sns']['Message']["sourceIPAddress"]
        result = event['Records'][0]['Sns']['Message']["responseElements"]["ConsoleLogin"]
        message = create_message.console_login_message(
            user_name, source_ip, result)

    else:
        message = "Unknown event with " + event_name

    headers = {'Content-Type': 'text/plain'}

    response = requests.post(SLACK_WEBHOOK_URL, headers=headers, data=message)
    print(str(response.status_code))
