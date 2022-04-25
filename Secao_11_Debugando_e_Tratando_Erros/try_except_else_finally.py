"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVER SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.


"""
"""# Caso o usuário digite um valor diferente do esperado gerará um FileError.
num1 = int(input("Informe um número: "))
print(f'Você digitou {num1}')


# Tratando o erro para caso o usuário digite um valore diferente do solicitado.
num2 = 0
try:
    num2 = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')

print(f'Você digitou {num2}')

# Usando o Else

try:
    num3 = int(input('Informe um número'))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num2}')


# Usando o Finally

try:
    num4 = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido')
else:
    print(f'Você digitou o número {num4}')
finally:
    print('Executando o finally')

# Obs: O bloco finally é SEMPRE executado. Independente se houve exceção ou não.

# O finally, geralmente, é utilizado para fechar ou desalocar recursos."""

"""# Exemplo mais complexo ERRADO


def dividir(a, b):
    return a/b


num1 = int(input('Informe o primeiro número: '))

try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser númerico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')"""

# Exemplo complexo CORRETO
# OBS: Você é responsável pelas esntradas das suas funções. Então, trate-as


def dividir_aeb(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possivel realizar uma divisão por zero'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir_aeb(num1, num2))