"""
POO - Atributos


ATributos -> Representam as características do objeto. Ou seja, pelos atributos nós conseguimos representar
computacionalmente os estados de um objeto.

em Python, dividimos os atributos em 3 grupos:

    - Atributos de Instância;
    - Atributos de Classes;
    - Atributos Dinâmicos;

# Atributos de instância: São atributos declarados dentro do método construtor.

# Obs: Método construtor: É um método especial utilizado para a construção do objeto.


# Em java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }

}


Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demostrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado,
utiliza-se __ duplo undercore no início de seu nome.

Isso é conhecido também como Name Mangling.



# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir que que façamos acesso
# aos atributos sinalizados como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '123456')

print(user.email)
#print(user.senha) # AttributeError: 'Acesso' object has no attribute 'senha'

print(user._Acesso__senha)

user.mostra_senha()
user.mostra_email()

# O que significa atributos de instância?

# Significa, que ao criarmos instâncias/objetos de uma classe, todas as instâncias
# terão estes atributos.

user1 = Acesso('user1@gmail.com', '123589')
user2 = Acesso('user2@gmail.com', '137784')

user1.mostra_email()
user2.mostra_email()



p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 2500)

print(p1.valor) # Acesso possível, mas incorreto de um atributo de classe.
print(p2.valor) # Acesso possível, mas incorreto de um atributo de classe.

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe.

print(Produto.imposto) # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python
# são chamados de atributos estáticos;

"""


# No Python

# Classes com Atributos de instância Públicos.
class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Self, se traduz como (O objeto "Usuario" no atributo -> nome Vai recer -> nome)
# Self, se traduz como (O objeto "Usuario" no atributo -> email Vai recer -> email)
# Self, se traduz como (O objeto "Usuario" no atributo -> senha Vai recer -> senha)


# Atributos Públicos  e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Atributos de Classe

"""
p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 2500)
"""


# Atributos de classes, são atributos, claro, que são declarados diretamente  na classe, ou seja,
# fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre
# todas as instâncias da classe. Ou seja, ao invés de cada instãncia da classe ter seus próprios
# valores como é o caso dos atributos de instância, com os atributos de classe todas as instãncias
# terão o mesmo valor para este atributo.

# Refatorar a classe Produto


class Produto:
    # Atributo de classe.
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


# Atributos Dinâmicos -> Um atributo de instancia que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('PlayStation 4', 'Video Game', 3200)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg'  # Note que a classe Produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')

# Deletando atributos

print(p2.__dict__)
print(p1.__dict__)

print(Produto.__dict__)

del p2.peso
del p2.valor
del p2.descricao

print(p2.__dict__)
print(p1.__dict__)
