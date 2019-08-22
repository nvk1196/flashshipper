# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

# my_msg = "This is my message with stuff and things"
# send_to_phone_number	= "+15184282729"
# client  = Client(account_sid, auth_token)
# message = client.messages \
#                 .create(
#                      body	= my_msg,
#                      from_	= my_phone_number,
#                      to		= send_to_phone_number
#                  )

# print(message.sid)
# print("SMS is sent!")

account_sid 	= "AC9f05e812b5954718ee0e25f764ec5c6d"
auth_token 		= "9f59fde1d33f14857fbf5615be881388"
my_phone_number = "+15012632545"	#Twilio gave me this phone number

def send_text (my_msg, send_to_phone_number):
	client  = Client(account_sid, auth_token)
	message = client.messages \
                .create(
                     body	= my_msg,
                     from_	= my_phone_number,
                     to		= send_to_phone_number
                 )
	print("SMS is sent!")

# Run this is terminal for window
# set TWILIO_ACCOUNT_SID=ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# set TWILIO_AUTH_TOKEN=your_auth_token

# import os

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']