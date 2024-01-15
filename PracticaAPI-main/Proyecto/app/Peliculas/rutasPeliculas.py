from flask import *
from flask_jwt_extended import jwt_required
from app.funciones import *

ficheroPeliculas = "PracticaAPI-main/Proyecto/app/Ficheros/peliculas.json"
ficheroEscenas = "PracticaAPI-main/Proyecto/app/Ficheros/escenas.json"

bluepPeliculas = Blueprint("peliculas",__name__)

@bluepPeliculas.get("/")
def get_peliculas():
    peliculas = leeFichero(ficheroPeliculas)#NEW
    return jsonify(peliculas)#Aqui el jsonify CONVIERTE EN FORMATO JSON LA LISTA DE DICCIONARIOS QUE HICIMOS ARRIBA COMO BD

@bluepPeliculas.get("/<int:id>")
#Esta funcion OBVIAMENTE RECIBE EL ID
def get_peli(id):
    peliculas = leeFichero(ficheroPeliculas)#NEW
    #Ahora debemos buscar la pelicula especifica
    for peli in peliculas:
        if(peli["id"]==id): #Si la pelicula de la iteracion contiene en el campo id, EL ID RECIBIDO POR PARAMETROS, entonces devuelve la peli
            return peli,200
    return {"Error":"No se pudo encontrar la pelicula"},404

@bluepPeliculas.get("/<int:id>/escenas")
def get_escenas(id):
    lista = []
    escenas = leeFichero(ficheroEscenas)
    for e in escenas:
        if e["idPelicula"] == id:
            lista.append(e)
    if len(lista)>0:
        return lista, 200
    else:
        return{"Error":"No hay escenas para esta pelicula"}
#=======================================================================================================================================================

#Para el metodo post se usa una funcion que recoge el ultimo id y le suma uno, para asignar a la pelicula que se va a añadir
def nuevoId():
    #Esto me lia un poco pero
    #peli["id"] genera una lista de todos los id, 
    #los id salen del bucle que recorre todas las peliculas, al maximo de la lista le suma 1
    peliculas = leeFichero(ficheroPeliculas)#NEW
    return max(peli["id"] for peli in peliculas)+1


@bluepPeliculas.post("/")
@jwt_required()
def postearPeli():
#Se comprueba si el request es jsoN
    peliculas = leeFichero(ficheroPeliculas)#NEW
    if request.is_json:
        #En caso de serlo se guardará la informacion en la variable pelicula
        pelicula = request.get_json()
        pelicula["id"]=nuevoId()#El id de la peli será el generado por la funcion de arriba
        peliculas.append(pelicula)#Se agrega a la lista de diccionarios la nueva pelicula creada
        #NEW
        escribeFichero(peliculas,ficheroPeliculas)
        return pelicula,201 #Si todo va bien, se muestra la peli y el codigo
    return{"Error":"La solicitud debe ser json"},415 #En caso contrario se mostrará este error

#=======================================================================================================================================================

@bluepPeliculas.put("/<int:id>")
@bluepPeliculas.patch("/<int:id>")
@jwt_required()
def modificarPeli(id):
    peliculas = leeFichero(ficheroPeliculas)
    if request.is_json:
        peliModificada = request.get_json()
        for peli in peliculas:
            if peli["id"] == id:
                for elemento in peliModificada:
                    peli[elemento] = peliModificada[elemento]
                escribeFichero(peliculas,ficheroPeliculas) 
                return peli, 200       
    return {"Se ha producido un error": "La solicitud debe ser JSON"}, 415

@bluepPeliculas.delete("/<int:id>")
@jwt_required()
def borrarPeli(id):#RECIBIMOS EL DI
    peliculas = leeFichero(ficheroPeliculas)
    for peli in peliculas:#Recorremos las peliculas
        if peli["id"] == id:#En caso de que el campo id de alguna de las peliculas coincida con el id QUE NOS PASAN POR PARAMETROS
            peliculas.remove(peli)#Eliminamos la peli de la lista
            return {},200 #Y regresamos un diccionario vacio
    escribeFichero(peliculas,ficheroPeliculas) 
    return {"Se ha producido un error":"No se pudo encontrar la pelicula"},404 #SI no coincide ningun id mostramos este error