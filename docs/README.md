# Sistema de Gestión de Inventario - AgroCol SAS

## Descripción

Sistema de escritorio desarrollado en Python orientado a objetos para la gestión eficiente de inventarios en el sector agrícola. La aplicación permite a AgroCol SAS administrar sus productos e insumos agrícolas de manera local, sin necesidad de conexión a internet.

## Características Principales

### Gestión de Productos
- Registro completo de productos con información detallada:
  - Código único
  - Nombre del producto
  - Unidad de medida (kg, ton, litro, unidad, bulto, caja, m³)
  - Fecha de ingreso
  - Proveedor asociado
  - Precio de costo
  - Cantidad en stock
  - Stock mínimo configurable

### Gestión de Inventario
- Visualización de stock total de cada producto
- Agregar stock (entradas)
- Retirar stock (salidas)
- Búsqueda rápida de productos por nombre o código
- Modificación de información de productos
- Eliminación de productos

### Alertas Automáticas
- Sistema de alertas cuando un producto alcanza el stock mínimo
- Indicadores visuales en la tabla (filas rojas para productos bajo stock)
- Notificaciones automáticas al iniciar la aplicación

### Gestión de Proveedores
- Registro de proveedores con información completa
- Asociación de productos con proveedores
- Consulta de productos por proveedor

### Reportes
- Reporte de productos bajo stock
- Resumen general del inventario con estadísticas
- Listado de productos por proveedor
- Cálculo automático del valor total del inventario

### Persistencia de Datos
- Almacenamiento local en formato JSON
- Guardado automático de cambios
- Sistema de backup manual
- No requiere conexión a internet

## Requisitos del Sistema

- Python 3.7 o superior
- Sistema operativo: Windows, macOS o Linux
- Librerías incluidas en Python (tkinter, json, datetime)

## Instalación

1. Asegúrate de tener Python instalado:
```bash
python --version
```

2. Los archivos del proyecto incluyen:
   - `main.py` - Archivo principal de la aplicación
   - `modelos.py` - Clases del modelo de dominio
   - `persistencia.py` - Gestión de almacenamiento
   - `interfaz.py` - Interfaz gráfica de usuario

3. No se requieren instalaciones adicionales, todas las librerías son estándar de Python.

## Uso de la Aplicación

### Iniciar la Aplicación

Desde la terminal, navega hasta el directorio del proyecto y ejecuta:

```bash
python main.py
```

### Primeros Pasos

1. **Agregar un Proveedor:**
   - Ve al menú "Proveedores" → "Gestionar Proveedores"
   - Haz clic en "Agregar Proveedor"
   - Completa la información del proveedor
   - Guarda el proveedor

2. **Agregar un Producto:**
   - En la ventana principal, haz clic en "Agregar Producto"
   - Completa todos los campos:
     - Código: identificador único del producto
     - Nombre: nombre descriptivo
     - Cantidad: cantidad inicial en stock
     - Unidad de medida: selecciona de la lista
     - Stock mínimo: nivel de alerta
     - Precio de costo: valor unitario
     - Proveedor: selecciona de la lista
     - Fecha de ingreso: fecha actual por defecto
   - Haz clic en "Guardar"

3. **Gestionar Stock:**
   - Selecciona un producto de la tabla
   - Usa "Agregar Stock" para entradas
   - Usa "Retirar Stock" para salidas
   - El sistema validará las cantidades automáticamente

### Funcionalidades del Menú

#### Menú Archivo
- **Guardar:** Guarda manualmente el inventario
- **Crear Backup:** Crea una copia de seguridad con fecha y hora
- **Salir:** Cierra la aplicación (pregunta si desea guardar)

#### Menú Proveedores
- **Gestionar Proveedores:** Ventana para administrar proveedores

#### Menú Reportes
- **Productos Bajo Stock:** Lista productos que necesitan reabastecimiento
- **Resumen Inventario:** Estadísticas generales del inventario
- **Productos por Proveedor:** Consulta productos de un proveedor específico

#### Menú Ayuda
- **Acerca de:** Información sobre la aplicación

### Búsqueda de Productos

- Escribe en el campo "Buscar" en la parte superior
- La tabla se filtra automáticamente mostrando coincidencias
- Busca por código o nombre de producto

### Alertas de Stock Bajo

- Al iniciar la aplicación, se verifica automáticamente el stock
- Si hay productos bajo el mínimo, aparece una alerta
- En la tabla, los productos bajo stock se muestran con fondo rojo
- El contador en la parte inferior muestra la cantidad de alertas

## Estructura del Proyecto (Orientación a Objetos)

