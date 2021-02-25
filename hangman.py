"""
This program allows a user to play a game of Hangman.



"""
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# Welcome User.
print("Welcome to Hangman!")
# Create a word list. 
word_list = ["aardvark", "baboon", "camel"]

# Choose a random word from a word list. 
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create a display blank for the random word chosen: ie) [_ _ _ _ _ _ ]
display = []
for i in range(0, word_length):
    display.append("_")
print(f"Current word: {display}")

# Game Loop that will loop until the user has 0 lives or has guessed the word. 
gameplay = True
user_lives = 6
guessed_words = []

while gameplay == True:
    # Keep a variable to check if the user has already guessed a particular letter.
    already_guessed = True
    while already_guessed:
        # Ask user for a guess. 
        user_guess = input("Guess a letter: ")
        # If the user hasn't guessed the letter:
            # Add the letter to a running list of guessed letters.
            # Exit the loop.
        if guessed_words.count(user_guess) == 0:
            guessed_words.append(user_guess)
            already_guessed = False
        else: # If the user already guessed the letter, loop back and ask again.
            print("You have already guessed this letter. Try again.")

    # Check the letter against the word. 
    # Make a variable to keep track if the letter was found.
    letter_found = False
    for index in range(0,word_length):
        letter = chosen_word[index]
        if letter == user_guess: 
            display[index] = letter 
            letter_found = True
    # If letter not found, take away one life.
    if letter_found == False:
        print("Incorrect guess.")
        user_lives = user_lives - 1
        # Lose Condition 
        if user_lives == 0: 
            gameplay = False
            print(f"You lose. The correct word was {chosen_word}.")
    else:
        print("Correct guess.")
    # Win Condition
    if display.count("_") == 0:
        gameplay = False
        print(display)
        print(f"You win! The correct word was {chosen_word}!")
    # Show the display of the current word and user lives ASCII
    else: 
        print(stages[user_lives])
        print(display)
        print(f"Guesses remaining: {user_lives}")

# End
