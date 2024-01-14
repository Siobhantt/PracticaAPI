import requests
apiurl = "https://jsonplaceholder.typicode.com/todos/10"

#Primero ejecuto un metodo get pa ver lo que quiero modificar
respuestaget = requests.get(apiurl)
print(respuestaget.json())
#Creo el diccionario con lo que quiero modificar
#como solo es una cosa me fijo en los valores del diccionario que me devolvio le get de arriba
newdata = {"title":"Martateadoroeresmonisima"}
#importante para el post,put,patch primero la url luego json=la variable con los datos
respuestapatch = requests.patch(apiurl, json=newdata)
print(respuestapatch.json())
print(respuestapatch.status_code)

