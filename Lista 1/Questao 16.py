soma: int = 0
y = 0
for x in range(1, 501):
    y = x % 2
    if y == 1:
        if x % 3 == 0:
            soma = soma + x
            print(x)
print(soma)