"""

Crie um vetor N que seja resultado da soma dos itens de outros dois vetores A e B. Exemplo: A[0] +
B[0] deverá ser salva em N[0].

"""
vetor_a = [1, 7, 3, 5]
vetor_b = [2, 4, 9, 6]
vetor_n = []

for i in range(len(vetor_a)):
    vetor_n.append(vetor_a[i] + vetor_b[i])
print(f"Vetor N é: {vetor_n}")

