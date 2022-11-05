import requests
import json

API_KEY = '35b465d840cdb4b33df96acdc4eb5e0e'
LAT = -8.05428
LOG = -34.8813 
url = (f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LOG}&appid={API_KEY}")

resposta   = requests.request("GET", url)
objetos    = json.loads(resposta.text)
# dados      = objetos['dados']

for i in objetos:
    print(f"{i} :: {objetos[i]}")
