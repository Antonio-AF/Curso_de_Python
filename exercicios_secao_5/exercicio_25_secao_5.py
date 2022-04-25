"""
    25 - Calcule as raízes da equaçõa do 2º grau;

                Lembrando que:

                x = -b +- Raiz quadrada de Delta/ 2.a

                onde;

                Delta = b² - 4.a.c

        E ax² + bx + c = 0 representa uma equação do 2º grau.


        A variavel a tem que ser diferente de zero. Coso seja igual, imprima a mensagem  Não
        é equaçao de segundo grau.


        * Se Delta < 0, não existe raiz real. Imprima a mensagem "Não existe raiz"
        * Se Delta = 0, existe uma raiz real, Imprima a raiz e a mensagem Raiz única
        * Se Delta >= 0, imprima as duas raízes reais.

"""

a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
c = int(input("Digite um valor para c: "))

delta = b**2 - 4*a*c

raiz_delta = delta**0.5

x_mais = (-b + raiz_delta)/2*a
x_menos = (-b - raiz_delta)/2*a

if delta < 0:
    print("Não existe raiz")
elif delta == 0:
    print(f"Existe somente uma raiz e ela é {x_mais}")
elif delta >= 0:
    print(f'As raizes sã0 ({x_mais}, {x_menos})')
else:
    print("Erro digite valores validos!!!")







