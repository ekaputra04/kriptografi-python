def xor_hex(hex1, hex2):
    # Konversi nilai heksadesimal ke integer
    int1 = int(hex1, 16)
    int2 = int(hex2, 16)
    
    # Lakukan operasi XOR
    result_int = int1 ^ int2
    
    # Konversi hasil XOR (integer) ke heksadesimal
    result_hex = hex(result_int)[2:].zfill(max(len(hex1), len(hex2)))
    
    return result_hex

# Contoh penggunaan
hex1 = "0x4B"
hex2 = "0x45"
result = xor_hex(hex1, hex2)
print(f"{hex1} XOR {hex2} = {result}")