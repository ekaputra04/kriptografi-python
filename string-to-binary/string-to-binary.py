def string_to_binary(input_string):
    binary_char = ""
    binary_result = ""
    for char in input_string:
        binary_char += f"{char} : {format(ord(char), '08b')}\n"
    binary_result = ''.join(format(ord(char), '08b') for char in input_string)
    return binary_char, binary_result

def main():
    input_string = input("Masukkan string: ")
    binary_char, binary_result = string_to_binary(input_string)
    print("Hasil konversi ke biner:")
    print(binary_char)
    print(binary_result)

if __name__ == "__main__":
    main()
