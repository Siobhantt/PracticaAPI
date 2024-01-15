import requests

apiurl = "http://localhost:5050/usuarios"

datos = {"username":"juanCalbo", 'password':"12345"}
rpost = requests.post(apiurl, json=datos)
print(rpost.json())
print(rpost.status_code)