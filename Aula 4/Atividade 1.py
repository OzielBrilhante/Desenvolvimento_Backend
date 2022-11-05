"""
Utilizar o arquivo csv e me mostra o filme com a maior bilheteria
"""
import csv
maior_renda = 0.0
maior_bilheteria = 0
nome_filme, nome_filme_b = '', ''
lista_selecionada = []

with open('filmes.csv', newline='', encoding="utf-8") as f:
    leitor = csv.reader(f)
    for linha in leitor:
       # print(f"Filme: {linha[2]} || Renda: {linha[9]}")

       if linha[9] != "Renda (R$) no ano de exibição":
           # utiliza-se esse if para ele nao fazer uma comparação com o titulo que é uma string, string e um numero da erro!
            if maior_renda < float(linha[9]):
                maior_renda = float(linha[9])
                nome_filme = linha[2]
            if maior_bilheteria < int(float(linha[8])):#transforma em float depois em inteiro, mas funciona se colocar apenas float
                maior_bilheteria = int(float(linha[8]))
                nome_filme_b = linha[2]



print(f"O filme é: {nome_filme} com a renda de R$: {maior_renda}")
print(f"O filme é: {nome_filme_b} com a bilheteria de: {maior_bilheteria}")
print(lista_selecionada)