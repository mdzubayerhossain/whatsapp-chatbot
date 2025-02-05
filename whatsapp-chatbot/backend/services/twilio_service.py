from twilio.rest import Client
import os

# Load Twilio credentials from environment variables
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_message(to, message):
    message = client.messages.create(
        body=message,
        from_=f'whatsapp:{TWILIO_WHATSAPP_NUMBER}',
        to=f'whatsapp:{to}'
    )
    return message.sid
