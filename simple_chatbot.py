import re

def chatbot_response(user_input):
    """
    Function to determine the chatbot's response based on user input.
    :param user_input: Input string from the user.
    :return: Response string from the chatbot.
    """

    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching
    
    # Greetings
    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "Hello! How can I help you today?"
    
    # Asking for help
    elif re.search(r"\b(help|assist|support)\b", user_input):
        return "Sure, I'm here to help! What do you need assistance with?"
    
    # Goodbye
    elif re.search(r"\b(bye|goodbye|exit|quit)\b", user_input):
        return "Goodbye! Have a great day!"

    # Asking about the chatbot's identity
    elif re.search(r"\b(who are you|what are you|your name)\b", user_input):
        return "I am a simple rule-based chatbot created to assist you."

    # Thank you
    elif re.search(r"\b(thank you|thanks)\b", user_input):
        return "You're welcome! If you have any more questions, feel free to ask."

    # Unknown input
    else:
        return "I'm not sure I understand that. Can you please rephrase?"

def chat():
    """
    Main function to run the chatbot.
    """
    print("Welcome to the Simple Chatbot! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")  # Take input from the user
        
        if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = chatbot_response(user_input)  # Get response from the chatbot
        print(f"Chatbot: {response}")  # Print chatbot response

# Start the chatbot
if __name__ == "__main__":
    chat()
