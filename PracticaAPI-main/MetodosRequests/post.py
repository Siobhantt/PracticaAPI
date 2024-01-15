import requests

apiurl ="https://jsonplaceholder.typicode.com/todos" #Hubo un momento en el que no funciono porque tenia un /1
#para postear no hay que especificar un registro
#Los datos que queremos postear van en un diccionario
datos = {"userId": 1, "title": "Marta", "completed": False}

respuesta = requests.post(apiurl,json=datos)#Esta es la linea que postea los datos de arriba

print(respuesta.json())
print("Codigo de estado de la solicitud:",respuesta.status_code)