alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO_1: COMBINE THE ENCRYPT() AND DECRYPT() FUNCTIONS INTO A SINGLE FUNCTION CALLED CAESAR().
############################## MY CODE! ITS WORKING!! ##############################
# def caesar(plain_text, cipher_text, shift_amount):
#     if direction == "encode":
#         cipher_text = ""
#         for letter in plain_text:
#             position = alphabet.index(letter)
#             new_position = position + shift_amount
#             new_letter = alphabet[new_position]
#             cipher_text += new_letter
#         print(f"The encoded text is {cipher_text}")
#     elif direction == "decode":
#         plain_text = ""
#         for letter in cipher_text:
#             position = alphabet.index(letter)
#             new_position = position - shift_amount
#             new_letter = alphabet[new_position]
#             plain_text += new_letter
#         print(f"The decoded text is {plain_text}")

############################## TEACHER CODE!! ##############################
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")


# TODO_2: CALL THE CAESAR() FUNCTION, PASSING OVER THE "TEXT", "SHIFT" AND "DIRECTION" VALUES.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


