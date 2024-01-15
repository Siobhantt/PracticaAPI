import requests

apiurl = "http://localhost:5050/peliculas"

datos = {"anio": 1999, "director": "messi", "genero": "romance", "titulo": "javiqueriiico"}
header = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTMwNTM4MiwianRpIjoiOTc3MDdjNDEtN2U0NS00ZDZjLTkyYWUtMWU2ZDg1OTM5OGI5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImphdmlsYWNodXBhcmlpaWljbyIsIm5iZiI6MTcwNTMwNTM4MiwiY3NyZiI6ImIwYmY5ODlmLWRhNmItNDcyOS04ZjE0LTNmNTM1Njc2YWZkZiIsImV4cCI6MTcwNTMwNjI4Mn0.HiIZeHBqumvcZHopW4HphtZTMCRLncM7FYoNnMu-Gzs"}
rpost = requests.post(apiurl, headers=header, json=datos)
print(rpost.json())
print(rpost.status_code)