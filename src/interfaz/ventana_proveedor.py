"""
Módulo ventana_proveedor.py
============================
Este archivo contiene las clases relacionadas con la gestión de proveedores
en el sistema de inventario de AgroCol SAS.

Clases incluidas:
----------------
1. VentanaProveedorSimple: Ventana simple para agregar un proveedor nuevo
2. VentanaProveedores: Ventana completa para gestionar todos los proveedores

¿Qué es un proveedor?
--------------------
Un proveedor es una empresa o persona que nos vende los productos que luego
almacenamos en nuestro inventario. Por ejemplo: Semillas del Valle, Agroquímicos SA.

Cada producto en nuestro inventario tiene asociado un proveedor.

Conceptos clave:
---------------
1. VENTANA SIMPLE vs COMPLETA:
   - Simple: Solo permite agregar un nuevo proveedor (formulario básico)
   - Completa: Permite ver, agregar y eliminar proveedores (tabla + acciones)

2. RELACIÓN CON PRODUCTOS:
   Un proveedor puede tener muchos productos asociados.
   No se puede eliminar un proveedor si tiene productos.

Autor: Estudiante de Ingeniería en Desarrollo de Software
Fecha: 2025
Semestre: 2
"""

# ==================== IMPORTACIONES ====================

# Importar tkinter para crear la interfaz gráfica
import tkinter as tk
from tkinter import ttk, messagebox

# Importar la clase Proveedor de nuestro modelo
from ..modelos.proveedor import Proveedor


# ==================== CLASE VENTANA PROVEEDOR SIMPLE ====================

