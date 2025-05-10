from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<teksti>')
def summa(teksti):
    is_prime = False
    luku = int(teksti)
    try:
        for i in range(2, luku):
            if luku % i == 0:
                vastaus = {
                    "Number": luku, "isPrime": is_prime
                }
                return vastaus
        if luku != 0:
            is_prime = True

        vastaus = {
            "Number": luku, "isPrime": is_prime
        }
        return vastaus


    except ValueError:
        return("Syötetyn arvon täytyy olla kokonaisluku!")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


