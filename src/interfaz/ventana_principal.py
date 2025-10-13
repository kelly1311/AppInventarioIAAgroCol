"""
Módulo ventana_principal.py
============================
Este archivo contiene la clase VentanaPrincipal, que es la ventana principal
de la aplicación de gestión de inventario para AgroCol SAS.

¿Qué es una ventana principal?
------------------------------
Es la ventana principal que se muestra cuando iniciamos el programa. Desde aquí
podemos acceder a todas las funcionalidades del sistema de inventario.

Conceptos clave para entender este código:
------------------------------------------
1. CLASE: Es como un molde o plantilla para crear objetos. Aquí definimos
   cómo debe comportarse nuestra ventana principal.

2. HERENCIA E INSTANCIAS: Esta clase usa tkinter (biblioteca de interfaces
   gráficas de Python) para crear ventanas y widgets.

3. SELF: Es una referencia al objeto actual. Cuando escribimos self.algo,
   estamos hablando de una variable que pertenece a este objeto específico.

4. MÉTODOS: Son funciones que pertenecen a una clase. Realizan acciones
   específicas sobre el objeto.

Autor: Estudiante de Ingeniería en Desarrollo de Software
Fecha: 2025
Semestre: 2
"""

# ==================== IMPORTACIONES ====================
# Las importaciones nos permiten usar código que ya existe en otras partes

# Importar tkinter: biblioteca para crear interfaces gráficas
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Importar datetime: para trabajar con fechas y horas
from datetime import datetime

# Importar typing: para especificar tipos de datos (ayuda a prevenir errores)
from typing import Optional

# Importar nuestras clases personalizadas del sistema
from ..modelos.producto import Producto
from ..modelos.proveedor import Proveedor
from ..modelos.inventario import Inventario
from ..persistencia.persistencia import GestorPersistencia


# ==================== CLASE VENTANA PRINCIPAL ====================

