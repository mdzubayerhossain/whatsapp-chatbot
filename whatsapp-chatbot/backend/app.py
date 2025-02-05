import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
from chatbot.gpt_integration import get_gpt_response
from chatbot.keyword_responses import get_keyword_response

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Twilio credentials
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.form.get("Body", "").strip()
    response = MessagingResponse()

    # Check if there is a keyword response
    keyword_response = get_keyword_response(incoming_msg)
    if keyword_response:
        response.message(keyword_response)
    else:
        # Otherwise, use GPT for AI-generated response
        gpt_response = get_gpt_response(incoming_msg)
        response.message(gpt_response)

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
