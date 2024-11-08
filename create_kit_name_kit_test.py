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
def positive_assert(kit_body):
    auth_token = sender_stand_request.post_new_user(data.user_body).json()["authToken"]
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert(kit_body):
    auth_token = sender_stand_request.post_new_user(data.user_body).json()["authToken"]
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400


 # Prueba 1. Numero permitido de caracteres (1)
# El parámetro "Name" contiene un caracter
def test_create_kit_1_character_in_name_get_success_response():
     positive_assert(data.one_letter)

# Prueba 2. Numero permitido de caracteres (511)
# El parámetro "Name" contiene 511 caracteres
def test_create_kit_511_characters_in_name_get_success_response():
     positive_assert(data.five_hundred_eleven_characters)

# Prueba 3. El numero de caracteres es menor que la cantidad permitida (0)

def test_create_kit_0_character_in_name_get_error_response():
    negative_assert(data.no_character)

# Prueba 4. El numero de caracteres es mayor que la cantidad permitida 512
def test_create_kit_512_characters_in_name_get_error_response():
    negative_assert(data.five_hundred_twelve_characters)

# Prueba 5. Se permiten caracteres especiales
def test_create_kit_special_character_in_name_get_success_response():
    positive_assert(data.special_characters)

# Prueba 6. Se permiten espacios
def test_create_kit_space_in_name_get_success_response():
    positive_assert(data.space_in_name)

# Prueba 7. Se permiten numeros
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert(data.numbers_in_name)

# Prueba 8. El parametro no se pasa en la solicitud
def test_create_kit_no_name_get_error_response():
    negative_assert(data.no_name)

# Prueba 9. Se ha pasado un tipo de parametro diferente (numero 123)
def test_create_user_number_type_first_name_get_error_response():
    negative_assert(data.number)



