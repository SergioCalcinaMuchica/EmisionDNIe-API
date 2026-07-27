from flask import Blueprint, jsonify, request
from src.aplicacion.interfaces.i_solicitud_dnie_service import ISolicitudDNIeService

solicitud_dnie_bp = Blueprint("solicitud_dnie", __name__, url_prefix="/api/solicitudes-dnie")

_service: ISolicitudDNIeService = None

@solicitud_dnie_bp.get("")
def listar_solicitudes():
    solicitudes = _service.listar_solicitudes()
    return jsonify([s.a_diccionario() for s in solicitudes]), 200

@solicitud_dnie_bp.get("/<int:id_solicitud>")
def obtener_solicitud(id_solicitud: int):
    solicitud = _service.obtener_solicitud(id_solicitud)
    if solicitud is None:
        return jsonify({"error": "Solicitud no encontrada"}), 404
    return jsonify(solicitud.a_diccionario()), 200

def inicializar_controlador(servicio: ISolicitudDNIeService):
    global _service
    _service = servicio

@solicitud_dnie_bp.post("")
def crear_solicitud():
    datos = request.get_json(silent=True) or {}
    try:
        solicitud = _service.registrar_solicitud(
            dni_ciudadano=datos.get("dni_ciudadano"),
            nombres=datos.get("nombres"),
            apellidos=datos.get("apellidos"),
        )
        return jsonify(solicitud.a_diccionario()), 201
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
