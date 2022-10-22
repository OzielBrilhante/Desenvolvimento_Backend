entrada = int(input("Entre com um numero inteiro: "))

if entrada == 0:
    print(f"O numero {entrada} é neutro")

elif entrada < 0:
    print(f"O numero {entrada} é negativo")

else:
    print(f"O numero {entrada} é positivo")

"""entrada = int(input("Entre com um numero inteiro: "))

if entrada > 0:
    print(f"O numero {entrada} é positivo")
elif entrada == 0:
    print("Digite outro numero")
    entrada = int(input("Entre com outro numero inteiro: "))
    if entrada > 0:
        print(f"O numero {entrada} é positivo")
    else:
        print(f"O numero {entrada} é negativo")
else:
    print(f"O numero {entrada} é negativo")
"""