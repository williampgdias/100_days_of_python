# STEP 5

# IMPORT MODULES
import random
from hangman_art import logo, stages
from hangman_words import word_list

# CREATING THE VARIABLES
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# SETTING THE LIVES TO A VARIABLE
lives = 6

print(logo)
print(f"Be really careful. You only have it {lives} chances.")

# CREATE BLANKS
display = []
for _ in range(word_length):
    display += "_"

print(f"{' '.join(display)}")

# CHECKING IF THE PLAYER WINS
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # CHECK GUESSED LETTER
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # CHECKING IF THE GUESS LETTER IS IN THE CHOSEN_WORD
    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word. You lose a life.")
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
        print("Uhuuull... Congratulations! You won!!")

    # PRINTING THE ASCII WHEN THE USER MISS THE LETTER
    print(stages[lives])