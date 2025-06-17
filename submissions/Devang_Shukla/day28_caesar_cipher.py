def caesar_cipher_decode(cipher_text,shift):
    decoded_text = ""
    for char in cipher_text:
        if char.isalpha():
            if char.isupper():
                decoded_char = chr((ord(char) - ord('A') - shift)% 26 + ord('A'))
            else:
                decoded_char = chr((ord(chr) - ord('a') - shift)% 26 + ord('a'))
            decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text
cipher_input = input("Enter cipher text: ")
shift_value = int(input("Enter shift value: "))
decoded_message = caesar_cipher_decode(cipher_input,shift_value)
print("\nDecoded message:",decoded_message)                    