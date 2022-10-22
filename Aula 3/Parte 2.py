# Caminho e nome do arquivo guardado na variável

filename = "path/arquivo.txt"

# Abrindo um arquivo para leitura
with open(filename, 'r', encoding="utf-8") as file_object:

    # Criando uma "repetição" para ler por linhas
    for linha in file_object:

        # Imprimmindo a linha lida
        print(linha)