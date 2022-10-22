"""
Faça um algoritmo para ler um vetor de 30 números.
Após isto, ler mais um número qualquer,
calcular e escrever quantas vezes esse número aparece no vetor.

for i in range(5):
    vetor.append(float(input("Digite um número: ")))

x = float(input("Digite um valor a ser encontrado na lista: "))

for i in range(5):
    if vetor[i] == x:
        posicao.append(i)
        contador += 1

print(f"\nA quantidade de vezes que o número escolhido aparece são: {contador}\n"
      f"nas posições: {posicao}")

"""
vetor = []
posicao = []
contador = 0

for i in range(5):
    vetor.append(float(input("Digite um número: ")))

x = float(input("Digite um valor a ser encontrado na lista: "))

for indice, valor in enumerate(vetor):
    if x == valor:
        posicao.append(indice)

print(f"\nA quantidade de vezes que o número escolhido aparece são: {vetor.count(x)}\n"
      f"nas posições: {posicao}")
