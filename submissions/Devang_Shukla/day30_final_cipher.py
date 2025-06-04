def decode_char(c,shift):
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        return chr((ord(c) - base - shift) % 26 + base)
    else:
        return c
def decode_cipher(text,shift):
    return ''.join(decode_char(c,shift) for c in text)
cipher_text = input("Enter cipher text: ")
shift_value = int(input("Enetr shift value: "))
decoded_message = decode_cipher(cipher_text,shift_value)
print("\nDecoded message : ",decoded_message)    