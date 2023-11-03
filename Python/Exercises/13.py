from flask import Flask, jsonify

app = Flask(__name__)


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


@app.route('/prime_number/<int:number>')
def check_prime(number):
    return jsonify(Number=number, isPrime=is_prime(number))


app.run()

'''Tehtävän osa 2: Oli vakavia teknisiä ongelmia, joiden vuoksi en saanut paikallista backendiä toimimaan, pahoittelen.'''



