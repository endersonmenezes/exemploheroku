from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    numero1 = request.args.get('numero1', None)
    numero2 = request.args.get('numero2', None)
    try:
        int(numero1)
    except ValueError:
        return jsonify({'erro': f'Nao é um valor inteiro o valor digitado. ({numero1})'})
    try:
        int(numero2)
    except ValueError:
        return jsonify({'erro': f'Nao é um valor inteiro o valor digitado. ({numero1})'})
    if numero1 and numero2:
        resultado = int(numero1) + int(numero2)
    else:
        resultado = "Envie dois numeros para somar."
    return jsonify({'resultado': resultado})

if __name__ == "__main__":
	app.run(debug=True)