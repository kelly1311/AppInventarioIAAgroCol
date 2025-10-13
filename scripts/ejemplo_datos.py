"""
Módulo ejemplo_datos.py
========================
Script para crear datos de ejemplo en el sistema de inventario AgroCol SAS.

Este archivo contiene código para poblar (llenar) el inventario con datos de prueba.
Es útil para:
- Probar la aplicación con datos reales
- Demostrar funcionalidades del sistema
- Aprender cómo se crean y guardan datos

¿Cómo ejecutar este archivo?
-----------------------------
Desde la terminal o línea de comandos:
    python ejemplo_datos.py

¿Qué hace este archivo?
------------------------
1. Crea varios proveedores de ejemplo
2. Crea múltiples productos de diferentes categorías
3. Guarda todo en el archivo JSON
4. Muestra estadísticas del inventario creado

Autor: Estudiante de Ingeniería en Desarrollo de Software
Fecha: 2025
"""

# ==================== IMPORTACIONES ====================

# Importar las clases necesarias desde nuestros módulos
from src.modelos import Proveedor, Producto, Inventario
from src.persistencia import GestorPersistencia



# ==================== FUNCIÓN PRINCIPAL ====================

def crear_datos_ejemplo():
    """
    Crea un inventario con datos de ejemplo para pruebas
    ===================================================

    Esta función genera un conjunto completo de datos de ejemplo que incluye:
    - 5 proveedores de diferentes tipos
    - 22 productos de diversas categorías
    - Algunos productos con stock bajo para probar alertas

    El inventario creado representa un caso real de uso en una empresa agrícola.
    """
    print("="*70)
    print("CREANDO INVENTARIO DE EJEMPLO PARA AGROCOL SAS")
    print("="*70)

    # ==================== PASO 1: CREAR INVENTARIO VACÍO ====================

    # Instanciar un nuevo inventario vacío
    # Este será el contenedor de todos los productos y proveedores
    inventario = Inventario()

    # ==================== PASO 2: CREAR PROVEEDORES ====================

    print("\n📦 CREANDO PROVEEDORES...")
    print("-" * 70)

    # Lista de proveedores de ejemplo
    # Cada proveedor tiene: ID, nombre, teléfono y email
    proveedores = [
        Proveedor("PROV001", "AgroInsumos del Valle", "3001234567", "contacto@agroinsumos.com"),
        Proveedor("PROV002", "Fertilizantes Nacionales S.A.", "3009876543", "ventas@fertinacionales.com"),
        Proveedor("PROV003", "Semillas El Campesino", "3005556677", "info@semillascampesino.com"),
        Proveedor("PROV004", "Herramientas Agrícolas Ltda", "3007778899", "pedidos@herragricolas.com"),
        Proveedor("PROV005", "Químicos y Plaguicidas del Sur", "3004445566", "atencion@quimisur.com")
    ]

    # Agregar cada proveedor al inventario
    for proveedor in proveedores:
        inventario.agregar_proveedor(proveedor)
        print(f"  ✓ Proveedor agregado: {proveedor.nombre}")

    # ==================== PASO 3: CREAR PRODUCTOS ====================

    print("\n🌾 CREANDO PRODUCTOS...")
    print("-" * 70)

    # Lista de productos organizados por categorías
    productos = [
        # ========== CATEGORÍA: FERTILIZANTES ==========
        Producto(
            codigo="FERT001",
            nombre="Fertilizante NPK 15-15-15",
            unidad_medida="kg",
            fecha_ingreso="01/10/2025",
            proveedor=proveedores[1],  # Fertilizantes Nacionales
            precio_costo=2500,
            cantidad=500,
            stock_minimo=100
        ),
        Producto("FERT002", "Urea Granulada", "kg", "05/10/2025",
                proveedores[1], 1800, 800, 150),
        Producto("FERT003", "Fertilizante Orgánico Compost", "bulto", "10/10/2025",
                proveedores[0], 35000, 50, 20),
        Producto("FERT004", "Abono Triple 15", "kg", "12/10/2025",
                proveedores[1], 2200, 300, 80),

        # ========== CATEGORÍA: SEMILLAS ==========
        Producto("SEM001", "Semilla de Maíz Híbrido", "kg", "02/10/2025",
                proveedores[2], 45000, 120, 30),
        Producto("SEM002", "Semilla de Frijol", "kg", "03/10/2025",
                proveedores[2], 12000, 80, 25),
        Producto("SEM003", "Semilla de Arveja", "kg", "08/10/2025",
                proveedores[2], 15000, 60, 20),
        Producto("SEM004", "Semilla de Tomate Cherry", "kg", "11/10/2025",
                proveedores[2], 180000, 15, 10),

        # ========== CATEGORÍA: PLAGUICIDAS ==========
        Producto("PLAG001", "Herbicida Glifosato", "litro", "04/10/2025",
                proveedores[4], 25000, 200, 50),
        Producto("PLAG002", "Insecticida Cipermetrina", "litro", "06/10/2025",
                proveedores[4], 32000, 150, 40),
        Producto("PLAG003", "Fungicida Mancozeb", "kg", "09/10/2025",
                proveedores[4], 18000, 90, 30),
        Producto("PLAG004", "Acaricida Abamectina", "litro", "13/10/2025",
                proveedores[4], 55000, 8, 15),  # ⚠️ BAJO STOCK

        # ========== CATEGORÍA: HERRAMIENTAS ==========
        Producto("HERR001", "Azadón con Mango", "unidad", "07/10/2025",
                proveedores[3], 35000, 45, 20),
        Producto("HERR002", "Pala Redonda", "unidad", "07/10/2025",
                proveedores[3], 28000, 38, 15),
        Producto("HERR003", "Rastrillo Metálico", "unidad", "10/10/2025",
                proveedores[3], 22000, 30, 10),
        Producto("HERR004", "Carretilla 60L", "unidad", "12/10/2025",
                proveedores[3], 85000, 12, 8),

        # ========== CATEGORÍA: INSUMOS VARIOS ==========
        Producto("INS001", "Cal Agrícola", "bulto", "03/10/2025",
                proveedores[0], 18000, 200, 50),
        Producto("INS002", "Tierra Abonada", "m3", "05/10/2025",
                proveedores[0], 45000, 25, 10),
        Producto("INS003", "Manguera de Riego 1/2 pulgada", "unidad", "08/10/2025",
                proveedores[3], 35000, 40, 15),
        Producto("INS004", "Aspersor Rotativo", "unidad", "11/10/2025",
                proveedores[3], 28000, 5, 10),  # ⚠️ BAJO STOCK

        # ========== PRODUCTOS CON STOCK CRÍTICO (para probar alertas) ==========
        Producto("CRIT001", "Abono Foliar Premium", "litro", "13/10/2025",
                proveedores[0], 42000, 3, 15),  # ⚠️⚠️ CRÍTICO
        Producto("CRIT002", "Semilla Cebolla Junca", "kg", "13/10/2025",
                proveedores[2], 95000, 2, 10),  # ⚠️⚠️ CRÍTICO
    ]

    # Agregar cada producto al inventario
    for producto in productos:
        inventario.agregar_producto(producto)

        # Determinar el estado del stock del producto
        if producto.esta_bajo_stock():
            estado = "⚠️ BAJO STOCK"
        else:
            estado = "✓ OK"

        # Mostrar información del producto agregado
        print(f"  {estado} {producto.nombre}")

    # ==================== PASO 4: GUARDAR EN ARCHIVO JSON ====================

    print("\n💾 GUARDANDO INVENTARIO EN ARCHIVO JSON...")
    print("-" * 70)

    # Crear el gestor de persistencia (maneja el guardado/carga de datos)
    gestor = GestorPersistencia()

    # Intentar guardar el inventario
    if gestor.guardar_inventario(inventario):
        print(f"  ✓ Inventario guardado exitosamente en: {gestor.archivo}")
    else:
        print("  ✗ Error al guardar el inventario")
        return  # Salir de la función si hubo error

    # ==================== PASO 5: MOSTRAR ESTADÍSTICAS ====================

    print("\n" + "="*70)
    print("📊 ESTADÍSTICAS DEL INVENTARIO CREADO")
    print("="*70)

    # Calcular y mostrar estadísticas
    total_productos = inventario.obtener_cantidad_total_productos()
    total_proveedores = len(inventario.listar_proveedores())
    productos_bajo_stock = len(inventario.obtener_productos_bajo_stock())
    valor_total = inventario.obtener_valor_total_inventario()

    print(f"\n  📦 Total de productos diferentes: {total_productos}")
    print(f"  🏢 Total de proveedores: {total_proveedores}")
    print(f"  ⚠️  Productos bajo stock: {productos_bajo_stock}")
    print(f"  💰 Valor total del inventario: ${valor_total:,.2f} COP")

    # Mostrar lista de productos bajo stock si los hay
    if productos_bajo_stock > 0:
        print(f"\n  🚨 ALERTA: Productos que necesitan reabastecimiento:")
        for p in inventario.obtener_productos_bajo_stock():
            print(f"     - {p.nombre}: {p.cantidad} {p.unidad_medida} "
                  f"(mínimo: {p.stock_minimo})")

    print("\n" + "="*70)

    # ==================== PASO 6: INSTRUCCIONES FINALES ====================

    print("\n✅ INVENTARIO DE EJEMPLO CREADO EXITOSAMENTE!")
    print("\n📖 Próximos pasos:")
    print("   1. Ejecuta 'python main.py' para iniciar la aplicación")
    print("   2. Explora el inventario creado")
    print("   3. Prueba agregar, modificar o eliminar productos")
    print("   4. Verifica las alertas de stock bajo")
    print("\n" + "="*70)


