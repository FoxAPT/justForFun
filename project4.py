# Arrays for mapping letters
original_alphabet = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

shifted_alphabet = [
    "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "A", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a"
]

# Function to encrypt a message using Caesar Cipher
def caesar_cipher_encrypt(message):
    encrypted_message = ""
    for char in message:
        if char in original_alphabet:
            index = original_alphabet.index(char)
            encrypted_char = shifted_alphabet[index]
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def main():
    # User input
    user_input = input("Enter the text to encrypt:  ")
    encrypted_text = caesar_cipher_encrypt(user_input)

    # Output the encrypted text
    print(encrypted_text)

if __name__ == "__main__":
    main()
