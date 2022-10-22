contador = 0

for x in range(1000, 2001):

    if (x % 11) == 5:
        contador = contador + 1
        print(f"O numero {x} tem resto 5.")

print(f"{contador} números que foram divididos por 11 e tiveram resto 5")
