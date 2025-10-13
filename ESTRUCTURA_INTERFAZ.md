# Estructura del Módulo de Interfaz - AgroCol SAS

## Resumen de Cambios

El archivo `interfaz.py` ha sido reorganizado para mejorar la mantenibilidad y organización del código. Anteriormente, todas las clases de interfaz (818 líneas) estaban en un solo archivo. Ahora están separadas en archivos individuales según su responsabilidad.

---

## Nueva Estructura

```
interfaz/
├── interfaz.py                 (161 líneas) - Archivo de importación y re-exportación
├── ventana_principal.py        (882 líneas) - Ventana principal de la aplicación
├── ventana_producto.py         (466 líneas) - Ventana para productos
└── ventana_proveedor.py        (513 líneas) - Ventanas para proveedores
```

**Total**: 2,022 líneas (distribuidas en 4 archivos)

---

## Descripción de Archivos

### 1. `interfaz.py`
**Propósito**: Punto de entrada centralizado para todas las clases de interfaz.

**Contenido**:
- Importa todas las clases de los archivos individuales
- Re-exporta las clases para uso externo
- Documentación de cada clase disponible

**Uso**:
```python
from interfaz import VentanaPrincipal, VentanaProducto
```

---

### 2. `ventana_principal.py`
**Propósito**: Ventana principal de la aplicación.

**Clase**: `VentanaPrincipal`

**Responsabilidades**:
- Mostrar el inventario completo en una tabla
- Permitir buscar productos
- Gestionar productos (agregar, modificar, eliminar)
- Gestionar stock (agregar, retirar)
- Mostrar estadísticas del inventario
- Generar reportes
- Guardar y cargar datos

**Características destacadas**:
- Sistema de menú completo (Archivo, Proveedores, Reportes, Ayuda)
- Tabla interactiva con colores para productos bajo stock
- Búsqueda en tiempo real
- Alertas automáticas de stock bajo
- Sistema de estadísticas en tiempo real

---

### 3. `ventana_producto.py`
**Propósito**: Ventana para agregar o modificar productos.

**Clase**: `VentanaProducto`

**Responsabilidades**:
- Mostrar formulario de producto
- Validar datos ingresados
- Crear productos nuevos
- Modificar productos existentes
- Permitir agregar proveedores desde la ventana

**Características destacadas**:
- Modo dual: agregar/modificar (según parámetros)
- Validación de datos numéricos
- Combo de proveedores con actualización automática
- Fecha de ingreso por defecto (fecha actual)
- Botón para agregar proveedor sin salir de la ventana

**Campos del formulario**:
- Código (readonly en modo modificar)
- Nombre
- Cantidad
- Unidad de medida (combo con opciones: kg, ton, unidad, litro, bulto, caja, m3)
- Stock mínimo
- Precio de costo
- Proveedor (combo con búsqueda)
- Fecha de ingreso

---

### 4. `ventana_proveedor.py`
**Propósito**: Gestión de proveedores.

**Clases**:
- `VentanaProveedorSimple`
- `VentanaProveedores`

#### Clase: `VentanaProveedorSimple`
**Responsabilidades**:
- Formulario simple para agregar proveedor
- Validar datos del proveedor
- Actualizar combo de proveedores en ventana origen

**Uso**: Se abre desde VentanaProducto o VentanaProveedores

**Campos**:
- ID Proveedor (obligatorio)
- Nombre (obligatorio)
- Teléfono (opcional)
- Email (opcional)

#### Clase: `VentanaProveedores`
**Responsabilidades**:
- Mostrar tabla con todos los proveedores
- Mostrar cantidad de productos por proveedor
- Permitir agregar nuevos proveedores
- Permitir eliminar proveedores (solo sin productos)

**Características**:
- Tabla con 5 columnas: ID, Nombre, Teléfono, Email, Productos
- Validación: no se puede eliminar si tiene productos asociados
- Integración con VentanaProveedorSimple

---

## Ventajas de la Nueva Estructura

### 1. **Organización y Mantenibilidad**
- Cada archivo tiene una responsabilidad clara
- Más fácil encontrar y modificar código específico
- Archivos más pequeños y manejables

### 2. **Escalabilidad**
- Fácil agregar nuevas ventanas sin afectar las existentes
- Cada ventana se puede modificar independientemente

### 3. **Claridad del Código**
- Nombres de archivo descriptivos
- Estructura lógica que refleja la funcionalidad
- Comentarios detallados en cada archivo

### 4. **Trabajo en Equipo**
- Varios desarrolladores pueden trabajar en ventanas diferentes
- Menos conflictos en control de versiones (git)
- Más fácil revisar cambios específicos

### 5. **Principios de POO**
- **Responsabilidad Única**: Cada clase/archivo tiene una sola responsabilidad
- **Bajo Acoplamiento**: Las clases están conectadas mínimamente
- **Alta Cohesión**: El código relacionado está junto

---

## Diagrama de Dependencias

