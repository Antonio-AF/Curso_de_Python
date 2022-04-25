"""
    Generators

Em aulas anteriores nós estudamos:

_ List Comprehension
- Dictionary Comprehensions:
- Set Comprehension:

Não vimos

- Tuple Comprehension porque elas se chamam Generations

nomes = ['Calors', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))



# Poderiamos ter feito utilizando Generators

nomes = ['Calors', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension

res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generator
# Ocupa menos espaço na memoria.
res = (nome[0] == 'C' for nome in nomes)
print(type(res))

"""

# Qual é a utilizadade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro.
from sys import getsizeof

# ostra quantos bytes a string 'Geek' está ocupando em memória. Quanto maior a string, mais espaço ocupa
print(getsizeof('Geek'))

print(getsizeof('University'))
print(getsizeof('Antonio'))

print(getsizeof('1'))
print(getsizeof('10'))
print(getsizeof('1000'))
print(getsizeof('1000'))

# Gerando uma lista de úmeros com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dict_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))


print('Para fazer a mesma tarefa gastamos em memória:')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set  Comprehension: {set_comp} bytes')
print(f'Doctionary Comprehension: {dict_comp} bytes ')
print(f'Generator Comprehension: {gen} bytes')

