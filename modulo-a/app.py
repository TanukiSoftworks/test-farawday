import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

MODULO_B_URL = "http://modulo-b:8003/api"


@app.route("/enviar", methods=["POST", "GET"])
def enviar_datos():
    if request.method == "GET":
        datos_a_enviar = {"valor": 75, "nombre": "test", "timestamp": "2026-01-14"}
    else:
        datos_a_enviar = request.get_json()

    # para debugging
    print(f"Enviando datos al Modulo B: {datos_a_enviar}")

    try:
        response = requests.post(
            MODULO_B_URL,
            json=datos_a_enviar,
            timeout=5,  # timeout de 5 segundos
        )

        response.raise_for_status()

        resultado = response.json()

        print(f"Respuesta del Modulo B: {resultado}")

        return jsonify(
            {
                "status": "success",
                "datos_enviados": datos_a_enviar,
                "respuesta_modulo_b": resultado,
                "mensaje": f"El Modulo B retorno: {resultado.get('resultado')}",
            }
        )

    except requests.exceptions.ConnectionError:
        return jsonify(
            {"status": "error", "mensaje": "No se pudo conectar con el Modulo B"}
        ), 503

    except requests.exceptions.Timeout:
        return jsonify(
            {"status": "error", "mensaje": "Timeout al conectar con el Modulo B"}
        ), 504

    except Exception as e:
        return jsonify({"status": "error", "mensaje": f"Error: {str(e)}"}), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "modulo": "A"})


# enviar datos personalizados
@app.route("/enviar-custom", methods=["POST"])
def enviar_custom():
    """
    USO:
    curl -X POST http://localhost:8001/enviar-custom \
      -H "Content-Type: application/json" \
      -d '{"valor": x}'
      (siendo x un número)
    """
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "No se enviaron datos"}), 400

    try:
        response = requests.post(MODULO_B_URL, json=datos, timeout=5)
        response.raise_for_status()
        resultado = response.json()

        return jsonify({"status": "success", "resultado_modulo_b": resultado})

    except Exception as e:
        return jsonify({"status": "error", "mensaje": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
