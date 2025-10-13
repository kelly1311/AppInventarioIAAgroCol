"""
Paquete persistencia
====================
Contiene las clases responsables de guardar y cargar datos.

La persistencia es el proceso de almacenar datos en un medio permanente
(como archivos) para que no se pierdan cuando el programa termina.

Clases:
-------
- GestorPersistencia: Maneja guardado/carga de inventario en JSON

¿Por qué separar la persistencia?
---------------------------------
Siguiendo el principio de Separación de Responsabilidades, las clases
del dominio no deben saber cómo se guardan los datos. Esta capa se
encarga exclusivamente de eso.

Uso:
----
    from src.persistencia import GestorPersistencia

    gestor = GestorPersistencia()
    gestor.guardar_inventario(inventario)
    inventario = gestor.cargar_inventario()

Autor: Estudiante de Ingeniería en Desarrollo de Software
"""

# Importar la clase de persistencia
from .persistencia import GestorPersistencia

# Definir qué se exporta
__all__ = ['GestorPersistencia']
