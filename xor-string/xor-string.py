def xor_encrypt(plaintext, key):
    encrypted = ""
    key_length = len(key)
    for i in range(len(plaintext)):
        encrypted += str(int(plaintext[i]) ^ int(key[i % key_length]))
    return encrypted

def xor_decrypt(ciphertext, key):
    decrypted = ""
    key_length = len(key)
    for i in range(len(ciphertext)):
        decrypted += str(int(ciphertext[i]) ^ int(key[i % key_length]))
    return decrypted

def string_to_binary(input_string):
    binary_char = ""
    binary_result = ""
    for char in input_string:
        binary_char += f"{char} : {format(ord(char), '08b')}\n"
    binary_result = ''.join(format(ord(char), '08b') for char in input_string)
    return binary_char, binary_result

def main():
    plaintext = input("Masukkan plaintext (biner) : ")
    plaintext_char, plaintext_full = string_to_binary(plaintext)
    key = input("Masukkan key (biner)       : ")
    key_char, key_full = string_to_binary(key)

    print("====================================================================")
    print(plaintext_char)
    print(plaintext_full)
    print("--------------------------------------------------------------------")
    print(key_char)
    print(key_full)
    print("--------------------------------------------------------------------")
    # Enkripsi
    encrypted_text = xor_encrypt(plaintext_full, key_full)
    print("Hasil enkripsi :", encrypted_text)

    # Dekripsi
    decrypted_text = xor_decrypt(encrypted_text, key_full)
    print("Hasil dekripsi :", decrypted_text)

if __name__ == "__main__":
    main()
