qtd_par = 0
qtd_impar = 0
soma = 0
qtd_num = 0
x = True

while x:
    num = int(input("Insira um valor: "))
    if num == 0:
        x = False

    if (num % 2 == 0) and num != 0:
        qtd_par += 1
    elif (num % 2 == 1) and num != 0:
        qtd_impar += 1

    soma += num
    if num != 0:
        qtd_num += 1

media = soma/qtd_num

print(f"\nA media dos valores inseridos é: {media}")
print(f"A quantidade de numeros pares é: {qtd_par}")
print(f"A quantidade de numeros impares é: {qtd_impar}")
