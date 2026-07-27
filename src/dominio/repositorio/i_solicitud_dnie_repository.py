from src.dominio.modelo.solicitud_dnie import SolicitudDNIe
from abc import ABC, abstractmethod
from typing import List, Optional

class ISolicitudDNIeRepository(ABC):
    @abstractmethod
    def crear(self, solicitud: SolicitudDNIe) -> SolicitudDNIe:
        ...

    @abstractmethod
    def buscar_por_id(self, id_solicitud: int) -> Optional[SolicitudDNIe]:
        ...

    @abstractmethod
    def listar(self) -> List[SolicitudDNIe]:
        ...
        
    @abstractmethod
    def eliminar(self, id_solicitud: int) -> bool:
        ...