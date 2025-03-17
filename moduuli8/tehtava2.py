import mysql.connector

def hae_lentoasemien_lukumaara(koodi):
    sql = f"SELECT DISTINCT airport.type as 'Asematyypit', COUNT(*) as 'Asemien määrä' FROM airport, country WHERE airport.iso_country = country.iso_country AND airport.iso_country = '{koodi}' GROUP BY airport.type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Maassa on {rivi[1]} kpl {rivi[0]}.")

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='jopo',
         password='Aj4Dr1VER1445',
         autocommit=True,
         collation='utf8mb3_general_ci'
         )

maakoodi = input("Anna maakoodi: ")
hae_lentoasemien_lukumaara(maakoodi)