# Criando uma lista de nomes
nomes = ["Ademir", "Leonardo", "Carina", "Laíse"]
print(nomes)
print(type(nomes))
print(nomes[3])
print(nomes[(len(nomes)-1)])

# Alterando um objeto da lista
frutas = ["pêra", "uva", "maçã", "kiwi"]
frutas[1] = "abacate"
print(frutas)

# Inserindo um objeto na posição desejada
frutas.insert(2, "morango")
print(frutas)
frutas.insert(100, "abacaxi")
print(frutas)

# Deletando um objeto pelo index
del frutas[0]
print(frutas)

# Pesquisando a posição do objeto
index_frutas = frutas.index("kiwi")
print(f"A posição do \"kiwi\" é: {index_frutas}")
# Deletando o index
del frutas[index_frutas]
print(frutas)

# Método remove
frutas.remove("morango")
print(frutas)

# Método do Pop
frutas = ["pêra", "uva", "maçã", "kiwi"]
print(frutas)
indice = frutas.index("uva")
pop_fruta = frutas.pop(indice)
print(frutas)
print(f"Você tirou {pop_fruta} da sua sacola de frutas")


