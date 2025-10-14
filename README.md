# AppInventarioIA
App creada en python con IA Claude

## Diagrama de Caso de Uso - Inicio de Sesión

```
┌─────────────────────────────────────────────────────────────────┐
│                    Sistema de Inventario                        │
│                                                                 │
│                                                                 │
│              ┌──────────────────────────┐                       │
│              │   Iniciar Sesión         │                       │
│       ┌──────┤                          │                       │
│       │      │   - Ingresar usuario     │                       │
│       │      │   - Ingresar contraseña  │                       │
│       │      │   - Validar credenciales │                       │
│   ┌───┴───┐  └────────┬─────────────────┘                       │
│   │       │           │                                         │
│   │Usuario│           │ <<include>>                             │
│   │       │           ▼                                         │
│   └───┬───┘  ┌──────────────────────────┐                       │
│       │      │  Validar Credenciales    │                       │
│       │      │                          │                       │
│       │      │  - Verificar usuario     │                       │
│       │      │  - Verificar contraseña  │                       │
│       │      │  - Consultar base datos  │                       │
│       │      └────────┬─────────────────┘                       │
│       │               │                                         │
│       │               │ <<extend>>                              │
│       │               ▼                                         │
│       │      ┌──────────────────────────┐                       │
│       └──────┤  Recuperar Contraseña    │                       │
│              │                          │                       │
│              │  - Validar correo        │                       │
│              │  - Enviar token          │                       │
│              │  - Restablecer password  │                       │
│              └──────────────────────────┘                       │
│                                                                 │
│              ┌──────────────────────────┐                       │
│       ┌──────┤  Cerrar Sesión           │                       │
│       │      │                          │                       │
│       │      │  - Finalizar sesión      │                       │
│       │      │  - Limpiar datos         │                       │
│   ┌───┴───┐  └──────────────────────────┘                       │
│   │       │                                                     │
│   │Usuario│                                                     │
│   │Autent.│                                                     │
│   │       │  ┌──────────────────────────┐                       │
│   └───┬───┘  │  Gestionar Perfil        │                       │
│       │      │                          │                       │
│       └──────┤  - Ver información       │                       │
│              │  - Modificar datos       │                       │
│              │  - Cambiar contraseña    │                       │
│              └──────────────────────────┘                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Descripción de Casos de Uso

#### CU-01: Iniciar Sesión
**Actor Principal:** Usuario

**Precondiciones:**
- El usuario debe estar registrado en el sistema
- La aplicación debe estar en ejecución

**Flujo Principal:**
1. El usuario accede a la pantalla de inicio de sesión
2. El sistema muestra el formulario con campos de usuario y contraseña
3. El usuario ingresa sus credenciales (nombre de usuario y contraseña)
4. El usuario presiona el botón "Iniciar Sesión"
5. El sistema valida las credenciales ingresadas
6. El sistema autentica al usuario
7. El sistema redirige al usuario a la ventana principal de la aplicación

**Flujos Alternativos:**
- **3a.** Usuario o contraseña incorrectos:
  - El sistema muestra un mensaje de error
  - El sistema solicita reingresar las credenciales

- **3b.** Campos vacíos:
  - El sistema muestra mensaje indicando campos obligatorios
  - El usuario debe completar los campos requeridos

**Postcondiciones:**
- El usuario queda autenticado en el sistema
- Se registra la sesión del usuario
- El usuario tiene acceso a las funcionalidades según su rol

---

#### CU-02: Validar Credenciales
**Actor Principal:** Sistema

**Precondiciones:**
- El usuario ha ingresado credenciales

**Flujo Principal:**
1. El sistema recibe las credenciales ingresadas
2. El sistema verifica que los campos no estén vacíos
3. El sistema consulta la base de datos de usuarios
4. El sistema compara el usuario y contraseña ingresados con los almacenados
5. El sistema confirma la validez de las credenciales

**Flujos Alternativos:**
- **4a.** Usuario no existe:
  - El sistema retorna error de autenticación

- **4b.** Contraseña incorrecta:
  - El sistema retorna error de autenticación
  - El sistema incrementa contador de intentos fallidos

**Postcondiciones:**
- Las credenciales son validadas o rechazadas
- Se genera registro de intento de acceso

---

#### CU-03: Recuperar Contraseña
**Actor Principal:** Usuario

**Precondiciones:**
- El usuario tiene una cuenta registrada
- El usuario tiene acceso a su correo electrónico registrado

**Flujo Principal:**
1. El usuario selecciona la opción "¿Olvidaste tu contraseña?"
2. El sistema muestra formulario de recuperación
3. El usuario ingresa su correo electrónico o nombre de usuario
4. El sistema valida que el correo/usuario existe
5. El sistema genera un token de recuperación
6. El sistema envía correo con enlace de recuperación
7. El usuario accede al enlace y establece nueva contraseña
8. El sistema actualiza la contraseña en la base de datos

**Flujos Alternativos:**
- **4a.** Correo/usuario no registrado:
  - El sistema muestra mensaje de error

- **7a.** Token expirado:
  - El sistema solicita nueva solicitud de recuperación

**Postcondiciones:**
- La contraseña del usuario es actualizada
- Se registra el cambio de contraseña

---

#### CU-04: Cerrar Sesión
**Actor Principal:** Usuario Autenticado

**Precondiciones:**
- El usuario debe estar autenticado

**Flujo Principal:**
1. El usuario selecciona la opción "Cerrar Sesión"
2. El sistema muestra confirmación de cierre de sesión
3. El usuario confirma el cierre de sesión
4. El sistema finaliza la sesión activa
5. El sistema limpia los datos de sesión
6. El sistema redirige a la pantalla de inicio de sesión

**Postcondiciones:**
- La sesión del usuario queda cerrada
- Se registra el cierre de sesión
- Los datos sensibles en memoria son eliminados

---

#### CU-05: Gestionar Perfil
**Actor Principal:** Usuario Autenticado

**Precondiciones:**
- El usuario debe estar autenticado

**Flujo Principal:**
1. El usuario accede a su perfil
2. El sistema muestra la información del usuario
3. El usuario modifica los datos deseados
4. El usuario guarda los cambios
5. El sistema valida los datos ingresados
6. El sistema actualiza la información en la base de datos
7. El sistema confirma la actualización exitosa

**Flujos Alternativos:**
- **5a.** Datos inválidos:
  - El sistema muestra mensajes de error específicos
  - El usuario debe corregir los datos

**Postcondiciones:**
- La información del usuario queda actualizada
- Se registra la modificación del perfil

---

---

# Casos de Uso Principales - Sistema de Gestión de Inventario AgroCol SAS

## Diagrama General de Casos de Uso

```
                    ╔════════════════════════════════════════════════════════╗
                    ║     Sistema de Gestión de Inventario - AgroCol SAS    ║
                    ║                                                        ║
                    ║                                                        ║
                    ║    ┌────────────────────────────┐                     ║
                    ║    │  CU-01: Gestionar          │                     ║
     ┌──────┐       ║    │  Productos                 │                     ║
     │      │       ║    │                            │                     ║
     │Admin.│◄──────╫────┤  - Agregar Producto        │                     ║
     │      │       ║    │  - Modificar Producto      │                     ║
     │      │       ║    │  - Eliminar Producto       │                     ║
     └───┬──┘       ║    │  - Buscar Producto         │                     ║
         │          ║    └────────────────────────────┘                     ║
         │          ║                                                        ║
         │          ║    ┌────────────────────────────┐                     ║
         │          ║    │  CU-02: Gestionar          │                     ║
         └──────────╫────┤  Stock                     │                     ║
                    ║    │                            │                     ║
     ┌──────┐       ║    │  - Agregar Stock (Entrada)│──────┐               ║
     │      │       ║    │  - Retirar Stock (Salida) │      │               ║
     │Oper. │◄──────╫────┤  - Consultar Disponibilidad│     │               ║
     │Invent│       ║    └────────────────────────────┘     │               ║
     │      │       ║                                       │               ║
     └───┬──┘       ║                                       │<<include>>    ║
         │          ║    ┌────────────────────────────┐    │               ║
         │          ║    │  CU-03: Gestionar          │    │               ║
         └──────────╫────┤  Proveedores               │    │               ║
                    ║    │                            │    │               ║
                    ║    │  - Agregar Proveedor       │    │               ║
     ┌──────┐       ║    │  - Consultar Proveedor     │    │               ║
     │      │       ║    │  - Eliminar Proveedor      │    │               ║
     │Admin.│◄──────╫────┤  - Listar Productos por    │    │               ║
     │      │       ║    │    Proveedor               │    │               ║
     │      │       ║    └────────────────────────────┘    │               ║
     └───┬──┘       ║                                      │               ║
         │          ║                                      ▼               ║
         │          ║    ┌────────────────────────────┐                     ║
         │          ║    │  CU-04: Validar            │                     ║
         │          ║    │  Stock Mínimo              │                     ║
         │          ║    │                            │                     ║
         │          ║    │  - Verificar niveles       │                     ║
         └──────────╫────┤  - Generar alertas         │                     ║
                    ║    │  - Listar productos        │                     ║
                    ║    │    bajo stock              │                     ║
                    ║    └────────────────────────────┘                     ║
                    ║                                                        ║
     ┌──────┐       ║    ┌────────────────────────────┐                     ║
     │      │       ║    │  CU-05: Generar            │                     ║
     │Admin.│◄──────╫────┤  Reportes                  │                     ║
     │      │       ║    │                            │                     ║
     │      │       ║    │  - Resumen de Inventario   │                     ║
     └──────┘       ║    │  - Productos Bajo Stock    │                     ║
                    ║    │  - Productos por Proveedor │                     ║
                    ║    │  - Valor Total Inventario  │                     ║
                    ║    └────────────────────────────┘                     ║
                    ║                                                        ║
     ┌──────┐       ║    ┌────────────────────────────┐                     ║
     │      │       ║    │  CU-06: Gestionar          │                     ║
     │Admin.│◄──────╫────┤  Persistencia              │                     ║
     │      │       ║    │                            │                     ║
     │      │       ║    │  - Guardar Datos           │                     ║
     └──────┘       ║    │  - Cargar Datos            │                     ║
                    ║    │  - Crear Backup            │                     ║
                    ║    └────────────────────────────┘                     ║
                    ║                                                        ║
                    ║                                                        ║
                    ║    ┌────────────────────────────┐                     ║
     ┌──────┐       ║    │  CU-07: Buscar y           │                     ║
     │      │       ║    │  Filtrar Información       │                     ║
     │Todos │◄──────╫────┤                            │                     ║
     │      │       ║    │  - Buscar por nombre       │                     ║
     │      │       ║    │  - Buscar por código       │                     ║
     └──────┘       ║    │  - Filtrar resultados      │                     ║
                    ║    └────────────────────────────┘                     ║
                    ║                                                        ║
                    ╚════════════════════════════════════════════════════════╝
