from typing import List, Optional

from src.aplicacion.interfaces.i_solicitud_dnie_service import ISolicitudDNIeService
from src.dominio.modelo.solicitud_dnie import SolicitudDNIe
from src.dominio.repositorio.i_solicitud_dnie_repository import ISolicitudDNIeRepository

class SolicitudDNIeService(ISolicitudDNIeService):

    def __init__(self, repositorio: ISolicitudDNIeRepository):
        self._repositorio = repositorio

    def listar_solicitudes(self) -> List[SolicitudDNIe]:
        return self._repositorio.listar()
    
    