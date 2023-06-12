# STEP 3

# IMPORT THE MODULE
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
word_length = len(chosen_word)

#  TESTING CODE
print(f"Pssst, the solution is {chosen_word}.")

# CREATE BLANKS
display = []
for _ in range(word_length):
    display += "_"

# TODO_1:
# USE A WHILE LOOP TO LET THE USER GUESS AGAIN. THE LOOP SHOULD ONLY STOP ONCE THE USER HAS GUESSED ALL THE LETTERS
# IN THE CHOSEN_WORD AND 'DISPLAY' HAS NO MORE BLANKS ("_"). THEN, YOU CAN TELL THE USER THEY'VE WON.
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # CHECK GUESSED LETTER
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n"
        #       f"Current letter: {letter}\n"
        #       f"Guessed letter: {guess}"
        #       )
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")
