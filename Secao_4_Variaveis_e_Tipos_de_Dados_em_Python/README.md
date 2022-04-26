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
    está limitado so bloco onde foi declarada. 