```

---

## Especificación Detallada de Casos de Uso

### CU-01: Gestionar Productos

**Actor Principal:** Administrador del Sistema

**Actores Secundarios:** Operador de Inventario

**Descripción:** Permite administrar el catálogo completo de productos e insumos agrícolas del sistema.

**Precondiciones:**
- El usuario debe tener permisos de administración
- La aplicación debe estar en ejecución
- El sistema de persistencia debe estar disponible

**Flujo Principal:**

**1. Agregar Producto:**
   1. El administrador selecciona "Agregar Producto"
   2. El sistema muestra el formulario de nuevo producto
   3. El administrador ingresa:
      - Código único del producto
      - Nombre descriptivo
      - Cantidad inicial en stock
      - Unidad de medida (kg, ton, litro, unidad, bulto, caja, m³)
      - Stock mínimo (nivel de alerta)
      - Precio de costo
      - Proveedor (selección de lista)
      - Fecha de ingreso (por defecto: fecha actual)
   4. El sistema valida los datos ingresados
   5. El sistema verifica que el código no exista
   6. El sistema crea el producto en el inventario
   7. El sistema actualiza la tabla de productos
   8. El sistema muestra confirmación exitosa

**2. Modificar Producto:**
   1. El administrador selecciona un producto de la tabla
   2. El administrador presiona "Modificar Producto"
   3. El sistema muestra el formulario con datos precargados
   4. El administrador modifica los campos deseados (excepto código)
   5. El sistema valida los cambios
   6. El sistema actualiza el producto en el inventario
   7. El sistema refresca la tabla
   8. El sistema muestra confirmación

**3. Eliminar Producto:**
   1. El administrador selecciona un producto de la tabla
   2. El administrador presiona "Eliminar Producto"
   3. El sistema solicita confirmación
   4. El administrador confirma la eliminación
   5. El sistema elimina el producto del inventario
   6. El sistema actualiza la tabla
   7. El sistema muestra confirmación

**4. Buscar Producto:**
   1. El usuario ingresa término de búsqueda (nombre o código)
   2. El sistema filtra la tabla en tiempo real
   3. El sistema muestra productos que coinciden con el criterio

**Flujos Alternativos:**

- **4a.** Código duplicado al agregar:
  - El sistema muestra mensaje de error
  - El sistema solicita ingresar código diferente

- **4b.** Datos inválidos:
  - El sistema resalta campos con error
  - El sistema muestra mensaje descriptivo
  - El usuario debe corregir los datos

- **4c.** Campos obligatorios vacíos:
  - El sistema indica campos faltantes
  - El usuario debe completar información

- **5a.** Error de validación:
  - El sistema muestra detalles del error
  - El formulario permanece abierto con datos ingresados

**Postcondiciones:**
- El catálogo de productos queda actualizado
- Los cambios se reflejan en la interfaz
- Las estadísticas se recalculan automáticamente
- Se puede guardar el estado del inventario

**Reglas de Negocio:**
- RN-01: El código de producto debe ser único en el sistema
- RN-02: El precio de costo debe ser mayor a cero
- RN-03: La cantidad y stock mínimo no pueden ser negativos
- RN-04: Todo producto debe tener un proveedor asignado

---

### CU-02: Gestionar Stock

**Actor Principal:** Operador de Inventario

**Actores Secundarios:** Administrador del Sistema

**Descripción:** Permite registrar entradas y salidas de productos del almacén, manteniendo actualizado el inventario en tiempo real.

**Precondiciones:**
- El producto debe existir en el sistema
- El usuario debe estar autenticado
- La aplicación debe estar en ejecución

**Flujo Principal:**

**1. Agregar Stock (Entrada):**
   1. El operador selecciona un producto de la tabla
   2. El operador presiona "Agregar Stock"
   3. El sistema muestra diálogo para ingresar cantidad
   4. El operador ingresa la cantidad a agregar
   5. El sistema valida que sea un número positivo
   6. El sistema incrementa el stock del producto
   7. El sistema actualiza la tabla y estadísticas
   8. El sistema muestra confirmación con nuevo total

**2. Retirar Stock (Salida):**
   1. El operador selecciona un producto de la tabla
   2. El operador presiona "Retirar Stock"
   3. El sistema muestra diálogo con stock disponible
   4. El operador ingresa la cantidad a retirar
   5. El sistema valida que no exceda el stock disponible
   6. El sistema reduce el stock del producto
   7. El sistema verifica si queda bajo stock mínimo
   8. Si está bajo stock mínimo, el sistema marca visualmente (fila roja)
   9. El sistema actualiza la tabla y estadísticas
   10. El sistema muestra confirmación con nuevo total

**3. Consultar Disponibilidad:**
   1. El usuario busca el producto en la tabla
   2. El sistema muestra cantidad actual en stock
   3. El sistema indica visualmente si está bajo stock (color rojo)
   4. El usuario puede ver stock mínimo configurado

**Flujos Alternativos:**

- **5a.** Cantidad a retirar excede el stock disponible:
  - El sistema muestra mensaje de error con stock disponible
  - El sistema no permite completar la operación
  - El operador debe ingresar cantidad válida o cancelar

- **5b.** Cantidad inválida (negativa, texto, cero):
  - El sistema muestra mensaje de error
  - El sistema solicita ingresar valor válido

- **7a.** Stock alcanza nivel mínimo tras retiro:
  - El sistema genera alerta automática
  - El sistema cambia color de fila a rojo
  - El sistema incrementa contador de alertas
  - La operación se completa exitosamente

- **7b.** No hay producto seleccionado:
  - El sistema muestra mensaje indicando seleccionar producto
  - La operación no continúa

**Postcondiciones:**
- El stock del producto queda actualizado
- El valor total del inventario se recalcula
- Las alertas de stock bajo se actualizan si aplica
- Los cambios quedan listos para guardar

**Reglas de Negocio:**
- RN-05: No se puede retirar más stock del disponible
- RN-06: Las cantidades deben ser números positivos
- RN-07: Al alcanzar stock mínimo se genera alerta automática
- RN-08: El stock nunca puede ser negativo

---

### CU-03: Gestionar Proveedores

**Actor Principal:** Administrador del Sistema

**Descripción:** Permite administrar el catálogo de proveedores de la empresa y asociarlos con productos.

**Precondiciones:**
- El usuario debe tener permisos de administración
- La aplicación debe estar en ejecución

**Flujo Principal:**

**1. Agregar Proveedor:**
   1. El administrador accede a "Proveedores" → "Gestionar Proveedores"
   2. El sistema muestra ventana con lista de proveedores
   3. El administrador presiona "Agregar Proveedor"
   4. El sistema muestra formulario de nuevo proveedor
   5. El administrador ingresa:
      - ID del proveedor (único)
      - Nombre o razón social
      - Teléfono de contacto
      - Correo electrónico
   6. El sistema valida los datos
   7. El sistema verifica que el ID no exista
   8. El sistema crea el proveedor
   9. El sistema actualiza la tabla de proveedores
   10. El sistema muestra confirmación

**2. Consultar Proveedor:**
   1. El administrador visualiza la tabla de proveedores
   2. El sistema muestra para cada proveedor:
      - ID del proveedor
      - Nombre
      - Teléfono
      - Email
      - Cantidad de productos asociados
   3. El administrador puede seleccionar un proveedor
   4. El administrador puede ver productos del proveedor

**3. Eliminar Proveedor:**
   1. El administrador selecciona un proveedor de la tabla
   2. El administrador presiona "Eliminar Proveedor"
   3. El sistema verifica si tiene productos asociados
   4. Si no tiene productos, el sistema solicita confirmación
   5. El administrador confirma
   6. El sistema elimina el proveedor
   7. El sistema actualiza la tabla
   8. El sistema muestra confirmación

**4. Listar Productos por Proveedor:**
   1. El administrador va a "Reportes" → "Productos por Proveedor"
   2. El sistema muestra combo con lista de proveedores
   3. El administrador selecciona un proveedor
   4. El sistema consulta productos del proveedor
   5. El sistema muestra ventana con:
      - Nombre del proveedor
      - Lista de productos (código, nombre, cantidad, precio)
      - Total de productos
      - Valor total de productos de ese proveedor

**Flujos Alternativos:**

- **7a.** ID de proveedor duplicado:
  - El sistema muestra mensaje de error
  - El sistema solicita ingresar ID diferente

- **3a.** Proveedor tiene productos asociados:
  - El sistema muestra mensaje indicando que no puede eliminarse
  - El sistema indica cantidad de productos asociados
  - La operación se cancela
  - El proveedor permanece en el sistema

- **5a.** Campos obligatorios vacíos (ID o Nombre):
  - El sistema muestra mensaje de error
  - El sistema indica campos requeridos
  - El usuario debe completar información

- **4a.** Proveedor sin productos:
  - El sistema muestra mensaje informativo
  - El sistema indica que no hay productos asociados

**Postcondiciones:**
- El catálogo de proveedores queda actualizado
- Los proveedores están disponibles para asociar con productos
- Los productos mantienen su referencia a proveedores
- No quedan productos sin proveedor

**Reglas de Negocio:**
- RN-09: El ID de proveedor debe ser único
- RN-10: No se puede eliminar un proveedor con productos asociados
- RN-11: Todo producto debe tener un proveedor asignado
- RN-12: El nombre del proveedor es obligatorio

---

### CU-04: Validar Stock Mínimo

**Actor Principal:** Sistema (Automático)

**Actores Secundarios:** Administrador, Operador

**Descripción:** El sistema verifica automáticamente los niveles de stock y genera alertas cuando productos alcanzan el stock mínimo configurado.

**Precondiciones:**
- Existen productos en el inventario
- Los productos tienen stock mínimo configurado

**Flujo Principal:**

**1. Verificación al Iniciar Aplicación:**
   1. El sistema carga el inventario desde disco
   2. El sistema recorre todos los productos
   3. Para cada producto, el sistema compara cantidad actual vs stock mínimo
   4. El sistema identifica productos bajo stock
   5. Si hay productos bajo stock:
      - El sistema cuenta la cantidad de alertas
      - El sistema muestra diálogo con lista de productos
      - El sistema indica código, nombre y cantidad actual
   6. El usuario toma conocimiento y cierra el diálogo
   7. La aplicación continúa normalmente

**2. Verificación en Tiempo Real:**
   1. Cuando se retira stock de un producto
   2. El sistema verifica la cantidad resultante
   3. Si la cantidad es menor o igual al stock mínimo:
      - El sistema marca el producto en la tabla (fila roja)
      - El sistema incrementa contador de alertas
      - El sistema actualiza el indicador visual en la barra inferior
   4. El usuario visualiza la alerta en la interfaz

**3. Generación de Alerta:**
   1. El sistema detecta producto bajo stock mínimo
   2. El sistema aplica estilo visual distintivo (fondo rojo en tabla)
   3. El sistema actualiza contador: "Alertas: X producto(s) bajo stock"
   4. El sistema mantiene el indicador hasta que se reponga stock

**4. Listado de Productos Bajo Stock:**
   1. El usuario accede a "Reportes" → "Productos Bajo Stock"
   2. El sistema consulta todos los productos
   3. El sistema filtra productos donde cantidad ≤ stock mínimo
   4. El sistema muestra ventana con:
      - Tabla con productos (código, nombre, cantidad, mínimo, proveedor)
      - Total de productos bajo stock
      - Botón para imprimir o cerrar
   5. El usuario revisa la información
   6. El usuario cierra el reporte

**Flujos Alternativos:**

- **5a.** No hay productos bajo stock:
  - El sistema muestra mensaje informativo
  - El sistema indica que todos los productos tienen stock adecuado
  - No se muestra diálogo de alertas al iniciar

- **3a.** Producto vuelve a tener stock suficiente:
  - Al agregar stock, el sistema recalcula
  - Si cantidad > stock mínimo:
    - El sistema quita estilo de alerta (fila normal)
    - El sistema decrementa contador de alertas
    - El sistema actualiza interfaz

**Postcondiciones:**
- El usuario está informado sobre productos que requieren reabastecimiento
- Las alertas son visibles en múltiples lugares de la interfaz
- Se facilita la toma de decisiones para compras
- Se previene desabastecimiento

**Reglas de Negocio:**
- RN-13: Un producto está bajo stock cuando cantidad ≤ stock mínimo
- RN-14: Las alertas deben ser visibles al iniciar la aplicación
- RN-15: Las alertas deben actualizarse en tiempo real
- RN-16: Los productos bajo stock deben destacarse visualmente

---

### CU-05: Generar Reportes

**Actor Principal:** Administrador del Sistema

**Actores Secundarios:** Operador de Inventario

**Descripción:** Permite generar diferentes reportes para análisis y toma de decisiones sobre el inventario.

**Precondiciones:**
- Existen datos en el inventario
- El usuario está autenticado
- La aplicación está en ejecución

**Flujo Principal:**

**1. Reporte de Resumen de Inventario:**
   1. El usuario selecciona "Reportes" → "Resumen Inventario"
   2. El sistema calcula estadísticas generales:
      - Cantidad total de productos diferentes
      - Cantidad de proveedores registrados
      - Valor total del inventario (suma de cantidad × precio de todos los productos)
      - Cantidad de productos bajo stock
   3. El sistema muestra ventana con estadísticas
   4. El sistema presenta la información de forma clara y legible
   5. El usuario revisa el resumen
   6. El usuario cierra el reporte

**2. Reporte de Productos Bajo Stock:**
   1. El usuario selecciona "Reportes" → "Productos Bajo Stock"
   2. El sistema consulta todos los productos
   3. El sistema filtra productos con cantidad ≤ stock mínimo
   4. El sistema muestra tabla con:
      - Código del producto
      - Nombre
      - Cantidad actual
      - Stock mínimo configurado
      - Proveedor
   5. El sistema muestra total de productos en situación crítica
   6. El usuario puede identificar productos para reabastecer
   7. El usuario cierra el reporte

**3. Reporte de Productos por Proveedor:**
   1. El usuario selecciona "Reportes" → "Productos por Proveedor"
   2. El sistema muestra combo con lista de proveedores
   3. El usuario selecciona un proveedor específico
   4. El sistema consulta productos del proveedor seleccionado
   5. El sistema muestra ventana con:
      - Nombre del proveedor
      - Tabla de productos (código, nombre, cantidad, unidad, precio, valor total)
      - Cantidad total de productos del proveedor
      - Valor total de productos del proveedor
   6. El usuario analiza la información
   7. El usuario puede cambiar de proveedor o cerrar

**4. Visualización de Estadísticas en Tiempo Real:**
   1. El usuario visualiza la ventana principal
   2. El sistema muestra permanentemente en la barra inferior:
      - Total de productos registrados
      - Valor total del inventario (formato moneda)
      - Cantidad de alertas de stock bajo
   3. El sistema actualiza estas estadísticas automáticamente tras cada operación

**Flujos Alternativos:**

- **2a.** No hay productos bajo stock:
  - El sistema muestra mensaje positivo
  - El sistema indica que no hay productos que requieran atención
  - No se muestra tabla vacía

- **3a.** Proveedor sin productos:
  - El sistema muestra mensaje informativo
  - El sistema indica que el proveedor no tiene productos asociados
  - El usuario puede seleccionar otro proveedor

- **1a.** Inventario vacío:
  - El sistema muestra reporte con valores en cero
  - El sistema indica que no hay datos para reportar

**Postcondiciones:**
- El usuario tiene información actualizada del inventario
- Los reportes reflejan el estado actual del sistema
- Se facilita la toma de decisiones de negocio
- No se modifican datos del inventario

**Reglas de Negocio:**
- RN-17: Los reportes deben mostrar datos en tiempo real
- RN-18: El valor total se calcula como: Σ(cantidad × precio_costo)
- RN-19: Los reportes deben ser claros y fáciles de interpretar
- RN-20: Las estadísticas deben actualizarse automáticamente

---

### CU-06: Gestionar Persistencia

**Actor Principal:** Sistema / Administrador

**Descripción:** Maneja el almacenamiento y recuperación de datos del inventario en formato JSON, incluyendo funcionalidades de guardado manual y backup.

**Precondiciones:**
- El sistema tiene permisos de escritura en el directorio
- Existe espacio en disco disponible

**Flujo Principal:**

**1. Cargar Datos al Iniciar:**
   1. La aplicación se inicia
   2. El sistema verifica si existe archivo "inventario_agrocol.json"
   3. Si existe:
      - El sistema lee el archivo JSON
      - El sistema deserializa productos y proveedores
      - El sistema reconstruye objetos en memoria
      - El sistema carga el inventario completo
   4. Si no existe:
      - El sistema crea inventario vacío
      - El sistema está listo para agregar datos
   5. El sistema muestra la ventana principal con datos cargados

**2. Guardar Datos Manualmente:**
   1. El usuario selecciona "Archivo" → "Guardar"
   2. El sistema serializa todos los productos y proveedores a diccionarios
   3. El sistema crea estructura JSON:
      ```json
      {
        "productos": [...],
        "proveedores": [...]
      }
      ```
   4. El sistema escribe el archivo "inventario_agrocol.json"
   5. El sistema muestra mensaje de confirmación
   6. Los datos quedan persistidos en disco

**3. Guardado Automático al Salir:**
   1. El usuario intenta cerrar la aplicación
   2. El sistema muestra diálogo de confirmación
   3. El sistema pregunta si desea guardar cambios
   4. Si el usuario acepta:
      - El sistema guarda el inventario (igual que guardado manual)
      - El sistema cierra la aplicación
   5. Si el usuario cancela:
      - La aplicación permanece abierta

**4. Crear Backup:**
   1. El usuario selecciona "Archivo" → "Crear Backup"
   2. El sistema obtiene fecha y hora actual
   3. El sistema genera nombre: "inventario_agrocol_backup_YYYYMMDD_HHMMSS.json"
   4. El sistema copia el contenido del inventario al archivo de backup
   5. El sistema guarda el archivo en el mismo directorio
   6. El sistema muestra confirmación con nombre del archivo generado
   7. El usuario puede usar el backup para restauración futura

**Flujos Alternativos:**

- **3a.** Archivo JSON corrupto al cargar:
  - El sistema detecta error de formato
  - El sistema muestra mensaje de error descriptivo
  - El sistema inicia con inventario vacío
  - El usuario debe restaurar desde backup o recrear datos

- **2a.** Error al guardar (permisos, disco lleno):
  - El sistema captura la excepción
  - El sistema muestra mensaje de error con detalles
  - Los datos permanecen en memoria
  - El usuario puede intentar guardar en otra ubicación

- **4a.** Error al crear backup:
  - El sistema muestra mensaje de error
  - El archivo original no se ve afectado
  - El usuario puede intentar nuevamente

- **3b.** Usuario elige no guardar al salir:
  - El sistema cierra sin guardar
  - Los cambios desde el último guardado se pierden
  - Se confirma la acción antes de cerrar

**Postcondiciones:**
- Los datos del inventario están persistidos en disco
- Se puede recuperar la información en sesiones futuras
- Existe copia de seguridad disponible si se creó backup
- El archivo JSON es legible y válido

**Reglas de Negocio:**
- RN-21: Los datos deben guardarse en formato JSON
- RN-22: El archivo principal se llama "inventario_agrocol.json"
- RN-23: Los backups deben incluir fecha y hora en el nombre
- RN-24: Al salir se debe preguntar si guardar cambios
- RN-25: El sistema debe manejar errores de archivo gracefully

---

### CU-07: Buscar y Filtrar Información

**Actor Principal:** Todos los usuarios del sistema

**Descripción:** Permite localizar rápidamente productos en el inventario mediante búsqueda en tiempo real.

**Precondiciones:**
- Existen productos en el inventario
- La aplicación está en ejecución

**Flujo Principal:**

**1. Búsqueda en Tiempo Real:**
   1. El usuario enfoca el campo de búsqueda en la parte superior
   2. El usuario comienza a escribir un término de búsqueda
   3. El sistema captura cada tecla presionada
   4. El sistema filtra la tabla inmediatamente
   5. El sistema busca coincidencias en:
      - Código de producto
      - Nombre de producto
   6. El sistema muestra solo productos que coinciden (parcial o total)
   7. El sistema mantiene formato y colores (ej: alertas rojas)
   8. El usuario visualiza resultados filtrados en tiempo real

**2. Búsqueda por Código:**
   1. El usuario escribe código exacto o parcial
   2. El sistema compara con códigos de productos
   3. El sistema muestra productos cuyo código contiene el texto
   4. El usuario identifica el producto buscado

**3. Búsqueda por Nombre:**
   1. El usuario escribe nombre o parte del nombre
   2. El sistema compara con nombres de productos (case-insensitive)
   3. El sistema muestra productos cuyo nombre contiene el texto
   4. El usuario puede ver múltiples coincidencias

**4. Limpiar Búsqueda:**
   1. El usuario borra el texto del campo de búsqueda
   2. El sistema detecta campo vacío
   3. El sistema muestra todos los productos nuevamente
   4. La tabla vuelve a su estado completo

**Flujos Alternativos:**

- **3a.** No se encuentran coincidencias:
  - El sistema muestra tabla vacía
  - El sistema no muestra mensaje de error
  - El usuario puede modificar el término de búsqueda
  - Al borrar, se muestran todos los productos nuevamente

- **1a.** Búsqueda con caracteres especiales:
  - El sistema los trata como texto literal
  - El sistema busca coincidencias exactas incluyendo esos caracteres

**Postcondiciones:**
- El usuario puede localizar productos rápidamente
- La tabla muestra solo información relevante
- No se modifican datos del inventario
- La búsqueda puede cancelarse fácilmente

**Reglas de Negocio:**
- RN-26: La búsqueda debe ser instantánea (sin botón buscar)
- RN-27: Se debe buscar en código y nombre simultáneamente
- RN-28: La búsqueda no distingue mayúsculas/minúsculas
- RN-29: Se deben mantener alertas visuales en resultados filtrados

---

## Resumen de Actores y Responsabilidades

| Actor | Responsabilidades |
|-------|------------------|
| **Administrador** | - Gestión completa de productos<br>- Gestión de proveedores<br>- Generación de reportes<br>- Creación de backups<br>- Configuración del sistema |
| **Operador de Inventario** | - Agregar stock (entradas)<br>- Retirar stock (salidas)<br>- Consultar disponibilidad<br>- Búsqueda de productos<br>- Visualizar reportes |
| **Sistema** | - Validación automática de stock mínimo<br>- Generación de alertas<br>- Cálculo de estadísticas<br>- Guardado y carga de datos<br>- Actualización de interfaz |

---

## Matriz de Trazabilidad: Casos de Uso vs Requisitos Funcionales

| Caso de Uso | Requisito Funcional | Prioridad |
|-------------|---------------------|-----------|
| CU-01 | RF-01: Gestión de productos agrícolas | Alta |
| CU-02 | RF-02: Control de entradas y salidas | Alta |
| CU-03 | RF-03: Gestión de proveedores | Media |
| CU-04 | RF-04: Sistema de alertas automáticas | Alta |
| CU-05 | RF-05: Generación de reportes | Media |
| CU-06 | RF-06: Persistencia local de datos | Alta |
| CU-07 | RF-07: Búsqueda y filtrado rápido | Media |

---

## Notas de Implementación

### Tecnologías Utilizadas:
- **Lenguaje:** Python 3.7+
- **Interfaz Gráfica:** Tkinter (estándar de Python)
- **Persistencia:** JSON (archivo local)
- **Patrón Arquitectónico:** Modelo-Vista-Controlador (MVC) simplificado

### Estructura de Archivos:
```
AppInventarioIA/
├── main.py                          # Punto de entrada
├── src/
│   ├── modelos/
│   │   ├── producto.py              # Clase Producto
│   │   ├── proveedor.py             # Clase Proveedor
│   │   ├── inventario.py            # Clase Inventario
│   │   └── usuario.py               # Sistema de usuarios
│   ├── interfaz/
│   │   ├── ventana_principal.py     # CU-01, CU-02, CU-04, CU-05, CU-07
│   │   ├── ventana_producto.py      # CU-01 (formularios)
│   │   └── ventana_proveedor.py     # CU-03 (formularios)
│   └── persistencia/
│       └── persistencia.py          # CU-06 (guardado/carga)
└── inventario_agrocol.json          # Almacenamiento de datos
```

### Principios de Diseño Aplicados:
- **Encapsulación:** Atributos privados con properties
- **Responsabilidad Única:** Cada clase tiene una función específica
- **Bajo Acoplamiento:** Módulos independientes
- **Alta Cohesión:** Funcionalidad relacionada agrupada
