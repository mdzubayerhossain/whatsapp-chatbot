import random

def get_joke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "What do you call fake spaghetti? An impasta!"
    ]
    return random.choice(jokes)
