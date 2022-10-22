def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1/n2

while True:
    controle = int(input("Digite a opçãp desejada:\n"
                                "1 - Somar\n"
                                "2 - Subtrair\n"
                                "3 - Multiplicar\n"
                                "4 - Dividir\n"
                                "0 - Sair\n"
                                "Digite a opçãp desejada: "))
    if controle != 0:
        numero1 = int(input("Digite o primeiro numero: "))
        numero2 = int(input("Digite o segundo numero: "))

        match controle:
            case 1:
                print(somar(numero1, numero2))
            case 2:
                print(subtrair(numero1, numero2))
            case 3:
                print(multiplicar(numero1, numero2))
            case 4:
                print(dividir(numero1, numero2))

        print(' ')
    else:
        break


