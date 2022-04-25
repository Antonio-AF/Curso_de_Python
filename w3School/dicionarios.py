thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964

}

print(thisdict)

print(thisdict["model"])
print(thisdict["year"])

# --> Usando o metodo get() para obter a chave.
print(thisdict.get("year"))

# --> Mudar valores das chaves.

thisdict["year"] = 2020
print(thisdict)

# --> Percorrer um dicionário com o for

for x in thisdict:
    print(x)

# --> Percorrendo um dicionário e alterando o valor de uma chave.
for x in thisdict:
    if x == "year":
        thisdict[x] = 2021
    else:
        print(x)
    print(thisdict)

# --> Retornando os valores das chaves com o método values()

for x in thisdict.values():
    print(x)

# -->  Laço de repetição while

i = 1
while i < 6:
    print(i)
    i += 1