class VentanaPrincipal:
    """
    Clase VentanaPrincipal
    ======================

    Esta clase representa la ventana principal de nuestra aplicación.
    Es lo primero que ve el usuario cuando abre el programa.

    Responsabilidades de esta clase:
    --------------------------------
    1. Mostrar el menú principal con todas las opciones
    2. Mostrar la tabla con todos los productos del inventario
    3. Permitir buscar, agregar, modificar y eliminar productos
    4. Mostrar estadísticas del inventario (valor total, productos bajo stock)
    5. Guardar y cargar los datos del inventario
    6. Generar reportes

    Atributos principales:
    ---------------------
    - root: La ventana principal de tkinter
    - inventario: Objeto que contiene todos los productos y proveedores
    - gestor_persistencia: Objeto que se encarga de guardar/cargar datos
    - tabla_productos: La tabla donde se muestran los productos
    """

    def __init__(self, root: tk.Tk):
        """
        Constructor de la clase
        =======================

        El constructor se ejecuta automáticamente cuando creamos una nueva
        instancia de VentanaPrincipal. Aquí inicializamos todo lo necesario.

        Parámetros:
        ----------
        root : tk.Tk
            La ventana raíz de tkinter (ventana principal del sistema operativo)

        ¿Qué hace este constructor?
        ---------------------------
        1. Guarda la referencia a la ventana root
        2. Configura el título y tamaño de la ventana
        3. Carga el inventario desde el archivo (o crea uno nuevo)
        4. Configura los estilos visuales
        5. Crea el menú y la interfaz
        6. Muestra los productos y verifica alertas
        """
        # Guardar la referencia a la ventana principal
        self.root = root

        # Configurar el título de la ventana (lo que aparece en la barra superior)
        self.root.title("Sistema de Gestión de Inventario - AgroCol SAS")

        # Configurar el tamaño de la ventana (ancho x alto en píxeles)
        self.root.geometry("1200x700")

        # Permitir que el usuario pueda cambiar el tamaño de la ventana
        self.root.resizable(True, True)

        # ========== INICIALIZAR GESTOR DE PERSISTENCIA E INVENTARIO ==========

        # Crear el objeto que maneja guardar/cargar datos
        self.gestor_persistencia = GestorPersistencia()

        # Intentar cargar el inventario desde el archivo
        self.inventario = self.gestor_persistencia.cargar_inventario()

        # Si no se pudo cargar (archivo no existe o está corrupto)
        if self.inventario is None:
            # Crear un inventario nuevo vacío
            self.inventario = Inventario()
            # Mostrar advertencia al usuario
            messagebox.showwarning("Advertencia",
                                   "No se pudo cargar el inventario. Se creará uno nuevo.")

        # ========== CONFIGURAR Y CREAR LA INTERFAZ ==========

        # Configurar los colores y fuentes de la aplicación
        self.configurar_estilo()

        # Crear el menú de la aplicación (Archivo, Proveedores, Reportes, etc.)
        self.crear_menu()

        # Crear toda la interfaz gráfica (botones, tabla, etc.)
        self.crear_interfaz()

        # ========== ACTUALIZAR VISTA INICIAL ==========

        # Cargar los productos en la tabla
        self.actualizar_tabla_productos()

        # Verificar si hay productos con stock bajo y mostrar alerta
        self.verificar_alertas_stock()

    def configurar_estilo(self):
        """
        Configurar el estilo visual de la aplicación
        ============================================

        Este método define los colores, fuentes y apariencia general
        de todos los elementos visuales de la aplicación.

        ¿Qué es ttk.Style?
        -----------------
        Es un objeto de tkinter que nos permite personalizar la apariencia
        de los widgets (botones, etiquetas, etc.)
        """
        # Crear objeto de estilo
        style = ttk.Style()

        # Usar el tema 'clam' (un tema moderno y limpio)
        style.theme_use('clam')

        # ========== CONFIGURAR COLORES Y FUENTES ==========

        # Configurar el fondo de los frames (contenedores)
        style.configure('TFrame', background='#f0f0f0')

        # Configurar las etiquetas (labels): fondo y fuente
        style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))

        # Configurar los botones: fuente
        style.configure('TButton', font=('Arial', 10))

        # Configurar etiquetas de encabezado: fuente más grande y negrita
        style.configure('Header.TLabel', font=('Arial', 14, 'bold'), background='#f0f0f0')

    def crear_menu(self):
        """
        Crear la barra de menú
        ======================

        Este método crea el menú que aparece en la parte superior de la ventana
        con opciones como Archivo, Proveedores, Reportes, etc.

        Estructura del menú:
        -------------------
        - Archivo: Guardar, Crear Backup, Salir
        - Proveedores: Gestionar Proveedores
        - Reportes: Productos Bajo Stock, Resumen, etc.
        - Ayuda: Acerca de
        """
        # Crear la barra de menú principal
        menubar = tk.Menu(self.root)

        # Asociar la barra de menú con la ventana principal
        self.root.config(menu=menubar)

        # ========== MENÚ ARCHIVO ==========

        # Crear el menú Archivo (tearoff=0 evita que se pueda separar del menú)
        menu_archivo = tk.Menu(menubar, tearoff=0)

        # Agregar el menú Archivo a la barra de menú
        menubar.add_cascade(label="Archivo", menu=menu_archivo)

        # Agregar opciones al menú Archivo
        menu_archivo.add_command(label="Guardar", command=self.guardar_inventario)
        menu_archivo.add_command(label="Crear Backup", command=self.crear_backup)
        menu_archivo.add_separator()  # Línea separadora
        menu_archivo.add_command(label="Salir", command=self.salir)

        # ========== MENÚ PROVEEDORES ==========

        menu_proveedores = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Proveedores", menu=menu_proveedores)
        menu_proveedores.add_command(label="Gestionar Proveedores", command=self.abrir_ventana_proveedores)

        # ========== MENÚ REPORTES ==========

        menu_reportes = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Reportes", menu=menu_reportes)
        menu_reportes.add_command(label="Productos Bajo Stock", command=self.mostrar_productos_bajo_stock)
        menu_reportes.add_command(label="Resumen Inventario", command=self.mostrar_resumen_inventario)
        menu_reportes.add_command(label="Productos por Proveedor", command=self.mostrar_productos_por_proveedor)

        # ========== MENÚ AYUDA ==========

        menu_ayuda = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_acerca_de)

    def crear_interfaz(self):
        """
        Crear la interfaz principal
        ===========================

        Este método crea todos los elementos visuales de la ventana principal:
        - El título
        - La barra de búsqueda
        - Los botones de acción
        - La tabla de productos
        - Las estadísticas en la parte inferior

        Sistema de Grid:
        ---------------
        Usamos el sistema "grid" para organizar los elementos en filas y columnas.
        Es como una tabla donde cada elemento ocupa una celda.
        """
        # ========== FRAME PRINCIPAL ==========

        # Crear el contenedor principal con padding (espaciado interno)
        frame_principal = ttk.Frame(self.root, padding="10")

        # Colocar el frame en la ventana usando grid
        # sticky=(tk.W, tk.E, tk.N, tk.S) hace que se expanda en todas direcciones
        frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # ========== CONFIGURAR EXPANSIÓN ==========

        # Configurar que la columna 0 de root se expanda horizontalmente
        self.root.columnconfigure(0, weight=1)

        # Configurar que la fila 0 de root se expanda verticalmente
        self.root.rowconfigure(0, weight=1)

        # Lo mismo para el frame principal
        frame_principal.columnconfigure(0, weight=1)
        frame_principal.rowconfigure(2, weight=1)  # La fila 2 es la tabla

        # ========== TÍTULO ==========

        # Crear etiqueta con el título usando el estilo Header
        titulo = ttk.Label(frame_principal, text="Sistema de Gestión de Inventario - AgroCol SAS",
                          style='Header.TLabel')
        titulo.grid(row=0, column=0, pady=10)

        # ========== FRAME DE BÚSQUEDA Y BOTONES ==========

        # Crear un contenedor para la búsqueda y botones
        frame_controles = ttk.Frame(frame_principal)
        frame_controles.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=10)

        # Etiqueta "Buscar:"
        ttk.Label(frame_controles, text="Buscar:").grid(row=0, column=0, padx=5)

        # Campo de texto para búsqueda
        self.entry_busqueda = ttk.Entry(frame_controles, width=30)
        self.entry_busqueda.grid(row=0, column=1, padx=5)

        # Asociar el evento KeyRelease (cuando se suelta una tecla) con buscar_productos
        # Esto hace que busque automáticamente mientras escribimos
        self.entry_busqueda.bind('<KeyRelease>', self.buscar_productos)

        # ========== BOTONES DE ACCIÓN ==========

        # Botón para agregar producto
        ttk.Button(frame_controles, text="Agregar Producto",
                  command=self.abrir_ventana_agregar_producto).grid(row=0, column=2, padx=5)

        # Botón para modificar producto
        ttk.Button(frame_controles, text="Modificar Producto",
                  command=self.modificar_producto).grid(row=0, column=3, padx=5)

        # Botón para eliminar producto
        ttk.Button(frame_controles, text="Eliminar Producto",
                  command=self.eliminar_producto).grid(row=0, column=4, padx=5)

        # Botón para agregar stock
        ttk.Button(frame_controles, text="Agregar Stock",
                  command=self.agregar_stock).grid(row=0, column=5, padx=5)

        # Botón para retirar stock
        ttk.Button(frame_controles, text="Retirar Stock",
                  command=self.retirar_stock).grid(row=0, column=6, padx=5)

        # ========== FRAME DE TABLA ==========

        # Crear contenedor para la tabla
        frame_tabla = ttk.Frame(frame_principal)
        frame_tabla.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        frame_tabla.columnconfigure(0, weight=1)
        frame_tabla.rowconfigure(0, weight=1)

        # ========== TABLA DE PRODUCTOS ==========

        # Definir las columnas de la tabla
        columnas = ("Código", "Nombre", "Cantidad", "Unidad", "Stock Mín", "Precio",
                   "Valor Total", "Proveedor", "Fecha Ingreso")

        # Crear el Treeview (tabla)
        # show='headings' oculta la primera columna (que sería el identificador)
        self.tabla_productos = ttk.Treeview(frame_tabla, columns=columnas, show='headings',
                                           height=15)

        # Configurar cada columna: encabezado y ancho
        anchos = [80, 150, 80, 80, 80, 100, 120, 120, 100]
        for col, ancho in zip(columnas, anchos):
            # Configurar el texto del encabezado
            self.tabla_productos.heading(col, text=col)
            # Configurar el ancho de la columna
            self.tabla_productos.column(col, width=ancho)

        # ========== SCROLLBARS (BARRAS DE DESPLAZAMIENTO) ==========

        # Scrollbar vertical
        scrollbar_y = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL,
                                   command=self.tabla_productos.yview)

        # Scrollbar horizontal
        scrollbar_x = ttk.Scrollbar(frame_tabla, orient=tk.HORIZONTAL,
                                   command=self.tabla_productos.xview)

        # Configurar la tabla para usar los scrollbars
        self.tabla_productos.configure(yscrollcommand=scrollbar_y.set,
                                      xscrollcommand=scrollbar_x.set)

        # Colocar la tabla y scrollbars en el frame
        self.tabla_productos.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar_y.grid(row=0, column=1, sticky=(tk.N, tk.S))
        scrollbar_x.grid(row=1, column=0, sticky=(tk.W, tk.E))

        # ========== FRAME DE ESTADÍSTICAS ==========

        # Crear contenedor para las estadísticas en la parte inferior
        frame_estadisticas = ttk.Frame(frame_principal)
        frame_estadisticas.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=10)

        # Etiqueta: Total de productos
        self.label_total_productos = ttk.Label(frame_estadisticas,
                                              text="Total de productos: 0")
        self.label_total_productos.grid(row=0, column=0, padx=10)

        # Etiqueta: Valor total del inventario
        self.label_valor_inventario = ttk.Label(frame_estadisticas,
                                               text="Valor total del inventario: $0.00")
        self.label_valor_inventario.grid(row=0, column=1, padx=10)

        # Etiqueta: Productos bajo stock (en rojo para llamar la atención)
        self.label_alertas = ttk.Label(frame_estadisticas,
                                       text="Productos bajo stock: 0",
                                       foreground='red')
        self.label_alertas.grid(row=0, column=2, padx=10)

    def actualizar_tabla_productos(self, productos: list = None):
        """
        Actualizar la tabla de productos
        =================================

        Este método actualiza la tabla mostrando los productos del inventario.

        Parámetros:
        ----------
        productos : list, opcional
            Lista de productos a mostrar. Si es None, muestra todos los productos.

        ¿Qué hace?
        ----------
        1. Limpia todos los elementos actuales de la tabla
        2. Obtiene la lista de productos a mostrar
        3. Por cada producto, crea una fila en la tabla
        4. Si un producto está bajo stock, lo marca en rojo
        5. Actualiza las estadísticas
        """
        # ========== LIMPIAR TABLA ==========

        # Eliminar todos los elementos actuales de la tabla
        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        # ========== OBTENER PRODUCTOS A MOSTRAR ==========

        # Si no se especificó una lista, obtener todos los productos
        if productos is None:
            productos = self.inventario.listar_productos()

        # ========== AGREGAR PRODUCTOS A LA TABLA ==========

        # Por cada producto en la lista
        for producto in productos:
            # Crear tupla con los valores a mostrar en cada columna
            valores = (
                producto.codigo,
                producto.nombre,
                f"{producto.cantidad:.2f}",  # :.2f formatea a 2 decimales
                producto.unidad_medida,
                f"{producto.stock_minimo:.2f}",
                f"${producto.precio_costo:,.2f}",  # :,.2f agrega comas como separador de miles
                f"${producto.valor_total_inventario():,.2f}",
                producto.proveedor.nombre,
                producto.fecha_ingreso
            )

            # Verificar si el producto está bajo stock
            if producto.esta_bajo_stock():
                # Insertar fila con tag 'bajo_stock' para colorearla
                item = self.tabla_productos.insert('', 'end', values=valores, tags=('bajo_stock',))
            else:
                # Insertar fila normal
                item = self.tabla_productos.insert('', 'end', values=valores)

        # ========== CONFIGURAR COLORES ==========

        # Configurar el color de fondo para filas con tag 'bajo_stock'
        self.tabla_productos.tag_configure('bajo_stock', background='#ffcccc')

        # ========== ACTUALIZAR ESTADÍSTICAS ==========

        self.actualizar_estadisticas()

    def actualizar_estadisticas(self):
        """
        Actualizar las etiquetas de estadísticas
        =========================================

        Actualiza los textos en la parte inferior de la ventana con:
        - Total de productos
        - Valor total del inventario
        - Cantidad de productos bajo stock
        """
        # Obtener los valores actuales del inventario
        total_productos = self.inventario.obtener_cantidad_total_productos()
        valor_total = self.inventario.obtener_valor_total_inventario()
        productos_bajo_stock = len(self.inventario.obtener_productos_bajo_stock())

        # Actualizar el texto de cada etiqueta
        self.label_total_productos.config(text=f"Total de productos: {total_productos}")
        self.label_valor_inventario.config(text=f"Valor total del inventario: ${valor_total:,.2f}")
        self.label_alertas.config(text=f"Productos bajo stock: {productos_bajo_stock}")

    def buscar_productos(self, event=None):
        """
        Buscar productos según el término ingresado
        ===========================================

        Este método se ejecuta cada vez que se presiona una tecla en el campo de búsqueda.

        Parámetros:
        ----------
        event : Event, opcional
            El evento de teclado (lo proporciona tkinter automáticamente)
        """
        # Obtener el texto del campo de búsqueda
        termino = self.entry_busqueda.get()

        # Si el campo está vacío, mostrar todos los productos
        if termino.strip() == "":
            self.actualizar_tabla_productos()
        else:
            # Buscar productos que coincidan con el término
            productos = self.inventario.buscar_productos(termino)
            # Actualizar la tabla solo con los productos encontrados
            self.actualizar_tabla_productos(productos)

    def abrir_ventana_agregar_producto(self):
        """
        Abrir la ventana para agregar un nuevo producto
        ===============================================

        Crea una nueva instancia de VentanaProducto sin pasar un producto existente,
        lo que indica que queremos crear un producto nuevo.
        """
        # Importar aquí para evitar importación circular
        from ventana_producto import VentanaProducto

        # Crear ventana de producto (None = nuevo producto)
        VentanaProducto(self.root, self, None)

    def modificar_producto(self):
        """
        Modificar el producto seleccionado
        ==================================

        Abre la ventana de producto con los datos del producto seleccionado
        en la tabla para poder modificarlo.
        """
        # Importar aquí para evitar importación circular
        from ventana_producto import VentanaProducto

        # Obtener el elemento seleccionado en la tabla
        seleccion = self.tabla_productos.selection()

        # Si no hay nada seleccionado, mostrar advertencia
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un producto para modificar")
            return

        # Obtener los datos del elemento seleccionado
        item = self.tabla_productos.item(seleccion[0])

        # El código del producto está en la primera columna (índice 0)
        codigo = item['values'][0]

        # Buscar el producto en el inventario
        producto = self.inventario.obtener_producto(codigo)

        # Si se encontró el producto, abrir ventana de edición
        if producto:
            VentanaProducto(self.root, self, producto)

    def eliminar_producto(self):
        """
        Eliminar el producto seleccionado
        =================================

        Elimina permanentemente el producto seleccionado del inventario
        después de confirmar con el usuario.
        """
        # Obtener selección
        seleccion = self.tabla_productos.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un producto para eliminar")
            return

        # Obtener datos del producto
        item = self.tabla_productos.item(seleccion[0])
        codigo = item['values'][0]
        nombre = item['values'][1]

        # Confirmar antes de eliminar
        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el producto '{nombre}'?"):
            try:
                # Eliminar del inventario
                self.inventario.eliminar_producto(codigo)

                # Guardar cambios
                self.guardar_inventario()

                # Actualizar tabla
                self.actualizar_tabla_productos()

                # Mostrar mensaje de éxito
                messagebox.showinfo("Éxito", "Producto eliminado correctamente")
            except Exception as e:
                # Si hay error, mostrarlo
                messagebox.showerror("Error", f"Error al eliminar producto: {str(e)}")

    def agregar_stock(self):
        """
        Agregar stock al producto seleccionado
        ======================================

        Permite incrementar la cantidad disponible de un producto.
        """
        # Obtener selección
        seleccion = self.tabla_productos.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un producto")
            return

        # Obtener producto
        item = self.tabla_productos.item(seleccion[0])
        codigo = item['values'][0]
        producto = self.inventario.obtener_producto(codigo)

        if producto:
            # Preguntar cuánto stock agregar
            cantidad = simpledialog.askfloat("Agregar Stock",
                                            f"Ingrese la cantidad a agregar ({producto.unidad_medida}):",
                                            minvalue=0.01)
            if cantidad:
                try:
                    # Agregar stock al producto
                    producto.agregar_stock(cantidad)

                    # Guardar y actualizar
                    self.guardar_inventario()
                    self.actualizar_tabla_productos()

                    messagebox.showinfo("Éxito", f"Se agregaron {cantidad} {producto.unidad_medida}")
                except Exception as e:
                    messagebox.showerror("Error", str(e))

    def retirar_stock(self):
        """
        Retirar stock del producto seleccionado
        =======================================

        Permite disminuir la cantidad disponible de un producto.
        """
        # Obtener selección
        seleccion = self.tabla_productos.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un producto")
            return

        # Obtener producto
        item = self.tabla_productos.item(seleccion[0])
        codigo = item['values'][0]
        producto = self.inventario.obtener_producto(codigo)

        if producto:
            # Preguntar cuánto stock retirar
            cantidad = simpledialog.askfloat("Retirar Stock",
                                            f"Ingrese la cantidad a retirar ({producto.unidad_medida}):\n"
                                            f"Disponible: {producto.cantidad}",
                                            minvalue=0.01)
            if cantidad:
                try:
                    # Retirar stock del producto
                    producto.retirar_stock(cantidad)

                    # Guardar y actualizar
                    self.guardar_inventario()
                    self.actualizar_tabla_productos()
                    self.verificar_alertas_stock()

                    messagebox.showinfo("Éxito", f"Se retiraron {cantidad} {producto.unidad_medida}")
                except Exception as e:
                    messagebox.showerror("Error", str(e))

    def abrir_ventana_proveedores(self):
        """
        Abrir la ventana de gestión de proveedores
        ==========================================

        Crea una nueva ventana donde se pueden ver, agregar y eliminar proveedores.
        """
        # Importar aquí para evitar importación circular
        from ventana_proveedor import VentanaProveedores

        VentanaProveedores(self.root, self)

    def mostrar_productos_bajo_stock(self):
        """
        Mostrar reporte de productos bajo stock
        ========================================

        Crea una ventana emergente con una tabla mostrando todos los productos
        que tienen una cantidad menor a su stock mínimo.
        """
        # Obtener productos bajo stock
        productos = self.inventario.obtener_productos_bajo_stock()

        # Si no hay productos bajo stock
        if not productos:
            messagebox.showinfo("Reporte", "No hay productos bajo stock")
            return

        # Crear ventana emergente
        ventana = tk.Toplevel(self.root)
        ventana.title("Productos Bajo Stock")
        ventana.geometry("900x400")

        frame = ttk.Frame(ventana, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        # Crear tabla
        columnas = ("Código", "Nombre", "Cantidad", "Stock Mínimo", "Unidad", "Proveedor")
        tabla = ttk.Treeview(frame, columns=columnas, show='headings')

        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=120)

        # Llenar tabla con productos
        for producto in productos:
            valores = (
                producto.codigo,
                producto.nombre,
                f"{producto.cantidad:.2f}",
                f"{producto.stock_minimo:.2f}",
                producto.unidad_medida,
                producto.proveedor.nombre
            )
            tabla.insert('', 'end', values=valores)

        # Agregar scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
        tabla.configure(yscrollcommand=scrollbar.set)

        tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def mostrar_resumen_inventario(self):
        """
        Mostrar resumen del inventario
        ==============================

        Muestra un cuadro de diálogo con estadísticas generales del inventario.
        """
        # Obtener estadísticas
        total_productos = self.inventario.obtener_cantidad_total_productos()
        valor_total = self.inventario.obtener_valor_total_inventario()
        productos_bajo_stock = len(self.inventario.obtener_productos_bajo_stock())
        total_proveedores = len(self.inventario.listar_proveedores())

        # Crear mensaje con formato
        mensaje = f"""
RESUMEN DEL INVENTARIO - AgroCol SAS
{'='*50}

Total de productos registrados: {total_productos}
Total de proveedores: {total_proveedores}
Productos bajo stock: {productos_bajo_stock}

Valor total del inventario: ${valor_total:,.2f}

Fecha del reporte: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
        """

        messagebox.showinfo("Resumen del Inventario", mensaje)

    def mostrar_productos_por_proveedor(self):
        """
        Mostrar productos agrupados por proveedor
        =========================================

        Crea una ventana que permite seleccionar un proveedor y ver
        todos sus productos asociados.
        """
        # Obtener lista de proveedores
        proveedores = self.inventario.listar_proveedores()

        if not proveedores:
            messagebox.showinfo("Reporte", "No hay proveedores registrados")
            return

        # Crear ventana
        ventana = tk.Toplevel(self.root)
        ventana.title("Productos por Proveedor")
        ventana.geometry("400x300")

        frame = ttk.Frame(ventana, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Seleccione un proveedor:").pack(pady=5)

        # Crear lista de proveedores
        lista_proveedores = tk.Listbox(frame)
        lista_proveedores.pack(fill=tk.BOTH, expand=True, pady=5)

        # Llenar lista
        for proveedor in proveedores:
            productos = self.inventario.obtener_productos_por_proveedor(proveedor.id_proveedor)
            lista_proveedores.insert(tk.END, f"{proveedor.nombre} ({len(productos)} productos)")

        def mostrar_detalle():
            """Función interna para mostrar detalle del proveedor seleccionado"""
            seleccion = lista_proveedores.curselection()
            if seleccion:
                proveedor = proveedores[seleccion[0]]
                productos = self.inventario.obtener_productos_por_proveedor(proveedor.id_proveedor)

                detalle = f"Productos de {proveedor.nombre}\n{'='*50}\n\n"
                for p in productos:
                    detalle += f"- {p.nombre} ({p.codigo}): {p.cantidad} {p.unidad_medida}\n"

                messagebox.showinfo("Detalle", detalle)

        ttk.Button(frame, text="Ver Detalle", command=mostrar_detalle).pack(pady=5)

    def verificar_alertas_stock(self):
        """
        Verificar y mostrar alertas de stock bajo
        =========================================

        Muestra una advertencia si hay productos con stock bajo.
        Se ejecuta al iniciar la aplicación y después de retirar stock.
        """
        productos_bajo_stock = self.inventario.obtener_productos_bajo_stock()

        if productos_bajo_stock:
            mensaje = "Los siguientes productos están bajo stock:\n\n"

            # Mostrar solo los primeros 5 para no saturar
            for producto in productos_bajo_stock[:5]:
                mensaje += f"- {producto.nombre}: {producto.cantidad} {producto.unidad_medida}\n"

            if len(productos_bajo_stock) > 5:
                mensaje += f"\n... y {len(productos_bajo_stock) - 5} más"

            messagebox.showwarning("Alerta de Stock Bajo", mensaje)

    def guardar_inventario(self):
        """
        Guardar el inventario en el archivo
        ===================================

        Usa el gestor de persistencia para guardar todos los datos
        del inventario en el archivo JSON.

        Retorna:
        -------
        bool
            True si se guardó correctamente, False si hubo error
        """
        if self.gestor_persistencia.guardar_inventario(self.inventario):
            return True
        else:
            messagebox.showerror("Error", "No se pudo guardar el inventario")
            return False

    def crear_backup(self):
        """
        Crear un backup del inventario
        ==============================

        Crea una copia de seguridad del archivo de inventario con la fecha actual.
        """
        if self.gestor_persistencia.crear_backup():
            messagebox.showinfo("Éxito", "Backup creado correctamente")
        else:
            messagebox.showerror("Error", "No se pudo crear el backup")

    def mostrar_acerca_de(self):
        """
        Mostrar información sobre la aplicación
        =======================================

        Muestra un cuadro de diálogo con información sobre el sistema.
        """
        mensaje = """
Sistema de Gestión de Inventario
AgroCol SAS

Versión: 1.0
Desarrollado para optimizar la gestión de inventarios
en el sector agrícola

Características:
- Gestión completa de productos e insumos
- Alertas de stock bajo
- Reportes y estadísticas
- Almacenamiento local (sin internet)
        """
        messagebox.showinfo("Acerca de", mensaje)

    def salir(self):
        """
        Cerrar la aplicación
        ===================

        Pregunta si desea guardar antes de salir y cierra la aplicación.
        """
        if messagebox.askyesno("Salir", "¿Desea guardar antes de salir?"):
            self.guardar_inventario()

        # Cerrar la aplicación
        self.root.quit()
