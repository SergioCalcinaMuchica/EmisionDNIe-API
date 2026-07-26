from typing import List, Optional

from src.aplicacion.interfaces.i_solicitud_dnie_service import ISolicitudDNIeService
from src.dominio.modelo.solicitud_dnie import SolicitudDNIe
from src.dominio.repositorio.i_solicitud_dnie_repository import ISolicitudDNIeRepository

class SolicitudDNIeService(ISolicitudDNIeService):

    def __init__(self, repositorio: ISolicitudDNIeRepository):
        self._repositorio = repositorio

    def listar_solicitudes(self) -> List[SolicitudDNIe]:
        return self._repositorio.listar()
    
    def registrar_solicitud(self, dni_ciudadano: str, nombres: str, apellidos: str) -> SolicitudDNIe:
        if not dni_ciudadano or len(dni_ciudadano) != 8:
            raise ValueError("dni_ciudadano debe tener 8 dígitos")
        if not nombres or not apellidos:
            raise ValueError("nombres y apellidos son obligatorios")

        solicitud = SolicitudDNIe(
            dni_ciudadano=dni_ciudadano,
            nombres=nombres,
            apellidos=apellidos,
        )
        return self._repositorio.crear(solicitud)