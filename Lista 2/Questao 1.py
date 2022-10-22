"""
Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol
e armazene os nomes lidos em um vetor (lista). Após isto,
o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e
depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos
anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

"""
i = 0
x = 0
achei = 0
posicao = 0
lista = [str]

for x in range(1, 11):
    lista.append(input("Informe o nome do clube de futebol: "))
nome_clube = input("Digite o nome de um clube, e veja encontra na lista de clubles armazenada: ")
for i in range(1, 11):
    if lista[i].lower().strip() == nome_clube.lower().strip():
        achei += 1
        posicao = i
    else:
        achei += 0
if achei == 1:
    print(f"Achei o nome na lista na posição: {posicao}!!")
else:
    print("Não Achei!!")


