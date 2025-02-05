KEYWORD_RESPONSES = {
    "help": "Here are the available commands:\n- help: Shows this message\n- news: Fetches the latest news\n- joke: Tells a funny joke\n- weather: Provides current weather information",
    "joke": "Why don't skeletons fight each other? They don't have the guts!",
    "weather": "To get the weather, use 'weather <city>' (e.g., 'weather Dhaka')."
}

def get_keyword_response(user_message):
    # Check if the user message matches any predefined command
    user_message_lower = user_message.lower()
    return KEYWORD_RESPONSES.get(user_message_lower)