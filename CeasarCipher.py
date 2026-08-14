alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def ceasar(direction, text, shift):
    output_text = ""
    if direction == "decode":
        shift *= -1

    for letter in text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {direction}d result:  {output_text}")


done = False
while not done:
    encodeDecode = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt.\n"
    ).lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Enter in your shift amount:\n"))

    ceasar(encodeDecode, text, shift)
    cont = input("Do you want to quit-->").lower()

    if cont == "yes" or cont == "y":
        done = True
