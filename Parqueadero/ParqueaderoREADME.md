# README.md: Sistema de Parqueadero

---

Este documento detalla el diseño y la implementación de un **sistema de gestión de parqueadero** desarrollado en Python. El sistema permite visualizar un mapa del parqueadero, registrar la entrada y salida de vehículos, y calcular la tarifa de estacionamiento basada en el tiempo y el tipo de vehículo.

## 1. Propósito e Implementación del Proyecto

### ¿Para qué se implementó?

Este proyecto se implementó con el objetivo de simular y gestionar las operaciones básicas de un parqueadero. Su propósito principal es:

* **Administrar espacios de estacionamiento**: Mantener un registro de los espacios disponibles y ocupados en un mapa virtual.
* **Registrar movimientos de vehículos**: Permitir la entrada y salida de vehículos, registrando la hora y calculando el tiempo de permanencia.
* **Calcular tarifas**: Determinar el costo de estacionamiento basándose en el tiempo transcurrido y el tipo de vehículo.
* **Proveer una interfaz de usuario simple**: Ofrecer un menú interactivo para que el usuario pueda realizar las operaciones.

### ¿Por qué se consideró necesario?

Se consideró necesario por las siguientes razones:

* **Aplicación práctica de la POO**: Permite demostrar cómo los conceptos de clases y objetos pueden modelar entidades del mundo real (vehículos, parqueadero, registros).
* **Gestión de recursos**: Simula un escenario de gestión de recursos limitados (espacios de parqueo).
* **Manejo de datos y tiempo**: Involucra la captura y manipulación de datos de entrada (placas, tipos de vehículos) y el cálculo de diferencias de tiempo.
* **Modularidad del código**: La división del proyecto en múltiples archivos (`main.py`, `parqueadero.py`, `vehiculo.py`, `registro.py`, `utilidades.py`) promueve un diseño limpio y mantenible.

### ¿Cómo se llevó a cabo su implementación?

La implementación se llevó a cabo siguiendo una estructura modular y orientada a objetos:

1.  **Definición de clases principales**: Se crearon clases para representar las entidades clave: `Vehiculo`, `Parqueadero` y `Registro`.
2.  **Manejo de utilidades**: Se segregaron funciones y constantes relacionadas con tarifas y cálculos de tiempo en un módulo `utilidades.py` para mayor claridad y reutilización.
3.  **Configuración del mapa**: La clase `Parqueadero` incluye lógica para inicializar un mapa bidimensional, definiendo bordes, vías y espacios de estacionamiento.
4.  **Flujo de operaciones**: La función `menu()` en `main.py` coordina las interacciones del usuario, llamando a los métodos apropiados de la clase `Parqueadero` para ingresar, retirar o mostrar vehículos.
5.  **Cálculo de tarifas dinámico**: Se implementó la lógica para calcular la tarifa en función del tiempo estacionado y el tipo de vehículo.

---

## 2. Documentación Detallada del Código

El proyecto está compuesto por cinco archivos Python, cada uno con una responsabilidad específica, lo que favorece la modularidad y la Programación Orientada a Objetos (POO).

### 2.1. `main.py`

Este archivo contiene la lógica principal del programa y la interfaz de usuario.

* **Función `menu()`**:
    * Crea una instancia de `Parqueadero` con un tamaño de 10x10.
    * Presenta un menú interactivo al usuario con opciones: "Mostrar Mapa y Disponibilidad", "Ingresar Vehículo", "Retirar Vehículo" y "Salir".
    * Utiliza un bucle `while True` para mantener el menú activo hasta que el usuario elija "Salir".
    * Según la opción seleccionada:
        * **Opción 1 (`mostrar_mapa`):** Llama al método `mostrar_mapa()` del objeto `parqueadero`.
        * **Opción 2 (`ingresar_vehiculo`):** Solicita la placa y el tipo de vehículo al usuario (carro, camioneta, moto). Valida la opción de tipo de vehículo y llama al método `ingresar_vehiculo()` del objeto `parqueadero`, pasando la placa y el tipo. Si la opción de tipo es inválida, asigna 'carro' por defecto.
        * **Opción 3 (`retirar_vehiculo`):** Solicita la placa del vehículo y llama al método `retirar_vehiculo()` del objeto `parqueadero`.
        * **Opción 4 (`Salir`):** Imprime un mensaje de despedida y rompe el bucle, terminando el programa.
        * Para opciones inválidas, imprime un mensaje de error.
