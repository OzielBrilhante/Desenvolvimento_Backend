"""
11. Construa uma matriz 5 x 5 com valores randômicos. A matriz não pode ter valores repetidos. Depois
apresente:
a. o resultado da soma de todos os valores da matriz;
b. o resultado da soma dos valores da diagonal principal;
c. o resultado da soma dos valores da diagonal secundária

"""
from random import randint
matriz = []
somaTotal = 0
somaDiaPrincipal = 0
somaDiaSecundaria = 0

for linha in range(2):
    lista_auxiliar = []

    for coluna in range(2):
        lista_auxiliar.append(randint(1, 100))
    matriz.append(lista_auxiliar)
print("\nResultado da matriz aleatória: ")
for m in matriz:
    print(m)

for i in range(2):
    for j in range(2):
        somaTotal += matriz[i][j]
print('\nsomaTotal: ',somaTotal)

#soma diagonal principal

for i in range(2):
    for j in range(2):
        if(i == j):
           somaDiaPrincipal += matriz[i][j]
print('somaDiaPrincipal: ', somaDiaPrincipal)

#soma diagonal secundária

for i in range(2):
    for j in range(2):
        if((i+j) == 1):
            somaDiaSecundaria += matriz[i][j]
print('somaDiaSecundaria: ', somaDiaSecundaria)