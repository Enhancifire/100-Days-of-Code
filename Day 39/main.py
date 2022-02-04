import requests
from twilio.rest import Client
import json

# res = requests.get(url="https://opentdb.com/api.php?amount=10").json()

# print(res)
with open('data.json') as f:
    data = json.load(f)

account_sid = data['sid']
auth_token = data['authToken']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Ki haal chal bhaiya?",
                     from_='+16165224806',
                     to='+919822713136'
                 )

print(message.sid)
