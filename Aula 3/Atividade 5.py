import os
from loguru import logger

def contador_palavras(filename):
    try:

        with open(filename, 'r', encoding="utf-8") as file_object:
            conteudo = file_object.read()
        palavras = conteudo.split()
        return len(palavras)

    except FileNotFoundError as error:
        logger.error(error)
    except Exception as error:
        logger.error(error)


def guardar_info(titulo, quant_palavras, quant_bytes):

    info = f"" \
           f"Titulo: {titulo}; " \
           f"Qtd Palavras: {quant_palavras}; " \
           f"Qtd MB: {quant_bytes}\n"
    try:

        with open("database.txt", "a", encoding="utf-8") as file_object:
            file_object.write(info)

    except (FileNotFoundError, Exception) as error:
        logger.error(error)



def ler_database():

    try:

        with open("database.txt", "r", encoding="utf-8") as file_object:
            for linha in file_object:
                print(linha.rstrip())

    except (FileNotFoundError, Exception) as error:
        logger.error(error)

opcao = 10

while True:


    try:
        opcao = int(input(
            "1 - The Prince\n"
            "2 - Princess of Mars\n"
            "3 - A Little Princess\n"
            "9 - Ler Database\n"
            "0 - Sair\n"
            "Informe o código do livro: "
        ))

    except Exception as error:
        logger.error(error)

    if opcao == 1:
        try:
            filename = 'Livros/the_prince.txt'
            print(f"O livro tem:\n{contador_palavras(filename)}")
            guardar_info(
                "The Prince",
                contador_palavras(filename),
                (os.path.getsize(filename)/1000000)
            )
        except (FileNotFoundError, Exception) as error:
            logger.error(error)

    elif opcao == 2:
        try:
            print(contador_palavras("Livros/princess_of_mars.txt"))
            guardar_info(
                "princess_of_mars",
                contador_palavras('Livros/princess_of_mars.txt'),
                (os.path.getsize('Livros/princess_of_mars.txt') / 1000000)
            )
        except (FileNotFoundError, Exception) as error:
            logger.error(error)

    elif opcao == 3:
        try:
            print(contador_palavras("Livros/little_princess.txt"))
            guardar_info(
                "little_princess",
                contador_palavras('Livros/little_princess.txt'),
                (os.path.getsize('Livros/little_princess.txt') / 1000000)
            )
        except (FileNotFoundError, Exception) as error:
            logger.error(error)

    elif opcao == 9:

        ler_database()

    elif opcao == 0:
        break