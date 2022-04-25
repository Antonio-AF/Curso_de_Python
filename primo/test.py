num=int(input("Digite um numero"))
contador=1
while contador <= num:
    if num%2==1:
        contador=contador+1
        print("primo")
        break
    else:
        print("não primo")
        break

#código 2 :

num=int(input("Digite um numero"))
if num%2==1:
    print("primo")
else:
    print("não primo")