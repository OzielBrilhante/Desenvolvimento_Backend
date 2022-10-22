import math


A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

delta = pow(B,2) - (4*A*C)
if delta > 0:
    x1 = (-B + math.sqrt(delta))/2*A
    x2 = (-B - math.sqrt(delta))/2*A

    print(f"O valor de delta é : {delta}")
    print(f"O valor da raíz x1 é : {x1:.2f}")
    print(f"O valor da raíz x2 é : {x2:.2f}")
else:
    print("Reduza os valores de A e C")
