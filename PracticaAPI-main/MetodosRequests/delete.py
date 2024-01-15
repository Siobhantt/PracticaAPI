import requests
apiurl = "https://jsonplaceholder.typicode.com/todos/10" #Eliminar es lo mas facil porque le indicamos la url con la barra del recurso a borrar
#Ejecutamos la funcion y listo

#Importante recordar que devulve llaves vacias porque lo ha borrado

respuestadelete = requests.delete(apiurl)

print(respuestadelete.status_code)
print(respuestadelete.json())
