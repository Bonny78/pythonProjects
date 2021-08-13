from twilio.rest import Client
import os

account_sid = "ACe61125908b41ec3d6c5b1ff1d0104914"
auth_token = "91dac36140642995681a84c85b8db729"
TWILIO_VIRTUAL_NUMBER = "+12055768110"
TWILIO_VERIFIED_NUMBER = "+13472649628"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body= message,
            from_= TWILIO_VIRTUAL_NUMBER,
            to= TWILIO_VERIFIED_NUMBER
        )
        #prints if successfully sent
        print(message.sid)