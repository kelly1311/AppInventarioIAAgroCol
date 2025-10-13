"""
Módulo usuario.py
=================
Archivo que contiene las clases de usuarios para el sistema de gestión de inventario AgroCol SAS.

Este módulo implementa el concepto de HERENCIA en Programación Orientada a Objetos.
Define una clase padre (Usuario) y dos clases hijas (Cajero y Administrador) que heredan
de ella y extienden su funcionalidad.

Autor: Estudiante de Ingeniería en Desarrollo de Software
Fecha: 2025
"""


class Usuario:
    """
    Clase Usuario (Clase Padre o Superclase)
    ========================================
    Representa un usuario genérico del sistema de inventario.

    Esta es la clase BASE que contiene los atributos y métodos comunes para todos
    los tipos de usuarios del sistema. Las clases Cajero y Administrador heredarán
    de esta clase.

    Atributos:
    ----------
    _id_usuario : str
        Identificador único del usuario (privado)
    _nombre : str
        Nombre completo del usuario (privado)
    _usuario : str
        Nombre de usuario para login (privado)
    _contrasena : str
        Contraseña del usuario (privado)
    _rol : str
        Rol del usuario en el sistema (privado)
    """

    def __init__(self, id_usuario: str, nombre: str, usuario: str, contrasena: str, rol: str):
        """
        Constructor de la clase Usuario
        ===============================
        Inicializa un nuevo objeto Usuario con los datos proporcionados.

        Parámetros:
        -----------
        id_usuario : str
            Identificador único del usuario
        nombre : str
            Nombre completo del usuario
        usuario : str
            Nombre de usuario para iniciar sesión
        contrasena : str
            Contraseña del usuario
        rol : str
            Rol del usuario ('cajero' o 'administrador')

        Ejemplo de uso:
        ---------------
        >>> usuario = Usuario("USR001", "Juan Pérez", "jperez", "123456", "cajero")
        """
        # Atributos privados protegidos con _
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._usuario = usuario
        self._contrasena = contrasena
        self._rol = rol

    # ==================== PROPIEDADES GETTER ====================

    @property
    def id_usuario(self) -> str:
        """Getter del ID del usuario"""
        return self._id_usuario

    @property
    def nombre(self) -> str:
        """Getter del nombre del usuario"""
        return self._nombre

    @property
    def usuario(self) -> str:
        """Getter del nombre de usuario"""
        return self._usuario

    @property
    def contrasena(self) -> str:
        """Getter de la contraseña del usuario"""
        return self._contrasena

    @property
    def rol(self) -> str:
        """Getter del rol del usuario"""
        return self._rol

    # ==================== PROPIEDADES SETTER ====================

    @nombre.setter
    def nombre(self, valor: str):
        """
        Setter del nombre con validación

        Parámetros:
        -----------
        valor : str
            Nuevo nombre del usuario
        """
        if not valor or valor.strip() == "":
            raise ValueError("El nombre del usuario no puede estar vacío")
        self._nombre = valor

    @contrasena.setter
    def contrasena(self, valor: str):
        """
        Setter de la contraseña con validación

        Parámetros:
        -----------
        valor : str
            Nueva contraseña
        """
        if not valor or len(valor) < 4:
            raise ValueError("La contraseña debe tener al menos 4 caracteres")
        self._contrasena = valor

    # ==================== MÉTODOS ====================

    def verificar_contrasena(self, contrasena: str) -> bool:
        """
        Verifica si la contraseña proporcionada es correcta
        ==================================================

        Parámetros:
        -----------
        contrasena : str
            Contraseña a verificar

        Retorna:
        --------
        bool : True si la contraseña es correcta, False en caso contrario

        Ejemplo:
        --------
        >>> usuario.verificar_contrasena("123456")
        True
        """
        return self._contrasena == contrasena

    def cambiar_contrasena(self, contrasena_actual: str, contrasena_nueva: str) -> bool:
        """
        Cambia la contraseña del usuario
        ================================

        Parámetros:
        -----------
        contrasena_actual : str
            Contraseña actual para verificación
        contrasena_nueva : str
            Nueva contraseña a establecer

        Retorna:
        --------
        bool : True si el cambio fue exitoso, False si la contraseña actual es incorrecta

        Excepciones:
        ------------
        ValueError : Si la nueva contraseña no cumple los requisitos
        """
        if not self.verificar_contrasena(contrasena_actual):
            return False
        self.contrasena = contrasena_nueva  # Usa el setter que ya valida
        return True

    def to_dict(self) -> dict:
        """
        Convierte el usuario a un diccionario
        ====================================

        Retorna:
        --------
        dict : Diccionario con los datos del usuario
        """
        return {
            'id_usuario': self._id_usuario,
            'nombre': self._nombre,
            'usuario': self._usuario,
            'contrasena': self._contrasena,
            'rol': self._rol
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Usuario':
        """
        Crea un usuario desde un diccionario
        ===================================

        Parámetros:
        -----------
        data : dict
            Diccionario con los datos del usuario

        Retorna:
        --------
        Usuario : Nueva instancia de Usuario
        """
        return cls(
            id_usuario=data['id_usuario'],
            nombre=data['nombre'],
            usuario=data['usuario'],
            contrasena=data['contrasena'],
            rol=data['rol']
        )

    def __str__(self) -> str:
        """
        Representación en texto del Usuario

        Retorna:
        --------
        str : Representación legible del usuario
        """
        return f"{self._nombre} ({self._usuario}) - Rol: {self._rol}"


class Cajero(Usuario):
    """
    Clase Cajero (Clase Hija o Subclase)
    ====================================
    Representa un usuario con rol de cajero en el sistema.

    Esta clase HEREDA de Usuario, lo que significa que tiene acceso a todos los
    atributos y métodos de la clase padre, pero puede agregar funcionalidad específica
    para el rol de cajero.

    HERENCIA: Cajero extiende Usuario
    - Hereda: id_usuario, nombre, usuario, contrasena, rol
    - Agrega: atributos y métodos específicos para cajeros
    """

    def __init__(self, id_usuario: str, nombre: str, usuario: str, contrasena: str,
                 caja_asignada: str = "Caja 1"):
        """
        Constructor de la clase Cajero
        ==============================

        Parámetros:
        -----------
        id_usuario : str
            Identificador único del usuario
        nombre : str
            Nombre completo del cajero
        usuario : str
            Nombre de usuario para login
        contrasena : str
            Contraseña del cajero
        caja_asignada : str, opcional
            Número o nombre de la caja asignada. Por defecto "Caja 1"

        Ejemplo de uso:
        ---------------
        >>> cajero = Cajero("USR001", "María López", "mlopez", "pass123", "Caja 1")
        """
        # Llamar al constructor de la clase padre (Usuario) usando super()
        # super() permite acceder a métodos de la clase padre
        super().__init__(id_usuario, nombre, usuario, contrasena, rol="cajero")

        # Atributo específico de Cajero
        self._caja_asignada = caja_asignada

    # ==================== PROPIEDADES ESPECÍFICAS DE CAJERO ====================

    @property
    def caja_asignada(self) -> str:
        """Getter de la caja asignada al cajero"""
        return self._caja_asignada

    @caja_asignada.setter
    def caja_asignada(self, valor: str):
        """Setter de la caja asignada"""
        if not valor or valor.strip() == "":
            raise ValueError("La caja asignada no puede estar vacía")
        self._caja_asignada = valor

    # ==================== MÉTODOS ESPECÍFICOS DE CAJERO ====================

    def realizar_venta(self, codigo_producto: str, cantidad: float) -> dict:
        """
        Simula el registro de una venta de producto
        ==========================================
        Método específico de cajeros para procesar ventas.

        Parámetros:
        -----------
        codigo_producto : str
            Código del producto vendido
        cantidad : float
            Cantidad vendida

        Retorna:
        --------
        dict : Información de la venta registrada

        Ejemplo:
        --------
        >>> cajero.realizar_venta("PROD001", 5.0)
        {'mensaje': 'Venta registrada', 'producto': 'PROD001', 'cantidad': 5.0}
        """
        # En una implementación real, aquí se procesaría la venta
        return {
            'mensaje': 'Venta registrada por cajero',
            'cajero': self._nombre,
            'caja': self._caja_asignada,
            'producto': codigo_producto,
            'cantidad': cantidad
        }

    def consultar_producto(self, codigo_producto: str) -> str:
        """
        Permite al cajero consultar información de un producto
        =====================================================

        Parámetros:
        -----------
        codigo_producto : str
            Código del producto a consultar

        Retorna:
        --------
        str : Mensaje de consulta
        """
        return f"Cajero {self._nombre} consultó el producto {codigo_producto}"

    # ==================== SOBRESCRITURA DE MÉTODOS ====================

    def to_dict(self) -> dict:
        """
        Convierte el cajero a un diccionario
        ===================================
        SOBRESCRITURA: Este método redefine el to_dict() de la clase padre
        para incluir atributos específicos de Cajero.

        Retorna:
        --------
        dict : Diccionario con datos del cajero
        """
        # Obtener el diccionario base de la clase padre
        data = super().to_dict()
        # Agregar atributos específicos de Cajero
        data['caja_asignada'] = self._caja_asignada
        return data

    @classmethod
    def from_dict(cls, data: dict) -> 'Cajero':
        """
        Crea un cajero desde un diccionario
        ==================================
        """
        return cls(
            id_usuario=data['id_usuario'],
            nombre=data['nombre'],
            usuario=data['usuario'],
            contrasena=data['contrasena'],
            caja_asignada=data.get('caja_asignada', 'Caja 1')
        )

    def __str__(self) -> str:
        """
        Representación en texto del Cajero
        SOBRESCRITURA: Redefine __str__ para mostrar información específica

        Retorna:
        --------
        str : Representación legible del cajero
        """
        return f"Cajero: {self._nombre} ({self._usuario}) - {self._caja_asignada}"


class Administrador(Usuario):
    """
    Clase Administrador (Clase Hija o Subclase)
    ==========================================
    Representa un usuario con rol de administrador en el sistema.

    Esta clase HEREDA de Usuario y tiene privilegios completos sobre el sistema,
    incluyendo la gestión de usuarios, productos, proveedores y reportes.

    HERENCIA: Administrador extiende Usuario
    - Hereda: todos los atributos y métodos de Usuario
    - Agrega: funcionalidad específica para administradores
    """

    def __init__(self, id_usuario: str, nombre: str, usuario: str, contrasena: str,
                 nivel_acceso: str = "completo"):
        """
        Constructor de la clase Administrador
        ====================================

        Parámetros:
        -----------
        id_usuario : str
            Identificador único del administrador
        nombre : str
            Nombre completo del administrador
        usuario : str
            Nombre de usuario para login
        contrasena : str
            Contraseña del administrador
        nivel_acceso : str, opcional
            Nivel de acceso del administrador. Por defecto "completo"

        Ejemplo de uso:
        ---------------
        >>> admin = Administrador("ADM001", "Carlos Rodríguez", "crodriguez", "admin123")
        """
        # Llamar al constructor de la clase padre
        super().__init__(id_usuario, nombre, usuario, contrasena, rol="administrador")

        # Atributo específico de Administrador
        self._nivel_acceso = nivel_acceso

    # ==================== PROPIEDADES ESPECÍFICAS DE ADMINISTRADOR ====================

    @property
    def nivel_acceso(self) -> str:
        """Getter del nivel de acceso del administrador"""
        return self._nivel_acceso

    @nivel_acceso.setter
    def nivel_acceso(self, valor: str):
        """Setter del nivel de acceso"""
        niveles_validos = ["completo", "limitado", "solo_lectura"]
        if valor not in niveles_validos:
            raise ValueError(f"Nivel de acceso debe ser uno de: {niveles_validos}")
        self._nivel_acceso = valor

    # ==================== MÉTODOS ESPECÍFICOS DE ADMINISTRADOR ====================

    def agregar_usuario(self, nuevo_usuario: Usuario) -> str:
        """
        Permite al administrador agregar un nuevo usuario al sistema
        ===========================================================

        Parámetros:
        -----------
        nuevo_usuario : Usuario
            Objeto Usuario (o Cajero/Administrador) a agregar

        Retorna:
        --------
        str : Mensaje confirmando la acción
        """
        return f"Administrador {self._nombre} agregó al usuario: {nuevo_usuario.nombre}"

    def eliminar_usuario(self, id_usuario: str) -> str:
        """
        Permite al administrador eliminar un usuario del sistema
        =======================================================

        Parámetros:
        -----------
        id_usuario : str
            ID del usuario a eliminar

        Retorna:
        --------
        str : Mensaje confirmando la acción
        """
        return f"Administrador {self._nombre} eliminó al usuario con ID: {id_usuario}"

    def generar_reporte_completo(self) -> dict:
        """
        Genera un reporte completo del sistema
        =====================================
        Solo los administradores pueden acceder a reportes completos.

        Retorna:
        --------
        dict : Información del reporte generado
        """
        return {
            'generado_por': self._nombre,
            'rol': self._rol,
            'nivel_acceso': self._nivel_acceso,
            'mensaje': 'Reporte completo del sistema generado'
        }

    def modificar_producto(self, codigo_producto: str, cambios: dict) -> str:
        """
        Permite al administrador modificar cualquier producto
        ====================================================

        Parámetros:
        -----------
        codigo_producto : str
            Código del producto a modificar
        cambios : dict
            Diccionario con los cambios a realizar

        Retorna:
        --------
        str : Mensaje confirmando la modificación
        """
        return f"Admin {self._nombre} modificó el producto {codigo_producto}"

    def gestionar_proveedores(self, accion: str, proveedor_id: str = None) -> str:
        """
        Permite gestionar proveedores (agregar, eliminar, modificar)
        ===========================================================

        Parámetros:
        -----------
        accion : str
            Acción a realizar ("agregar", "eliminar", "modificar")
        proveedor_id : str, opcional
            ID del proveedor (para eliminar o modificar)

        Retorna:
        --------
        str : Mensaje confirmando la acción
        """
        return f"Admin {self._nombre} ejecutó acción '{accion}' en proveedores"

    # ==================== SOBRESCRITURA DE MÉTODOS ====================

    def to_dict(self) -> dict:
        """
        Convierte el administrador a un diccionario
        ==========================================
        SOBRESCRITURA: Incluye atributos específicos de Administrador

        Retorna:
        --------
        dict : Diccionario con datos del administrador
        """
        data = super().to_dict()
        data['nivel_acceso'] = self._nivel_acceso
        return data

    @classmethod
    def from_dict(cls, data: dict) -> 'Administrador':
        """
        Crea un administrador desde un diccionario
        =========================================
        """
        return cls(
            id_usuario=data['id_usuario'],
            nombre=data['nombre'],
            usuario=data['usuario'],
            contrasena=data['contrasena'],
            nivel_acceso=data.get('nivel_acceso', 'completo')
        )

    def __str__(self) -> str:
        """
        Representación en texto del Administrador
        ========================================
        SOBRESCRITURA: Muestra información específica del administrador

        Retorna:
        --------
        str : Representación legible del administrador
        """
        return f"Administrador: {self._nombre} ({self._usuario}) - Acceso: {self._nivel_acceso}"
