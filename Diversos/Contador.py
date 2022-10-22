contador = 0

varA = float(input("Digite um valor A inteiro: "))
if varA > 10:
    contador += 1
varB = float(input("Digite um valor B inteiro: "))
if varB > 10:
    contador += 1
varC = float(input("Digite um valor C inteiro: "))
if varC > 10:
    contador += 1
varD = float(input("Digite um valor D inteiro: "))
if varD > 10:
    contador += 1
varE = float(input("Digite um valor E inteiro: "))
if varE > 10:
    contador += 1

print(f"A quantidade de números maiores que 10 são: {contador}")
