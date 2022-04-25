""""
Decoradores (Decorators)

O que são decorators?

- Decoradores são funções;
- Decoradores envolvem  outras funções e aprimoram seus comportamentos;

|------------------------------------------------------------|
|       Function Decorator                                   |
|------------------------------------------------------------|

--------------------------------------------------------------

|----------------------------------------------------------------|
| |------------------------------------------------------------| |
| |           Função                                           | |
| |------------------------------------------------------------| |
|--------------------------------------------------------------- |

"""

# Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você! ')
        funcao()
        print('Tenha um ótimo dia! ')
    return sendo


def saudacao():
    print('Seja bem-vindo(a) à Geek University ')

# Testando 1

teste = seja_educado(saudacao)
teste()

# Testando 2


def raiva():
    print('EU TE ODEIO')


raiva_educada = seja_educado(raiva)

raiva_educada()