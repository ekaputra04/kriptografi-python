def encrypt_vigenere(plaintext, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.upper()) - ord('A')
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_vigenere(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.upper()) - ord('A')
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        print("Vigenere Algorithm")
        print("Pilihan program : [1] Enkripsi [2] Dekripsi [3] Exit")
        pilihan = input("[1] atau [2] atau [3] : ")
        if pilihan == "1":
            plaintext = input("Masukkan plaintext : ")
            key = input("Masukkan key : ") 
            encrypted_text = encrypt_vigenere(plaintext, key)
            print("Plaintext:", plaintext)
            print("Key:", key)
            print("Encrypted Text:", encrypted_text)
        elif pilihan == "2":
            encrypted_text = input("Masukkan encrypted_text : ")
            key = input("Masukkan key : ") 
            decrypted_text = decrypt_vigenere(encrypted_text, key)
            print("Encrypted text:", encrypted_text)
            print("Key:", key)
            print("Decrypted Text:", decrypted_text)
        elif pilihan == "3" :
            exit()

if __name__ == "__main__":
    main()