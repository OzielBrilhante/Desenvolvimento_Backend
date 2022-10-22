from random import randint
minha_lista2 = []
i = 0
cont_par = 0
cont_impar = 0

for n in range(10):
    minha_lista2.append(randint(1, 1000))
for i in minha_lista2:
    if (i % 2) == 0:
        cont_par += 1
    else:
        cont_impar += 1

print("Minha lista 2")
print(minha_lista2)
print("Quantidade de numeros pares: ")
print(cont_par)
print("Quantidade de numeros impares: ")
print(cont_impar)