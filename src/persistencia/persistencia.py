"""
Módulo persistencia.py
======================
Archivo que contiene la clase GestorPersistencia para el sistema AgroCol SAS.

Esta clase es responsable de guardar y cargar el inventario desde archivos JSON.
Permite que los datos persistan (se mantengan) incluso después de cerrar la aplicación.

Autor: Estudiante de Ingeniería en Desarrollo de Software
Fecha: 2025
"""

# Importar módulos necesarios de Python
import json  # Para trabajar con archivos JSON
import os    # Para operaciones del sistema de archivos
from typing import Optional  # Para indicar valores opcionales
from datetime import datetime  # Para manejar fechas y horas

# Importar la clase Inventario
from ..modelos import Inventario


class GestorPersistencia:
    """
    Clase GestorPersistencia
    ========================
    Encargada de gestionar la persistencia de datos del inventario.

    La persistencia es el proceso de guardar datos en un medio de almacenamiento
    permanente (como un archivo) para que no se pierdan cuando el programa termina.
    Esta clase utiliza archivos JSON para almacenar los datos.

    ¿Por qué JSON?
    --------------
    - Es un formato de texto legible por humanos
    - Fácil de leer y escribir con Python
    - Compatible con muchos lenguajes de programación
    - Ideal para almacenar estructuras de datos complejas

    Atributos:
    ----------
    _archivo : str
        Nombre del archivo donde se guarda el inventario (privado)
    _ruta_completa : str
        Ruta completa al archivo en el sistema (privado)
    """

    def __init__(self, archivo: str = "inventario_agrocol.json"):
        """
        Constructor de la clase GestorPersistencia
        =========================================

        Parámetros:
        -----------
        archivo : str, opcional
            Nombre del archivo JSON donde se guardará el inventario.
            Por defecto: "inventario_agrocol.json"

        Ejemplo de uso:
        ---------------
        >>> gestor = GestorPersistencia()  # Usa el archivo por defecto
        >>> gestor2 = GestorPersistencia("mi_inventario.json")  # Usa archivo personalizado
        """
        # Guardar el nombre del archivo
        self._archivo = archivo

        # Obtener la ruta completa uniendo el directorio actual con el nombre del archivo
        # os.getcwd() retorna el directorio de trabajo actual
        # os.path.join() une rutas de forma segura según el sistema operativo
        self._ruta_completa = os.path.join(os.getcwd(), archivo)

    # ==================== PROPIEDADES ====================

    @property
    def archivo(self) -> str:
        """
        Getter del nombre del archivo

        Retorna:
        --------
        str : Nombre del archivo
        """
        return self._archivo

    @property
    def ruta_completa(self) -> str:
        """
        Getter de la ruta completa al archivo

        Retorna:
        --------
        str : Ruta completa del archivo en el sistema
        """
        return self._ruta_completa

    # ==================== MÉTODO PRINCIPAL: GUARDAR ====================

    def guardar_inventario(self, inventario: Inventario) -> bool:
        """
        Guarda el inventario completo en un archivo JSON
        ===============================================

        Este método convierte el objeto Inventario a un diccionario y luego
        lo guarda en formato JSON en el archivo especificado.

        Parámetros:
        -----------
        inventario : Inventario
            Instancia de Inventario que se desea guardar

        Retorna:
        --------
        bool :
            True si se guardó correctamente
            False si ocurrió algún error

        Proceso:
        --------
        1. Convertir el inventario a diccionario usando to_dict()
        2. Abrir el archivo en modo escritura ('w')
        3. Usar json.dump() para escribir el diccionario como JSON
        4. Retornar True si todo salió bien

        Ejemplo:
        --------
        >>> gestor = GestorPersistencia()
        >>> inventario = Inventario()
        >>> if gestor.guardar_inventario(inventario):
        ...     print("Inventario guardado exitosamente")
        """
        try:
            # PASO 1: Convertir el inventario a un diccionario
            datos = inventario.to_dict()

            # PASO 2: Abrir el archivo en modo escritura
            # 'w' = write (escritura, crea o sobrescribe el archivo)
            # encoding='utf-8' = permite caracteres especiales (tildes, ñ, etc.)
            with open(self._ruta_completa, 'w', encoding='utf-8') as archivo:
                # PASO 3: Guardar el diccionario como JSON
                # ensure_ascii=False permite caracteres no ASCII (español)
                # indent=4 formatea el JSON con sangría para que sea legible
                json.dump(datos, archivo, ensure_ascii=False, indent=4)

            # PASO 4: Si llegamos aquí, todo salió bien
            return True

        except Exception as e:
            # Si ocurre cualquier error, mostrar mensaje y retornar False
            print(f"Error al guardar el inventario: {str(e)}")
            return False

    # ==================== MÉTODO PRINCIPAL: CARGAR ====================

    def cargar_inventario(self) -> Optional[Inventario]:
        """
        Carga el inventario desde un archivo JSON
        ========================================

        Lee el archivo JSON y reconstruye el objeto Inventario completo
        con todos sus productos y proveedores.

        Retorna:
        --------
        Inventario | None :
            Instancia de Inventario cargada si todo sale bien
            None si ocurre algún error

        Proceso:
        --------
        1. Verificar si el archivo existe
        2. Si no existe, crear uno nuevo vacío
        3. Si existe, leer el archivo JSON
        4. Convertir el JSON a objeto Inventario usando from_dict()
        5. Retornar el inventario cargado

        Ejemplo:
        --------
        >>> gestor = GestorPersistencia()
        >>> inventario = gestor.cargar_inventario()
        >>> if inventario:
        ...     print(f"Productos cargados: {inventario.obtener_cantidad_total_productos()}")
        """
        try:
            # PASO 1: Verificar si el archivo existe
            if not os.path.exists(self._ruta_completa):
                # Si no existe, crear un inventario nuevo vacío
                print("Archivo no encontrado. Creando nuevo inventario...")
                inventario_nuevo = Inventario()
                self.guardar_inventario(inventario_nuevo)
                return inventario_nuevo

            # PASO 2: Abrir y leer el archivo JSON
            # 'r' = read (lectura)
            with open(self._ruta_completa, 'r', encoding='utf-8') as archivo:
                # Cargar el contenido JSON como diccionario Python
                datos = json.load(archivo)

            # PASO 3: Convertir el diccionario a objeto Inventario
            return Inventario.from_dict(datos)

        except json.JSONDecodeError as e:
            # Error específico: el archivo JSON está mal formado
            print(f"Error al decodificar JSON: {str(e)}")
            return None

        except Exception as e:
            # Cualquier otro error
            print(f"Error al cargar el inventario: {str(e)}")
            return None

    # ==================== MÉTODOS AUXILIARES ====================

    def existe_archivo(self) -> bool:
        """
        Verifica si el archivo de inventario existe en el sistema
        ========================================================

        Retorna:
        --------
        bool :
            True si el archivo existe
            False si no existe

        Ejemplo:
        --------
        >>> gestor = GestorPersistencia()
        >>> if gestor.existe_archivo():
        ...     print("El archivo existe")
        ... else:
        ...     print("El archivo no existe")
        """
        # os.path.exists() verifica si una ruta existe en el sistema
        return os.path.exists(self._ruta_completa)

    def crear_backup(self, sufijo: str = None) -> bool:
        """
        Crea una copia de seguridad del archivo de inventario
        ====================================================

        Un backup (respaldo) es una copia de seguridad de los datos para
        prevenir pérdida de información. Es una buena práctica crear backups
        antes de operaciones importantes.

        Parámetros:
        -----------
        sufijo : str, opcional
            Sufijo para el nombre del backup.
            Si no se proporciona, usa la fecha y hora actual

        Retorna:
        --------
        bool :
            True si se creó el backup correctamente
            False si hubo algún error

        Ejemplo:
        --------
        >>> gestor = GestorPersistencia()
        >>> if gestor.crear_backup():
        ...     print("Backup creado exitosamente")

        Nombre del backup generado:
        ---------------------------
        inventario_agrocol_backup_20250113_153045.json
        (año-mes-día_hora-minuto-segundo)
        """
        try:
            # Verificar que el archivo original exista
            if not self.existe_archivo():
                print("No se puede crear backup: el archivo no existe")
                return False

            # Si no se proporciona sufijo, usar fecha y hora actual
            if sufijo is None:
                # strftime formatea la fecha como string
                # Formato: año(4)mes(2)día(2)_hora(2)minuto(2)segundo(2)
                sufijo = datetime.now().strftime("%Y%m%d_%H%M%S")

            # Construir el nombre del archivo de backup
            # Ejemplo: "inventario_agrocol" + "_backup_" + "20250113_153045" + ".json"
            nombre_base = os.path.splitext(self._archivo)[0]  # Quita la extensión
            nombre_backup = f"{nombre_base}_backup_{sufijo}.json"
            ruta_backup = os.path.join(os.getcwd(), nombre_backup)

            # Leer el contenido del archivo original
            with open(self._ruta_completa, 'r', encoding='utf-8') as origen:
                contenido = origen.read()

            # Escribir el contenido en el archivo de backup
            with open(ruta_backup, 'w', encoding='utf-8') as destino:
                destino.write(contenido)

            print(f"Backup creado: {nombre_backup}")
            return True

        except Exception as e:
            print(f"Error al crear backup: {str(e)}")
            return False

    def eliminar_archivo(self) -> bool:
        """
        Elimina el archivo de inventario del sistema
        ===========================================

        ¡CUIDADO! Esta operación es irreversible. El archivo se elimina
        permanentemente del disco. Se recomienda crear un backup antes.

        Retorna:
        --------
        bool :
            True si se eliminó correctamente
            False si hubo algún error o el archivo no existe

        Ejemplo:
        --------
        >>> gestor = GestorPersistencia()
        >>> gestor.crear_backup()  # Crear backup primero
        >>> if gestor.eliminar_archivo():
        ...     print("Archivo eliminado")
        """
        try:
            # Verificar que el archivo exista antes de intentar eliminarlo
            if self.existe_archivo():
                # os.remove() elimina el archivo del disco
                os.remove(self._ruta_completa)
                print(f"Archivo eliminado: {self._archivo}")
                return True
            else:
                print("El archivo no existe")
                return False

        except Exception as e:
            print(f"Error al eliminar archivo: {str(e)}")
            return False
