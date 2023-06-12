# STEP 4

# IMPORT THE MODULE
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

end_of_game = False
word_list = [
    "photoshop",
    "chatgpt",
    "python",
    "javascript",
    "software",
    "hardware"
]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# TODO_1:
    # CREATE A VARIABLE CALLED "LIVES" TO KEEP TRACK OF THE NUMBER OF LIVES LEFT.
    # SET "LIVES" EQUAL TO 6.
lives = 6

print("Welcome to Hangman. Try to get the word.")

#  TESTING CODE
print(f"Pssst, the solution is {chosen_word}.")

# CREATE BLANKS
display = []
for _ in range(word_length):
    display += "_"

print(f"{' '.join(display)}")

# CHECKING IF THE PLAYER WINS
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # CHECK GUESSED LETTER
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # TODO_2:
        # IF GUESS IS NOT A LETTER IN THE CHOSEN_WORD, THEN REDUCE "LIVES" BY 1.
        # IF LIVES GOES DOWN TO 0, THEN THE GAME SHOULD STOP AND IT SHOULD PRINT "YOU LOSE".
    if guess not in chosen_word:
        lives -= 1
        if lives == 1:
            print(f"Be careful now. You only has {lives} chance")
        elif lives == 0:
            end_of_game = True
            print("I am sorry, but you have to try again!! You lose!")

    # JOIN ALL THE ELEMENTS IN THE LIST AND TURN IT INTO A STRING.
    print(f"{' '.join(display)}")

    # CHECK IF THE USER HAS GOT ALL LETTERS
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO_3:
        # PRINT THE ASCII ART FROM 'STAGES' THAT CORRESPONDS TO THE CURRENT NUMBER OF 'LIVES' THE USER HAS REMAINING.
    print(stages[lives])