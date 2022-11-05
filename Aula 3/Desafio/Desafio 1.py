import requests
import json

API_KEY = '35b465d840cdb4b33df96acdc4eb5e0e'
LAT = []
LOG = []

url = []
numero_cidade = int(input("Informe o numero de cidades a serem pesquisadas: "))

for i in range(numero_cidade):
    LAT.append(float(input("Informe a latitude da cidade: ")))
    LOG.append(float(input("Informe a longitude da cidade: ")))

for i in range(numero_cidade):
    url[i] = (f"https://api.openweathermap.org/data/2.5/weather?lat={LAT[i]}&lon={LOG[i]}&appid={API_KEY}")

for i in range(numero_cidade):
    resposta = requests.request("GET", url[i])
    objetos = json.loads(resposta.text)
    # dados      = objetos['dados']
for i in objetos:
    print(f"{i} :: {objetos[i]}")
