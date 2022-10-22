# Caminho e nome do arquivo guardado na variável

filename = "path/arquivo2.txt"

# Abrindo um arquivo para leitura
with open(filename, 'r', encoding="utf-8") as file_object:
    conteudo = file_object.readlines()
print(conteudo)
    # Criando uma "repetição" para ler por linhas
for linha in conteudo:
    print(linha.rstrip())
        # Imprimmindo a linha lida
