personagens = ["Rambo", "Jiraya", "Naruto"]
print(personagens)

personagens.remove('Rambo')
print(personagens)

convidado1 = input("Insira um novo convidado: ")
personagens.insert(0, convidado1)
print(personagens)

convidado2 = input("Insira um novo convidado: ")
personagens.insert(2, convidado2)
print(personagens)

convidado3 = input("Insira um novo convidado: ")
personagens.insert(len(personagens), convidado3)
print(personagens)