

from random_word import RandomWords

from FOLDER_UPDATED.PYTHON_100_PROJECTS.hangman.hangman_art import HANGMAN_LOGO, HANGMAN_PICS  # Import logo and hangman pics

# Display the Hangman logo at the start of the game
print(HANGMAN_LOGO)


# Initialize the random word generator
r = RandomWords()
random_word = r.get_random_word().lower()
print(f"The random word has {len(random_word)} letters.")

# Initialize variables
word_length = len(random_word)
display = ["_"] * word_length  # Word display with underscores
attempts = 0  # Track wrong guesses
max_attempts = len(HANGMAN_PICS) - 1  # Max allowed attempts
guessed_letters = []  # Store guessed letters

print(" ".join(display))  # Initial display with underscores

# Game loop
game_over = False
while not game_over:
    user_input = input("\nGuess a letter: ").lower()

    # Check if letter was already guessed
    if user_input in guessed_letters:
        print(f"You already guessed '{user_input}'. Try again.")
        continue

    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(user_input)

    # Check if the guessed letter is in the word
    if user_input in random_word:
        print(f"Good guess! '{user_input}' is in the word.")
        for index, letter in enumerate(random_word):
            if letter == user_input:
                display[index] = letter  # Update correct guess
    else:
        attempts += 1
        print(f"Wrong guess! '{user_input}' is not in the word.")
        print(HANGMAN_PICS[attempts])  # Show hangman stage

    # Print the current state of the word
    print(" ".join(display))

    # Check if the player has guessed the entire word
    if "_" not in display:
        game_over = True
        print("\nCongratulations! You guessed the word:", random_word)

    # Check if the player has used all attempts
    if attempts == max_attempts:
        game_over = True
        print("\nGame Over! You ran out of attempts.")
        print(f"The word was: {random_word}")
