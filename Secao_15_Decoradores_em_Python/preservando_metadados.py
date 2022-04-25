
"""
    Preservando Metadados com wraps

Metadados -> São dados intrísecos em arquívos.de

Wraps -> São funções que envolvem elementos com diversas finalidades.de


"""

# Problema
# Resolução do Problema

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma doís números."""
    return a + b


print(soma(10, 30))


print(soma.__name__) #soma
print(soma.__doc__) # Soma dois números.