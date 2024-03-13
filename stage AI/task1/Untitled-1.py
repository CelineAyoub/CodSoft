def respond_to_user_input(user_input):
    if user_input.lower() in ["hi", "hello", "hey"]:
        return "Hello! How can I assist you today?"
    elif user_input.lower() in ["bye", "goodbye"]:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("Welcome to the Simple Chatbot!")
    print("You can start chatting. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(respond_to_user_input(user_input))
            break
        else:
            print("Bot:", respond_to_user_input(user_input))

if __name__ == "__main__":
    main()
