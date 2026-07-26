from flask import Blueprint, jsonify, request
from src.aplicacion.interfaces.i_solicitud_dnie_service import ISolicitudDNIeService

solicitud_dnie_bp = Blueprint("solicitud_dnie", __name__, url_prefix="/api/solicitudes-dnie")

_service: ISolicitudDNIeService = None

@solicitud_dnie_bp.get("")
def listar_solicitudes():
    solicitudes = _service.listar_solicitudes()
    return jsonify([s.a_diccionario() for s in solicitudes]), 200