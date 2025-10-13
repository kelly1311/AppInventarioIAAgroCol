"""
Módulo main.py
==============
Archivo principal del Sistema de Gestión de Inventario - AgroCol SAS

Este es el punto de entrada (entry point) de la aplicación. Cuando ejecutas el programa,
Python busca y ejecuta este archivo primero. Desde aquí se inicializa toda la aplicación.

¿Qué hace este archivo?
------------------------
1. Importa las bibliotecas necesarias
2. Importa la interfaz gráfica (VentanaPrincipal)
3. Crea la ventana principal de tkinter
4. Inicia el bucle de eventos de la aplicación

Autor: Estudiante de Ingeniería en Desarrollo de Software
Fecha: 2025
"""

# ==================== IMPORTACIONES ====================

# Importar el módulo tkinter para crear la interfaz gráfica
# tkinter es la biblioteca estándar de Python para crear interfaces gráficas (GUI)
import tkinter as tk

# Importar la clase VentanaPrincipal desde el módulo interfaz
# Esta clase contiene toda la lógica de la interfaz gráfica
from src.interfaz import VentanaPrincipal


# ==================== FUNCIÓN PRINCIPAL ====================

def main():
    """
    Función principal que inicia la aplicación
    =========================================

    Esta función es el punto de partida de toda la aplicación.
    Realiza las siguientes tareas:

    1. Crea la ventana raíz de tkinter (la ventana principal del sistema operativo)
    2. Crea una instancia de VentanaPrincipal (nuestra interfaz personalizada)
    3. Configura el protocolo de cierre de ventana
    4. Inicia el bucle principal de eventos (event loop)

    ¿Qué es el event loop?
    ----------------------
    Es un bucle infinito que espera eventos del usuario (clics, teclas, etc.)
    y los procesa. Sin este bucle, la ventana se abriría y cerraría inmediatamente.

    Flujo de ejecución:
    -------------------
    main() → crear ventana → mostrar interfaz → esperar eventos → procesar eventos
                                                     ↑__________________|
                                                     (bucle infinito)
    """
    # PASO 1: Crear la ventana raíz de tkinter
    # ------------------------------------------
    # tk.Tk() crea la ventana principal del sistema operativo
    # Esta es la "ventana contenedora" donde se mostrará toda nuestra interfaz
    root = tk.Tk()

    # PASO 2: Crear la aplicación
    # ----------------------------
    # VentanaPrincipal es nuestra clase personalizada que hereda de tkinter
    # Cuando se crea, automáticamente:
    # - Carga el inventario desde el archivo JSON
    # - Crea todos los widgets (botones, tablas, etc.)
    # - Configura los eventos
    # - Muestra los datos iniciales
    app = VentanaPrincipal(root)

    # PASO 3: Configurar el protocolo de cierre
    # ------------------------------------------
    # "WM_DELETE_WINDOW" es el evento que se dispara cuando el usuario
    # intenta cerrar la ventana (clic en la X)
    # Le decimos a tkinter que ejecute app.salir() en lugar de cerrar directamente
    # Esto permite preguntar al usuario si quiere guardar antes de salir
    root.protocol("WM_DELETE_WINDOW", app.salir)

    # PASO 4: Iniciar el bucle principal de eventos
    # ----------------------------------------------
    # mainloop() inicia el bucle infinito que mantiene la aplicación ejecutándose
    # Este método bloquea la ejecución aquí hasta que se cierre la ventana
    # Durante el bucle:
    # - Espera eventos del usuario (clics, teclas, movimientos del mouse)
    # - Procesa los eventos cuando ocurren
    # - Actualiza la interfaz gráfica
    # - Repite indefinidamente hasta que se cierre la aplicación
    root.mainloop()

    # NOTA: El código después de mainloop() solo se ejecuta cuando se cierra la aplicación


# ==================== PUNTO DE ENTRADA ====================

# Esta condición verifica si el archivo se está ejecutando directamente
# (no siendo importado como módulo desde otro archivo)
if __name__ == "__main__":
    """
    Condicional especial de Python
    ==============================

    __name__ es una variable especial de Python que contiene:
    - "__main__" si el archivo se ejecuta directamente (python main.py)
    - El nombre del módulo si se importa desde otro archivo

    ¿Por qué usar esto?
    -------------------
    - Permite que el archivo pueda ser ejecutado O importado
    - Si se ejecuta: llama a main() y arranca la aplicación
    - Si se importa: NO llama a main(), solo carga las definiciones

    Ejemplo:
    --------
    # Ejecutando directamente:
    $ python main.py
    → __name__ == "__main__" → Ejecuta main()

    # Importando desde otro archivo:
    >>> import main
    → __name__ == "main" → NO ejecuta main()
    """
    # Llamar a la función principal para iniciar la aplicación
    main()


# ==================== NOTAS ADICIONALES ====================
"""
Estructura de la aplicación:
============================

main.py (este archivo)
    ↓
interfaz.py (VentanaPrincipal)
    ↓
├── persistencia.py (GestorPersistencia) → Guarda/Carga datos
├── inventario.py (Inventario) → Gestiona productos y proveedores
    ↓
    ├── producto.py (Producto) → Representa un producto
    └── proveedor.py (Proveedor) → Representa un proveedor

Flujo de datos:
==============

1. Usuario abre la aplicación (main.py)
2. Se carga el inventario desde JSON (persistencia.py)
3. Se muestra la interfaz con los datos (interfaz.py)
4. Usuario interactúa con la interfaz (agregar, modificar, eliminar)
5. Los cambios se reflejan en el inventario (inventario.py)
6. Los cambios se guardan en JSON (persistencia.py)

Conceptos de POO aplicados:
===========================

1. ENCAPSULAMIENTO:
   - Atributos privados con _ (ej: self._productos)
   - Acceso controlado mediante getters y setters

2. HERENCIA:
   - VentanaPrincipal hereda comportamientos básicos de tkinter
   - Usuario → Cajero, Administrador (herencia de roles)

3. COMPOSICIÓN:
   - Producto "tiene un" Proveedor
   - Inventario "tiene muchos" Productos

4. POLIMORFISMO:
   - to_dict() y from_dict() en todas las clases
   - Mismo método, diferente implementación en cada clase

Buenas prácticas aplicadas:
===========================

✓ Separación de responsabilidades (cada clase tiene un propósito específico)
✓ Código modular (cada clase en su propio archivo)
✓ Comentarios explicativos (documentación clara)
✓ Manejo de errores (try-except)
✓ Validaciones de datos (verificar antes de guardar)
✓ Nombres descriptivos (variables y funciones con nombres claros)
"""
