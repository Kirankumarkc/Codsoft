# Define a dictionary to store the rules and responses
rules = {
    "hello|hi|hey": "Hello! how's your day going?",
    "what is your name?": "My name is Noobot AI.",
    "how are you": "I'm good,thanks!",
    "all good":"That's great to hear!",
    "bye|see you": "See you later! It was nice chatting with you.",
    "default": "I didn't understand that. Can you please rephrase?",
    "exit":"sure! if you want to chat again, send me a message."
}

def respond(user_input):
    # Convert the user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Iterate through the rules and check if the user input matches any of them
    for pattern, response in rules.items():
        if any(word in user_input for word in pattern.split("|")):
            return response

    # If no rule matches, return the default response
    return rules["default"]

# Test the chatbot
while True:
    user_input = input("You: ")
    response = respond(user_input)
    print("Noobot AI:", response)


