# Basic Rule-Based Chatbot

## Overview
This project is a simple rule-based chatbot developed in Python. The chatbot responds to predefined user inputs using `if-elif-else` statements and continues interacting with the user until they choose to exit. This project demonstrates the basic concepts of Python programming, including functions, loops, conditional statements, and user input/output.

## Features
- Greets the user with a welcome message.
- Responds to greetings such as **hi** and **hello**.
- Responds when the user says they are doing well.
- Tells a simple joke.
- Responds when the user laughs.
- Ends the conversation when the user types **bye**.
- Displays a default message for unrecognized inputs.

## Technologies Used
- Python 3
- Functions
- While Loop
- If-Elif-Else Statements
- User Input and Output

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code or any Python IDE.
4. Run the following command in the terminal:

```bash
python chatbot.py
```

## Sample Conversation

```text
Hello! I am Piko
Your friendly chatbot. How can I assist you today?

You: hi
Piko: Hello! How are you?

You: i am good
Piko: That's great to hear! What can I do for you today?

You: tell me a joke
Piko: Why is the math book sad? Because it has too many problems.

You: haha
Piko: I'm glad you liked it!

You: bye
Piko: Goodbye! Have a great day!
```

## Project Structure

```text
basic-rule-based-chatbot/
│── chatbot.py
│── README.md
```

## Future Improvements
- Add more conversation options.
- Make the chatbot case-insensitive using `.lower()`.
- Support more user commands.
- Store conversation history.
- Create a graphical user interface (GUI).

## Learning Outcomes
Through this project, I learned:
- How to create functions in Python.
- How to use loops for continuous interaction.
- How to implement decision-making using `if-elif-else`.
- How to take user input and display appropriate responses.
- How to organize and upload a Python project to GitHub.

  # Hangman Game

## Description
This is a simple text-based Hangman game written in Python. The player tries to guess a randomly selected word one letter at a time. The game ends when the player correctly guesses the word or makes 6 incorrect guesses.

## Features
- Uses a list of 5 predefined words.
- Randomly selects a word each time the game starts.
- Allows one-letter guesses.
- Tracks guessed letters.
- Limits incorrect guesses to 6.
- Displays a win or lose message at the end.

## Concepts Used
- Python `random` module
- `while` loop
- `if-else` statements
- Strings
- Lists
- User input (`input()`)

## How to Run
1. Make sure Python is installed on your computer.
2. Save the program as `hangman.py`.
3. Open a terminal or command prompt.
4. Navigate to the project folder.
5. Run the following command:

```bash
python hangman.py
```

## Sample Words
- apple
- tiger
- house
- python
- school

## Rules
1. The computer randomly selects a word.
2. Guess one letter at a time.
3. Correct letters are revealed in the word.
4. Incorrect guesses reduce the remaining attempts.
5. You have a maximum of 6 incorrect guesses.
6. Win by guessing the complete word before running out of attempts.

## Example Output

```
=== Welcome to Hangman ===

Word: _ _ _ _ _
Guessed Letters:
Remaining Incorrect Guesses: 6

Enter a letter: a
Correct!

Word: a _ _ _ _
```


## License
This project is for educational purposes.

## Author
**Alina Batool**

Python Internship Project