```
main.py
    ↓
interfaz.py (re-exporta)
    ↓
    ├── ventana_principal.py
    │       ↓
    │       ├── ventana_producto.py
    │       │       ↓
    │       │       └── ventana_proveedor.py (VentanaProveedorSimple)
    │       │
    │       └── ventana_proveedor.py (VentanaProveedores)
    │               ↓
    │               └── ventana_proveedor.py (VentanaProveedorSimple)
    │
    └── Módulos de negocio
            ├── inventario.py
            ├── producto.py
            ├── proveedor.py
            └── persistencia.py
```

---

## Flujo de Navegación del Usuario

```
1. INICIO
   └─> VentanaPrincipal (ventana_principal.py)
        │
        ├─> Agregar Producto
        │   └─> VentanaProducto (ventana_producto.py)
        │       └─> Agregar Proveedor
        │           └─> VentanaProveedorSimple (ventana_proveedor.py)
        │
        ├─> Modificar Producto
        │   └─> VentanaProducto (ventana_producto.py)
        │
        ├─> Gestionar Proveedores (desde menú)
        │   └─> VentanaProveedores (ventana_proveedor.py)
        │       └─> Agregar Proveedor
        │           └─> VentanaProveedorSimple (ventana_proveedor.py)
        │
        └─> Reportes (desde menú)
            ├─> Productos Bajo Stock
            ├─> Resumen Inventario
            └─> Productos por Proveedor
```

---

## Características Técnicas

### Sistema de Importación
- **Importaciones circulares evitadas**: Las ventanas importan localmente dentro de métodos
- **Re-exportación limpia**: interfaz.py actúa como fachada (facade pattern)

### Validaciones Implementadas
1. **VentanaProducto**:
   - Campos obligatorios: código, nombre, unidad de medida, proveedor
   - Conversión correcta de números (float)
   - Código inmutable en modo modificar

2. **VentanaProveedorSimple**:
   - Campos obligatorios: ID y nombre
   - Validación de ID duplicado (excepción)

3. **VentanaProveedores**:
   - No permite eliminar proveedores con productos
   - Confirmación antes de eliminar

### Sistema de Actualización
- Las ventanas secundarias actualizan automáticamente las ventanas padre
- La tabla se refresca después de cada operación
- Las estadísticas se calculan en tiempo real

---

## Comentarios Didácticos

Todos los archivos incluyen:
- **Docstrings completos**: Explicación de qué hace cada clase/método
- **Comentarios de sección**: Separadores visuales para cada parte
- **Comentarios inline**: Explicación línea por línea de conceptos clave
- **Ejemplos de uso**: En los docstrings principales
- **Conceptos teóricos**: Explicaciones de POO, patrones, etc.

**Nivel**: Apropiado para estudiantes de segundo semestre

---

## Compatibilidad

### Con el código existente
✅ `main.py` no requiere cambios (importa desde interfaz.py)
✅ Todos los módulos de negocio permanecen iguales
✅ La funcionalidad es exactamente la misma

### Con versiones anteriores
- **Versión 1.0**: Todas las clases en interfaz.py
- **Versión 2.0**: Clases separadas en archivos individuales
- **Migración**: Solo se necesita tener los nuevos archivos

---

## Archivos del Proyecto (Completo)

```
app/
├── main.py                     - Punto de entrada de la aplicación
│
├── interfaz.py                 - Re-exportación de clases de interfaz
├── ventana_principal.py        - Ventana principal
├── ventana_producto.py         - Ventana de productos
├── ventana_proveedor.py        - Ventanas de proveedores
│
├── inventario.py               - Lógica del inventario
├── producto.py                 - Clase Producto
├── proveedor.py                - Clase Proveedor
├── persistencia.py             - Guardar/cargar datos JSON
│
├── usuario.py                  - Sistema de usuarios (roles)
├── modelos.py                  - (Archivo anterior, no eliminar aún)
│
└── datos/
    └── inventario.json         - Almacenamiento de datos
```

---

## Próximos Pasos Recomendados

1. **Probar la aplicación**: Ejecutar `python main.py` y verificar funcionalidad
2. **Revisar comentarios**: Leer los comentarios detallados en cada archivo
3. **Experimentar**: Modificar una ventana y ver cómo afecta solo esa parte
4. **Agregar funcionalidades**: Crear nuevas ventanas siguiendo el mismo patrón

---

## Preguntas Frecuentes

### ¿Puedo eliminar el archivo interfaz.py original?
No, ahora es el punto de entrada. Pero se actualizó para ser solo un archivo de re-exportación.

### ¿Por qué no están todas las importaciones al inicio de cada archivo?
Para evitar importaciones circulares. Algunas importaciones se hacen dentro de métodos (importación local).

### ¿Puedo agregar más ventanas?
Sí, crea un nuevo archivo `ventana_nombre.py`, define tu clase, y agrégala a `interfaz.py`.

### ¿Cómo funcionan las ventanas emergentes (Toplevel)?
Son ventanas secundarias que se abren encima de la ventana principal sin cerrarla.

---

## Contacto y Ayuda

Si tienes preguntas sobre esta estructura, revisa:
1. Los comentarios en cada archivo
2. Los docstrings de cada clase
3. Este documento

**Autor**: Estudiante de Ingeniería en Desarrollo de Software
**Fecha**: 2025
**Versión**: 2.0.0
