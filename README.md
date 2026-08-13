# Urban Routes — Automatización de pruebas E2E

## Descripción del proyecto

Este proyecto corresponde al Sprint 9 del programa de QA Engineer de TripleTen.

El objetivo es automatizar mediante Selenium el flujo completo para solicitar un taxi en la aplicación web **Urban Routes**.

Las pruebas automatizadas verifican diferentes acciones del usuario, desde introducir las direcciones de origen y destino hasta solicitar un taxi y comprobar que aparezca el modal correspondiente.

## Funcionalidades automatizadas

El proyecto cubre las siguientes pruebas:

1. Configurar la dirección de origen y destino.
2. Seleccionar la tarifa **Comfort**.
3. Introducir y confirmar un número de teléfono.
4. Agregar una tarjeta de crédito.
5. Escribir un mensaje para el conductor.
6. Solicitar manta y pañuelos.
7. Solicitar dos helados.
8. Pedir un taxi y comprobar que aparezca el modal de búsqueda.

Actualmente las 8 pruebas obligatorias se ejecutan correctamente mediante `pytest`.

## Tecnologías utilizadas

* Python
* Selenium WebDriver
* Pytest
* Google Chrome
* PyCharm
* Git
* GitHub

## Técnicas utilizadas

### Page Object Model

El proyecto utiliza una estructura basada en **Page Object Model (POM)**.

La clase `UrbanRoutesPage` contiene:

* Localizadores de los elementos de la interfaz.
* Métodos para interactuar con Urban Routes.
* Esperas explícitas mediante `WebDriverWait`.
* Acciones como introducir texto, hacer clic y consultar valores.

La clase `TestUrbanRoutes` contiene las pruebas automatizadas.

### Esperas explícitas

Se utiliza `WebDriverWait` junto con `expected_conditions` para esperar a que los elementos estén disponibles antes de interactuar con ellos.

Esto ayuda a evitar errores provocados por intentar acceder a un elemento antes de que termine de cargar.

### Recuperación del código de teléfono

Para confirmar el número de teléfono se utiliza la función `retrieve_phone_code()` proporcionada por TripleTen.

La función obtiene el código de confirmación utilizando los registros de rendimiento de Chrome.

### Interacción con la tarjeta

Para agregar una tarjeta se completan el número y el código CVV.

Después de introducir el CVV se utiliza `Keys.TAB` para hacer que el campo pierda el enfoque y habilitar el botón para agregar la tarjeta.

## Estructura del proyecto

```text
qa-project-Urban-Routes-es/
│
├── data.py
├── main.py
└── README.md
```

### `data.py`

Contiene los datos utilizados por las pruebas:

* URL de Urban Routes.
* Dirección de origen.
* Dirección de destino.
* Número de teléfono.
* Número de tarjeta.
* Código de tarjeta.
* Mensaje para el conductor.

### `main.py`

Contiene:

* La función `retrieve_phone_code()`.
* La clase `UrbanRoutesPage`.
* Los localizadores de Selenium.
* Los métodos para interactuar con la aplicación.
* La clase `TestUrbanRoutes`.
* Las pruebas automatizadas.

## Requisitos

Para ejecutar el proyecto es necesario tener instalado:

* Python
* Google Chrome
* Selenium
* Pytest

## Instalación de dependencias

Desde la terminal del proyecto ejecutar:

```bash
python -m pip install selenium pytest
```

## Configuración del servidor

Antes de ejecutar las pruebas es necesario iniciar el servidor de Urban Routes desde la plataforma de TripleTen.

Después se debe copiar la URL completa generada, incluyendo:

```text
?lng=es
```

La URL debe colocarse en `data.py`:

```python
urban_routes_url = 'URL_DEL_SERVIDOR?lng=es'
```

La URL puede cambiar al reiniciar el servidor, por lo que debe actualizarse antes de volver a ejecutar las pruebas.

## Ejecución de las pruebas

Abrir la terminal de PyCharm en la carpeta raíz del proyecto y ejecutar:

```bash
python -m pytest main.py -v
```

Pytest ejecutará todas las pruebas automatizadas.

## Resultado esperado

La ejecución correcta debe mostrar las 8 pruebas aprobadas:

```text
test_set_route PASSED
test_select_comfort PASSED
test_set_phone_number PASSED
test_add_card PASSED
test_message_for_driver PASSED
test_blanket_and_handkerchiefs PASSED
test_two_ice_creams PASSED
test_order_taxi PASSED
```

Resultado:

```text
8 passed
```

## Autor

Fidel Ortega

Proyecto realizado como parte de la formación de **QA Engineer de TripleTen**.
