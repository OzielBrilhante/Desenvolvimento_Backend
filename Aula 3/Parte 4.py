# Caminho e nome do arquivo guardado na variável

filename = "path/arquivo_escrita.txt"

# Abrindo um arquivo para leitura
with open(filename, 'a') as file_object:
    file_object.write("Eu amo Python!\n")
    file_object.write("Eu amo ministrar aula!\n")
