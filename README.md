# Proyecto-arcial-Corte-3

## Integrante

- **Alejandro Moreno Lacharme**

---

## Estructura del repositorio

El repositorio contiene dos carpetas principales:

- `/pokemon-battle` – Proyecto en C++ de combate por turnos entre Pokémon.
- `/parqueadero` – Proyecto en Python de gestión de parqueadero con interfaz por consola.

---

## Desarrollos innovadores por proyecto

### 1. **Proyecto Pokémon – Lenguaje: C++**

**Requisitos mínimos cumplidos:**
- Combate por turnos entre dos Pokémon.
- Menú textual de interacción para el jugador.
- Cada Pokémon tiene al menos dos ataques.
- Finalización automática del combate con anuncio del ganador.

**Desarrollos innovadores:**
- **Modularidad del código:** El sistema está dividido en clases como `Pokemon` y `Ataque`, permitiendo una mejor mantenibilidad y escalabilidad.
- **Sistema de tipos y daño variable:** Se implementa un sistema de ataques con diferencias en daño y probabilidad de éxito, lo que enriquece la estrategia del jugador.
- **Simulación animada de turnos:** El uso de impresión secuencial y mensajes durante el combate mejora la experiencia del usuario.
- **Extensibilidad preparada:** El diseño permite agregar fácilmente nuevos Pokémon o ataques con diferentes efectos.

---

### 2. **Proyecto Parqueadero – Lenguaje: Python**

**Requisitos mínimos cumplidos:**
- Mapa visual mayor a 7x7 (10x10), con vías, entrada, salida y espacios accesibles.
- Registro de vehículos con placa y tiempo de entrada.
- Sistema de cobro por tiempo de permanencia, según el tipo de vehículo.
- Visualización en tiempo real de espacios disponibles y ocupados.

**Desarrollos innovadores:**
- **Visualización a color del mapa:** Uso de códigos ANSI para mostrar gráficamente en consola los espacios libres (verde), ocupados (rojo), entrada (azul), salida (amarillo), vías (blanco) y bordes (gris), mejorando la comprensión visual.
- **Sistema de tipos de vehículo con tarifas diferenciadas:** El usuario puede seleccionar entre *carro*, *camioneta* y *moto*, cada uno con una tarifa distinta, añadiendo realismo y personalización al sistema.
- **Asignación automática de parqueadero:** El sistema busca el primer espacio libre disponible y lo asigna automáticamente al vehículo que ingresa.
- **Manejo de errores robusto:** Validación del tipo de vehículo, control de vehículos duplicados y manejo de entradas/salidas no registradas correctamente.
- **Estructura modular del código:** Separación clara en clases y archivos (`Main`,`Vehiculo`, `Parqueadero`, `Registro`, `Utilidades`), facilitando futuras ampliaciones y mantenibilidad del proyecto.
- **Cálculo preciso del tiempo:** Se calcula el tiempo exacto de permanencia del vehículo en minutos, mejorando la precisión del cobro.
