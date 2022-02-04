import requests
from twilio.rest import Client

# res = requests.get(url="https://opentdb.com/api.php?amount=10").json()

# print(res)

account_sid = 'AC46d0e80047812c5bf003f571c0e8ef50'
auth_token = 'fd6e0f409140a67b0c51a82163e5f27b'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Ki haal chal bhaiya?",
                     from_='+16165224806',
                     to='+919822713136'
                 )

print(message.sid)