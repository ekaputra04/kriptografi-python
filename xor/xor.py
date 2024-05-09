def is_binary(input_str):
    return all(bit == '0' or bit == '1' for bit in input_str)

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

def main():
    plaintext = input("Masukkan plaintext (biner) : ")
    while not is_binary(plaintext):
        print("Input tidak valid! Masukkan hanya bilangan biner (0 atau 1).")
        plaintext = input("Masukkan plaintext (biner) : ")

    key = input("Masukkan key (biner)       : ")
    while not is_binary(key):
        print("Input tidak valid! Masukkan hanya bilangan biner (0 atau 1).")
        key = input("Masukkan key (biner)       : ")

    print("==========================================================")
    # Enkripsi
    encrypted_text = xor_encrypt(plaintext, key)
    print("Hasil enkripsi             :", encrypted_text)

    # Dekripsi
    decrypted_text = xor_decrypt(encrypted_text, key)
    print("Hasil dekripsi             :", decrypted_text)

if __name__ == "__main__":
    main()
