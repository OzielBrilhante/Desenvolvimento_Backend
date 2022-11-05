import requests
import json
from deep_translator import GoogleTranslator


# URL para chamada da API de texto em inglês
url = "https://api.adviceslip.com/advice"

# CHamada na API de texto.
resposta = requests.request("GET", url)
mensagem = json.loads(resposta.text)
texto = mensagem['slip']['advice']

#for i in mensagem.keys(): não precisa usar pq só aparece 1 por vez
#print(mensagem['slip']['advice']) #o slip é a chave "mae" e o advice a chave da frase

# Chamar API do Google Tradutor
texto_trad = GoogleTranslator(Source='english', target='portuguese').translate(texto)

print(texto)
print(texto_trad)