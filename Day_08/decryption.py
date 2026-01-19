alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.

def decrypt(original_text,shift_amount):
    cipher_text =''
    for i in original_text:
        re_shifted_position = alphabet.index(i)- shift_amount
        re_shifted_position %= len(alphabet)
        cipher_text += alphabet[re_shifted_position]

    print(f"Here's your decoded results: {cipher_text}")

decrypt(text,shift)