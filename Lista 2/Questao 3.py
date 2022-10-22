"""
Ler um vetor Q de 20 posições (aceitar somente números positivos).
Escrever a seguir: o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;

"""

vetor = []
maior_valor = 0
menor_valor = 0
posicao_maior = 0
posicao_menor = 0

for i in range(0, 4):
    vetor.append(float(input("Informe um numero positivo: ")))
    if vetor[i] >= 0:
           if i == 0:
              maior_valor = menor_valor = vetor[i]
           else:
                if vetor[i] > maior_valor:
                   maior_valor = vetor[i]
                   posicao_maior = i
                if vetor[i] < menor_valor:
                   menor_valor = vetor[i]
                   posicao_menor = i

print(f"\nO valor do maior número é: {maior_valor}, e sua posição na lista é: {posicao_maior}\n"
      f"O valor do menor numero é: {menor_valor}, e sua posição na lista é: {posicao_menor}")

