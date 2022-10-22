import fontstyle

mensagemPessoal = "gosto de Programar em python"

print(mensagemPessoal.upper())
print(mensagemPessoal.lower())
print(mensagemPessoal.title())

print(" ")
autor = "Albert Einstein"
frase = "\"Algo só é impossível até que alguém duvide e resolva provar o contrário\""

citacao = autor + ": " + frase
print(fontstyle.apply(citacao, 'italic/bold'))
