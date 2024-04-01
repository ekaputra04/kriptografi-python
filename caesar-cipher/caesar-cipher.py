def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# def decrypt_multiple_times(ciphertext):
#     for i in range(26):
#         decrypted_text = decrypt_caesar_cipher(ciphertext, i)
#         print(f"With key {i}: {decrypted_text}")

def decrypt_multiple_times(ciphertext):
    decrypted_text = decrypt_caesar_cipher(ciphertext, 12)
    print(f"With key 12: {decrypted_text}")

ciphertext = input("Masukkan ciphertext: ")
decrypt_multiple_times(ciphertext)
