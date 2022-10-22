
print("Olá, Prof", nome_completo.title())

print("-------------Tabulação-----------")

print("Harry Potter")
print("\tHarry Potter")

print("-------------Quebra de Linha-----------")

print("Harry\nHermione\nRonnie")

print("-------------Removendo Espaços-----------")

professor = " Dumbledore "

print(professor)
print(professor.lstrip()) #remove lado esquerdo
print(professor.rstrip()) #remove lado direito
print(professor.strip())  #remove os dois lados

print("-------------Formatação de Strings-----------")

ano = 2022
print(f"Este ano de {ano} será maravilhoso")
pi = 3.14466699999
print("O valor de pi é: {:0.2f}".format(pi))
altura = 1.77490
print(f"A altura é: {altura:0.2f}")

print("-------------Formatação de Strings Antigas-----------")

ano = 2022
print("Este ano de %d será maravilhoso" % ano)
nome = "Oziel"
print("Meu nome é: %s" % nome)
altura = 1.77490
print("A altura é: %0.2f" % altura)