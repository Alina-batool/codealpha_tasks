import random  # Import the random module to choose a random word

# List of 5 predefined words
words = ["apple", "tiger", "house", "python", "school"]

# Randomly select one word from the list
word = random.choice(words)

# Create a list of underscores (_) to represent hidden letters
guessed_word = ["_"] * len(word)

# List to store letters the user has already guessed
guessed_letters = []

# Variables to track incorrect guesses
incorrect_guesses = 0
max_guesses = 6

# Display welcome message
print("=== Welcome to Hangman ===")

# Continue the game until the player wins or reaches the guess limit
while incorrect_guesses < max_guesses and "_" in guessed_word:

    # Display the current word with guessed letters
    print("\nWord:", " ".join(guessed_word))

    # Display all guessed letters
    print("Guessed Letters:", ", ".join(guessed_letters))

    # Display remaining incorrect guesses
    print("Remaining Incorrect Guesses:", max_guesses - incorrect_guesses)

    # Ask the user to enter a letter
    guess = input("Enter a letter: ").lower()

    # Check if the input is a single alphabet letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue  # Restart the loop

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guessed letter to the guessed letters list
    guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in word:
        print("Correct!")

        # Reveal all matching letters in the hidden word
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        # Increase incorrect guess count if the letter is not in the word
        print("Wrong!")
        incorrect_guesses += 1

# Check if the player guessed the entire word
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    # Player used all 6 incorrect guesses
    print("\nGame Over!")
    print("The correct word was:", word)