# ==================== PUNTO DE ENTRADA ====================

if __name__ == "__main__":
    """
    Punto de entrada del script
    ===========================

    Este bloque se ejecuta solo si el archivo se ejecuta directamente:
        python ejemplo_datos.py

    No se ejecuta si el archivo se importa desde otro módulo.
    """
    # Llamar a la función principal para crear los datos de ejemplo
    crear_datos_ejemplo()


# ==================== NOTAS PARA ESTUDIANTES ====================
"""
Conceptos aplicados en este archivo:
====================================

1. CREACIÓN DE OBJETOS
   - Se crean instancias de Proveedor y Producto
   - Cada objeto tiene sus propios datos únicos

2. LISTAS Y BUCLES
   - Se usan listas para almacenar múltiples objetos
   - Los bucles 'for' recorren las listas

3. CONDICIONALES
   - if/else para verificar condiciones
   - Ejemplo: verificar si el stock está bajo

4. MANEJO DE ARCHIVOS
   - Uso del GestorPersistencia para guardar datos
   - Los datos se guardan en formato JSON

5. COMPOSICIÓN
   - Producto "tiene un" Proveedor
   - Inventario "tiene muchos" Productos

Ejercicio sugerido:
==================
Modifica este archivo para:
1. Agregar más proveedores
2. Crear productos de otras categorías
3. Cambiar los precios y cantidades
4. Agregar más productos con stock crítico

¡Experimenta y aprende!
"""
