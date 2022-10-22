idade = int(input("Digite sua idade: "))
ingresso = input("ingresso VIP ou PISTA: ")

if idade >= 18 and ingresso.upper().strip() == "VIP":
    print("Pode entrar na festa na areá VIP")
elif idade >= 18 and ingresso.upper().strip() == "PISTA":
    print("Pode entrar na festa na areá PISTA")
else:
    print("Não pode entrar na festa")
