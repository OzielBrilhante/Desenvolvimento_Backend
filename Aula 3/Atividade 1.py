filename = "Livros/the_prince.txt"

with open(filename, 'r', encoding="utf-8") as f:
    conteudo = f.read()

quantidade_palavra = conteudo.split()
print(len(quantidade_palavra))