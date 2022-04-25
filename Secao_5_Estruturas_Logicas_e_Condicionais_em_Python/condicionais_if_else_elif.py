"""
Estruturas Condicionais

if (Se), else, elif.


# Estrutura condicional if, em C.

if(idade < 18){
    printf("Menor de idade");
}
"""

idade = int(input('Qual a sua idade?'))

if idade < 12:
    print('Você é criança:')

elif (idade >= 12) and (idade <= 18):
    print('Você é adolecente:')

else:
    print("Maior de idade:")
