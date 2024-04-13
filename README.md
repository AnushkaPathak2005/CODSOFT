# CODSOFT
# Define a dictionary of rules and responses
rules = {
     "hello": "Hello! How can I help you?",
      "goodbye": "Goodbye! Have a great day!",
      "how are you": "I'm just a computer program, but thanks for asking!",
      "default": "I'm sorry, I don't understand. Can you please rephrase your question?",
}

# Function to generate a response
def generate_response(user_input):
    #Convert the input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    #Check if the Input matches any of the predefined rules
    for key in rules:
        if key in user_input:
           return rules[key]

    #If no rule matches, return the default response
    return rules["default"]

# Main loop for the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
       print("Chatbot: Goodbye!")
       break
    response = generate_response(user_input)
print("Chatbot:", response )
