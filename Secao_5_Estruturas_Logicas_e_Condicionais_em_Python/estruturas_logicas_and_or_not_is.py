"""

Estruturas Lógicas: and (e), or(ou), not(não), is(é).

Operadores unários:

    - not

Operadores binários:

    - and, or, is
    
Regras de Funcionamento:

Para o 'and', ambos os valores devem ser True.
Para o 'or', um o outro valor precisa ser True.
Para o 'not', o valor do booleano é invertido, ou seja, se  for True, vira False, se fo False via True.

"""
ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo usuário!')

else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
