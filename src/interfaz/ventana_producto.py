"""
Módulo ventana_producto.py
===========================
Este archivo contiene la clase VentanaProducto, que es la ventana para agregar
o modificar productos en el inventario de AgroCol SAS.

¿Qué es esta ventana?
--------------------
Es una ventana emergente (diálogo) que se abre cuando:
1. El usuario quiere agregar un nuevo producto
2. El usuario quiere modificar un producto existente

La ventana muestra un formulario con todos los campos necesarios para
un producto: código, nombre, cantidad, precio, proveedor, etc.

Conceptos clave:
---------------
1. VENTANA MODAL: Es una ventana que se abre encima de la ventana principal
   y requiere que el usuario complete la acción antes de volver a la principal.

2. FORMULARIO: Conjunto de campos (Entry, Combobox) donde el usuario ingresa datos.

3. VALIDACIÓN: Proceso de verificar que los datos ingresados sean correctos
   antes de guardarlos.

Autor: Estudiante de Ingeniería en Desarrollo de Software
Fecha: 2025
Semestre: 2
"""

# ==================== IMPORTACIONES ====================

# Importar tkinter para crear la interfaz gráfica
import tkinter as tk
from tkinter import ttk, messagebox

# Importar datetime para trabajar con fechas
from datetime import datetime

# Importar typing para anotaciones de tipo
from typing import Optional

# Importar las clases de negocio que necesitamos
from ..modelos.producto import Producto
from ..modelos.proveedor import Proveedor


# ==================== CLASE VENTANA PRODUCTO ====================

