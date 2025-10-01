# Día 32 : Consumir API 

import requests 

url = "https://dragonball-api.com/api/characters?page=1&limit=80"

r = requests.get(url)

if(r.status_code == 200):
    data = r.json()
    personaje = data["items"]
    print(personaje[:5])
else:
    print("Ocurrio un error")