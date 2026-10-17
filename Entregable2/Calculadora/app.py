from uuid import uuid4

from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

import calculadora

app = Flask(__name__)
conexiones = {}

@app.post("/api/v1/conexiones")
def abrir_conexion():
    conexion_id = str(uuid4())
    instancia = calculadora.calculadora()
    conexiones[conexion_id] = instancia
    return jsonify({"conexion_id": conexion_id, "result": instancia.get_result()}), 201


@app.post("/api/v1/conexiones/<conexion_id>/operar")
def operar(conexion_id):
    instancia = conexiones.get(conexion_id)
    if instancia is None:
        return jsonify({"error": "Conexión no encontrada"}), 404

    mensaje = request.get_json().get("mensaje")
    resultado = instancia.operar(mensaje)
    return jsonify({"result": resultado}), 200


@app.get("/api/v1/conexiones/<conexion_id>/resultado")
def obtener_resultado(conexion_id):
    instancia = conexiones.get(conexion_id)
    if instancia is None:
        return jsonify({"error": "Conexión no encontrada"}), 404
    return jsonify({"result": instancia.get_result()}), 200


@app.post("/api/v1/conexiones/<conexion_id>/reset")
def resetear(conexion_id):
    instancia = conexiones.get(conexion_id)
    if instancia is None:
        return jsonify({"error": "Conexión no encontrada"}), 404
    return jsonify({"message": instancia.reset(), "result": instancia.get_result()}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
