import requests

apiurl="http://localhost:5050/escenas"

rget = requests.get(apiurl)
print(rget.json())
print(rget.status_code)