* **Bloque `if __name__ == '__main__':`**: Asegura que la función `menu()` se ejecute solo cuando el script se ejecuta directamente (no cuando se importa como módulo).

### 2.2. `parqueadero.py`

Este archivo define la clase `Parqueadero`, que gestiona la estructura física y las operaciones del parqueadero.

* **Clase `Parqueadero`**:
    * **Constructor (`__init__`)**:
        * Inicializa el parqueadero con un número de `filas` y `columnas` (por defecto 10x10).
        * Crea un `mapa` bidimensional (una lista de listas) inicializado con '#' (bordes).
        * Crea una instancia de `Registro` para gestionar las entradas y salidas de vehículos.
        * Llama a `_configurar_mapa()` para establecer la disposición inicial del parqueadero.
        * `self.vehiculos_en_espacios = {}`: Un diccionario para almacenar la ubicación `(r, c)` de cada vehículo en el mapa, mapeando la placa a sus coordenadas.
    * **Método `_configurar_mapa()`**:
        * Es un método "privado" (convención Python con `_` inicial) para configurar la estructura del mapa.
        * Establece los bordes del parqueadero con '#'.
        * Define una vía principal central con 'V'.
        * Asigna 'E' para la entrada y 'S' para la salida en la vía central.
        * Asigna espacios de parqueo 'P' a ambos lados de la vía principal, evitando los bordes y la entrada/salida.
        * Imprime el número de espacios de parqueo configurados.
    * **Método `mostrar_mapa()`**:
        * Imprime una representación visual del `mapa` del parqueadero.
        * Utiliza códigos de escape ANSI para colorear los diferentes tipos de celdas: verde para 'P' (libres), rojo para 'O' (ocupados), azul para 'E' (entrada), amarillo para 'S' (salida), blanco para 'V' (vía) y gris para '#' (bordes/obstáculos).
        * Calcula y muestra el número de espacios libres, ocupados y el total de espacios de parqueo.
    * **Método `ingresar_vehiculo(self, placa, tipo_vehiculo)`**:
        * Verifica si un vehículo con la misma placa ya está en el parqueadero utilizando el registro. Si es así, imprime un mensaje y retorna.
        * Valida que el `tipo_vehiculo` sea uno de los tipos permitidos (carro, camioneta, moto) basándose en `TARIFAS_POR_MINUTO`. Si no es válido, imprime un error y retorna.
        * Busca el primer espacio 'P' (libre) en el mapa.
        * Si encuentra un espacio:
            * Crea un objeto `Vehiculo` con la placa y el tipo.
            * Asigna las coordenadas del espacio al atributo `espacio_asignado` del vehículo.
            * Cambia el estado de la celda en el `mapa` a 'O' (ocupado).
            * Registra la entrada del vehículo utilizando `self.registro.registrar_entrada()`.
            * Almacena la ubicación del vehículo en `self.vehiculos_en_espacios`.
            * Imprime un mensaje de confirmación.
        * Si no hay espacios disponibles, imprime un mensaje.
    * **Método `retirar_vehiculo(self, placa)`**:
        * Intenta registrar la salida del vehículo utilizando `self.registro.registrar_salida(placa)`. Si el vehículo no se encuentra, imprime un mensaje y retorna.
        * Recupera las coordenadas `(r, c)` del vehículo del diccionario `self.vehiculos_en_espacios`.
        * Libera el espacio en el `mapa` cambiando la celda de 'O' a 'P'.
        * Elimina la entrada del vehículo de `self.vehiculos_en_espacios`.
        * Calcula el tiempo estacionado en minutos usando `vehiculo.obtener_tiempo_estacionado()`.
        * Calcula la tarifa a pagar utilizando la función `calcular_tarifa()` del módulo `utilidades`, pasando los minutos y el tipo de vehículo.
        * Imprime un resumen de la salida del vehículo, incluyendo el tiempo y la tarifa.
        * Maneja el caso donde la ubicación del vehículo no se encuentra en `vehiculos_en_espacios`, pero el registro de salida se completa.

