from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/api", methods=["POST"])
def procesar_datos():
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "No se recibieron datos"}), 400

    if datos.get("valor", 0) > 50:
        resultado = 1
    else:
        resultado = 0

    return jsonify({"resultado": resultado}), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003, debug=True)
