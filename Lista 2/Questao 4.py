"""
Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável X. Armazenar
em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após, imprimir o
vetor M.

"""
vetor_a = []
vetor_m = []
x = 0
i = 0

for i in range(9):
    vetor_a.append(float(input("Digite um número: ")))

x = float(input("Digite um valor a ser multiplicado: "))

for i in range(9):
    vetor_m.append(vetor_a[i] * x)

print(f"O vetor M é: {vetor_m}")

