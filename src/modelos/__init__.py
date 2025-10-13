"""
Paquete modelos
===============
Contiene las clases del dominio del negocio (entidades principales).

Estas clases representan los conceptos fundamentales del sistema:
- Proveedor: Empresa que suministra productos
- Producto: Insumo agrícola en el inventario
- Inventario: Colección de productos y proveedores
- Usuario: Usuarios del sistema (con roles Cajero y Administrador)

¿Qué es una clase del dominio?
------------------------------
Son las clases que representan los conceptos centrales del negocio.
En este caso, el negocio es la gestión de inventarios agrícolas.

Uso:
----
    from src.modelos import Proveedor, Producto, Inventario
    from src.modelos import Usuario, Cajero, Administrador

Autor: Estudiante de Ingeniería en Desarrollo de Software
"""

# Importar las clases del dominio para facilitar su uso
from .proveedor import Proveedor
from .producto import Producto
from .inventario import Inventario
from .usuario import Usuario, Cajero, Administrador

# Definir qué se exporta cuando se hace: from src.modelos import *
__all__ = [
    'Proveedor',
    'Producto',
    'Inventario',
    'Usuario',
    'Cajero',
    'Administrador'
]
