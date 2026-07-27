# Importaciones de las tres capas
from src.infraestructura.repositorios.solicitud_dnie_repository_impl import SolicitudDNIeRepositoryImpl
from src.aplicacion.servicios.solicitud_dnie_service import SolicitudDNIeService
from src.presentacion.controladores.solicitud_dnie_controller import SolicitudDNIeController

def inicializar_dependencias():
    # 1. Capa de Infraestructura (Instanciar el repositorio)
    repositorio = SolicitudDNIeRepositoryImpl()
    
    # 2. Capa de Aplicación (Inyectar repositorio al servicio)
    servicio = SolicitudDNIeService(repositorio)
    
    # 3. Capa de Presentación (Inyectar servicio al controlador)
    controlador = SolicitudDNIeController(servicio)
    
    return controlador

# Se expone la instancia lista para usar
controlador_dnie = inicializar_dependencias()