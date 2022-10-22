"""
12. Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do
garçom, considerando 10% do valor da conta.

"""


def valor_gorjeta(x):
    valor_conta = (x * 10) / 100
    return valor_conta


conta = float(input("Informe o valor da conta a ser paga: R$ "))

gorjeta = valor_gorjeta(conta)
print(f"O valor da gorjeta será de : R$ {gorjeta}")
