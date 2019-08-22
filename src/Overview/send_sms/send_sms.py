# Download the helper library from https://www.twilio.com/docs/python/install
from .b import account_sid, auth_token, my_phone_number
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

my_msg 					= "This is my message with stuff and things"
send_to_phone_number	= "+15184282729"

client  = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body	= my_msg,
                     from_	= my_phone_number,
                     to		= send_to_phone_number
                 )

print(message.sid)
print("SMS is sent!")


# def send_sms (my_msg, send_to_phone_number):
# 	client  = Client(account_sid, auth_token)
# 	message = client.messages \
#                 .create(
#                      body	= my_msg,
#                      from_	= my_phone_number,
#                      to		= send_to_phone_number
#                  )