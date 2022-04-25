"""
            :::FUNÇÕES COM PARÂMETROS PADRÃO (DEFAULT: PARAMETERS)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional;

print('Geek University')

print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória.

def quadrado(numero):
    return numero ** 2


print(quadrado(3))
print(quadrado()) # TypeError


def exponincial(numero, potencia=2):
    return numero ** potencia


print(exponincial(2, 3))
print(exponincial(3, 2))

print(exponincial(3))  # Por padrão eleve ao quadrado
print(exponincial(3, 5))  # Eleva á potência informada pelo usuário

# OBS:

# Se o usuário passar somente 1 argumento, este será atribuído ao parâmetro numero,
# e será calculado o quadrado deste números;

# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro e o segundo ao
# parâmetro potencia. Então será calculando esta potência.


# OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

# ERRO!!

def teste(num = 2, potencia):
    return num ** potencia

print(teste(6))


# Outros exemplos

def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))
print(soma(4))
print(sema())


# Exemplo mais complexo.


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek!!!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))


# Por quê utilizar parâmetros com valor default?

- Nos permite se mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de códigos;


# Quais tipos de dados podemos usar como valores default para parâmetros?

- Qualquer tipo de dados;
- Números, strings, float, booleanos, listas, tuplas, dicionbários, funções e etc.


# Exemplos

def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusoes...

# Variáveis Globais
# Variáveis Locais.

instrutor = 'Geek' # Variável global.

def diz_oi():
    instrutor = 'Python' # Variável local
    return f'Oi {instrutor}'


print(diz_oi())

# OBS: Se tivermos uyma variável local com o mesmo nome de uma variável global,
# a local terá preferência.


def diz_oi():
    prof = 'Geek'
    return f'Olá {prof}'


print(diz_oi())

print(prof) # NameError

# ATENÇÂO com variáveis globais (Se puder ecitar, evite!)

total = 0

def incremento():
    total = total + 1 # UnboundLocalError (A variável local está sendo utilizada para processamento sem ter sido inicializada)
    return total


print(incremento())


# ATENÇÂO com variáveis globais (Se puder ecitar, evite!)

total = 0

def incremento():
    global total # Avisando que queremos utilizar a variável global

    total = total + 1
    return total

print(incremento())
print(incremento())
print(incremento())


# Podemos ter funções que são declaradas dentro de funções, e também tem um forma especial de escopo de variável.

def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador

    return dentro()


print(fora())
"""