### Clase `Proveedor` (modelos.py)
Representa un proveedor de productos agrícolas.

**Atributos:**
- `id_proveedor`: Identificador único
- `nombre`: Nombre del proveedor
- `telefono`: Número de contacto
- `email`: Correo electrónico

**Métodos principales:**
- `to_dict()`: Serialización para JSON
- `from_dict()`: Deserialización desde JSON

### Clase `Producto` (modelos.py)
Representa un producto o insumo agrícola.

**Atributos:**
- `codigo`: Código único del producto
- `nombre`: Nombre del producto
- `unidad_medida`: Unidad de medida (kg, litro, etc.)
- `fecha_ingreso`: Fecha de registro
- `proveedor`: Instancia de Proveedor
- `precio_costo`: Precio unitario
- `cantidad`: Cantidad en stock
- `stock_minimo`: Nivel mínimo de inventario

**Métodos principales:**
- `agregar_stock(cantidad)`: Incrementa el stock
- `retirar_stock(cantidad)`: Disminuye el stock
- `esta_bajo_stock()`: Verifica si está bajo el mínimo
- `valor_total_inventario()`: Calcula el valor total

### Clase `Inventario` (modelos.py)
Gestiona la colección completa de productos y proveedores.

**Métodos principales:**
- `agregar_producto(producto)`
- `obtener_producto(codigo)`
- `actualizar_producto(producto)`
- `eliminar_producto(codigo)`
- `listar_productos()`
- `buscar_productos(termino)`
- `obtener_productos_bajo_stock()`
- `obtener_cantidad_total_productos()`
- `obtener_valor_total_inventario()`
- `obtener_productos_por_proveedor(id_proveedor)`

### Clase `GestorPersistencia` (persistencia.py)
Maneja el almacenamiento y recuperación de datos.

**Métodos principales:**
- `guardar_inventario(inventario)`: Guarda en JSON
- `cargar_inventario()`: Carga desde JSON
- `crear_backup(sufijo)`: Crea copia de seguridad
- `existe_archivo()`: Verifica existencia del archivo

### Clases de Interfaz (interfaz.py)
- `VentanaPrincipal`: Ventana principal de la aplicación
- `VentanaProducto`: Formulario para agregar/modificar productos
- `VentanaProveedores`: Gestión de proveedores
- `VentanaProveedorSimple`: Formulario rápido de proveedores

## Almacenamiento de Datos

Los datos se guardan en el archivo `inventario_agrocol.json` en el mismo directorio de la aplicación.

**Formato del archivo JSON:**
```json
{
    "productos": [
        {
            "codigo": "001",
            "nombre": "Fertilizante NPK",
            "unidad_medida": "kg",
            "fecha_ingreso": "13/10/2025",
            "proveedor": {...},
            "precio_costo": 25000,
            "cantidad": 500,
            "stock_minimo": 100
        }
    ],
    "proveedores": [...]
}
```

## Limitaciones Conocidas

De acuerdo con los objetivos del proyecto:

- ✗ No genera facturas
- ✗ No gestiona clientes
- ✗ No funciona en dispositivos móviles
- ✗ No requiere ni utiliza internet
- ✗ No se conecta a sistemas externos en línea

Estas limitaciones son intencionales y están alineadas con el alcance del proyecto.

## Ventajas de la Aplicación

- Funciona sin conexión a internet
- Almacenamiento local seguro
- Interfaz intuitiva y fácil de usar
- Alertas automáticas de stock
- Reportes instantáneos
- Sistema de backup integrado
- Búsqueda rápida de productos
- Gestión completa de proveedores
- Cálculos automáticos de valores

## Solución de Problemas

### La aplicación no inicia
- Verifica que Python esté correctamente instalado
- Asegúrate de estar en el directorio correcto
- Verifica que todos los archivos (.py) estén presentes

### No se guardan los datos
- Verifica permisos de escritura en el directorio
- Revisa que el archivo JSON no esté corrupto
- Usa la opción "Crear Backup" regularmente

### Error al cargar el inventario
- El archivo JSON puede estar dañado
- Restaura desde un backup si existe
- Elimina el archivo JSON para crear uno nuevo

## Soporte y Contacto

Para reportar problemas o sugerencias relacionadas con el sistema de gestión de inventario de AgroCol SAS, contacta al administrador del sistema.

## Versión

**Versión 1.0** - Sistema de Gestión de Inventario AgroCol SAS

## Autor

Desarrollado como solución para la gestión eficiente de inventarios en el sector agrícola.

---

**AgroCol SAS** - Optimizando la gestión de inventarios en el sector agropecuario
