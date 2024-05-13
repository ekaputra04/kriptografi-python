def ascii_to_hex(ascii_string):
    hex_values = []
    for char in ascii_string:
        hex_value = hex(ord(char))[2:].zfill(2)  # Mengonversi karakter ke heksadesimal
        hex_values.append(hex_value)
    return ''.join(hex_values)

# Contoh penggunaan
ascii_string = input("Masukkan Ascii : ")
hex_string = ascii_to_hex(ascii_string)
print(f"String ASCII: {ascii_string}")
print(f"Representasi Heksadesimal: {hex_string}")