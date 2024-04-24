def nilai_huruf(string):
    # Menginisialisasi dictionary untuk menampung nilai setiap huruf
    nilai_huruf = {}
    for i in range(26):
        # Menggunakan ASCII code untuk mendapatkan nilai setiap huruf
        nilai_huruf[chr(97+i)] = i
    # Menginisialisasi list untuk menampung hasil
    hasil = []
    for char in string:
        # Mengecek apakah karakter merupakan huruf kecil
        if char.isalpha() and char.islower():
            hasil.append(nilai_huruf[char])
        else:
            # Jika bukan huruf kecil, tambahkan karakter aslinya
            hasil.append(char)
    return hasil

def dekripsi(ciphertext, plaintext):
    # Mengonversi ciphertext dan plaintext menjadi nilai huruf
    nilai_ciphertext = nilai_huruf(ciphertext)
    nilai_plaintext = nilai_huruf(plaintext)
    
    # Menghitung nilai key dari proses dekripsi
    key = [(nilai_ciphertext[i] - nilai_plaintext[i]) % 26 for i in range(len(plaintext))]
    key_huruf = [chr(97 + k) for k in key]
    
    return key, key_huruf, ''.join(key_huruf)

# Contoh penggunaan
ciphertext = input("Masukkan ciphertext: ").lower()
plaintext = input("Masukkan plaintext: ").lower()

# Mendapatkan nilai ciphertext, plaintext, key, dan huruf dari key
nilai_ciphertext = nilai_huruf(ciphertext)
nilai_plaintext = nilai_huruf(plaintext)
key, key_huruf, key_str = dekripsi(ciphertext, plaintext)

# Menampilkan pasangan huruf, nilai dari ciphertext, plaintext, key, dan huruf dari key
print("Pasangan huruf dan nilai:")
for i in range(len(ciphertext)):
    print(f"{ciphertext[i]}: {nilai_ciphertext[i]:<5} | {plaintext[i]}: {nilai_plaintext[i]:<5} | Key: {key[i]:<2} ({key_huruf[i]})")

print(key_str)
