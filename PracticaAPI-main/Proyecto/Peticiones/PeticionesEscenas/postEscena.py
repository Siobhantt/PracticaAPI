import requests

#Para postear algo que requiera token lo primero que hago es solicitr los datos y el user
#Para ello necesito la url del usuario y los datos del usuario
urluser = "http://localhost:5050/usuarios"
datos = {"username":"juanCalbo", "password":"12345"}

#Luego hago una solicitud del usuario para obtener el token de autorizacion
#Para ello la contraseña debe estar correcta

rget = requests.get(urluser,json=datos)
dictoken = rget.json()#Esto me da el diccionario del token y su valor
token = dictoken["token"]#Esto me da el valor de la clave token
print(rget.status_code)

#Ahora para postear una escena
escenaurl = "http://localhost:5050/escenas"

datosEscena =   {"nombre": "Parraque","duración": "666 minutos","idPelicula": 2}
autorizacion = {"Authorization":f"Bearer {token}"}
rpost = requests.post(escenaurl,headers=autorizacion,json=datosEscena)
print(rpost.json())