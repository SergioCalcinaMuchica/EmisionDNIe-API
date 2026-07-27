from src.dominio.modelo.solicitud_dnie import SolicitudDNIe
from src.dominio.repositorio.i_solicitud_dnie_repository import ISolicitudDNIeRepository
from typing import List, Optional

class SolicitudDNIeRepositoryImpl(ISolicitudDNIeRepository):
    def __init__(self):
        self._almacen: dict[int, SolicitudDNIe] = {}
        self._siguiente_id = 1

    def crear(self, solicitud: SolicitudDNIe) -> SolicitudDNIe:
        solicitud.id_solicitud = self._siguiente_id
        self._almacen[self._siguiente_id] = solicitud
        self._siguiente_id += 1
        return solicitud

    def buscar_por_id(self, id_solicitud: int) -> Optional[SolicitudDNIe]:
        return self._almacen.get(id_solicitud)

    def listar(self) -> List[SolicitudDNIe]:
        return list(self._almacen.values())
    
    def eliminar(self, id_solicitud: int) -> bool:
        if id_solicitud in self._almacen:
            del self._almacen[id_solicitud]
            return True
        return False