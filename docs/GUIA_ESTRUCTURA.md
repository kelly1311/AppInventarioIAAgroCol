# 📂 Guía de Estructura del Proyecto - AgroCol SAS

## 🎯 Introducción

Este documento explica la nueva estructura modular y profesional del proyecto, diseñada siguiendo las mejores prácticas de desarrollo de software.

---

## 📁 Estructura Actual

```
app/
│
├── 📂 src/                              # Código fuente principal
│   │
│   ├── 📂 modelos/                      # Capa de Dominio
│   │   ├── __init__.py                  # Exporta: Proveedor, Producto, Inventario, Usuario
│   │   ├── proveedor.py                 # Clase Proveedor
│   │   ├── producto.py                  # Clase Producto (tiene un Proveedor)
│   │   ├── inventario.py                # Clase Inventario (gestiona Productos)
│   │   └── usuario.py                   # Clases Usuario, Cajero, Administrador
│   │
│   ├── 📂 persistencia/                 # Capa de Datos
│   │   ├── __init__.py                  # Exporta: GestorPersistencia
│   │   └── persistencia.py              # Clase GestorPersistencia
│   │
│   ├── 📂 interfaz/                     # Capa de Presentación
│   │   ├── __init__.py                  # Exporta todas las ventanas
│   │   ├── interfaz.py                  # Re-exporta ventanas (compatibilidad)
│   │   ├── ventana_principal.py         # Ventana principal
│   │   ├── ventana_producto.py          # Formulario de productos
│   │   └── ventana_proveedor.py         # Gestión de proveedores
│   │
│   └── 📂 utilidades/                   # Utilidades generales
│       └── __init__.py                  # (preparado para futuras utilidades)
│
├── 📂 datos/                            # Archivos de datos
│   └── inventario_agrocol.json          # Inventario actual
│
├── 📂 scripts/                          # Scripts auxiliares
│   └── ejemplo_datos.py                 # Crea datos de prueba
│
├── 📂 docs/                             # Documentación
│   ├── README.md                        # Documentación principal
│   ├── README_ESTRUCTURA.md             # Documentación de estructura antigua
│   ├── GUIA_ESTRUCTURA.md               # Este archivo
│   ├── DIAGRAMA_CLASES.txt              # Diagrama de clases
│   └── INICIO_RAPIDO.txt                # Guía rápida
│
├── 📂 tests/                            # Tests unitarios (opcional)
│   └── (vacío - preparado para pruebas)
│
├── main.py                              # Punto de entrada principal
├── requirements.txt                     # Dependencias
└── .gitignore                           # Archivos ignorados por Git
```

---

## 🏗️ Arquitectura por Capas

El proyecto está organizado siguiendo **Arquitectura por Capas** (Layered Architecture):

```
┌─────────────────────────────────────────────┐
│     PRESENTACIÓN (interfaz/)                │
│     - Ventanas tkinter                      │
│     - Interacción con el usuario            │
└─────────────────┬───────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│     LÓGICA DE NEGOCIO (modelos/)            │
│     - Clases del dominio                    │
│     - Reglas de negocio                     │
└─────────────────┬───────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│     DATOS (persistencia/)                   │
│     - Guardado/Carga de datos               │
│     - Interacción con archivos JSON         │
└─────────────────────────────────────────────┘
```

### Ventajas de esta arquitectura:

✅ **Separación de responsabilidades** - Cada capa tiene un propósito específico
✅ **Mantenibilidad** - Cambios en una capa no afectan las demás
✅ **Testabilidad** - Puedes probar cada capa independientemente
✅ **Escalabilidad** - Fácil agregar nuevas funcionalidades
✅ **Reusabilidad** - El código es más fácil de reutilizar

---

## 📦 Paquetes Python

### ¿Qué es un paquete?

Un paquete es una carpeta que contiene un archivo `__init__.py`. Esto permite:
- Organizar módulos relacionados
- Controlar qué se exporta
- Crear namespaces (espacios de nombres)

### Archivos `__init__.py` del proyecto:

#### `src/__init__.py`
Define el paquete raíz de código fuente.

#### `src/modelos/__init__.py`
```python
# Exporta todas las clases del dominio
from .proveedor import Proveedor
from .producto import Producto
from .inventario import Inventario
from .usuario import Usuario, Cajero, Administrador
```

