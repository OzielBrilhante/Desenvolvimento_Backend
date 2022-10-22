"""

import math

x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

distancia = math.sqrt(((x2-x1)**2)+((y2-y1)**2))

print(f"O valor da distância é: {distancia}")

r = float(input("Digite o valor do Raio: "))
PI = 3.14

volume = (4*PI*(r**3))/3

print(f"O valor do volume é: {volume}")

"""

qtd_max = int(input("Digite a quantidade máxima do estoque: "))
qtd_min = int(input("Digite a quantidade miníma do estoque: "))
qtd_real = int(input("Digite a quantidade real do estoque: "))

media = qtd_max/qtd_min

if qtd_real < media:
   print(f"A empresa tem necessidade de reabaster o estoque em pelo menos {media - qtd_real} unidades")
elif qtd_real > media:
    print("Não precisa adquirir novos produtos")
else:
    print("Em breve necessitará adquirir novos produtos")

