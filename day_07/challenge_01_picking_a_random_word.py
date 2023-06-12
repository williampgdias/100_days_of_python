# STEP 1

word_list = [
    "photoshop",
    "chatgpt",
    "python",
    "javascript",
    "software",
    "hardware"
]

# TODO_1:
    # RANDOMLY CHOOSE A WORD FROM THE WORD_LIST AND ASSIGN IT OT A VARIABLE CALLED "CHOSEN_WORD".
import random

chosen_word = random.choice(word_list)

# TODO_2:
    # ASK THE USER TO GUESS A LETTER AND ASSIGN THEIR ANSWER TO A VARIABLE CALLED GUESS. MAKE GUESS LOWERCASE.
guess = input("Guess a letter: ").lower()

# TODO_3:
    # CHECK IF THE LETTER THE USER GUESSED (GUESS) IS ONE OF THE LETTERS IN THE CHOSEN_WORD.
# for guess in chosen_word:
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")