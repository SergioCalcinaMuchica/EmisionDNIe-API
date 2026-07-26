from src.dominio.modelo.solicitud_dnie import SolicitudDNIe
from abc import ABC, abstractmethod
from typing import List

class ISolicitudDNIeService(ABC):
    @abstractmethod
    def registrar_solicitud(self, dni_ciudadano: str, nombres: str, apellidos: str) -> SolicitudDNIe:
        ...

    @abstractmethod
    def listar_solicitudes(self) -> List[SolicitudDNIe]:
        ...