from twilio.rest import TwilioRestClient

account_sid = '' #Replace this with your Twilio account sid
auth_token = '' # Replace this with your Twilio authentication token

client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body = "My name is Ilyes",
    to = "+xxx-xxxxxx", # Replace this with your phone number
    from = "+xxx-xxxxx" # Replace with your Twilio phone number
)
print message.sid