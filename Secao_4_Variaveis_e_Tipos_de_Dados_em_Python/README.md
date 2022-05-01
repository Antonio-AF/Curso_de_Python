## Seção 4

### Variáveis e Tipos de Dados em Python

Para declarar uma variável em Python faemos:

nom_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos o tipo de dado dela.

Este tipo é inferido ao atribuírmos o valor à mesma.

**Exemplo em C:**
```C
 int numero = 42;
```

**Exemplo em Java;**
```Java
int numero = 42;
```

**Exemplo em Python;**
```Python
numero = 42
```


#### * Variável Global

Em Python, uma variável declarada fora da função ou que seja de escopo global é conhecida como variável global. Isto significa que a variável global pode ser lida e atualizada dentro ou fora da função.
  
1 - Variáveis  Globais;
    - Variáveis globais são reconhecidas em todo o código, ou seja, seu escopo compreende todo o programa.

 - Exemplo de Variável Global!
  
 ```Python 
 x = 10 
 y = 20
 # x e y são variáveis globais.
  
 def soma(x, y):
    return x + y
    
 def mult(x, y):
    return x * y
    
print(soma(x,y))
print(mult(x, y))

```
Retorno:
```sh
-----------------------------------
30
200
-----------------------------------
 ```
2- Variáveis Locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado so ao bloco onde foi declarada. Veja exemplo a seguir:
 
 ```Python
 
 def soma():
    x = 10
    y = 14
    return x + y
    
 print(soma())
 
 
  def mult():
    x = 13
    y = 45
    return x * y
    
print(soma())
print(mult())
  
 ```
 Retorno:
 ```sh
 34
 585
 
 ```
### Tipos Numéricos

Em Python os tipos de dados usados para números se dividem em três tipos:

- Inteiros
- Números de pntos flutuante
- Complexos

#### Tipo Inteiro (int)

Esse tipo representa os números inteiros positivos e negativos.

**Exemplo:**
```Python

num1 = 1
num2 = 3.1415


print(num1 * 2)
print(type(num1))
print(num2)
print(type(num2))

```

Retorno:
```sh
2
A Variável num1 é do tipo:  <class 'int'>

3141500
A Variável num2 é do tipo:  <class 'int'>

```
O intervalo de valor desse tipo é ilimitado e está sujeto apenas à capacidade da mémoria.

#### Tipo Ponto Flutuante (float)

Esses são números reais, que contém casas decimais. Exemplo, comprimento de um lado de um triangulo, peso de um objeto.

**Exemplo**

```Python

num3 = 3.141516 # Constante PI
num4 = 2**0.5 # Raiz quadrada de 2

print(num3)
print("A Variável num3 é do Tipo: ", type(num3))

print(num4)
print("A Variável num4 é do Tipo: ", type(num4))

```
Retorno:
```Sh
Tipo Float ou Ponto Flutuante
3.141516
A Variável num3 é do Tipo:  <class 'float'>
1.4142135623730951
A Variável num4 é do Tipo:  <class 'float'>
```

#### Tipo Decimal

Em Python nos utilizamos float para ponto flutuante, caso seja necessário uma precisão de casas decimais, podemos usar Decimal.

**Exemplo**
```Python

from decimal import Decimal

num1 = Decimal(5/3) # Mais precisão em casas numéricas.
num2 = Decimal(10/3)


print(num1)
print(type(num1))

print(num2)
print(type(num2))

```


