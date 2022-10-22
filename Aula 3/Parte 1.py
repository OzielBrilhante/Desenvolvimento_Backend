# Abrindo um arquivo para leitura

with open('path/arquivo.txt', 'r', encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)

# Os dois pontos volta a cada pasta... se tiverem duas pastas seria '../../Aula 2/teste.txt e assim sucessivamente
# e depois acessar o arquivo de leitura da Aula 2

"""
with open('../Aula 2/teste.txt', 'r', encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)
"""


path = "path/"
file = "arquivo.txt"
pathfile = path + file

with open(pathfile, 'r', encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)

