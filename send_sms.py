# Python 2.7.15 Code

from twilio.rest import TwilioRestClient

account_sid = '' #Replace this with your Twilio account sid
auth_token = '' # Replace this with your Twilio authentication token

provoke = TwilioRestClient(account_sid, auth_token)

content = provoke.sms.messages.create(
    body = "My name is Ilyes CH",
    to = "+xxx-xxxxxx", # Replace this with your phone number
    from = "+xxx-xxxxx" # Replace with your Twilio phone number
)
print content.sid
