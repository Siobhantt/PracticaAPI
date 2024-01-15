import requests

apiurl = "http://localhost:5050/usuarios"

datos = {"username":"LuisaGaming", 'password':"1234"}
rpost = requests.post(apiurl, json=datos)
print(rpost.json())
print(rpost.status_code)