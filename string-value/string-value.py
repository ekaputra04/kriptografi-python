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
            hasil.append((char, nilai_huruf[char]))
        else:
            # Jika bukan huruf kecil, tambahkan karakter aslinya dengan nilai None
            hasil.append((char, None))
    return hasil

# Contoh penggunaan
input_string = input("Masukkan string: ").lower()
hasil = nilai_huruf(input_string)
print("Hasil:")
for item in hasil:
    print(item)
