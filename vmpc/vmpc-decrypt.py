def vmpc_decrypt(ciphertext, key, num_iterations):
    # Konversi kunci ke nilai heksadesimal
    key_hex = ''.join(f'{ord(c):02x}' for c in key)
    
    # Inisialisasi variabel internal (register)
    registers = [int(key_hex[i:i+2], 16) for i in range(0, len(key_hex), 2)]
    num_registers = len(registers)
    
    # Inisialisasi memori
    memory = [i for i in range(256)]
    
    # Proses permutasi
    for _ in range(num_iterations):
        for i in range(num_registers):
            temp = memory[registers[i]]
            memory[registers[i]] = memory[temp]
            registers[i] = (registers[i] + temp) % 256
    
    # Dekripsi data
    plaintext = bytearray()
    for byte in ciphertext:
        for i in range(num_registers):
            temp = memory[registers[i]]
            byte ^= temp
            memory[registers[i]] = memory[temp]
            registers[i] = (registers[i] + temp) % 256
        plaintext.append(byte)
    
    return bytes(plaintext).decode()

# Contoh penggunaan
ciphertext = bytes.fromhex("0af520a3")
key = "KEY"
num_iterations = 2
plaintext = vmpc_decrypt(ciphertext, key, num_iterations)
print(f"Ciphertext: {ciphertext.hex()}")
print(f"Kunci: {key}")
print(f"Jumlah Iterasi: {num_iterations}")
print(f"Plaintext: {plaintext}")