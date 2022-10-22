
def contador_palavras(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        conteudo = f.read()
    palavras = conteudo.split()
    return len(palavras)

while True:

    opcao = int(input(
        "1 - The Prince\n"
        "2 - Princess of Mars\n"
        "3 - A Little Princess\n"
        "0 - Sair\n"
        "Informe o código do livro: "))
    if opcao == 1:
        print(f"O livro tem: {contador_palavras('Livros/the_prince.txt')}\n")
    elif opcao == 2:
        print(f"O livro tem: {contador_palavras('Livros/princess_of_mars.txt')}\n")
    elif opcao == 3:
        print(f"O livro tem: {contador_palavras('Livros/little_princess.txt')}\n")
    else:
        break

