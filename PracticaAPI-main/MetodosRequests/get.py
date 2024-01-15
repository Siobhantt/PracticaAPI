import requests
#Url de donde haremos las solicitudes
apiurl = "https://jsonplaceholder.typicode.com/todos/1" #Importante fijarse que en este cado especifica un registro -> /1
# La respuesta que nos va a devolver el metodo get
response  = requests.get(apiurl)
#La respuesta debe ser invocada con la funcion .json()
print(response.json())