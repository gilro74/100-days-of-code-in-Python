alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encrypt(original_text, shift_amount):
    encrypted_text = ''
    for i in original_text:
        if i not in alphabet:
            encrypted_text += i
        else:
            shifted_position = (alphabet.index(i) + shift_amount) % len(alphabet)
            encrypted_text += alphabet[shifted_position]

    print(f"\nHere is the encoded result: {encrypted_text}")

def decrypt(original_text, shift_amount):
    decrypted_text = ''
    for i in original_text:
        if i not in alphabet:
            decrypted_text += i
        else:
            re_shifted_position = (alphabet.index(i) - shift_amount) % len(alphabet)
            decrypted_text += alphabet[re_shifted_position]

    print(f"\nHere is the decoded result: {decrypted_text}")


should_continue = True

while should_continue:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
    text = input("Type your message:\n").lower().strip()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Please type 'encode' or 'decode' only!")

    restart = input("\nDo you want to go again? Type 'yes' or 'no':\n").lower().strip()
    if restart != "yes":
        should_continue = False
        print("Goodbye 👋")

