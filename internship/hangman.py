import random

# List of words for the game
words = ["apple", "banana", "orange", "grape", "strawberry", "watermelon"]

# Function to select a random word from the list
def select_word():
    return random.choice(words)

# Function to initialize the display
def initialize_display(word):
    return ["_" for _ in word]

# Function to update the display with guessed letters
def update_display(word, display, letter):
    for i, char in enumerate(word):
        if char == letter:
            display[i] = letter
    return display

# Function to print Hangman ASCII art based on incorrect guesses
def print_hangman(incorrect_guesses):
    stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]
    print(stages[incorrect_guesses])

# Function to play the game
def play_hangman():
    word = select_word()
    display = initialize_display(word)
    incorrect_guesses = 0
    guessed_letters = []

    while True:
        print("\n" + " ".join(display))
        print_hangman(incorrect_guesses)
        print("Guessed letters:", guessed_letters)

        guess = input("Guess a letter: ").lower()

        # Check if the guess is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in word:
            display = update_display(word, display, guess)
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess!")

        # Check if the player has won
        if "_" not in display:
            print("\nCongratulations! You guessed the word:", word)
            break

        # Check if the player has lost
        if incorrect_guesses == len(stages):
            print("\nSorry, you ran out of guesses. The word was:", word)
            break

# Start the game
play_hangman()
