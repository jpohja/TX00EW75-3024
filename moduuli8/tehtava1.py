import mysql.connector

def hae_lentoaseman_nimi(koodi):
    sql = f"SELECT airport.name, municipality FROM airport WHERE ident = '{koodi}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokentän nimi on {rivi[0]} ja kunta on {rivi[1]}.")
    else:
        print("Antamallasi koodilla ei löydy lentoasemaa.")

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='jopo',
         password='Aj4Dr1VER1445',
         autocommit=True,
         collation='utf8mb3_general_ci'
         )

lentoaseman_icao_koodi = input("Anna lentoaseman ICAO-koodi: ")
hae_lentoaseman_nimi(lentoaseman_icao_koodi)