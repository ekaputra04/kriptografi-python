def vmpc_encrypt(plaintext, key, num_iterations):
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
    
    # Enkripsi data
    ciphertext = bytearray()
    for char in plaintext:
        char_value = ord(char)
        for i in range(num_registers):
            temp = memory[registers[i]]
            char_value ^= temp
            memory[registers[i]] = memory[temp]
            registers[i] = (registers[i] + temp) % 256
        ciphertext.append(char_value)
    
    return bytes(ciphertext), bytes(registers)

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
    
    return bytes(plaintext).decode(), bytes(registers)

def ascii_to_hex(ascii_string):
    hex_values = []
    for char in ascii_string:
        hex_value = hex(ord(char))[2:].zfill(2)  # Mengonversi karakter ke heksadesimal
        hex_values.append(hex_value)
    return ''.join(hex_values)

def main():
    # contoh enkripsi
    plaintext = "VMPC"
    key = "KEY"
    num_iterations = 2  # Jumlah iterasi permutasi
    ciphertext, registers = vmpc_encrypt(plaintext, key, num_iterations)
    print(f"Plaintext     : {plaintext}")
    print(f"Kunci         : {key}")
    print(f"Jumlah Iterasi: {num_iterations}")
    print(f"Plaintext hex : {ascii_to_hex(plaintext)}")
    print(f"Registers     : {registers.hex()}")
    print(f"Ciphertext    : {ciphertext.hex()}")
    print("====================================================")
    
    ciphertext = bytes.fromhex(ciphertext.hex())
    key = "KEY"
    num_iterations = 2
    plaintext, registers = vmpc_decrypt(ciphertext, key, num_iterations)
    print(f"Ciphertext    : {ciphertext.hex()}")
    print(f"Kunci         : {key}")
    print(f"Jumlah Iterasi: {num_iterations}")
    print(f"Ciphertext hex: {ciphertext.hex()}")
    print(f"Registers     : {registers.hex()}")
    print(f"Plaintext     : {plaintext}")

if __name__ == "__main__":
    main()