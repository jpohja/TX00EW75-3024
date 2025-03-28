import requests
import json

paikkakunta = input("Anna paikkakunnan nimi: ")

#muuttuja api_avain place holderina

saatiedot = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_avain}"

saatiedot_haku = requests.get(saatiedot).json()
json.dumps(saatiedot_haku, indent=2)

#hae sanakirjasta stringillä ja listasta indeksillä

print(f"Säätila: {saatiedot_haku["weather"][0]["description"]}")

lampotila = round(saatiedot_haku["main"]["temp"] - 273.15)

print(f"Lämpötila (celsius): {lampotila}")