**Uso:**
```python
from src.modelos import Proveedor, Producto, Inventario
```

#### `src/persistencia/__init__.py`
```python
# Exporta la clase de persistencia
from .persistencia import GestorPersistencia
```

**Uso:**
```python
from src.persistencia import GestorPersistencia
```

#### `src/interfaz/__init__.py`
```python
# Exporta todas las ventanas
from .ventana_principal import VentanaPrincipal
from .ventana_producto import VentanaProducto
from .ventana_proveedor import VentanaProveedorSimple, VentanaProveedores
```

**Uso:**
```python
from src.interfaz import VentanaPrincipal
```

---

## 🔄 Sistema de Imports

### Imports Relativos (dentro de paquetes)

Usados dentro de `src/` para importar entre módulos del mismo paquete:

```python
# En src/modelos/producto.py
from .proveedor import Proveedor  # Mismo paquete (modelos)

# En src/modelos/inventario.py
from .producto import Producto     # Mismo paquete (modelos)
from .proveedor import Proveedor   # Mismo paquete (modelos)

# En src/persistencia/persistencia.py
from ..modelos import Inventario   # Paquete padre (src) → modelos

# En src/interfaz/ventana_principal.py
from ..modelos import Producto     # Paquete padre (src) → modelos
from ..persistencia import GestorPersistencia  # Paquete padre → persistencia
```

**Notación:**
- `.` = mismo paquete
- `..` = paquete padre (subir un nivel)
- `...` = paquete abuelo (subir dos niveles)

### Imports Absolutos (desde raíz del proyecto)

Usados en archivos de la raíz del proyecto (`main.py`, `scripts/`):

```python
# En main.py
from src.interfaz import VentanaPrincipal

# En scripts/ejemplo_datos.py
from src.modelos import Proveedor, Producto, Inventario
from src.persistencia import GestorPersistencia
```

---

## 🚀 Cómo Ejecutar el Proyecto

### Opción 1: Crear datos de ejemplo primero

```bash
# Ir al directorio del proyecto
cd "C:\...\app"

# Crear datos de ejemplo
python -m scripts.ejemplo_datos

# Ejecutar la aplicación
python main.py
```

### Opción 2: Ejecutar directamente

```bash
# Ir al directorio del proyecto
cd "C:\...\app"

# Ejecutar la aplicación
python main.py
```

---

## 📝 Agregar Nuevas Funcionalidades

### 1. Agregar una nueva clase del dominio

**Archivo:** `src/modelos/categoria.py`

```python
"""
Módulo categoria.py
Clase para categorizar productos
"""

class Categoria:
    def __init__(self, id_categoria, nombre):
        self._id_categoria = id_categoria
        self._nombre = nombre

    # ... resto del código
```

**Actualizar:** `src/modelos/__init__.py`
```python
from .categoria import Categoria  # Agregar esta línea

__all__ = [
    'Proveedor',
    'Producto',
    'Inventario',
    'Usuario',
    'Cajero',
    'Administrador',
    'Categoria'  # Agregar aquí
]
```

**Usar:**
```python
from src.modelos import Categoria
```

### 2. Agregar una nueva ventana

**Archivo:** `src/interfaz/ventana_reportes.py`

```python
"""
Módulo ventana_reportes.py
Ventana para generar reportes
"""

import tkinter as tk
from ..modelos import Inventario

class VentanaReportes:
    def __init__(self, parent, inventario):
        # ... código
```

**Actualizar:** `src/interfaz/__init__.py`
```python
from .ventana_reportes import VentanaReportes  # Agregar

__all__ = [
    'VentanaPrincipal',
    'VentanaProducto',
    'VentanaProveedorSimple',
    'VentanaProveedores',
    'VentanaReportes'  # Agregar
]
```

### 3. Agregar utilidades

**Archivo:** `src/utilidades/validaciones.py`

```python
"""
Módulo validaciones.py
Funciones de validación de datos
"""

def validar_email(email):
    """Valida formato de email"""
    import re
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None

def validar_telefono(telefono):
    """Valida formato de teléfono"""
    return len(telefono) == 10 and telefono.isdigit()
```

