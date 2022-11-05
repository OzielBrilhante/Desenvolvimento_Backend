import requests
import json
from loguru import logger
from deep_translator import GoogleTranslator

def chamar_api():
    # URL para chamada da API de texto em inglês
    url = "https://api.adviceslip.com/advice"

    # CHamada na API de texto.
    resposta = requests.request("GET", url)
    mensagem = json.loads(resposta.text)
    texto = mensagem['slip']['advice']

    # Chamar API do Google Tradutor
    texto_trad = GoogleTranslator(Source='english', target='portuguese').translate(texto)

    return texto, texto_trad

def salvar_tradução(texto, texto_trad):
    try:
        with open('frases.traduzidas.txt', 'a', encoding='utf-8') as f:
            t = texto_trad + ": " + texto + "\n"
            f.write(t)

    except Exception as error:
        logger.exception(error)

for i in range(5):
    texto, texto_traduzido = chamar_api()

    salvar_tradução(texto, texto_traduzido)
