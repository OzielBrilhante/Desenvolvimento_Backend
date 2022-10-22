raio = float(input("Digite o Raio: "))
h = float(input("Digite o altura: "))
PI = 3.14

area_do_cilindro = (PI * (raio**2)) + (2*PI*raio*h)
quantidade_de_litros = area_do_cilindro/3
quantidade_latas = quantidade_de_litros/5
custo = quantidade_latas * 50

print(f"Para pintar o cilindro precisamos de: ")
print(f"{quantidade_latas} latas de tinta.")
print(f"A um custo de R$ {custo:0.2f}.")