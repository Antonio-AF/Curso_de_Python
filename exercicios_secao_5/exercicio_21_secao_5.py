"""
    21 - Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação
    escolhida. Escreva uma mensagem de erro se a opçõo for inválida.

"""
print(" ")
print("###Escolha a opçõo desejada!###\n"
      "1 - Soma de 2 números.\n"
      "2 - Diferença entre 2 número (maior pelo menor).\n"
      "3 - Produto entre 2 números.\n"
      "4 - Divisão entre 2 números (o denominador não pode ser zero\n")

opcao = int(input('Digite uma das Opções do Menu: '))

if opcao <= 4:

    def menu(opcao):
        if opcao == 1:
            print(soma(num1, num2))
        elif opcao == 2:
            print(subtracao(num1, num2))
        elif opcao == 3:
            print(produto(num1, num2))
        elif opcao == 4:
            print(divisao(num1, num2))

        return 'A opcao digitada foi', opcao


    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo  número: '))


    def soma(num1, num2):
        return "A soma dos numeros é: ",  num1 + num2


    def subtracao(num1, num2):
        if num1 > num2:
            sub = num1 - num2
            print("A subtração é: ", sub)
        else:
            sub = num2 - num1
            print("A subtração é: ", sub)


    def produto(num1, num2):
        return f'A mutiplicação de {num1} por {num2} é: ', num1 * num2


    def divisao(num1, num2):
        if num2 == 0:
            print(f'É impossivel dividir {num1} por 0!!!')
        else:
            div = num1/num2
            print(f'A divisão de {num1} por {num2} é {div}')




    print(menu(opcao))

else:
    print('A opção digitada é inválida, favor digitar uma opção do Menu!!!')
