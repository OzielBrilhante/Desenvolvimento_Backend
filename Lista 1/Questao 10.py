peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso / (altura**2)

if imc < 18.5:
    print(f"O resultado do imc é: {imc}, você está abaixo do peso")
elif 18.5 <= imc < 25:
    print(f"O resultado do imc é: {imc}, você está com o peso normal")
elif 25 <= imc < 30:
    print(f"O resultado do imc é: {imc}, você está acima do peso")
else:
    print(f"O resultado do imc é: {imc}, você está obeso")