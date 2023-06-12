# STEP 2

import random

word_list = [
    "photoshop",
    "chatgpt",
    "python",
    "javascript",
    "software",
    "hardware"
]

chosen_word = random.choice(word_list)

#  TESTING CODE
print(f"Pssst, the solution is {chosen_word}.")

# TODO_1:
    # FOR EACH LETTER IN THE CHOSEN_WORD, ADD A "_" TO 'DISPLAY'.
    # SO, IF THE CHOSEN_WORD WAS "PYTHON", DISPLAY SHOULD BE ["_", "_", "_", "_", "_", "_"] WITH 6 "_" REPRESENTING
    # EACH LETTER TO GUESS.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)


guess = input("Guess a letter: ").lower()

# TODO_2:
    # LOOP THROUGH EACH POSITION IN THE CHOSEN_WORD;
    # IF THE LETTER AT THAT POSITION MATCHES 'GUESS', THEN REVEAL THAT LETTER IN THE DISPLAY AT THAT POSITION.
    # E.G. IF THE USER GUESSED "P" AND THE CHOSEN WORD WAS "PYTHON", THEN DISPLAY SHOULD BE ["P", "_", "_", "_", "_",
    # "_"].

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

# TODO_3:
    # PRINT "DISPLAY" AND YOU SHOULD SEE THE GUESSED LETTER IN THE CORRECT POSITION AND EVERY OTHER LETTER REPLACE WITH
    # "_".
    # HINT: DON'T WORRY ABOUT GETTING THE USER TO GUESS THE NEXT LETTER. WE'LL TACKLE THAT IN STEP 3.

print(display)
