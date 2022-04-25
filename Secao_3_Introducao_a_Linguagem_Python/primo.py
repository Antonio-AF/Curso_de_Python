n = 10

mult = 0 # Contador

for count in range(2, n):
    if(n % count == 0):
        print('Múltiplo de', count)
        mult = mult + 1

        if(mult == 0):
            print('É primo')

else:
    print('Tem',mult, 'Múltilo de 2 a',n)