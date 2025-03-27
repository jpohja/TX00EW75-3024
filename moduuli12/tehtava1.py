import requests
import json

osoite = f"https://api.chucknorris.io/jokes/random"

vitsi = requests.get(osoite).json()

json.dumps(vitsi, indent=2)

print(vitsi["value"])