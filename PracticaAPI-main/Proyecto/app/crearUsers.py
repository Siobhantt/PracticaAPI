import requests
import json

# URL de tu aplicación Flask
url = "http://localhost:5050/usuarios" 

# Datos para la ruta POST
data_post = {
    "username": "tu_nombre_de_usuario",
    "password": "tu_contraseña"
}

# Realizar la solicitud POST
response_post = requests.post(url, json=data_post)

# Intentar imprimir la respuesta de la solicitud POST como JSON
try:
    print(f'Respuesta POST: {response_post.json()}')
except json.JSONDecodeError:
    print(f'Respuesta POST no es un JSON válido: {response_post.text}')

# Si la solicitud POST fue exitosa, intentar la solicitud GET
if response_post.status_code == 201:
    # Datos para la ruta GET
    data_get = {
        "username": "tu_nombre_de_usuario",
        "password": "tu_contraseña"
    }

    # Realizar la solicitud GET
    response_get = requests.get(url, json=data_get)

    # Intentar imprimir la respuesta de la solicitud GET como JSON
    try:
        print(f'Respuesta GET: {response_get.json()}')
    except json.JSONDecodeError:
        print(f'Respuesta GET no es un JSON válido: {response_get.text}')