import fontstyle

glossario = {'algoritmo':"\tUma sequência finita de ações executáveis que visam obter uma solução para um determinado tipo de problema.",
             'webscraping':"\tRaspagem de rede – é uma técnica de coleta de dados de plataformas online, como sites, redes sociais etc",
             'python':"\tUma linguagem de programação de alto nível — ou High Level Language —, dinâmica, interpretada, modular, multiplataforma e orientada a objetos",
             'googlecolab':"\tUm serviço de nuvem gratuito hospedado pelo próprio Google para incentivar a pesquisa de Aprendizado de Máquina e Inteligência Artificial.",
             'visualcode':"\tUm editor de código de código aberto desenvolvido pela Microsoft."}


while True:
    import fontstyle
    import time

    print("\t\nListamos 5 palavras e seus significados.\n"
          "1 - Algoritmo\n"
          "2 - Webscraping\n"
          "3 - Python\n"
          "4 - Google Colab\n"
          "5 - Visual Studio Code"
          )
    numero = int(input(fontstyle.apply("Informe o número da respectiva palavra para conhecer sua definição: ", 'bold/green')))

    if numero == 1:
        print(fontstyle.apply("\nALgoritmo é: ", 'bold/blue'))
        print(fontstyle.apply(glossario['algoritmo'], 'italic'))
    elif numero == 2:
        print(fontstyle.apply("\nWebscraping é: ", 'bold/blue'))
        print(fontstyle.apply(glossario['webscraping'], 'italic'))
    elif numero == 3:
        print(fontstyle.apply("\nPython é: ", 'bold/blue'))
        print(fontstyle.apply(glossario['python'], 'italic'))
    elif numero == 4:
        print(fontstyle.apply("\nGoogle Colab é: ", 'bold/blue'))
        print(fontstyle.apply(glossario['googlecolab'], 'italic'))
    elif numero == 5:
        print(fontstyle.apply("\nVisual Studio Code é: ", 'bold/blue'))
        print(fontstyle.apply(glossario['visualcode'], 'italic'))
    elif numero < 1 or numero >5:
        break
    else:
        break;

    time.sleep(7)