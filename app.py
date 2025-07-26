from flask import Flask, request, jsonify
import base64
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
    return "Servicio activo", 200

@app.route("/subir_imagen", methods=["POST"])
def subir_imagen():
    if 'imagen' not in request.files:
        return jsonify({"error": "No se encontró el archivo 'imagen'"}), 400

    imagen = request.files['imagen']
    nombre = secure_filename(imagen.filename)
    contenido = imagen.read()
    tipo = imagen.content_type

    base64_data = base64.b64encode(contenido).decode('utf-8')

    return jsonify({
        "nombre": nombre,
        "tipo": tipo,
        "base64": base64_data
    })
