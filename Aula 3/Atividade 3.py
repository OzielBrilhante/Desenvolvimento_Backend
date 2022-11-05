import os

def contador_palavras(filename):
    with open(filename, 'r', encoding="utf-8") as file_object:
        conteudo = file_object.read()
    palavras = conteudo.split()
    return len(palavras)


def guardar_info(titulo, quant_palavras, quant_bytes):

    info = f"" \
           f"Titulo: {titulo};" \
           f"Qtd Palavras: {quant_palavras};" \
           f"Qtd MegaBytes: {quant_bytes}\n"

    with open("database.txt", "a", encoding="utf-8") as file_object:
        file_object.write(info)


def ler_database():

    with open("database.txt", "r", encoding="utf-8") as file_object:
        for linha in file_object:
            print(linha.rstrip())


while True:
    opcao = int(input(
        "1 - The Prince\n"
        "2 - Princess of Mars\n"
        "3 - A Little Princess\n"
        "9 - Ler Database\n"
        "0 - Sair\n"
        "Informe o código do livro: "
    ))

    if opcao == 1:
        print(f"O livro tem:\n{contador_palavras('Livros/the_prince.txt')}")
        guardar_info(
            "the_prince",
            contador_palavras('Livros/the_prince.txt'),
            (os.path.getsize('Livros/the_prince.txt')/1000000)
        )

    elif opcao == 2:
        print(contador_palavras("Livros/princess_of_mars.txt"))
        guardar_info(
            "princess_of_mars",
            contador_palavras('Livros/princess_of_mars.txt'),
            (os.path.getsize('Livros/princess_of_mars.txt')/1000000)
        )

    elif opcao == 3:
        print(contador_palavras("Livros/little_princess.txt"))
        guardar_info(
            "little_princess",
            contador_palavras('Livros/little_princess.txt'),
            (os.path.getsize('Livros/little_princess.txt')/1000000)
        )

    elif opcao == 9:
        ler_database()

    elif opcao == 0:
        break
