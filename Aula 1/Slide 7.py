"""
maças = int(input("Digite a quantidade de maças a serem compradas: "))

custo_total = 0

if maças >= 12:
    custo_total = maças * 1.24
else:
    custo_total = maças * 1.37

print(f"O custo total será: {custo_total:.2f}")
"""

deposito = float(input("Digite o valor do deposito: "))
saque = float(input("Digite o valor do saque: "))

saldo = deposito - saque

print(saldo)

if saldo < 0:

    print(f"O valor para quitar o débito será: {saldo*-1}")
