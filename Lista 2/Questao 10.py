"""
10. Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
a. Imprima o resultado da soma de todos os valores da matriz no terminal;
b. E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;

"""
from random import randint

matriz = []
matriz_b = []
valor_mult = 0
soma = 0
for linha in range(10):
    lista_auxiliar = []

    for coluna in range(10):
        lista_auxiliar.append(randint(1, 100))
    matriz.append(lista_auxiliar)
print(f"\nResultado da matriz aleatoria: ")

for m in matriz:
    print(m)

for linha in matriz:
    for coluna in linha:
        soma += coluna
print(f"\nResultado da soma dos elementos da matriz: {soma} ")

for linha in range(10):
    lista_auxiliar1 = []

    for coluna in range(10):
        lista_auxiliar1.append(matriz[linha][coluna]*3)
    matriz_b.append(lista_auxiliar1)