# Exemplo 1: Como dir() trabalha?

print("Exemplo 1: Como dir() trabalha?")

number = [1, 2, 3]
print(dir(number))

print("Valores de retorno do dir() vazio")
print(dir())


# Exemplo 2: dir() Na definição de Objetos pelo usuário.
print()
print("Exemplo 2: dir() Na definição de Objetos pelo usuário.")


class Pessoa:
    def __dir__(self):
        return ['idade', 'nome', 'salario']


professor = Pessoa()
print(dir(professor))

# Saída do dir(professor) -> ['idade', 'nome', 'salario']