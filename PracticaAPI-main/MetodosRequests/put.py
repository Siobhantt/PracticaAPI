import requests

apiurl = "https://jsonplaceholder.typicode.com/todos/10"

#Aqui estamos solicitando el recurso que queremos modificar
respuestaget = requests.get(apiurl)
print(respuestaget.json())#Ahora con la repuesta haremos un diccionario con las modificaciones correspondientes
#Hay que recodar que para el put hay que especificar el id a modificar
#Y tambien que con el put modificamos todo el recurso
newdata = {"userID":1,"title":"Mondongo","completed":True}
#Importante aqui, primero va la url y luego json=(En este cado el diccionario "newdata")
respuestaput = requests.put(apiurl,json=newdata)
print(respuestaput.json())#Esto imprime las modificaciones
print(respuestaput.status_code)#Esto imprime el codigo que indica si la solicitud fue bien o no