**Actualizar:** `src/utilidades/__init__.py`
```python
from .validaciones import validar_email, validar_telefono

__all__ = ['validar_email', 'validar_telefono']
```

**Usar:**
```python
from src.utilidades import validar_email, validar_telefono

if validar_email("test@example.com"):
    print("Email válido")
```

---

## 🧪 Agregar Tests (Opcional)

**Archivo:** `tests/test_proveedor.py`

```python
"""
Tests para la clase Proveedor
"""

import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.modelos import Proveedor

def test_crear_proveedor():
    """Prueba crear un proveedor"""
    proveedor = Proveedor("PROV001", "Test", "3001234567", "test@example.com")
    assert proveedor.id_proveedor == "PROV001"
    assert proveedor.nombre == "Test"
    print("✓ Test crear_proveedor pasó")

def test_modificar_nombre():
    """Prueba modificar nombre de proveedor"""
    proveedor = Proveedor("PROV001", "Test")
    proveedor.nombre = "Nuevo Nombre"
    assert proveedor.nombre == "Nuevo Nombre"
    print("✓ Test modificar_nombre pasó")

if __name__ == "__main__":
    test_crear_proveedor()
    test_modificar_nombre()
    print("\n✅ Todos los tests pasaron")
```

**Ejecutar:**
```bash
python tests/test_proveedor.py
```

---

## 📊 Comparación: Antes vs Después

### ❌ Antes (todos los archivos en una carpeta)

```
app/
├── proveedor.py
├── producto.py
├── inventario.py
├── usuario.py
├── persistencia.py
├── interfaz.py
├── ventana_principal.py
├── ventana_producto.py
├── ventana_proveedor.py
├── main.py
├── ejemplo_datos.py
└── inventario_agrocol.json
```

**Problemas:**
- ❌ Difícil encontrar archivos
- ❌ No hay separación de responsabilidades
- ❌ Imports confusos
- ❌ No escalable

### ✅ Después (estructura modular)

```
app/
├── src/
│   ├── modelos/
│   ├── persistencia/
│   └── interfaz/
├── scripts/
├── datos/
├── docs/
└── main.py
```

**Ventajas:**
- ✅ Organización clara
- ✅ Separación por capas
- ✅ Fácil de mantener
- ✅ Escalable y profesional

---

## 🎓 Conceptos Aplicados

### 1. Modularidad
Código dividido en módulos independientes y reutilizables.

### 2. Separación de Responsabilidades (SoC)
Cada módulo/clase tiene una responsabilidad específica.

### 3. Principio DRY (Don't Repeat Yourself)
Los archivos `__init__.py` evitan repetir imports largos.

### 4. Namespace
Los paquetes crean espacios de nombres para evitar conflictos.

### 5. Arquitectura por Capas
Separación en presentación, lógica y datos.

---

## 🆘 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'src'"

**Causa:** Estás ejecutando desde el directorio incorrecto.

**Solución:**
```bash
# Asegúrate de estar en el directorio app/
cd "C:\...\app"
python main.py
```

### Error: "ImportError: attempted relative import with no known parent package"

**Causa:** Intentas ejecutar un archivo interno directamente.

**Solución:** No ejecutes archivos internos directamente. Ejecuta siempre `main.py` o scripts desde la raíz.

```bash
# ❌ NO HACER:
python src/modelos/proveedor.py

# ✅ HACER:
python main.py
```

### Los cambios no se reflejan

**Causa:** Python cachea archivos .pyc

**Solución:**
```bash
# Eliminar cache
rm -rf __pycache__
rm -rf src/__pycache__
rm -rf src/*/__pycache__

# O reiniciar Python/IDE
```

---

## 📚 Recursos Adicionales

- [Python Packages](https://docs.python.org/es/3/tutorial/modules.html#packages)
- [Import System](https://docs.python.org/es/3/reference/import.html)
- [Layered Architecture](https://en.wikipedia.org/wiki/Multitier_architecture)

---

**Autor:** Estudiante de Ingeniería en Desarrollo de Software
**Fecha:** 2025
**Proyecto:** Sistema de Gestión de Inventario AgroCol SAS
**Versión:** 2.0 (Estructura Modular)
