"""
Módulo proveedor.py
===================
Archivo que contiene la clase Proveedor para el sistema de gestión de inventario AgroCol SAS.

Esta clase representa a un proveedor de productos agrícolas y almacena su información
básica como identificación, nombre y datos de contacto.

Autor: Estudiante de Ingeniería en Desarrollo de Software
Fecha: 2025
"""


class Proveedor:
    """
    Clase Proveedor
    ===============
    Representa un proveedor de productos agrícolas en el sistema.

    Un proveedor es una empresa o persona que suministra productos al inventario.
    Esta clase utiliza encapsulamiento para proteger los datos mediante atributos privados
    y proporciona acceso controlado a través de propiedades (getters y setters).

    Atributos:
    ----------
    _id_proveedor : str
        Identificador único del proveedor (privado)
    _nombre : str
        Nombre del proveedor (privado)
    _telefono : str
        Número de teléfono de contacto (privado, opcional)
    _email : str
        Correo electrónico de contacto (privado, opcional)
    """

    def __init__(self, id_proveedor: str, nombre: str, telefono: str = "", email: str = ""):
        """
        Constructor de la clase Proveedor
        =================================
        Inicializa un nuevo objeto Proveedor con los datos proporcionados.

        Parámetros:
        -----------
        id_proveedor : str
            Identificador único del proveedor (requerido)
        nombre : str
            Nombre completo del proveedor (requerido)
        telefono : str, opcional
            Número de teléfono del proveedor. Por defecto es cadena vacía
        email : str, opcional
            Correo electrónico del proveedor. Por defecto es cadena vacía

        Ejemplo de uso:
        ---------------
        >>> proveedor = Proveedor("PROV001", "Agrícola del Valle", "3001234567", "contacto@agricola.com")
        """
        # Atributos privados (usan _ al inicio para indicar que son privados)
        self._id_proveedor = id_proveedor
        self._nombre = nombre
        self._telefono = telefono
        self._email = email

    # ==================== PROPIEDADES GETTER ====================
    # Los getters permiten leer los atributos privados desde fuera de la clase

    @property
    def id_proveedor(self) -> str:
        """
        Getter del ID del proveedor

        Retorna:
        --------
        str : El identificador único del proveedor
        """
        return self._id_proveedor

    @property
    def nombre(self) -> str:
        """
        Getter del nombre del proveedor

        Retorna:
        --------
        str : El nombre del proveedor
        """
        return self._nombre

    @property
    def telefono(self) -> str:
        """
        Getter del teléfono del proveedor

        Retorna:
        --------
        str : El número de teléfono del proveedor
        """
        return self._telefono

    @property
    def email(self) -> str:
        """
        Getter del email del proveedor

        Retorna:
        --------
        str : El correo electrónico del proveedor
        """
        return self._email

    # ==================== PROPIEDADES SETTER ====================
    # Los setters permiten modificar los atributos privados con validaciones

    @nombre.setter
    def nombre(self, valor: str):
        """
        Setter del nombre del proveedor
        Valida que el nombre no esté vacío antes de asignarlo

        Parámetros:
        -----------
        valor : str
            Nuevo nombre del proveedor

        Excepciones:
        ------------
        ValueError : Si el nombre está vacío o solo contiene espacios
        """
        # Validación: el nombre no puede estar vacío
        if not valor or valor.strip() == "":
            raise ValueError("El nombre del proveedor no puede estar vacío")
        self._nombre = valor

    @telefono.setter
    def telefono(self, valor: str):
        """
        Setter del teléfono del proveedor

        Parámetros:
        -----------
        valor : str
            Nuevo número de teléfono
        """
        self._telefono = valor

    @email.setter
    def email(self, valor: str):
        """
        Setter del email del proveedor

        Parámetros:
        -----------
        valor : str
            Nuevo correo electrónico
        """
        self._email = valor

    # ==================== MÉTODOS DE CONVERSIÓN ====================

    def to_dict(self) -> dict:
        """
        Convierte el objeto Proveedor a un diccionario
        =============================================
        Este método es útil para guardar los datos en formato JSON.

        Retorna:
        --------
        dict : Diccionario con todos los atributos del proveedor

        Ejemplo de retorno:
        -------------------
        {
            'id_proveedor': 'PROV001',
            'nombre': 'Agrícola del Valle',
            'telefono': '3001234567',
            'email': 'contacto@agricola.com'
        }
        """
        return {
            'id_proveedor': self._id_proveedor,
            'nombre': self._nombre,
            'telefono': self._telefono,
            'email': self._email
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Proveedor':
        """
        Crea un objeto Proveedor desde un diccionario
        ============================================
        Método de clase (classmethod) que permite crear un objeto Proveedor
        a partir de un diccionario. Útil para cargar datos desde JSON.

        Parámetros:
        -----------
        data : dict
            Diccionario con los datos del proveedor

        Retorna:
        --------
        Proveedor : Nueva instancia de Proveedor con los datos del diccionario

        Ejemplo de uso:
        ---------------
        >>> datos = {'id_proveedor': 'PROV001', 'nombre': 'Agrícola del Valle'}
        >>> proveedor = Proveedor.from_dict(datos)
        """
        return cls(
            id_proveedor=data['id_proveedor'],
            nombre=data['nombre'],
            # get() se usa para campos opcionales, retorna cadena vacía si no existe
            telefono=data.get('telefono', ''),
            email=data.get('email', '')
        )

    # ==================== MÉTODO ESPECIAL ====================

    def __str__(self) -> str:
        """
        Representación en texto del Proveedor
        ====================================
        Método especial que define cómo se muestra el objeto cuando se convierte a string.
        Se llama automáticamente con print() o str().

        Retorna:
        --------
        str : Representación legible del proveedor

        Ejemplo:
        --------
        >>> proveedor = Proveedor("PROV001", "Agrícola del Valle")
        >>> print(proveedor)
        Agrícola del Valle (ID: PROV001)
        """
        return f"{self._nombre} (ID: {self._id_proveedor})"
