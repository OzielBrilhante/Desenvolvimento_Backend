"""altura = float(input("Digite sua altura: "))
sexo = input("informe seu sexo M ou F: ")

if sexo.lower().strip() == "m":
    print((72.7 * altura) - 58)
elif sexo.lower().strip() == "f":
     print((62.1 * altura) - 44.7)"""

ano = int(input("Digite seu ano de nascimento: "))

idade = 2022 - ano

if idade >= 16:
    print("Já tem idade para votar")
    if idade >= 18:
         print("Já tem idade para carteira de habilitação")
    else:
         print("Não tem idade para tirar carteira de habilitação")
else:
    print(" Menor de 16 anos")
