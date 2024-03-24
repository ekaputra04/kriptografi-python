def generate_monoalphabetic_key(key):
    # Inisialisasi alfabet biasa
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Menghapus duplikasi huruf dalam kunci dan membuat kunci unik
    unique_key = ""
    for char in key:
        if char not in unique_key:
            unique_key += char
    # Menambahkan huruf yang belum ada di kunci ke dalamnya
    for char in alphabet:
        if char not in unique_key:
            unique_key += char
    return unique_key

def encrypt_monoalphabetic(plaintext, key):
    encrypted_text = ""
    key = generate_monoalphabetic_key(key.lower())
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_text += key[ord(char.lower()) - 97].upper()
            else:
                encrypted_text += key[ord(char) - 97]
        else:
            encrypted_text += char
    return encrypted_text, key

def decrypt_monoalphabetic(ciphertext, key):
    decrypted_text = ""
    key = generate_monoalphabetic_key(key.lower())
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr(key.upper().index(char) + 65)
            else:
                decrypted_text += chr(key.index(char) + 97)
        else:
            decrypted_text += char
    return decrypted_text, key

def main():
    while True:
        print("Monoalpabetik Substitution")
        print("Pilihan program : [1] Enkripsi [2] Dekripsi [3] Exit")
        pilihan = input("[1] atau [2] atau [3] : ")
        if pilihan == "1":
            plaintext = input("Masukkan plaintext : ")
            key = input("Masukkan key : ") 
            encrypted_text, monoalpanetic_key = encrypt_monoalphabetic(plaintext, key)
            print("Plaintext:", plaintext)
            print("Key:", key)
            print("Monoalpabetic Key:", monoalpanetic_key)
            print("Encrypted Text:", encrypted_text)
        elif pilihan == "2":
            encrypted_text = input("Masukkan encrypted text : ")
            key = input("Masukkan key : ") 
            decrypted_text, monoalpanetic_key = decrypt_monoalphabetic(encrypted_text, key)
            print("Encrypted text:", encrypted_text)
            print("Key:", key)
            print("Monoalpabetic Key:", monoalpanetic_key)
            print("Decrypted Text:", decrypted_text)
        elif pilihan == "3" :
            exit()

if __name__ == "__main__":
    main()