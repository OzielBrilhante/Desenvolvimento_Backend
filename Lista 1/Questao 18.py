i = 0
qtd_positivo = 0
qtd_negativo = 0
soma = 0
num_var = 0

quantity = int(input("Defina a quantidade de numeros: "))
num_var = quantity

while i < quantity:

    num = int(input("Digite o numero a ser lido: "))

    soma += num
    if num > 0:
        qtd_positivo += 1
    if num < 0:
        qtd_negativo += 1

    quantity -= 1

media = soma/num_var
total = qtd_positivo + qtd_negativo
per_pos = ((qtd_positivo/total)*100)
per_neg = (qtd_negativo/total)*100

print(f"A media dos valores inseridos é: {media}")
print(f"A quantidade de numeros positivos é: {qtd_positivo}")
print(f"A quantidade de numeros negativos é: {qtd_negativo}")
print(f"A porcentagem de numeros positivos é: {per_pos}%")
print(f"A porcentagem de numeros negativos é: {per_neg}%")



