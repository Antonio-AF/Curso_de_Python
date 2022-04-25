"""
        :::Definindo Funções:::

- Funções são pequenas partes de códigos que realizam tarefas específicas.
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
É bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções deesde que iniciamos este curso:
-print()
-len()
-max()
-min()
- count()
- e muitas outras;



"""
# Exemplo de utilização de funções:

# cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()

# print(cores)

# curso = 'Programação em Python: Essencial'

# print(curso)

# cores.append('roxo')

# print(cores)

# curso.append('Mais dados...') # AttributError
# print(curso)

# cores.clear()
# print(cores)

# print(help(print))

# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código.


# MAs então, como definir uma Função?

"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separados por underline (Snake Case)
parametros_de_entrada -> opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não:
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
neste cloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra rezervada 'def' informando ao Python que estamos
definindo uma função. Também abrirmos o bloco de código com o já conhecido dois pontos ':',
que é utlizado em Python para definir blocos.
"""


# Definindo a primeira Função.

# Definição
def diz_oi():
    print('Oi Burro!')


"""
OBS:

1 - Veja que, dentro das nossas funções podemos utlizar outras funções;
2 - Veja que nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nem um parâmetro de entrada;
4 - Veja que esta função não retorna nada;
"""
# Utilizando funções

# Chamada de execução.
diz_oi()

"""
        :::ATENÇÃO:::
        
Nunca esqueça de utilizar o parênteses ao executar uma função.

Exemplo:

# Errado:
diz_oi

# Certo
diz_oi()

# Errado
diz_oi () # Nunca por espaço entre os parênteses da função.
"""


# Exemplo 2

def cantar_parabens():
    print('Parabens para você')
    print('Nesta data querida')
    print('Muitos felicidades')
    print('Muitos anos de vida')
    print('Viva ao aniversariante')


# for n in range(5):
#    cantar_parabens()

# Em Python podemos inclusive criar variaveis do tipo de uma função e executar esta função atrávez da variável.

canta = cantar_parabens

canta()
