# README.md: Juego de Batalla Pokemon Básico

---

Este documento detalla el diseño y la implementación de un **juego de batalla Pokemon básico** desarrollado en C++. El juego simula combates entre un Pokemon del jugador y una serie de Pokemon rivales, incorporando elementos como ataques, vida, y la posibilidad de curación y captura.

## 1. Propósito e Implementación del Proyecto

### ¿Para qué se implementó?

Este proyecto se implementó con el objetivo de crear una **simulación simple y funcional de batallas Pokemon**, utilizando los principios de la **Programación Orientada a Objetos (POO)**. Sirve como una base para comprender cómo interactúan diferentes entidades (los Pokemon) dentro de un sistema definido por reglas de juego.

### ¿Por qué se consideró necesario?

Se consideró necesario para:

* **Demostrar la aplicación de la POO:** A través de la creación de la clase `Pokemon`, se encapsulan características (nombre, vida, ataques) y comportamientos (atacar, recibir golpe).
* **Practicar la lógica de juego:** Implementar turnos, gestión de vida, selección de ataques y la introducción de objetos.
* **Explorar el uso de estructuras de datos:** El `vector` se utiliza para manejar múltiples Pokemon rivales y los Pokemon capturados.
* **Introducir conceptos de aleatoriedad:** El uso de `rand()` para la selección de ataques del rival y la probabilidad de captura añade un elemento dinámico al juego.

### ¿Cómo se llevó a cabo su implementación?

La implementación se llevó a cabo siguiendo los siguientes pasos:

1.  **Diseño de la clase `Pokemon`:** Se definió la estructura base para cualquier Pokemon, incluyendo sus atributos (nombre, vida, ataques y sus respectivos golpes) y métodos (obtener nombre, obtener vida, verificar si está vivo, restaurar vida, mostrar ataques, usar ataque, obtener nombre de ataque y recibir golpe).
2.  **Manejo de la lógica del juego:** Se estableció un bucle principal que simula los combates. Este bucle incluye la alternancia de turnos entre el jugador y el rival.
3.  **Implementación de interacciones del jugador:** Se permiten acciones como atacar y usar objetos, ofreciendo opciones al jugador durante el combate.
4.  **Integración de la aleatoriedad:** Se utilizaron funciones aleatorias para las decisiones del oponente y las probabilidades de eventos como la captura.
5.  **Gestión de objetos:** Se implementó un sistema básico de `pokebolas` y `curas` para añadir estrategia al juego.
6.  **Control de flujo del juego:** Se definieron condiciones de victoria y derrota para cada combate y para el juego en general.

---

## 2. Documentación Detallada del Código

### Estructura del Código

El código está organizado en una **clase `Pokemon`** y la función principal `main()`, junto con algunas funciones auxiliares.

### Clase `Pokemon`

La clase `Pokemon` es el pilar de la programación orientada a objetos en este juego. Representa a cada criatura con sus atributos y habilidades.

* **Atributos (miembros de datos):**
    * `string nombre`: El nombre del Pokemon (ej., "Pikachu").
    * `int vida`: Los puntos de salud actuales del Pokemon.
    * `string ataque1`, `ataque2`, `ataque3`: Nombres de los tres ataques disponibles para el Pokemon.
    * `int golpe1`, `golpe2`, `golpe3`: El valor de daño asociado a cada ataque.

* **Constructor:**
    ```cpp
    Pokemon(string nombre, int vida, string ataque1, int golpe1, string ataque2, int golpe2, string ataque3, int golpe3)
        : nombre(nombre), vida(vida), ataque1(ataque1), golpe1(golpe1), ataque2(ataque2), golpe2(golpe2), ataque3(ataque3), golpe3(golpe3) {}
    ```
    Este constructor inicializa un objeto `Pokemon` con todos sus atributos al momento de su creación. Utiliza una **lista de inicialización de miembros** para asignar los valores pasados como argumentos a los miembros de la clase.

* **Métodos (funciones miembro):**
    * `string getNombre()`: Devuelve el nombre del Pokemon.
    * `int getVida()`: Devuelve la vida actual del Pokemon.
    * `bool estaVivo()`: Devuelve `true` si la vida del Pokemon es mayor que 0, indicando que aún está en combate.
    * `void restaurarVida()`: Restaura la vida del Pokemon a un valor predefinido (30 en este caso).
    * `void mostrarAtaques()`: Imprime en consola los nombres y los valores de impacto de los tres ataques del Pokemon, permitiendo al jugador o al sistema conocer las opciones disponibles.
    * `int usarAtaque(int opcion)`:
        * Recibe un número que representa la opción de ataque elegida (1, 2 o 3).
        * Incluye un bucle `while` para **validar la entrada del usuario**, asegurándose de que la opción esté dentro del rango permitido.
        * Utiliza un `switch` para devolver el valor de impacto (`golpe`) correspondiente al ataque seleccionado.
    * `string getNombreAtaque(int opcion)`:
        * Recibe un número de opción de ataque.
        * Utiliza un `switch` para devolver el nombre del ataque correspondiente a la opción.
    * `void recibirGolpe(int cantidad)`:
        * Recibe un valor de daño (`cantidad`).
        * Resta esta cantidad a la vida actual del Pokemon.
        * Asegura que la vida no baje de cero (`vida = 0`) si el daño excede la vida restante, evitando valores negativos.

