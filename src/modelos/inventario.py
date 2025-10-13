"""
Módulo inventario.py
====================
Archivo que contiene la clase Inventario para el sistema de gestión AgroCol SAS.

Esta clase gestiona la colección completa de productos y proveedores del sistema.
Actúa como controlador central que coordina todas las operaciones del inventario.

Autor: Estudiante de Ingeniería en Desarrollo de Software
Fecha: 2025
"""

# Importar las clases necesarias desde otros módulos
from typing import Optional
from .producto import Producto
from .proveedor import Proveedor


class Inventario:
    """
    Clase Inventario
    ================
    Gestiona el inventario completo de productos agrícolas y sus proveedores.

    Esta clase utiliza estructuras de datos tipo diccionario para almacenar y
    organizar eficientemente productos y proveedores. Proporciona métodos para
    todas las operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

    AGREGACIÓN: El inventario contiene múltiples Productos y Proveedores.
    La relación es "tiene muchos" (has-many).

    Atributos:
    ----------
    _productos : dict[str, Producto]
        Diccionario que almacena productos usando el código como clave (privado)
    _proveedores : dict[str, Proveedor]
        Diccionario que almacena proveedores usando el ID como clave (privado)
    """

    def __init__(self):
        """
        Constructor de la clase Inventario
        ==================================
        Inicializa un inventario vacío con diccionarios para productos y proveedores.

        Los diccionarios permiten acceso rápido O(1) a productos y proveedores
        por su código/ID sin necesidad de recorrer toda la lista.

        Ejemplo de uso:
        ---------------
        >>> inventario = Inventario()
        >>> print(f"Productos: {inventario.obtener_cantidad_total_productos()}")
        Productos: 0
        """
        # Diccionario vacío para almacenar productos: {codigo: objeto_producto}
        self._productos: dict[str, Producto] = {}

        # Diccionario vacío para almacenar proveedores: {id: objeto_proveedor}
        self._proveedores: dict[str, Proveedor] = {}

    # ==================== MÉTODOS DE GESTIÓN DE PROVEEDORES ====================

    def agregar_proveedor(self, proveedor: Proveedor) -> None:
        """
        Agrega un nuevo proveedor al sistema
        ====================================

        Parámetros:
        -----------
        proveedor : Proveedor
            Objeto Proveedor a agregar al inventario

        Excepciones:
        ------------
        ValueError : Si ya existe un proveedor con el mismo ID

        Ejemplo:
        --------
        >>> proveedor = Proveedor("PROV001", "Agrícola del Valle")
        >>> inventario.agregar_proveedor(proveedor)
        """
        # Validar que no exista un proveedor con el mismo ID
        if proveedor.id_proveedor in self._proveedores:
            raise ValueError(f"El proveedor con ID {proveedor.id_proveedor} ya existe")

        # Agregar al diccionario usando el ID como clave
        self._proveedores[proveedor.id_proveedor] = proveedor

    def obtener_proveedor(self, id_proveedor: str) -> Optional[Proveedor]:
        """
        Obtiene un proveedor específico por su ID
        ========================================

        Parámetros:
        -----------
        id_proveedor : str
            ID del proveedor a buscar

        Retorna:
        --------
        Proveedor | None :
            El objeto Proveedor si existe, None si no se encuentra

        Ejemplo:
        --------
        >>> proveedor = inventario.obtener_proveedor("PROV001")
        >>> if proveedor:
        ...     print(proveedor.nombre)
        """
        # get() retorna None si la clave no existe (no lanza excepción)
        return self._proveedores.get(id_proveedor)

    def listar_proveedores(self) -> list[Proveedor]:
        """
        Retorna la lista de todos los proveedores registrados
        ====================================================

        Retorna:
        --------
        list[Proveedor] : Lista con todos los objetos Proveedor

        Ejemplo:
        --------
        >>> proveedores = inventario.listar_proveedores()
        >>> for p in proveedores:
        ...     print(p.nombre)
        """
        # values() retorna todos los valores del diccionario
        # list() convierte la vista de valores en una lista
        return list(self._proveedores.values())

    # ==================== MÉTODOS DE GESTIÓN DE PRODUCTOS ====================

    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega un nuevo producto al inventario
        ======================================
        Si el proveedor del producto no está registrado, lo registra automáticamente.

        Parámetros:
        -----------
        producto : Producto
            Objeto Producto a agregar al inventario

        Excepciones:
        ------------
        ValueError : Si ya existe un producto con el mismo código

        Ejemplo:
        --------
        >>> proveedor = Proveedor("PROV001", "Agrícola")
        >>> producto = Producto("FERT001", "Fertilizante", "kg", "01/01/2025",
        ...                     proveedor, 2500.0, 100, 20)
        >>> inventario.agregar_producto(producto)
        """
        # Validar que no exista un producto con el mismo código
        if producto.codigo in self._productos:
            raise ValueError(f"El producto con código {producto.codigo} ya existe")

        # Verificar si el proveedor está registrado, si no, agregarlo
        if producto.proveedor.id_proveedor not in self._proveedores:
            self.agregar_proveedor(producto.proveedor)

        # Agregar el producto al diccionario usando el código como clave
        self._productos[producto.codigo] = producto

    def obtener_producto(self, codigo: str) -> Optional[Producto]:
        """
        Obtiene un producto específico por su código
        ===========================================

        Parámetros:
        -----------
        codigo : str
            Código del producto a buscar

        Retorna:
        --------
        Producto | None :
            El objeto Producto si existe, None si no se encuentra

        Ejemplo:
        --------
        >>> producto = inventario.obtener_producto("FERT001")
        >>> if producto:
        ...     print(f"{producto.nombre}: {producto.cantidad}")
        """
        return self._productos.get(codigo)

    def actualizar_producto(self, producto: Producto) -> None:
        """
        Actualiza la información de un producto existente
        ================================================
        Reemplaza el producto anterior con el nuevo objeto.

        Parámetros:
        -----------
        producto : Producto
            Objeto Producto con los datos actualizados

        Excepciones:
        ------------
        ValueError : Si el producto no existe en el inventario

        Ejemplo:
        --------
        >>> producto = inventario.obtener_producto("FERT001")
        >>> producto.precio_costo = 3000.0
        >>> inventario.actualizar_producto(producto)
        """
        # Validar que el producto exista
        if producto.codigo not in self._productos:
            raise ValueError(f"El producto con código {producto.codigo} no existe")

        # Actualizar el producto en el diccionario
        self._productos[producto.codigo] = producto

    def eliminar_producto(self, codigo: str) -> None:
        """
        Elimina un producto del inventario
        ==================================

        Parámetros:
        -----------
        codigo : str
            Código del producto a eliminar

        Excepciones:
        ------------
        ValueError : Si el producto no existe

        Ejemplo:
        --------
        >>> inventario.eliminar_producto("FERT001")
        """
        # Validar que el producto exista
        if codigo not in self._productos:
            raise ValueError(f"El producto con código {codigo} no existe")

        # Eliminar del diccionario usando del
        del self._productos[codigo]

    def listar_productos(self) -> list[Producto]:
        """
        Retorna la lista de todos los productos en el inventario
        =======================================================

        Retorna:
        --------
        list[Producto] : Lista con todos los objetos Producto

        Ejemplo:
        --------
        >>> productos = inventario.listar_productos()
        >>> print(f"Total productos: {len(productos)}")
        """
        return list(self._productos.values())

    # ==================== MÉTODOS DE BÚSQUEDA Y FILTRADO ====================

    def buscar_productos(self, termino: str) -> list[Producto]:
        """
        Busca productos por nombre o código
        ===================================
        La búsqueda no distingue entre mayúsculas y minúsculas.

        Parámetros:
        -----------
        termino : str
            Término de búsqueda a buscar en nombre o código

        Retorna:
        --------
        list[Producto] : Lista de productos que coinciden con la búsqueda

        Ejemplo:
        --------
        >>> productos = inventario.buscar_productos("ferti")
        >>> for p in productos:
        ...     print(p.nombre)  # Mostrará productos con "ferti" en el nombre
        """
        # Convertir el término a minúsculas para búsqueda no sensible a mayúsculas
        termino = termino.lower()

        # Lista para almacenar resultados
        resultados = []

        # Recorrer todos los productos del diccionario
        for producto in self._productos.values():
            # Buscar en nombre y código (convertidos a minúsculas)
            if (termino in producto.nombre.lower() or
                termino in producto.codigo.lower()):
                resultados.append(producto)

        return resultados

    def obtener_productos_bajo_stock(self) -> list[Producto]:
        """
        Retorna los productos que están por debajo del stock mínimo
        ==========================================================
        Útil para generar alertas de reabastecimiento.

        Retorna:
        --------
        list[Producto] : Lista de productos con stock bajo

        Ejemplo:
        --------
        >>> productos_bajo_stock = inventario.obtener_productos_bajo_stock()
        >>> if productos_bajo_stock:
        ...     print("¡Alerta! Productos que necesitan reabastecimiento:")
        ...     for p in productos_bajo_stock:
        ...         print(f"- {p.nombre}: {p.cantidad} {p.unidad_medida}")
        """
        # List comprehension: crea lista filtrando productos bajo stock
        return [p for p in self._productos.values() if p.esta_bajo_stock()]

    def obtener_productos_por_proveedor(self, id_proveedor: str) -> list[Producto]:
        """
        Retorna los productos de un proveedor específico
        ===============================================

        Parámetros:
        -----------
        id_proveedor : str
            ID del proveedor cuyos productos se quieren obtener

        Retorna:
        --------
        list[Producto] : Lista de productos del proveedor especificado

        Ejemplo:
        --------
        >>> productos = inventario.obtener_productos_por_proveedor("PROV001")
        >>> print(f"Productos del proveedor: {len(productos)}")
        """
        # List comprehension: filtrar productos por ID de proveedor
        return [p for p in self._productos.values()
                if p.proveedor.id_proveedor == id_proveedor]

    # ==================== MÉTODOS DE ESTADÍSTICAS ====================

    def obtener_cantidad_total_productos(self) -> int:
        """
        Retorna la cantidad total de productos diferentes en el inventario
        =================================================================
        Cuenta cuántos productos distintos hay (no la cantidad en stock).

        Retorna:
        --------
        int : Número total de productos diferentes

        Ejemplo:
        --------
        >>> total = inventario.obtener_cantidad_total_productos()
        >>> print(f"Productos diferentes: {total}")
        """
        # len() retorna la cantidad de elementos en el diccionario
        return len(self._productos)

    def obtener_valor_total_inventario(self) -> float:
        """
        Calcula el valor total de todo el inventario
        ===========================================
        Suma el valor total de todos los productos (cantidad × precio).

        Retorna:
        --------
        float : Valor total del inventario en dinero

        Ejemplo:
        --------
        >>> valor_total = inventario.obtener_valor_total_inventario()
        >>> print(f"Valor total del inventario: ${valor_total:,.2f}")
        """
        # sum() con generador: suma el valor total de cada producto
        return sum(p.valor_total_inventario() for p in self._productos.values())

    # ==================== MÉTODOS DE CONVERSIÓN (SERIALIZACIÓN) ====================

    def to_dict(self) -> dict:
        """
        Convierte el inventario completo a un diccionario
        ================================================
        Útil para guardar todo el inventario en formato JSON.

        Retorna:
        --------
        dict : Diccionario con productos y proveedores convertidos

        Estructura del retorno:
        -----------------------
        {
            'productos': [lista de diccionarios de productos],
            'proveedores': [lista de diccionarios de proveedores]
        }
        """
        return {
            # List comprehension: convertir cada producto a diccionario
            'productos': [p.to_dict() for p in self._productos.values()],
            # List comprehension: convertir cada proveedor a diccionario
            'proveedores': [p.to_dict() for p in self._proveedores.values()]
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Inventario':
        """
        Crea un inventario completo desde un diccionario
        ===============================================
        Método de clase para reconstruir el inventario desde datos JSON.

        Parámetros:
        -----------
        data : dict
            Diccionario con la estructura:
            {
                'productos': [...],
                'proveedores': [...]
            }

        Retorna:
        --------
        Inventario : Nueva instancia de Inventario con todos los datos cargados

        Ejemplo de uso:
        ---------------
        >>> datos = {
        ...     'productos': [...],
        ...     'proveedores': [...]
        ... }
        >>> inventario = Inventario.from_dict(datos)
        """
        # Crear un inventario vacío
        inventario = cls()

        # PASO 1: Cargar proveedores primero (porque productos los necesitan)
        for proveedor_data in data.get('proveedores', []):
            # Reconstruir cada proveedor desde su diccionario
            proveedor = Proveedor.from_dict(proveedor_data)
            # Agregar al diccionario interno usando el ID como clave
            inventario._proveedores[proveedor.id_proveedor] = proveedor

        # PASO 2: Cargar productos (que referencian a los proveedores ya cargados)
        for producto_data in data.get('productos', []):
            # Reconstruir cada producto desde su diccionario
            producto = Producto.from_dict(producto_data)
            # Agregar al diccionario interno usando el código como clave
            inventario._productos[producto.codigo] = producto

        return inventario