class VentanaProducto:
    """
    Clase VentanaProducto
    ====================

    Esta clase representa la ventana para agregar o modificar productos.

    Responsabilidades:
    -----------------
    1. Mostrar un formulario con todos los campos del producto
    2. Validar que los datos ingresados sean correctos
    3. Guardar el producto (nuevo o modificado) en el inventario
    4. Permitir agregar proveedores nuevos desde esta ventana

    Atributos principales:
    ---------------------
    - ventana: La ventana emergente (Toplevel)
    - ventana_principal: Referencia a la ventana principal
    - producto: El producto a modificar (None si es nuevo)
    - es_nuevo: Booleano que indica si estamos creando un producto nuevo
    - entry_*: Campos de texto del formulario
    - combo_*: Listas desplegables del formulario
    """

    def __init__(self, parent, ventana_principal, producto: Optional[Producto] = None):
        """
        Constructor de la clase
        =======================

        Parámetros:
        ----------
        parent : tk.Tk o tk.Toplevel
            La ventana padre (la ventana principal)

        ventana_principal : VentanaPrincipal
            Referencia a la ventana principal para acceder al inventario

        producto : Producto, opcional
            Si es None, estamos creando un producto nuevo.
            Si tiene valor, estamos modificando ese producto.

        ¿Qué hace este constructor?
        ---------------------------
        1. Guarda las referencias necesarias
        2. Determina si es un producto nuevo o existente
        3. Crea la ventana emergente
        4. Configura título y tamaño
        5. Crea el formulario
        6. Si es modificación, carga los datos del producto
        """
        # Guardar referencia a la ventana principal
        self.ventana_principal = ventana_principal

        # Guardar el producto (puede ser None)
        self.producto = producto

        # Determinar si es un producto nuevo
        # Si producto es None, entonces es_nuevo es True
        self.es_nuevo = producto is None

        # ========== CREAR VENTANA EMERGENTE ==========

        # Toplevel crea una ventana nueva encima de parent
        self.ventana = tk.Toplevel(parent)

        # Configurar título según si es nuevo o modificación
        if self.es_nuevo:
            self.ventana.title("Agregar Producto")
        else:
            self.ventana.title("Modificar Producto")

        # Configurar tamaño de la ventana
        self.ventana.geometry("500x550")

        # No permitir cambiar tamaño (para mantener diseño consistente)
        self.ventana.resizable(False, False)

        # ========== CREAR INTERFAZ ==========

        self.crear_interfaz()

        # ========== CARGAR DATOS SI ES MODIFICACIÓN ==========

        # Si NO es nuevo (es modificación), cargar datos del producto
        if not self.es_nuevo:
            self.cargar_datos_producto()

    def crear_interfaz(self):
        """
        Crear la interfaz de la ventana
        ===============================

        Este método crea todos los elementos visuales del formulario:
        - Etiquetas (labels) para cada campo
        - Campos de texto (Entry) para ingresar datos
        - Listas desplegables (Combobox) para opciones predefinidas
        - Botones para guardar o cancelar
        """
        # ========== FRAME PRINCIPAL ==========

        # Crear contenedor principal con padding
        frame = ttk.Frame(self.ventana, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        # ========== CAMPO: CÓDIGO ==========

        # Etiqueta "Código:"
        ttk.Label(frame, text="Código:").grid(row=0, column=0, sticky=tk.W, pady=5)

        # Campo de texto para código
        self.entry_codigo = ttk.Entry(frame, width=30)
        self.entry_codigo.grid(row=0, column=1, pady=5)

        # Si es modificación, el código no se puede cambiar
        if not self.es_nuevo:
            self.entry_codigo.config(state='readonly')

        # ========== CAMPO: NOMBRE ==========

        ttk.Label(frame, text="Nombre:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_nombre = ttk.Entry(frame, width=30)
        self.entry_nombre.grid(row=1, column=1, pady=5)

        # ========== CAMPO: CANTIDAD ==========

        ttk.Label(frame, text="Cantidad:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_cantidad = ttk.Entry(frame, width=30)
        self.entry_cantidad.grid(row=2, column=1, pady=5)

        # ========== CAMPO: UNIDAD DE MEDIDA ==========

        ttk.Label(frame, text="Unidad de Medida:").grid(row=3, column=0, sticky=tk.W, pady=5)

        # Combobox con opciones predefinidas
        # values: lista de opciones que aparecerán en la lista desplegable
        self.combo_unidad = ttk.Combobox(frame, width=28,
                                        values=["kg", "ton", "unidad", "litro", "bulto", "caja", "m3"])
        self.combo_unidad.grid(row=3, column=1, pady=5)

        # ========== CAMPO: STOCK MÍNIMO ==========

        ttk.Label(frame, text="Stock Mínimo:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.entry_stock_minimo = ttk.Entry(frame, width=30)
        self.entry_stock_minimo.grid(row=4, column=1, pady=5)

        # ========== CAMPO: PRECIO DE COSTO ==========

        ttk.Label(frame, text="Precio de Costo:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.entry_precio = ttk.Entry(frame, width=30)
        self.entry_precio.grid(row=5, column=1, pady=5)

        # ========== CAMPO: PROVEEDOR ==========

        ttk.Label(frame, text="Proveedor:").grid(row=6, column=0, sticky=tk.W, pady=5)

        # Combobox readonly: el usuario solo puede seleccionar, no escribir
        self.combo_proveedor = ttk.Combobox(frame, width=28, state='readonly')
        self.combo_proveedor.grid(row=6, column=1, pady=5)

        # Llenar el combo con los proveedores actuales
        self.actualizar_combo_proveedores()

        # Botón para agregar un proveedor nuevo
        ttk.Button(frame, text="Nuevo Proveedor",
                  command=self.agregar_proveedor).grid(row=6, column=2, padx=5)

        # ========== CAMPO: FECHA DE INGRESO ==========

        ttk.Label(frame, text="Fecha de Ingreso:").grid(row=7, column=0, sticky=tk.W, pady=5)
        self.entry_fecha = ttk.Entry(frame, width=30)
        self.entry_fecha.grid(row=7, column=1, pady=5)

        # Insertar fecha actual por defecto
        # strftime formatea la fecha: %d=día, %m=mes, %Y=año
        self.entry_fecha.insert(0, datetime.now().strftime("%d/%m/%Y"))

        # ========== BOTONES DE ACCIÓN ==========

        # Crear frame para los botones
        frame_botones = ttk.Frame(frame)
        frame_botones.grid(row=8, column=0, columnspan=3, pady=20)

        # Botón Guardar
        ttk.Button(frame_botones, text="Guardar",
                  command=self.guardar).pack(side=tk.LEFT, padx=5)

        # Botón Cancelar
        ttk.Button(frame_botones, text="Cancelar",
                  command=self.ventana.destroy).pack(side=tk.LEFT, padx=5)

    def actualizar_combo_proveedores(self):
        """
        Actualizar el combo de proveedores
        ==================================

        Este método obtiene la lista de proveedores del inventario
        y actualiza las opciones del Combobox de proveedores.

        Formato de cada opción: "Nombre (ID)"
        Ejemplo: "Semillas SA (PROV001)"
        """
        # Obtener lista de proveedores del inventario
        proveedores = self.ventana_principal.inventario.listar_proveedores()

        # Crear lista de strings con formato "Nombre (ID)"
        # Usamos list comprehension (forma compacta de crear listas)
        nombres = [f"{p.nombre} ({p.id_proveedor})" for p in proveedores]

        # Asignar la lista al combo
        self.combo_proveedor['values'] = nombres

        # Si hay proveedores, seleccionar el primero por defecto
        if nombres:
            self.combo_proveedor.current(0)

    def agregar_proveedor(self):
        """
        Abrir ventana para agregar un nuevo proveedor
        =============================================

        Abre la ventana simple para agregar un proveedor y luego
        actualiza el combo de proveedores.
        """
        # Importar aquí para evitar importación circular
        from ventana_proveedor import VentanaProveedorSimple

        # Crear ventana de proveedor simple
        # Pasamos self para que la ventana pueda actualizar nuestro combo
        VentanaProveedorSimple(self.ventana, self)

    def cargar_datos_producto(self):
        """
        Cargar los datos del producto en el formulario
        ==============================================

        Este método se ejecuta cuando estamos modificando un producto existente.
        Llena todos los campos del formulario con los datos actuales del producto.

        Nota sobre readonly:
        -------------------
        El campo código está en readonly cuando modificamos, pero necesitamos
        ponerlo en 'normal' temporalmente para poder insertar el valor.
        """
        # ========== CÓDIGO (readonly) ==========

        # Temporalmente habilitar el campo para insertar valor
        self.entry_codigo.config(state='normal')

        # Insertar el código
        self.entry_codigo.insert(0, self.producto.codigo)

        # Volver a readonly para que no se pueda modificar
        self.entry_codigo.config(state='readonly')

        # ========== OTROS CAMPOS ==========

        # Insertar nombre
        self.entry_nombre.insert(0, self.producto.nombre)

        # Insertar cantidad (convertir a string)
        self.entry_cantidad.insert(0, str(self.producto.cantidad))

        # Seleccionar unidad de medida en el combo
        self.combo_unidad.set(self.producto.unidad_medida)

        # Insertar stock mínimo
        self.entry_stock_minimo.insert(0, str(self.producto.stock_minimo))

        # Insertar precio
        self.entry_precio.insert(0, str(self.producto.precio_costo))

        # ========== FECHA ==========

        # Borrar fecha por defecto
        self.entry_fecha.delete(0, tk.END)

        # Insertar fecha del producto
        self.entry_fecha.insert(0, self.producto.fecha_ingreso)

        # ========== SELECCIONAR PROVEEDOR ==========

        # Obtener lista de proveedores
        proveedores = self.ventana_principal.inventario.listar_proveedores()

        # Buscar el proveedor actual del producto en la lista
        for i, p in enumerate(proveedores):
            # Si el ID coincide
            if p.id_proveedor == self.producto.proveedor.id_proveedor:
                # Seleccionar este proveedor en el combo
                self.combo_proveedor.current(i)
                break  # Salir del bucle, ya lo encontramos

    def guardar(self):
        """
        Guardar el producto
        ==================

        Este método se ejecuta cuando el usuario presiona "Guardar".

        ¿Qué hace?
        ----------
        1. Obtiene todos los valores de los campos del formulario
        2. Valida que los datos sean correctos
        3. Si es nuevo, crea un producto nuevo
        4. Si es modificación, actualiza el producto existente
        5. Guarda el inventario en el archivo
        6. Actualiza la tabla en la ventana principal
        7. Cierra esta ventana

        Manejo de errores:
        -----------------
        Usamos try-except para capturar errores:
        - ValueError: cuando un número no es válido
        - Exception: cualquier otro error
        """
        try:
            # ========== OBTENER VALORES DE LOS CAMPOS ==========

            # Obtener código y quitar espacios en blanco
            codigo = self.entry_codigo.get().strip()

            # Obtener nombre y quitar espacios
            nombre = self.entry_nombre.get().strip()

            # Obtener cantidad y convertir a float (número decimal)
            cantidad = float(self.entry_cantidad.get())

            # Obtener unidad de medida
            unidad_medida = self.combo_unidad.get()

            # Obtener stock mínimo
            stock_minimo = float(self.entry_stock_minimo.get())

            # Obtener precio
            precio_costo = float(self.entry_precio.get())

            # Obtener fecha
            fecha_ingreso = self.entry_fecha.get()

            # ========== VALIDAR CAMPOS OBLIGATORIOS ==========

            # Verificar que los campos importantes no estén vacíos
            if not all([codigo, nombre, unidad_medida]):
                messagebox.showerror("Error", "Complete todos los campos obligatorios")
                return

            # ========== OBTENER PROVEEDOR ==========

            # Obtener el texto seleccionado en el combo
            seleccion = self.combo_proveedor.get()

            # Verificar que se haya seleccionado un proveedor
            if not seleccion:
                messagebox.showerror("Error", "Seleccione un proveedor")
                return

            # Extraer el ID del proveedor del formato "Nombre (ID)"
            # split("(") divide el string por el paréntesis
            # [1] toma la segunda parte (después del paréntesis)
            # strip(")") quita el paréntesis final
            id_proveedor = seleccion.split("(")[1].strip(")")

            # Buscar el objeto Proveedor completo en el inventario
            proveedor = self.ventana_principal.inventario.obtener_proveedor(id_proveedor)

            # ========== GUARDAR PRODUCTO ==========

            if self.es_nuevo:
                # ===== CREAR PRODUCTO NUEVO =====

                # Crear instancia de Producto con todos los datos
                producto = Producto(
                    codigo=codigo,
                    nombre=nombre,
                    unidad_medida=unidad_medida,
                    fecha_ingreso=fecha_ingreso,
                    proveedor=proveedor,
                    precio_costo=precio_costo,
                    cantidad=cantidad,
                    stock_minimo=stock_minimo
                )

                # Agregar al inventario
                self.ventana_principal.inventario.agregar_producto(producto)

            else:
                # ===== MODIFICAR PRODUCTO EXISTENTE =====

                # Actualizar los atributos del producto existente
                self.producto.nombre = nombre
                self.producto.unidad_medida = unidad_medida
                self.producto.precio_costo = precio_costo
                self.producto.cantidad = cantidad
                self.producto.stock_minimo = stock_minimo
                self.producto.proveedor = proveedor

            # ========== GUARDAR Y ACTUALIZAR ==========

            # Guardar inventario en archivo
            self.ventana_principal.guardar_inventario()

            # Actualizar tabla de productos en ventana principal
            self.ventana_principal.actualizar_tabla_productos()

            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", "Producto guardado correctamente")

            # Cerrar esta ventana
            self.ventana.destroy()

        except ValueError as e:
            # Error al convertir a número
            messagebox.showerror("Error", f"Error en los datos: {str(e)}")

        except Exception as e:
            # Cualquier otro error
            messagebox.showerror("Error", str(e))
