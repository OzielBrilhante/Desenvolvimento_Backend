altura_menor = 0
altura_maior = 0
altura = []

for x in range(0, 5):
    altura.append(float(input("Informe a altura: ")))
    if x == 0:
        altura_maior = altura_menor = altura[x]
    else:
        if altura[x] > altura_maior:
            altura_maior = altura[x]
        if altura[x] < altura_menor:
            altura_menor = altura[x]

print(f"A menor altura registrada foi: {altura_menor:0.2f}")
print(f"A maior altura registrada foi: {altura_maior}")
