# Funcion para cambiar el parametro name en el cuerpo de la solicitud
import data
import sender_stand_request
from data import kit_body

# Función para cambiar el valor del parámetro name en el cuerpo de la solicitud
def get_kit_body(name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data"  para conservar los datos del diccionario de origen
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro Name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor Name requerido
    return current_body

# Función para recibir el valor del token
def get_new_user_token(name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data"  para conservar los datos del diccionario de origen
    current_token = data.auth_token.copy()
    # Se cambia el valor del parámetro Name
    current_token["name"] = name
    return current_token

# Función de prueba positiva
def positive_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert kit_response.json()["authToken"] != ""

        # String que debe estar en el cuerpo de respuesta
    str_kit = kit_body["name"] + "," + kit_body["card"] + "," \
               + kit_body["productsList"] + ",,," + kit_body["id"] \
               + kit_body["productsCount"] + kit_response.json()["authToken"]

    # Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert_character(name): # Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
     kit_body = get_kit_body(name)
 # El resultado se guarda en la variable kit_response
     kit_response = sender_stand_request.post_new_client_kit(kit_body)

     assert kit_response.status_code == 400  # Comprueba si el código de estado es 400

     assert kit_response.json()["code"] == 400  # Comprueba que el atributo code en el cuerpo de respuesta es 400

     assert kit_response.json()["message"] == "No se han aprobado todos los parametros requeridos" # Comprueba el atributo message en el cuerpo de respuesta

# Función de prueba negativa cuando el error es "No se enviaron todos los parámetros requeridos"
def negative_assert_no_name(name):
    # El resultado se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
   # Comprueba si el código de estado es "400"
    assert kit_response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert kit_response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert kit_response.json()["message"] == "No se enviaron todos los parámetros requeridos"

# Prueba 1. Numero permitido de caracteres (1)
# El parámetro "Name" contiene un caracter
def test_create_kit_1_character_in_name_get_success_response():
     positive_assert("a")

# Prueba 2. Numero permitido de caracteres (511)
# El parámetro "Name" contiene 511 caracteres
def test_create_kit_511_characters_in_name_get_success_response():
     positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Prueba 3. El numero de caracteres es menor que la cantidad permitida (0)

def test_create_kit_0_character_in_name_get_error_response():
    negative_assert_character("")

# Prueba 4. El numero de caracteres es mayor que la cantidad permitida 512
def test_create_kit_512_characters_in_name_get_error_response():
    negative_assert_character("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Prueba 5. Se permiten caracteres especiales
def test_create_kit_special_character_in_name_get_success_response():
    positive_assert("№%@,")

# Prueba 6. Se permiten espacios
def test_create_kit_space_in_name_get_success_response():
    positive_assert("A Aaa")

# Prueba 7. Se permiten numeros
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")

# Prueba 8. El parametro no se pasa en la solicitud
def test_create_kit_no_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "kit_body"
    kit_body = data.kit_body.copy()
    # El parámetro "Name" se elimina de la solicitud
    kit_body.pop("name")
    # Comprueba la respuesta
    negative_assert_no_name(kit_body)

# Prueba 9. Se ha pasado un tipo de parametro diferente (numero 123)
def test_create_user_number_type_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(123)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)
    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400


