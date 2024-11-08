# Proyecto Urban Grocers Nayibe Luna Sprint 7, Grupo 15.

# Creación de un kit para el usuario o usuaria
- El objetivo de este proyecto es crear un kit dentro de un usuario o usuaria, no una tarjeta.
- Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
- Para instalar el paquete Pytest existen dos metodos:
- 1) Usando el comando "pip" en la terminal
- Primero abre la terminal o consola luego ingresa el comando: pip install pytest. pip es el gestor de paquetes de Python.
- 2) A traves de la interfaz de pycharm en "Python packages"
- En pycharm dirigete al panel inferior y selecciona la pestaña "Python packages". 
- En el campo de busqueda introduce "Pytest"
- Localiza y selecciona el paquete "Pytest" de la lista y haz click en el boton "install"
- Para instalar el paquete requests existen dos metodos:
- 1) Usando el comando "pip" en la terminal
- Abre la terminal o consola, ingresa el comando pip install requests.
- 2) En pycharm dirigete al panel inferior y selecciona la pestaña "Python packages"
- En la barra de busqueda, escribe "requests", localiza y selecciona el paquete requests de la lista, haz click en el boton "install".
# EJECUCION DE LA PRUEBA
- Dirigete a la pestaña de la "terminal" en la parte inferior de PyCharm.
- para ejecutar las pruebas escribe pytest \qa-project-Urban-Grocers-app-es\create_kit_name_kit_test.py 

- Una caracteristica clave de pytest es que reconoce las pruebas basandose en un prefijo especifico.
- Por eso en este proyecto las funciones que empiezan con test (en minusculas) son tratadas como pruebas.
- Ejecuta todas las pruebas con el comando pytest.
- Fuente de la documentacion: Apidoc
- Ejecuta las pruebas implementadas segun la lista de comprobacion.
- Lista de comprobación de pruebas:
- 1. El número permitido de caracteres (1): kit_body = { "name": "a"}	
-    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
- 2. El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
-    Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
- 3. El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
-    Código de respuesta: 400
- 4. El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }
-    Código de respuesta: 400
- 5. Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
-    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
- 6. Se permiten espacios: kit_body = { "name": " A Aaa " }
-    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
- 7. Se permiten números: kit_body = { "name": "123" }
-    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
- 8. El parámetro no se pasa en la solicitud: kit_body = { }
-    Código de respuesta: 400
- 9. Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
-    Código de respuesta: 400