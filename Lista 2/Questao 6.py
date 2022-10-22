"""
Faça um algoritmo para ler dois vetores V1 e V2 de 15 números cada.
Calcular e escrever a quantidade de vezes que V1 e V2 possuem os mesmos números e nas mesmas posições.

"""
v1 = []
v2 = []
v_igual = []
posicao = []
contador = 0

for i in range(14):
    v1.append(float(input("Digite um número para o vetor 1: ")))
print(" ")
for i in range(14):
    v2.append(float(input("Digite um número para o vetor 2: ")))

for i in range(14):
    if v1[i] == v2[i]:
        v_igual.append(v1[i])
        posicao.append(i)
        contador += 1

print(f"\nOs numeros presentes nas duas listas são: {v_igual}\n"
      f"nas posições: {posicao}, e a quantidade de numeros iguais: {contador}")


