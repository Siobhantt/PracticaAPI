import requests

urluser = "http://localhost:5050/usuarios" 
datos = {"username":"LuisaGaming","password":"1234"} #Los datos con los que se hará la request

rget = requests.get(urluser, json=datos) #Con esto solicito el nombre y el usuario
token = rget.json() #Esto obtiene un diccionario con el nombre y el usuario
token = token["token"] #Del diccionario tomo el valor del campo toke
print(rget.status_code)

apiurl = "http://localhost:5050/peliculas" #Este es el url a donde quiero subir la pelicula


datospeli = {"anio": 19, "director": "me", "genero": "romance", "titulo": "javiq"} #Datos de la pelicula
token = {'Authorization': f'Bearer {token}'} #Esto es lo que va a solicita para autorizar
rpost = requests.post(apiurl, headers=token, json=datospeli) #intentamos postear
print(rpost.json())
print(rpost.status_code)