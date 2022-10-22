from random import randint

controle = 100
minha_lista = []

while controle >= 1:
    minha_lista.append(randint(1, 1000))
    controle = controle - 1
print(minha_lista)

