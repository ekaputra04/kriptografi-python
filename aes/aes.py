from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def encrypt_aes(plaintext, key):
    # Memastikan panjang kunci valid (16, 24, atau 32 byte)
    if len(key) not in [16, 24, 32]:
        raise ValueError("Panjang kunci harus 16, 24, atau 32 byte")

    # Mengonversi plaintext dan kunci menjadi bytes
    plaintext = plaintext.encode()
    key = key.encode()

    # Membuat objek cipher dengan algoritma AES dalam mode CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Melakukan enkripsi
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return ciphertext

def decrypt_aes(ciphertext, key):
    # Memastikan panjang kunci valid (16, 24, atau 32 byte)
    if len(key) not in [16, 24, 32]:
        raise ValueError("Panjang kunci harus 16, 24, atau 32 byte")

    # Mengonversi kunci menjadi bytes
    key = key.encode()

    # Membuat objek cipher dengan algoritma AES dalam mode CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Melakukan dekripsi
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return plaintext.decode()

# Contoh penggunaan
plaintext = "KAMUSKECILBAHASA"
key = "KRIPTOGRAFIAESKU"  # Kunci 16 byte (128 bit)
iv = b'\x00' * 16  # Vektor inisialisasi 16 byte

# Enkripsi
ciphertext = encrypt_aes(plaintext, key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi
decrypted_text = decrypt_aes(ciphertext, key)
print("Plaintext setelah dekripsi:", decrypted_text)