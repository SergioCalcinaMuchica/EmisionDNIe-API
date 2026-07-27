from flask import Flask

# Importamos la función desde el archivo dependencies.py de la raíz
from dependencies import inicializar_dependencias

from src.presentacion.controladores.solicitud_dnie_controller import (
    inicializar_controlador,
    solicitud_dnie_bp,
)

def crear_app() -> Flask:
    app = Flask(__name__)

    # Obtenemos el servicio ya instanciado desde el Composition Root
    servicio = inicializar_dependencias()

    # Lo conectamos con el controlador y registramos las rutas
    inicializar_controlador(servicio)
    app.register_blueprint(solicitud_dnie_bp)

    @app.get("/health")
    def health():
        return {"status": "UP"}, 200

    return app


if __name__ == "__main__":
    app = crear_app()
    app.run(host="0.0.0.0", port=5000, debug=True)