"""
Módulo producto.py
==================
Archivo que contiene la clase Producto para el sistema de gestión de inventario AgroCol SAS.

Esta clase representa un producto o insumo agrícola en el inventario y maneja
todas sus operaciones relacionadas (agregar stock, retirar stock, verificar stock bajo, etc.).

Autor: Estudiante de Ingeniería en Desarrollo de Software
Fecha: 2025
"""

# Importar la clase Proveedor desde el módulo proveedor
from .proveedor import Proveedor


class Producto:
    """
    Clase Producto
    ==============
    Representa un producto o insumo agrícola en el inventario.

    Un producto contiene información sobre su identificación, cantidad disponible,
    precio, proveedor y otras características importantes para la gestión del inventario.
    Utiliza COMPOSICIÓN: un Producto "tiene un" Proveedor.

    Atributos:
    ----------
    _codigo : str
        Código único identificador del producto (privado)
    _nombre : str
        Nombre descriptivo del producto (privado)
    _unidad_medida : str
        Unidad en que se mide el producto (kg, litros, unidades, etc.) (privado)
    _fecha_ingreso : str
        Fecha en que el producto ingresó al inventario (privado)
    _proveedor : Proveedor
        Objeto Proveedor que suministra este producto (composición) (privado)
    _precio_costo : float
        Precio de costo del producto (privado)
    _cantidad : float
        Cantidad disponible en stock (privado)
    _stock_minimo : float
        Cantidad mínima que debe haber en stock (alerta) (privado)
    """

    def __init__(self, codigo: str, nombre: str, unidad_medida: str,
                 fecha_ingreso: str, proveedor: Proveedor, precio_costo: float,
                 cantidad: float = 0, stock_minimo: float = 10):
        """
        Constructor de la clase Producto
        ================================
        Inicializa un nuevo producto con todos sus atributos.

        Parámetros:
        -----------
        codigo : str
            Código único del producto (ej: "FERT001")
        nombre : str
            Nombre del producto (ej: "Fertilizante Urea")
        unidad_medida : str
            Unidad de medida (ej: "kg", "litro", "unidad")
        fecha_ingreso : str
            Fecha de ingreso al inventario (formato: "DD/MM/YYYY")
        proveedor : Proveedor
            Objeto de tipo Proveedor que suministra el producto
        precio_costo : float
            Precio de costo unitario del producto
        cantidad : float, opcional
            Cantidad inicial en stock. Por defecto es 0
        stock_minimo : float, opcional
            Cantidad mínima en stock para alertas. Por defecto es 10

        Ejemplo de uso:
        ---------------
        >>> proveedor = Proveedor("PROV001", "Agrícola del Valle")
        >>> producto = Producto("FERT001", "Fertilizante Urea", "kg",
        ...                     "15/01/2025", proveedor, 2500.0, 100, 20)
        """
        # Inicializar atributos privados
        self._codigo = codigo
        self._nombre = nombre
        self._unidad_medida = unidad_medida
        self._fecha_ingreso = fecha_ingreso
        self._proveedor = proveedor  # Composición: Producto tiene un Proveedor
        self._precio_costo = precio_costo
        self._cantidad = cantidad
        self._stock_minimo = stock_minimo

    # ==================== PROPIEDADES GETTER ====================
    # Permiten acceder a los atributos privados de forma controlada

    @property
    def codigo(self) -> str:
        """
        Getter del código del producto

        Retorna:
        --------
        str : Código único del producto
        """
        return self._codigo

    @property
    def nombre(self) -> str:
        """
        Getter del nombre del producto

        Retorna:
        --------
        str : Nombre del producto
        """
        return self._nombre

    @property
    def unidad_medida(self) -> str:
        """
        Getter de la unidad de medida

        Retorna:
        --------
        str : Unidad de medida del producto
        """
        return self._unidad_medida

    @property
    def fecha_ingreso(self) -> str:
        """
        Getter de la fecha de ingreso

        Retorna:
        --------
        str : Fecha de ingreso al inventario
        """
        return self._fecha_ingreso

    @property
    def proveedor(self) -> Proveedor:
        """
        Getter del proveedor
        Retorna el objeto Proveedor completo (composición)

        Retorna:
        --------
        Proveedor : Objeto proveedor del producto
        """
        return self._proveedor

    @property
    def precio_costo(self) -> float:
        """
        Getter del precio de costo

        Retorna:
        --------
        float : Precio de costo unitario
        """
        return self._precio_costo

    @property
    def cantidad(self) -> float:
        """
        Getter de la cantidad en stock

        Retorna:
        --------
        float : Cantidad disponible en el inventario
        """
        return self._cantidad

    @property
    def stock_minimo(self) -> float:
        """
        Getter del stock mínimo

        Retorna:
        --------
        float : Cantidad mínima requerida en stock
        """
        return self._stock_minimo

    # ==================== PROPIEDADES SETTER ====================
    # Permiten modificar los atributos privados con validaciones

    @nombre.setter
    def nombre(self, valor: str):
        """
        Setter del nombre con validación

        Parámetros:
        -----------
        valor : str
            Nuevo nombre del producto

        Excepciones:
        ------------
        ValueError : Si el nombre está vacío
        """
        if not valor or valor.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío")
        self._nombre = valor

    @unidad_medida.setter
    def unidad_medida(self, valor: str):
        """
        Setter de la unidad de medida

        Parámetros:
        -----------
        valor : str
            Nueva unidad de medida
        """
        self._unidad_medida = valor

    @precio_costo.setter
    def precio_costo(self, valor: float):
        """
        Setter del precio de costo con validación

        Parámetros:
        -----------
        valor : float
            Nuevo precio de costo

        Excepciones:
        ------------
        ValueError : Si el precio es negativo
        """
        if valor < 0:
            raise ValueError("El precio de costo no puede ser negativo")
        self._precio_costo = valor

    @cantidad.setter
    def cantidad(self, valor: float):
        """
        Setter de la cantidad con validación

        Parámetros:
        -----------
        valor : float
            Nueva cantidad en stock

        Excepciones:
        ------------
        ValueError : Si la cantidad es negativa
        """
        if valor < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = valor

    @stock_minimo.setter
    def stock_minimo(self, valor: float):
        """
        Setter del stock mínimo con validación

        Parámetros:
        -----------
        valor : float
            Nuevo stock mínimo

        Excepciones:
        ------------
        ValueError : Si el stock mínimo es negativo
        """
        if valor < 0:
            raise ValueError("El stock mínimo no puede ser negativo")
        self._stock_minimo = valor

    @proveedor.setter
    def proveedor(self, valor: Proveedor):
        """
        Setter del proveedor con validación de tipo

        Parámetros:
        -----------
        valor : Proveedor
            Nuevo proveedor del producto

        Excepciones:
        ------------
        ValueError : Si el valor no es una instancia de Proveedor
        """
        if not isinstance(valor, Proveedor):
            raise ValueError("El proveedor debe ser una instancia de la clase Proveedor")
        self._proveedor = valor

    # ==================== MÉTODOS DE OPERACIÓN ====================

    def agregar_stock(self, cantidad: float) -> None:
        """
        Incrementa la cantidad en stock del producto
        ===========================================
        Este método se usa cuando llega nueva mercancía al inventario.

        Parámetros:
        -----------
        cantidad : float
            Cantidad a agregar al stock actual (debe ser positiva)

        Excepciones:
        ------------
        ValueError : Si la cantidad a agregar no es mayor a cero

        Ejemplo:
        --------
        >>> producto.agregar_stock(50.0)  # Agrega 50 unidades al stock
        >>> print(producto.cantidad)  # Muestra la cantidad actualizada
        """
        # Validar que la cantidad sea positiva
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser mayor a cero")
        # Incrementar el stock
        self._cantidad += cantidad

    def retirar_stock(self, cantidad: float) -> None:
        """
        Disminuye la cantidad en stock del producto
        ==========================================
        Este método se usa cuando se realiza una venta o se retira mercancía.

        Parámetros:
        -----------
        cantidad : float
            Cantidad a retirar del stock actual (debe ser positiva)

        Excepciones:
        ------------
        ValueError :
            - Si la cantidad a retirar no es mayor a cero
            - Si no hay suficiente stock disponible

        Ejemplo:
        --------
        >>> producto.retirar_stock(10.0)  # Retira 10 unidades del stock
        >>> print(producto.cantidad)  # Muestra la cantidad actualizada
        """
        # Validar que la cantidad sea positiva
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor a cero")
        # Validar que haya suficiente stock
        if cantidad > self._cantidad:
            raise ValueError(f"No hay suficiente stock. Disponible: {self._cantidad}")
        # Disminuir el stock
        self._cantidad -= cantidad

    def esta_bajo_stock(self) -> bool:
        """
        Verifica si el producto está por debajo del stock mínimo
        =======================================================
        Este método es útil para generar alertas cuando un producto
        necesita ser reabastecido.

        Retorna:
        --------
        bool :
            True si la cantidad actual es menor o igual al stock mínimo
            False si hay suficiente stock

        Ejemplo:
        --------
        >>> producto.stock_minimo = 20
        >>> producto.cantidad = 15
        >>> if producto.esta_bajo_stock():
        ...     print("¡Alerta! Stock bajo")
        ¡Alerta! Stock bajo
        """
        return self._cantidad <= self._stock_minimo

    def valor_total_inventario(self) -> float:
        """
        Calcula el valor total del inventario de este producto
        =====================================================
        Multiplica la cantidad en stock por el precio de costo unitario.
        Es útil para conocer cuánto dinero está invertido en este producto.

        Retorna:
        --------
        float : Valor total (cantidad × precio_costo)

        Ejemplo:
        --------
        >>> producto.cantidad = 100
        >>> producto.precio_costo = 2500.0
        >>> valor = producto.valor_total_inventario()
        >>> print(f"Valor total: ${valor:,.2f}")
        Valor total: $250,000.00
        """
        return self._cantidad * self._precio_costo

    # ==================== MÉTODOS DE CONVERSIÓN ====================

    def to_dict(self) -> dict:
        """
        Convierte el producto a un diccionario
        =====================================
        Útil para guardar los datos en formato JSON.
        Incluye el proveedor convertido también a diccionario.

        Retorna:
        --------
        dict : Diccionario con todos los atributos del producto

        Ejemplo de retorno:
        -------------------
        {
            'codigo': 'FERT001',
            'nombre': 'Fertilizante Urea',
            'unidad_medida': 'kg',
            'fecha_ingreso': '15/01/2025',
            'proveedor': {'id_proveedor': 'PROV001', ...},
            'precio_costo': 2500.0,
            'cantidad': 100.0,
            'stock_minimo': 20.0
        }
        """
        return {
            'codigo': self._codigo,
            'nombre': self._nombre,
            'unidad_medida': self._unidad_medida,
            'fecha_ingreso': self._fecha_ingreso,
            # Convertir el proveedor a diccionario también (composición)
            'proveedor': self._proveedor.to_dict(),
            'precio_costo': self._precio_costo,
            'cantidad': self._cantidad,
            'stock_minimo': self._stock_minimo
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Producto':
        """
        Crea un objeto Producto desde un diccionario
        ===========================================
        Método de clase que permite reconstruir un producto desde datos JSON.
        Reconstruye también el objeto Proveedor asociado.

        Parámetros:
        -----------
        data : dict
            Diccionario con los datos del producto

        Retorna:
        --------
        Producto : Nueva instancia de Producto con los datos del diccionario

        Ejemplo de uso:
        ---------------
        >>> datos = {
        ...     'codigo': 'FERT001',
        ...     'nombre': 'Fertilizante',
        ...     'proveedor': {'id_proveedor': 'PROV001', 'nombre': 'Agrícola'}
        ...     # ... más campos
        ... }
        >>> producto = Producto.from_dict(datos)
        """
        # Reconstruir el objeto Proveedor primero
        proveedor = Proveedor.from_dict(data['proveedor'])

        # Crear y retornar el objeto Producto
        return cls(
            codigo=data['codigo'],
            nombre=data['nombre'],
            unidad_medida=data['unidad_medida'],
            fecha_ingreso=data['fecha_ingreso'],
            proveedor=proveedor,
            precio_costo=data['precio_costo'],
            # get() permite valores por defecto si la clave no existe
            cantidad=data.get('cantidad', 0),
            stock_minimo=data.get('stock_minimo', 10)
        )

    # ==================== MÉTODO ESPECIAL ====================

    def __str__(self) -> str:
        """
        Representación en texto del Producto
        ===================================
        Define cómo se muestra el producto cuando se convierte a string.

        Retorna:
        --------
        str : Representación legible del producto

        Ejemplo:
        --------
        >>> producto = Producto("FERT001", "Fertilizante Urea", "kg", ...)
        >>> print(producto)
        Fertilizante Urea (FERT001) - Stock: 100.00 kg
        """
        return f"{self._nombre} ({self._codigo}) - Stock: {self._cantidad} {self._unidad_medida}"