### 2.3. `registro.py`

Este archivo define la clase `Registro`, que se encarga de llevar un control de los vehículos actualmente en el parqueadero.

* **Clase `Registro`**:
    * **Constructor (`__init__`)**:
        * Inicializa un diccionario vacío `self.entradas` para almacenar los objetos `Vehiculo` usando su placa como clave.
    * **Método `registrar_entrada(self, vehiculo)`**:
        * Agrega el objeto `vehiculo` al diccionario `self.entradas` usando su atributo `placa` como clave.
    * **Método `registrar_salida(self, placa)`**:
        * Remueve y devuelve el objeto `Vehiculo` asociado a la `placa` del diccionario `self.entradas`.
        * Si la `placa` no se encuentra, devuelve `None`.
    * **Método `obtener_vehiculo(self, placa)`**:
        * Devuelve el objeto `Vehiculo` asociado a la `placa` del diccionario `self.entradas` sin removerlo.
        * Si la `placa` no se encuentra, devuelve `None`.

### 2.4. `vehiculo.py`

Este archivo define la clase `Vehiculo`, que representa a cada vehículo individual que ingresa al parqueadero.

* **Clase `Vehiculo`**:
    * **Constructor (`__init__`)**:
        * Inicializa un vehículo con su `placa` y `tipo` (ej., 'carro', 'camioneta', 'moto').
        * Registra la `hora_entrada` del vehículo usando `datetime.now()` al momento de su creación.
        * Inicializa `espacio_asignado` a `None`, que luego será actualizado con las coordenadas del espacio de parqueo.
    * **Método `obtener_tiempo_estacionado()`**:
        * Calcula el tiempo transcurrido desde `hora_entrada` hasta el momento actual (`datetime.now()`).
        * Devuelve la diferencia en minutos (`total_seconds() / 60`).
    * **Método `__str__()`**:
        * Define la representación en cadena del objeto `Vehiculo` para una impresión fácil.
        * Retorna una cadena formateada que incluye la placa, el tipo y la hora de entrada del vehículo.

### 2.5. `utilidades.py`

Este archivo contiene constantes y funciones auxiliares relacionadas con el cálculo de tarifas.

* **`TARIFAS_POR_MINUTO`**:
    * Un diccionario que almacena las tarifas por minuto para diferentes tipos de vehículos.
    * Define: 'carro': $100/min, 'camioneta': $150/min, 'moto': $70/min.
* **Función `calcular_tarifa(minutos, tipo_vehiculo)`**:
    * Recibe el `minutos` estacionados y el `tipo_vehiculo`.
    * Obtiene la `tarifa_por_minuto_especifica` del diccionario `TARIFAS_POR_MINUTO` para el `tipo_vehiculo` dado (insensible a mayúsculas/minúsculas con `.lower()`). Si el tipo no se encuentra, devuelve 0.
    * Si la tarifa específica es 0 (tipo no reconocido), imprime una advertencia.
    * Calcula el `valor_a_pagar` multiplicando los `minutos` por la `tarifa_por_minuto_especifica`.
    * Devuelve el `valor_a_pagar`.

### 2.6. `Herramientas de apoyo`

En este código al momento de implementar funciones como datetime, fue consultado su uso e implementacion en el código con apoyo de IA con el propósito de entender mejor la forma como funciona el sistema de cobro con base en el tiempo del parqueadero.

---
