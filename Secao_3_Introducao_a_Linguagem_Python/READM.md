# Seção 3

### Introdução ao Python 
<img height="90em" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" />
          
Utilitário Python para te auxiliar na progração.

**Dif** 👉  Apresenta todos os atributos/propriedades  e funções/métodos disponíveis para determinado
tipo de dado ou variável.

### No terminal do PyCharm.

```
PycharmProjects\guppe> python

>>> dir(print) // Fazendo um exemplo com o print()

['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute
__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne_
_', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__
', '__str__', '__subclasshook__', '__text_signature__']
>>>

```

###  No Pycharm.
```
# Exemplo 1: Como dir() trabalha?

number = [1, 2, 3]
print(dir(number))

print("Valores de retorno do dir() vazio")
print(dir())

```

Saída da função dir().

```
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
Valores de retorno do dir() vazio
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'number']

Process finished with exit code 0
```

**Help** 👉  Apresenta a documentação como utilizar os atributos/propriedades e funções/métodos disponiveis
para determindo tipo de dado ou variável.

O método help() chama o sistema de ajuda Python integrado.

```
Explemplo:

help(print)

help(dir)

```
Saída do método help().
```
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

dir(...)
    dir([object]) -> list of strings
    
    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes
        of its bases.
      for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.
        
        
```
