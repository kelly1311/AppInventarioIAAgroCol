# 📚 Estructura del Proyecto - Sistema AgroCol SAS

## 📋 Índice
1. [Introducción](#introducción)
2. [Estructura de Archivos](#estructura-de-archivos)
3. [Descripción de Módulos](#descripción-de-módulos)
4. [Conceptos de POO Aplicados](#conceptos-de-poo-aplicados)
5. [Flujo de Ejecución](#flujo-de-ejecución)
6. [Cómo Ejecutar el Proyecto](#cómo-ejecutar-el-proyecto)

---

## 🎯 Introducción

Este documento explica la organización del código del **Sistema de Gestión de Inventario AgroCol SAS**, diseñado para estudiantes de segundo semestre de Ingeniería en Desarrollo de Software.

El proyecto aplica principios de **Programación Orientada a Objetos (POO)** y buenas prácticas de organización de código.

---

## 📁 Estructura de Archivos

```
app/
│
├── 🎯 MÓDULOS DE DOMINIO (Clases principales)
│   ├── proveedor.py          # Clase Proveedor
│   ├── producto.py           # Clase Producto
│   ├── inventario.py         # Clase Inventario
│   └── usuario.py            # Clases Usuario, Cajero, Administrador
│
├── 💾 PERSISTENCIA DE DATOS
│   └── persistencia.py       # Clase GestorPersistencia
│
├── 🖥️ INTERFAZ GRÁFICA
│   ├── interfaz.py           # Punto de entrada de interfaz (re-exporta clases)
│   ├── ventana_principal.py  # Clase VentanaPrincipal
│   ├── ventana_producto.py   # Clase VentanaProducto
│   └── ventana_proveedor.py  # Clases VentanaProveedorSimple, VentanaProveedores
│
├── 🚀 EJECUCIÓN
│   ├── main.py               # Punto de entrada principal
│   └── ejemplo_datos.py      # Script para crear datos de prueba
│
├── 📄 DATOS
│   └── inventario_agrocol.json  # Archivo JSON con datos del inventario
│
└── 📚 DOCUMENTACIÓN
    ├── README.md             # Documentación principal
    ├── README_ESTRUCTURA.md  # Este archivo
    ├── DIAGRAMA_CLASES.txt   # Diagrama de clases
    └── INICIO_RAPIDO.txt     # Guía de inicio rápido
```

---

## 📖 Descripción de Módulos

### 🎯 MÓDULOS DE DOMINIO

#### **proveedor.py**
- **Clase:** `Proveedor`
- **Propósito:** Representar un proveedor de productos agrícolas
- **Atributos:**
  - `_id_proveedor`: Identificador único
  - `_nombre`: Nombre del proveedor
  - `_telefono`: Teléfono de contacto
  - `_email`: Correo electrónico
- **Métodos principales:**
  - Getters y Setters (propiedades)
  - `to_dict()`: Convierte a diccionario
  - `from_dict()`: Crea instancia desde diccionario

#### **producto.py**
- **Clase:** `Producto`
- **Propósito:** Representar un producto o insumo agrícola
- **Atributos:**
  - `_codigo`: Código único del producto
  - `_nombre`: Nombre del producto
  - `_unidad_medida`: Unidad (kg, litro, etc.)
  - `_fecha_ingreso`: Fecha de ingreso
  - `_proveedor`: Objeto Proveedor (composición)
  - `_precio_costo`: Precio unitario
  - `_cantidad`: Stock actual
  - `_stock_minimo`: Cantidad mínima requerida
- **Métodos principales:**
  - `agregar_stock()`: Incrementa cantidad
  - `retirar_stock()`: Disminuye cantidad
  - `esta_bajo_stock()`: Verifica si hay stock bajo
  - `valor_total_inventario()`: Calcula valor total

#### **inventario.py**
- **Clase:** `Inventario`
- **Propósito:** Gestionar colección de productos y proveedores
- **Atributos:**
  - `_productos`: Diccionario de productos {codigo: producto}
  - `_proveedores`: Diccionario de proveedores {id: proveedor}
- **Métodos principales:**
  - `agregar_producto()`, `eliminar_producto()`, `actualizar_producto()`
  - `agregar_proveedor()`, `obtener_proveedor()`
  - `buscar_productos()`: Búsqueda por término
  - `obtener_productos_bajo_stock()`: Productos con stock bajo
  - `obtener_valor_total_inventario()`: Valor total del inventario

#### **usuario.py**
- **Clases:** `Usuario`, `Cajero`, `Administrador`
- **Propósito:** Gestionar usuarios del sistema con diferentes roles
- **Concepto aplicado:** **HERENCIA**
  - `Usuario` es la clase padre
  - `Cajero` y `Administrador` heredan de `Usuario`
- **Atributos de Usuario:**
  - `_id_usuario`: Identificador único
  - `_nombre`: Nombre completo
  - `_usuario`: Nombre de usuario (login)
  - `_contrasena`: Contraseña
  - `_rol`: Rol del usuario
- **Métodos específicos:**
  - **Cajero:** `realizar_venta()`, `consultar_producto()`
  - **Administrador:** `agregar_usuario()`, `eliminar_usuario()`, `generar_reporte_completo()`

---

### 💾 PERSISTENCIA DE DATOS

#### **persistencia.py**
- **Clase:** `GestorPersistencia`
- **Propósito:** Guardar y cargar datos en formato JSON
- **Métodos principales:**
  - `guardar_inventario()`: Guarda en JSON
  - `cargar_inventario()`: Carga desde JSON
  - `crear_backup()`: Crea copia de seguridad
  - `existe_archivo()`: Verifica existencia del archivo

---

### 🖥️ INTERFAZ GRÁFICA

#### **interfaz.py**
- **Propósito:** Punto de entrada centralizado que re-exporta todas las clases de ventanas
- **Contenido:** Importaciones y re-exportaciones
- **Ventaja:** Permite hacer `from interfaz import VentanaPrincipal` sin conocer el archivo específico

#### **ventana_principal.py**
- **Clase:** `VentanaPrincipal`
- **Propósito:** Ventana principal de la aplicación
- **Componentes:**
  - Menú de navegación (Archivo, Proveedores, Reportes, Ayuda)
  - Barra de búsqueda
  - Tabla de productos (Treeview)
  - Botones de acción (Agregar, Modificar, Eliminar, etc.)
  - Panel de estadísticas
- **Responsabilidades:**
  - Mostrar inventario completo
  - Gestionar operaciones CRUD de productos
  - Generar reportes
  - Guardar/Cargar datos

#### **ventana_producto.py**
- **Clase:** `VentanaProducto`
- **Propósito:** Ventana modal para agregar/modificar productos
- **Componentes:**
  - Formulario con todos los campos del producto
  - Combo de proveedores
  - Botón para agregar nuevo proveedor
  - Validaciones de datos
- **Uso:**
  - Agregar nuevo producto: `VentanaProducto(parent, ventana_principal, None)`
  - Modificar existente: `VentanaProducto(parent, ventana_principal, producto)`

#### **ventana_proveedor.py**
- **Clases:** `VentanaProveedorSimple`, `VentanaProveedores`
- **Propósito:** Gestión de proveedores
- **VentanaProveedorSimple:**
  - Formulario simple para agregar proveedor rápidamente
  - Usado desde VentanaProducto
- **VentanaProveedores:**
  - Ventana completa para gestionar todos los proveedores
  - Tabla con lista de proveedores
  - Agregar/Eliminar proveedores

---

### 🚀 EJECUCIÓN

#### **main.py**
- **Propósito:** Punto de entrada principal de la aplicación
- **Función:** `main()`
- **Flujo:**
  1. Crea ventana raíz de tkinter
  2. Instancia VentanaPrincipal
  3. Configura protocolo de cierre
  4. Inicia bucle de eventos (`mainloop()`)

#### **ejemplo_datos.py**
- **Propósito:** Crear datos de prueba
- **Contenido:** 5 proveedores y 22 productos de ejemplo
- **Uso:** `python ejemplo_datos.py`
- **Ventaja:** Permite probar la aplicación con datos reales

---

## 🧩 Conceptos de POO Aplicados

### 1️⃣ **ENCAPSULAMIENTO**
```python
class Proveedor:
    def __init__(self, id_proveedor, nombre):
        self._id_proveedor = id_proveedor  # Atributo privado
        self._nombre = nombre               # Atributo privado

    @property
    def nombre(self):                       # Getter
        return self._nombre

    @nombre.setter
    def nombre(self, valor):                # Setter con validación
        if not valor:
            raise ValueError("Nombre vacío")
        self._nombre = valor
```
**Dónde:** `proveedor.py`, `producto.py`, `inventario.py`, `usuario.py`

### 2️⃣ **HERENCIA**
```python
class Usuario:                           # Clase padre
    def __init__(self, id, nombre, ...):
        self._id_usuario = id
        # ...

class Cajero(Usuario):                   # Clase hija
    def __init__(self, id, nombre, ..., caja_asignada):
        super().__init__(id, nombre, ...) # Llama constructor padre
        self._caja_asignada = caja_asignada

    def realizar_venta(self):            # Método específico
        # ...
```
**Dónde:** `usuario.py` (Usuario → Cajero, Administrador)

### 3️⃣ **COMPOSICIÓN**
```python
class Producto:
    def __init__(self, codigo, nombre, ..., proveedor):
        self._codigo = codigo
        self._proveedor = proveedor    # Producto "tiene un" Proveedor
```
**Dónde:**
- `producto.py` (Producto tiene un Proveedor)
- `inventario.py` (Inventario tiene muchos Productos)

### 4️⃣ **POLIMORFISMO**
```python
# Todas las clases tienen to_dict() con diferente implementación
proveedor.to_dict()  # Retorna dict de proveedor
producto.to_dict()   # Retorna dict de producto (incluye proveedor)
inventario.to_dict() # Retorna dict completo con productos y proveedores
```
**Dónde:** Todas las clases del dominio

### 5️⃣ **ABSTRACCIÓN**
```python
# El usuario no necesita saber cómo funciona JSON internamente
gestor = GestorPersistencia()
gestor.guardar_inventario(inventario)  # Abstrae la complejidad
```
**Dónde:** `persistencia.py`

---

## 🔄 Flujo de Ejecución

### Inicio de la Aplicación

```
1. Usuario ejecuta: python main.py
         ↓
2. main.py crea ventana raíz tkinter
         ↓
3. main.py crea VentanaPrincipal
         ↓
4. VentanaPrincipal.__init__()
   ├── Crea GestorPersistencia
   ├── Carga inventario desde JSON
   ├── Crea interfaz (menú, tabla, botones)
   └── Muestra datos iniciales
         ↓
5. root.mainloop() - Bucle de eventos
   ├── Espera interacción del usuario
   ├── Procesa eventos (clics, teclas)
   └── Actualiza interfaz
```

### Agregar un Producto

```
1. Usuario clic en "Agregar Producto"
         ↓
2. VentanaPrincipal.abrir_ventana_agregar_producto()
         ↓
3. VentanaProducto(parent, ventana_principal, None)
   ├── Crea formulario
   ├── Carga combo de proveedores
   └── Espera datos del usuario
         ↓
4. Usuario llena formulario y clic "Guardar"
         ↓
5. VentanaProducto.guardar()
   ├── Valida datos
   ├── Crea objeto Producto
   ├── inventario.agregar_producto(producto)
   ├── gestor.guardar_inventario()
   └── Actualiza tabla en VentanaPrincipal
```

### Flujo de Datos

```
Usuario → Interfaz → Inventario → GestorPersistencia → JSON
  ↑                                                      ↓
  └──────────────────← Carga ←──────────────────────────┘
```

---

## 🚀 Cómo Ejecutar el Proyecto

### Requisitos Previos
- Python 3.8 o superior
- Tkinter (incluido con Python)

### Paso 1: Crear Datos de Ejemplo (Opcional)
```bash
python ejemplo_datos.py
```
Esto crea un inventario con 22 productos y 5 proveedores de prueba.

### Paso 2: Ejecutar la Aplicación
```bash
python main.py
```

### Paso 3: Usar la Aplicación
1. **Buscar productos:** Escribe en la barra de búsqueda
2. **Agregar producto:** Clic en "Agregar Producto"
3. **Modificar producto:** Selecciona producto y clic "Modificar"
4. **Eliminar producto:** Selecciona producto y clic "Eliminar"
5. **Agregar/Retirar stock:** Selecciona producto y usa los botones
6. **Gestionar proveedores:** Menú → Proveedores → Gestionar
7. **Ver reportes:** Menú → Reportes
8. **Guardar:** Menú → Archivo → Guardar (se guarda automáticamente)

---

## 📊 Diagrama de Relaciones

```
┌─────────────────────────────────────────────────────┐
│                     main.py                         │
│                 (Punto de entrada)                  │
└────────────────────┬────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────┐
│               VentanaPrincipal                      │
│           (Interfaz gráfica principal)              │
└─────┬──────────────┬──────────────┬─────────────────┘
      │              │              │
      ↓              ↓              ↓
┌─────────────┐ ┌─────────────┐ ┌──────────────────┐
│VentanaProducto│ │VentanaProveedor│ │GestorPersistencia│
└──────┬──────┘ └──────┬──────┘ └────────┬─────────┘
       │               │                  │
       ↓               ↓                  ↓
┌─────────────────────────────────────────────────────┐
│                  Inventario                         │
│         (Gestiona productos y proveedores)          │
└─────────────────┬────────────────┬──────────────────┘
                  │                │
                  ↓                ↓
         ┌────────────┐    ┌──────────────┐
         │  Producto  │    │  Proveedor   │
         └──────┬─────┘    └──────────────┘
                │
                └──────→ Tiene un Proveedor (composición)
```

---

## 📝 Notas para Estudiantes

### Buenas Prácticas Aplicadas

✅ **Separación de responsabilidades:** Cada clase tiene un propósito específico
✅ **Código modular:** Cada clase en su propio archivo
✅ **Comentarios explicativos:** Documentación clara en español
✅ **Nombres descriptivos:** Variables y funciones con nombres significativos
✅ **Validaciones:** Verificar datos antes de guardar
✅ **Manejo de errores:** Try-except para capturar excepciones
✅ **Principios SOLID:** Responsabilidad única, abierto/cerrado

### Ejercicios Sugeridos

1. **Modificar:** Agrega un nuevo atributo a Producto (ej: categoría)
2. **Extender:** Crea una clase nueva que herede de Usuario (ej: Supervisor)
3. **Implementar:** Agrega un método para generar reportes en PDF
4. **Mejorar:** Agrega validación de email en Proveedor
5. **Crear:** Implementa una ventana de login usando Usuario/Cajero/Administrador

---

## 🆘 Solución de Problemas Comunes

### Error: "ModuleNotFoundError"
**Problema:** Python no encuentra un módulo
**Solución:** Asegúrate de estar en el directorio correcto (`app/`)

### Error: "FileNotFoundError"
**Problema:** No encuentra el archivo JSON
**Solución:** Ejecuta `python ejemplo_datos.py` para crear el archivo

### Error: "TypeError" al abrir ventanas
**Problema:** Imports incorrectos
**Solución:** Verifica que todos los archivos estén en el mismo directorio

---

## 📚 Recursos Adicionales

- [Documentación oficial de Python](https://docs.python.org/es/3/)
- [Tutorial de tkinter](https://docs.python.org/es/3/library/tkinter.html)
- [JSON en Python](https://docs.python.org/es/3/library/json.html)
- [POO en Python](https://docs.python.org/es/3/tutorial/classes.html)

---

**Autor:** Estudiante de Ingeniería en Desarrollo de Software
**Semestre:** 2
**Año:** 2025
**Proyecto:** Sistema de Gestión de Inventario AgroCol SAS
