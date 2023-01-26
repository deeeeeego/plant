# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC84a10c3d4088d8309ef01b2a20e063fe"
auth_token = "422abf9ed13f43b34f502f1a2210f971"
client = Client(account_sid, auth_token)

def message():
    message = client.messages.create(
  body="Hello from Twilio",
  from_="+17755005288",
  to="+17132287703"
)
