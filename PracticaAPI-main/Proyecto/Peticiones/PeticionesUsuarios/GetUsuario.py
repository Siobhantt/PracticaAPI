import requests

apiurl = "http://localhost:5050/usuarios"
datos = {"username":"LuisaGaming","password":"1234"}

rget = requests.get(apiurl, json=datos)
print(rget.json())
print(rget.status_code)