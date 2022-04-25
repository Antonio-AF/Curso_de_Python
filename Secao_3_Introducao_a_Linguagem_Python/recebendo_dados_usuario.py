"""
Recebendo dados do usuario:

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que esticer entre:

- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:

- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
"""

# - Aspas duplas triplas -> """Angelina Jolie"""


# Entrada de dados
#print("Qual seu nome? ")
#nome = input() # Input -> Entrada de Dandos.

nome = input('Qual seu nome? ')

# Exeplo de print 'antigo' 2.x

#print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x

#print('Seja bem-vindo(a) %s {0}'.forma(nome))


# Exemplo de print 'mais atual' 3.8
print(f'Seja bem-vindo(a) {nome}')


#print('Qual sua idade?')
#idade = input()

idade = int(input('Qual sua Idade? '))

# Processamento

# Saída
# Exemplo de print 'antigo' 2.x
# print('A %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('A {0} tem {1} anos'.format(nome, idade))


# Exemplo de print 'moderno' 3.7
print(f'A {nome} tem  {idade} anos')


"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""
print(f'A {nome} nasceu em {2018 - idade}')



