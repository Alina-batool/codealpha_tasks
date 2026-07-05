def chatbot():
    print("Hello! I am Piko" + "\n" + "Your freindly chatbot, How can i assist you today?")

    while True:
        user = input("You: ")
        if user == "hi" or user == "hello":
            print("Piko: Hello! How are you?")
        elif user == "i am good":
            print("Piko: That's great to hear! What can I do for you today?")
        elif user == "tell me a joke":
            print("Piko:  why is the math book sad? because it has too many problems")
        elif user == "haha":
            print("Piko: I'm glad you liked it !")    
        elif user == "bye":
            print("Piko: Goodbye! Have a great day!")
        else:
            print("Piko= I m sorry , I didn't understand that:(")

chatbot()