from flask import *
from flask_jwt_extended import jwt_required
from app.funciones import *

ficheroEscenas = "PracticaAPI-main/Proyecto/app/Ficheros/escenas.json"

bluepEscenas = Blueprint("escenas",__name__)

#Este decorador lo da flask 
#Lo que hace es asociar una url con una funcion de python
#Entonces cuando se visite la ruta "/"(La principal), se mostrará lo que esté en la funcion de abajo
#


@bluepEscenas.get("/")
def get_escenas():
    escenas = leeFichero(ficheroEscenas)#NEW
    return jsonify(escenas)#Aqui el jsonify CONVIERTE EN FORMATO JSON LA LISTA DE DICCIONARIOS QUE HICIMOS ARRIBA COMO BD


@bluepEscenas.get("/<int:id>")
#Esta funcion OBVIAMENTE RECIBE EL ID
def get_escena(id):
    escenas = leeFichero(ficheroEscenas)#NEW
    #Ahora debemos buscar la pelicula especifica
    for e in escenas:
        if(e["id"]==id): #Si la pelicula de la iteracion contiene en el campo id, EL ID RECIBIDO POR PARAMETROS, entonces devuelve la peli
            return e,200
    return {"Error":"No se pudo encontrar la escena"},404

#=======================================================================================================================================================

def nuevoId():
    escenas = leeFichero(ficheroEscenas)#NEW
    return max(e["id"] for e in escenas)+1


@bluepEscenas.post("/")
@jwt_required()
def subirEscena():
#Se comprueba si el request es jsoN
    escenas = leeFichero(ficheroEscenas)#NEW
    if request.is_json:
        #En caso de serlo se guardará la informacion en la variable pelicula
        e = request.get_json()
        e["id"]=nuevoId()#El id de la peli será el generado por la funcion de arriba
        escenas.append(e)#Se agrega a la lista de diccionarios la nueva pelicula creada
        #NEW
        escribeFichero(escenas,ficheroEscenas)
        return e,201 #Si todo va bien, se muestra la peli y el codigo
    return{"Error":"La solicitud debe ser json"},415 #En caso contrario se mostrará este error

#=======================================================================================================================================================

@bluepEscenas.put("/<int:id>")
@bluepEscenas.patch("/<int:id>")
@jwt_required()
def modificarEscena(id):
    escenas = leeFichero(ficheroEscenas)
    if request.is_json:
        escenaModificada = request.get_json()
        for e in escenas:
            if e["id"] == id:
                for elemento in escenaModificada:
                    e[elemento] = escenaModificada[elemento]
                escribeFichero(escenas,ficheroEscenas) 
                return e, 200       
    return {"Se ha producido un error": "La solicitud debe ser JSON"}, 415

@bluepEscenas.delete("/<int:id>")
@jwt_required()
def borrarPeli(id):#RECIBIMOS EL DI
    escenas = leeFichero(ficheroEscenas)
    for e in escenas:#Recorremos las peliculas
        if e["id"] == id:#En caso de que el campo id de alguna de las peliculas coincida con el id QUE NOS PASAN POR PARAMETROS
            escenas.remove(e)#Eliminamos la peli de la lista
            return {},200 #Y regresamos un diccionario vacio
    escribeFichero(escenas,ficheroEscenas) 
    return {"Se ha producido un error":"No se pudo encontrar la pelicula"},404 #SI no coincide ningun id mostramos este error