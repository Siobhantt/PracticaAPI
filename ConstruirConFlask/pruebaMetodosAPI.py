import requests

#from metodosAPI import *
from APIconJson import *

miurl= "http://localhost:5050/peliculas"

#A ver si me explico
#Los metodos que declaramos en el script en donde se instanciaba flask
#Sirven para que cuando yo haga un request.get o .loquesea funcionen como los metodos que se usaron en el ejemplo
#No tengo que llamar a los que yo escribi, para eso esta el requests

#Vamos a crear una especie de crud para practicar las solicitudes
mensaje()
opcion = int(input("Por favor introduzca la accion que desea realizar en la API:"))
while opcion!=0:
    match opcion:
        case 1:
            respuesta = requests.get(miurl)#Se realiza la peticion
            #print(respuesta.text)
            print(respuesta.json())#Se imprime la respuesta
            print("Codigo de estado de la solicitud:",respuesta.status_code)

        case 2:
            id = int(input("Introduzca el id de la pelicula que quiere obtener:"))
            respuesta = requests.get(f"{miurl}/{id}")
            print(respuesta.json())
            print("Codigo de estado de la solicitud:",respuesta.status_code)

        case 3:
            datos = datosPelicula()
            respuesta = requests.post(miurl,json=datos)
            print(respuesta.json())
            print("Codigo de estado de la solicitud:",respuesta.status_code)

        case 4:
            #Importante este fallo
            id = int(input("Introduzca el id de la pelicula que quiere modificar:"))#Se pide el id para traer la pelicula
            peliUrl = f"{miurl}/{id}"#Tengo que recordar que a la hora de modificar tengo que concatenar el id a la url, por eso falló ayer
            nuevosdatos = datosPelicula()#Solicito los datos de la pelicula
            
            rput = requests.put(peliUrl, json=nuevosdatos)#A la url de la peli que quiero cambiar le adjunto los nuevo datos
            if rput.status_code == 200:
                print(rput.json())
            else:
                print("Hay un problema")
            

        case 5:
            id = int(input("Introduzca el id de la pelicula que quiere modificar:"))#Se pide el id para traer la pelicula
            clave = input("Que campo desea modificar?:").lower()
            valor = input("Introduzca el valor:")
            if clave == "anio" and valor.isdigit():
                valor = int(valor)
            nuevosdatos = {clave:valor}
            peliUrl = f"{miurl}/{id}"#IMPORTANTE LA BARRAAAAAA
            rget = requests.get(peliUrl)

            rpatch = requests.patch(peliUrl,json=nuevosdatos)
            print(rpatch.json())
            print("Codigo de estado:", rpatch.status_code)

        case 6:
            id = int(input("Introduzca el id de la pelicula que quiere borrar:"))
            peliUrl = f"{miurl}/{id}"
            rdelete = requests.delete(peliUrl)
            print(rdelete.json())
            print("Codigo de estado:",rdelete.status_code)

    mensaje()        
    opcion = int(input("Por favor introduzca la accion que desea realizar en la API:\n"))
    print()
        
            
print("Todo ha ido bien!!!")