string = input("Digite uma Palavra para converter em Binary: ")
binary_convert = ' '.join(format(ord(c), 'b') for c in string)
print("O binario da palavra digitada é : ", binary_convert)


def decode_binary_string(s):
    return ''.join(chr(int(s[i * 8:i * 8 + 8], 2)) for i in range(len(s) //8))


resultado = decode_binary_string(binary_convert)
print("A conversão é: ", resultado)
