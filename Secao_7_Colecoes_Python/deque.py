"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance.

"""

# Importar.

from collections import deque

deq = deque('geek')
print(deq)

# Adicionando elementos no deque.

deq.append('y') # Adiciona o elemento no final.

print(deq)

deq.appendleft('k') # Adiciona o elemento no começo.

print(deq)

# Remover elementos.

print(deq.pop()) # Remove o ultimo elemento da lista.
print(deq)

print(deq.popleft()) # Remove o primeiro elemento da lista.
print(deq)