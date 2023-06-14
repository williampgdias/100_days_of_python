alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


# TODO_1: CREATE A DIFFERENT FUNCTION CALLED "DECRYPT" THAT TAKES THE "TEXT" AND "SHIFT" AS INPUTS.
def decrypt(cipher_text, shift_amount):
    # TODO_2: INSIDE THE 'DECRYPT' FUNCTION, SHIFT EACH LETTER OF THE 'TEXT' *BACKWARDS* IN THE ALPHABET BY THE
    # SHIFT AMOUNT AND PRINT THE DECRYPTED TEXT.
    # E.G.
    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    # print_output: "The decoded text is hello"
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decoded text is {plain_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)