class VentanaProveedorSimple:
    """
    Clase VentanaProveedorSimple
    ===========================

    Esta es una ventana simple que solo permite agregar un nuevo proveedor.

    ¿Cuándo se usa?
    --------------
    - Cuando estamos agregando/modificando un producto y necesitamos crear
      un proveedor nuevo rápidamente.
    - Desde la ventana de gestión completa de proveedores.

    Responsabilidades:
    -----------------
    1. Mostrar un formulario con los campos del proveedor
    2. Validar que los datos sean correctos
    3. Crear el proveedor en el inventario
    4. Actualizar el combo de proveedores en la ventana que la llamó

    Atributos principales:
    ---------------------
    - ventana: La ventana emergente
    - ventana_producto: Referencia a la ventana de producto (si fue llamada desde allí)
    - entry_*: Campos de texto del formulario
    """

    def __init__(self, parent, ventana_producto):
        """
        Constructor de la clase
        =======================

        Parámetros:
        ----------
        parent : tk.Tk o tk.Toplevel
            La ventana padre

        ventana_producto : VentanaProducto o VentanaPrincipal
            Referencia a la ventana que abrió esta ventana.
            Necesitamos esta referencia para:
            1. Acceder al inventario
            2. Actualizar el combo de proveedores después de agregar

        ¿Qué hace este constructor?
        ---------------------------
        1. Guarda la referencia a ventana_producto
        2. Crea la ventana emergente
        3. Configura título y tamaño
        4. Crea el formulario
        """
        # Guardar referencia a la ventana que nos llamó
        self.ventana_producto = ventana_producto

        # ========== CREAR VENTANA EMERGENTE ==========

        # Crear ventana nueva encima de parent
        self.ventana = tk.Toplevel(parent)

        # Configurar título
        self.ventana.title("Agregar Proveedor")

        # Configurar tamaño
        self.ventana.geometry("400x250")

        # No permitir redimensionar
        self.ventana.resizable(False, False)

        # ========== CREAR INTERFAZ ==========

        self.crear_interfaz()

    def crear_interfaz(self):
        """
        Crear la interfaz de la ventana
        ===============================

        Este método crea el formulario con todos los campos necesarios
        para crear un proveedor:
        - ID del proveedor (código único)
        - Nombre
        - Teléfono
        - Email
        """
        # ========== FRAME PRINCIPAL ==========

        # Crear contenedor con padding
        frame = ttk.Frame(self.ventana, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        # ========== CAMPO: ID PROVEEDOR ==========

        # Etiqueta
        ttk.Label(frame, text="ID Proveedor:").grid(row=0, column=0, sticky=tk.W, pady=5)

        # Campo de texto
        # Este será el identificador único del proveedor (ej: PROV001)
        self.entry_id = ttk.Entry(frame, width=30)
        self.entry_id.grid(row=0, column=1, pady=5)

        # ========== CAMPO: NOMBRE ==========

        ttk.Label(frame, text="Nombre:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_nombre = ttk.Entry(frame, width=30)
        self.entry_nombre.grid(row=1, column=1, pady=5)

        # ========== CAMPO: TELÉFONO ==========

        ttk.Label(frame, text="Teléfono:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_telefono = ttk.Entry(frame, width=30)
        self.entry_telefono.grid(row=2, column=1, pady=5)

        # ========== CAMPO: EMAIL ==========

        ttk.Label(frame, text="Email:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.entry_email = ttk.Entry(frame, width=30)
        self.entry_email.grid(row=3, column=1, pady=5)

        # ========== BOTONES ==========

        # Frame para botones
        frame_botones = ttk.Frame(frame)
        frame_botones.grid(row=4, column=0, columnspan=2, pady=20)

        # Botón Guardar
        ttk.Button(frame_botones, text="Guardar", command=self.guardar).pack(side=tk.LEFT, padx=5)

        # Botón Cancelar
        ttk.Button(frame_botones, text="Cancelar", command=self.ventana.destroy).pack(side=tk.LEFT, padx=5)

    def guardar(self):
        """
        Guardar el proveedor
        ===================

        Este método se ejecuta cuando el usuario presiona "Guardar".

        ¿Qué hace?
        ----------
        1. Obtiene los valores de los campos
        2. Valida que los campos obligatorios estén completos
        3. Crea un objeto Proveedor
        4. Agrega el proveedor al inventario
        5. Guarda el inventario en el archivo
        6. Actualiza el combo de proveedores en la ventana que nos llamó
        7. Cierra esta ventana

        Campos obligatorios:
        -------------------
        - ID Proveedor
        - Nombre
        (Teléfono y email son opcionales)
        """
        try:
            # ========== OBTENER VALORES ==========

            # Obtener y limpiar espacios en blanco
            id_proveedor = self.entry_id.get().strip()
            nombre = self.entry_nombre.get().strip()
            telefono = self.entry_telefono.get().strip()
            email = self.entry_email.get().strip()

            # ========== VALIDAR CAMPOS OBLIGATORIOS ==========

            # Verificar que ID y nombre no estén vacíos
            if not id_proveedor or not nombre:
                messagebox.showerror("Error", "El ID y nombre son obligatorios")
                return

            # ========== CREAR PROVEEDOR ==========

            # Crear instancia de Proveedor
            proveedor = Proveedor(id_proveedor, nombre, telefono, email)

            # ========== AGREGAR AL INVENTARIO ==========

            # Agregar al inventario
            # Nota: esto puede lanzar una excepción si el ID ya existe
            self.ventana_producto.ventana_principal.inventario.agregar_proveedor(proveedor)

            # Guardar inventario en archivo
            self.ventana_producto.ventana_principal.guardar_inventario()

            # Actualizar combo de proveedores en la ventana de producto
            self.ventana_producto.actualizar_combo_proveedores()

            # ========== MOSTRAR ÉXITO Y CERRAR ==========

            messagebox.showinfo("Éxito", "Proveedor agregado correctamente")

            # Cerrar esta ventana
            self.ventana.destroy()

        except Exception as e:
            # Si hay error (ej: ID duplicado), mostrarlo
            messagebox.showerror("Error", str(e))


# ==================== CLASE VENTANA PROVEEDORES ====================

class VentanaProveedores:
    """
    Clase VentanaProveedores
    ========================

    Esta es la ventana completa para gestionar proveedores.
    Permite ver todos los proveedores, agregar nuevos y eliminar existentes.

    ¿Cuándo se usa?
    --------------
    Cuando el usuario selecciona "Gestionar Proveedores" desde el menú principal.

    Responsabilidades:
    -----------------
    1. Mostrar una tabla con todos los proveedores
    2. Mostrar cuántos productos tiene cada proveedor
    3. Permitir agregar nuevos proveedores
    4. Permitir eliminar proveedores (solo si no tienen productos)

    Atributos principales:
    ---------------------
    - ventana: La ventana emergente
    - ventana_principal: Referencia a la ventana principal
    - tabla: Tabla (Treeview) que muestra los proveedores
    """

    def __init__(self, parent, ventana_principal):
        """
        Constructor de la clase
        =======================

        Parámetros:
        ----------
        parent : tk.Tk o tk.Toplevel
            La ventana padre

        ventana_principal : VentanaPrincipal
            Referencia a la ventana principal para acceder al inventario

        ¿Qué hace este constructor?
        ---------------------------
        1. Guarda la referencia a ventana_principal
        2. Crea la ventana emergente
        3. Configura título y tamaño
        4. Crea la interfaz (tabla y botones)
        5. Carga los proveedores en la tabla
        """
        # Guardar referencia a la ventana principal
        self.ventana_principal = ventana_principal

        # ========== CREAR VENTANA EMERGENTE ==========

        # Crear ventana nueva
        self.ventana = tk.Toplevel(parent)

        # Configurar título
        self.ventana.title("Gestión de Proveedores")

        # Configurar tamaño
        self.ventana.geometry("700x400")

        # ========== CREAR INTERFAZ Y CARGAR DATOS ==========

        self.crear_interfaz()
        self.actualizar_tabla()

    def crear_interfaz(self):
        """
        Crear la interfaz de la ventana
        ===============================

        Crea la interfaz con:
        - Botones: Agregar y Eliminar proveedor
        - Tabla: Lista de todos los proveedores con su información
        """
        # ========== FRAME PRINCIPAL ==========

        frame = ttk.Frame(self.ventana, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        # ========== FRAME DE BOTONES ==========

        # Crear frame para los botones (en la parte superior)
        frame_botones = ttk.Frame(frame)
        frame_botones.pack(fill=tk.X, pady=5)

        # Botón para agregar proveedor
        ttk.Button(frame_botones, text="Agregar Proveedor",
                  command=self.agregar_proveedor).pack(side=tk.LEFT, padx=5)

        # Botón para eliminar proveedor
        ttk.Button(frame_botones, text="Eliminar Proveedor",
                  command=self.eliminar_proveedor).pack(side=tk.LEFT, padx=5)

        # ========== TABLA DE PROVEEDORES ==========

        # Definir columnas de la tabla
        columnas = ("ID", "Nombre", "Teléfono", "Email", "Productos")

        # Crear Treeview (tabla)
        self.tabla = ttk.Treeview(frame, columns=columnas, show='headings')

        # Configurar cada columna
        for col in columnas:
            # Configurar encabezado
            self.tabla.heading(col, text=col)
            # Configurar ancho
            self.tabla.column(col, width=120)

        # ========== SCROLLBAR ==========

        # Crear scrollbar vertical
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tabla.yview)

        # Asociar scrollbar con tabla
        self.tabla.configure(yscrollcommand=scrollbar.set)

        # ========== COLOCAR TABLA Y SCROLLBAR ==========

        # pack: otro sistema de layout (más simple que grid)
        # side=tk.LEFT: colocar a la izquierda
        # fill=tk.BOTH: expandir en ambas direcciones
        # expand=True: usar todo el espacio disponible
        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def actualizar_tabla(self):
        """
        Actualizar la tabla de proveedores
        ==================================

        Este método actualiza la tabla mostrando todos los proveedores
        del inventario con su información y la cantidad de productos
        que tiene cada uno.

        ¿Qué muestra?
        ------------
        Por cada proveedor:
        - ID
        - Nombre
        - Teléfono
        - Email
        - Cantidad de productos asociados
        """
        # ========== LIMPIAR TABLA ==========

        # Eliminar todos los elementos actuales
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # ========== OBTENER PROVEEDORES ==========

        # Obtener lista de todos los proveedores del inventario
        proveedores = self.ventana_principal.inventario.listar_proveedores()

        # ========== LLENAR TABLA ==========

        # Por cada proveedor
        for proveedor in proveedores:
            # Obtener lista de productos de este proveedor
            productos = self.ventana_principal.inventario.obtener_productos_por_proveedor(
                proveedor.id_proveedor)

            # Crear tupla con los valores de la fila
            valores = (
                proveedor.id_proveedor,
                proveedor.nombre,
                proveedor.telefono,
                proveedor.email,
                len(productos)  # Cantidad de productos
            )

            # Insertar fila en la tabla
            self.tabla.insert('', 'end', values=valores)

    def agregar_proveedor(self):
        """
        Abrir ventana para agregar proveedor
        ====================================

        Abre la ventana simple para agregar un nuevo proveedor
        y luego actualiza la tabla.

        Nota importante:
        ---------------
        Después de cerrar la ventana de agregar, actualizamos la tabla.
        Pero necesitamos esperar a que la ventana se cierre, por eso
        usamos wait_window().
        """
        # Crear ventana simple de proveedor
        # Pasamos self.ventana_principal para que tenga acceso al inventario
        ventana_simple = VentanaProveedorSimple(self.ventana, self.ventana_principal)

        # Esperar a que la ventana se cierre
        self.ventana.wait_window(ventana_simple.ventana)

        # Una vez cerrada, actualizar la tabla
        self.actualizar_tabla()

    def eliminar_proveedor(self):
        """
        Eliminar el proveedor seleccionado
        ==================================

        Permite eliminar un proveedor, pero solo si no tiene productos asociados.

        ¿Por qué no se puede eliminar si tiene productos?
        -------------------------------------------------
        Porque cada producto necesita tener un proveedor. Si eliminamos
        el proveedor, los productos quedarían sin proveedor (error de integridad).

        Solución: Primero hay que eliminar o reasignar todos los productos
        del proveedor, y luego sí se puede eliminar el proveedor.
        """
        # ========== OBTENER SELECCIÓN ==========

        # Obtener elemento seleccionado en la tabla
        seleccion = self.tabla.selection()

        # Si no hay nada seleccionado
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un proveedor")
            return

        # ========== OBTENER DATOS DEL PROVEEDOR ==========

        # Obtener datos del elemento seleccionado
        item = self.tabla.item(seleccion[0])

        # Extraer valores
        id_proveedor = item['values'][0]
        nombre = item['values'][1]
        num_productos = item['values'][4]  # Cantidad de productos

        # ========== VERIFICAR SI TIENE PRODUCTOS ==========

        # Si tiene productos asociados, no permitir eliminar
        if num_productos > 0:
            messagebox.showerror("Error",
                               f"No se puede eliminar el proveedor '{nombre}' porque tiene {num_productos} productos asociados")
            return

        # ========== CONFIRMAR ELIMINACIÓN ==========

        # Pedir confirmación al usuario
        if messagebox.askyesno("Confirmar", f"¿Eliminar proveedor '{nombre}'?"):
            # NOTA: Esta funcionalidad requiere agregar el método en la clase Inventario
            # Por ahora solo mostramos un mensaje informativo
            messagebox.showinfo("Info", "Funcionalidad pendiente de implementación")

            # TODO: Implementar el método eliminar_proveedor en la clase Inventario
            # Código esperado:
            # self.ventana_principal.inventario.eliminar_proveedor(id_proveedor)
            # self.ventana_principal.guardar_inventario()
            # self.actualizar_tabla()
            # messagebox.showinfo("Éxito", "Proveedor eliminado correctamente")

    def actualizar_combo_proveedores(self):
        """
        Actualizar combo de proveedores
        ===============================

        Este método existe para mantener compatibilidad con VentanaProveedorSimple.
        La ventana simple espera que el objeto que la llama tenga este método.

        Como esta ventana tiene una tabla en lugar de un combo, simplemente
        actualizamos la tabla.
        """
        self.actualizar_tabla()