### Funciones Auxiliares

* `void mostrarMenuObjetos(int pokebolas, int curas, vector<string> pokemonsCapturados)`:
    * Muestra al jugador la cantidad actual de pokebolas y objetos de curación.
    * Lista los nombres de los Pokemon que han sido capturados hasta el momento.
    * Proporciona información útil para que el jugador tome decisiones estratégicas sobre el uso de objetos.

* `bool intentarCaptura(string nombre, int vecesDerrotado, int& pokebolas, vector<string>& capturados)`:
    * Simula el intento de captura de un Pokemon.
    * Verifica si el jugador tiene `pokebolas` disponibles.
    * Decrementa el número de `pokebolas` si se realiza el intento.
    * Calcula una `probabilidad` de captura basada en el número de veces que el Pokemon ha sido derrotado (`vecesDerrotado`). La probabilidad aumenta con cada derrota, con un máximo del 80% (`min(20 * vecesDerrotado, 80)`). Esto significa que la probabilidad inicial es del 20% (para 1 derrota), luego 40%, 60%, 80%, y se mantiene en 80% si es derrotado más veces.
    * `int chance = rand() % 100;`: **Esta línea genera un número aleatorio entre 0 y 99 (inclusive).** Se utiliza la función `rand()` de la librería `<cstdlib>` para obtener un número pseudoaleatorio. El operador `% 100` (módulo 100) asegura que el resultado esté en el rango de 0 a 99, lo que es ideal para comparar con un porcentaje (0-100).
    * Si `chance` es menor que la `probabilidad` calculada, la captura es exitosa, el Pokemon se añade a la lista de `capturados` y se devuelve `true`. De lo contrario, la captura falla y se devuelve `false`.

### Función `main()`

La función `main()` orquesta el flujo principal del juego.

* **Inicialización de aleatoriedad:**
    ```cpp
    srand(time(0));
    ```
    Esta línea inicializa el generador de números pseudoaleatorios. `srand()` toma una "semilla" para empezar a generar números. `time(0)` devuelve el tiempo actual del sistema (en segundos desde el 1 de enero de 1970). Al usar el tiempo actual como semilla, se asegura que la secuencia de números aleatorios sea diferente cada vez que se ejecuta el programa, lo que hace que la experiencia de juego sea menos predecible. Si no se usara `srand()`, `rand()` generaría la misma secuencia de números cada vez.

* **Creación de Pokemon:** Se instancian varios objetos `Pokemon` (Pikachu, Charmander, Squirtle, Bulbasaur) con sus nombres, vida y ataques predefinidos.
* **Listas de juego:**
    * `vector<Pokemon> rivales`: Contiene los Pokemon que el jugador deberá enfrentar.
    * `vector<int> derrotas`: Almacena el número de veces que cada Pokemon rival ha sido derrotado, lo cual influye en la probabilidad de captura.
    * `vector<string> pokemonsCapturados`: Guarda los nombres de los Pokemon que el jugador ha logrado capturar.
    * `int pokebolas` y `int curas`: Contadores para los objetos disponibles.
* **Elección del Pokemon del jugador:** Se le pide al usuario que elija su Pokemon inicial.
* **Bucle de combate:** Se itera a través de cada Pokemon en el vector `rivales`.
    * Dentro de cada combate, se resetea la vida de ambos Pokemon (`restaurarVida()`).
    * Un bucle `while` simula los turnos de combate mientras ambos Pokemon estén vivos.
    * **Menú de acciones:** El jugador puede elegir entre atacar o usar objetos.
        * Si elige usar objeto, se muestra el menú de objetos y se da la opción de usar una curación si hay disponibles.
    * **Turno del jugador:** Se le pide al jugador que elija un ataque, se calcula el daño y el rival lo recibe.
    * **Turno del rival:** El rival elige un ataque aleatoriamente (`ataque = (rand() % 3) + 1;`) y el jugador recibe el daño.
    * Se actualiza y muestra la vida de ambos Pokemon después de cada ataque.
* **Resultados del combate:**
    * Si el jugador derrota al rival, se incrementa el contador de derrotas del rival.
    * Hay una **probabilidad del 50% de obtener una Pokebola o un objeto de curación** después de cada victoria, hasta un máximo de 3 de cada uno.
    * Se le da la opción al jugador de intentar capturar al Pokemon derrotado, utilizando la función `intentarCaptura`.
    * Si el Pokemon del jugador es derrotado, el juego termina.
* **Condición de victoria final:** Si el jugador logra capturar a los tres Pokemon rivales, se muestra un mensaje de felicitación.

---
