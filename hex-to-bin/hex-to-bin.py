def hex_to_bin(hex_str):
    # Inisialisasi string biner kosong
    bin_str = ''
    
    # Melakukan konversi setiap digit heksadesimal ke biner
    for i in range(0, len(hex_str), 2):
        # Mengambil setiap dua digit heksadesimal
        hex_byte = hex_str[i:i+2]
        
        # Mengonversi nilai heksadesimal ke desimal
        decimal = int(hex_byte, 16)
        
        # Mengonversi nilai desimal ke biner (8 bit)
        bin_val = bin(decimal)[2:].zfill(8)
        
        # Menggabungkan bit-bit biner ke string biner
        bin_str += bin_val
    
    return bin_str

# Contoh penggunaan
hex_value = "4b414d55"
bin_value = hex_to_bin(hex_value)
print(f"Nilai heksadesimal: {hex_value}")
print(f"Nilai biner: {bin_value}")