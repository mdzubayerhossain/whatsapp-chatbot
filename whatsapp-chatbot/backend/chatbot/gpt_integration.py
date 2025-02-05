import openai
import os

# Load OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_gpt_response(user_message):
    try:
        # Get GPT-3 response from OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "Sorry, I couldn't generate a response at the moment."
