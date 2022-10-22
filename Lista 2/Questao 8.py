"""
Ler uma matriz D 5 x 5 (considere que não serão informados valores duplicados). A seguir, leia um
número X e escreva uma mensagem indicando se o valor de X existe ou NÃO na matriz.

"""
matriz = []
contador = 0
linha1 = []
coluna1 = []
for linha in range(5):
    lista_auxiliar = []

    for coluna in range(5):
        lista_auxiliar.append(int(input("Informe um número para preencher uma matriz 5x5: ")))
    matriz.append(lista_auxiliar)

x = int(input("Informe um número x a ser encontrado na matriz: "))

for m in matriz:
    print(m)
for linha in range(5):
    for coluna in range(5):
        if x == matriz[linha][coluna]:
            contador += 1
            linha1.append(linha)
            coluna1.append(coluna)

if contador > 0:
    print(f"\nO número {x} foi encontrado na matriz! Na linha {linha1} e coluna {coluna1}")
else:
    print(f"\nO número {x} não foi encontrado na matriz!")