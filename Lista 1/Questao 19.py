cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
x = True
while x:
    num = int(input("Insira um valor: "))
    if num < 0:
        x = False
    if num >= 0 and num <=25:
        cont1 += 1
    elif num >= 26 and num <=50:
        cont2 += 1
    elif num >= 51 and num <=75:
        cont3 += 1
    elif num >= 76 and num <=100:
        cont4 += 1

print(f"A quantidade de números entre [0-25] é: {cont1}")
print(f"A quantidade de números entre [26-50] é: {cont2}")
print(f"A quantidade de números entre [51-75] é: {cont3}")
print(f"A quantidade de números entre [76-100] é: {cont4}")