class Cachorro():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def sentar(self):
        print(self.nome.title() + " está sentado. ")


cachorro_1 = Cachorro('toto', 2)
cachorro_1.sentar()
cachorro_2 = Cachorro('flipper', 3)
cachorro_2.sentar()
