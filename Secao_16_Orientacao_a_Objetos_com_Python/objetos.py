"""

POO - Objetos

Objetos -> São instâcias da classe. Ou seja,  após o mapeamento do objeto do mundo real para sua
representação computacional, devemos poder criar quantos objetos forem  necessários. Podemos pensar
nos objetos/instâcias de uma classe como variáveis do tipo definido na classe.



# Instância/Objetos
lamp1 = Lampada('Branca', 110, 60)

lamp1.ligar_desligar()
lamp1.ligar_desligar()

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000, 20000)

user1 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')


lamp = Lampada('Branca', 220, 2000)

nome = 'Angelina'
sobrenome = 'Jolie'
email = 'angelina@gmail.com'
senha = '1235698'

user = Usuario(nome, sobrenome, email, senha)
print(user) # Endereço de memoria
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__volgem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi')



class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O Cliente é {self.__cliente._Cliente__nome}')

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha



cli1 = Cliente('Angelina', '123.415.458.78')

cc = ContaCorrente(5000, 10000, cli1)

cc.mostra_cliente()

cc._ContaCorrente__cliente.diz()


