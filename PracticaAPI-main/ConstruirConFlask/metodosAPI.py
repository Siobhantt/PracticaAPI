"""Aqui vamos a probar la libreria flask
Definiremos una pagina donde se va a lanzar"""
from flask import *

def mensaje():
    print("Opciones disponibles: \n"+"1.Obtener todas la peliculas\n"+"2.Obtener una pelicula\n"+"3.Agregar una pelicula\n"+"4.Modificar todos los campos de una pelicula\n"+"5.Modificar un campo de una pelicula\n"+"6.Borrar una pelicula\n"+"0.Salir") 

def datosPelicula():
    titulo = input("Por favor introduzca el titulo de la pelicula:")
    director = input("Por favor introduzca el director de la pelicula:")
    anio = input("Por favor introduzca el anio de la pelicula:")
    genero = input("Por favor introduzca el genero de la pelicula:")
    peli = {"titulo":titulo,"director":director,"anio":anio,"genero":genero}
    return peli


#Vamos a crear una lista de diccionarios que haga de bd
peliculas = [
    {"id":1,"titulo": "El Padrino","director": "Francis Ford Coppola","anio": 1972,"genero": "Drama"},
    {"id":2,"titulo": "Pulp Fiction","director": "Quentin Tarantino","anio": 1994,"genero": "Crimen"},
    {"id":3,"titulo": "Titanic","director": "James Cameron","anio": 1997,"genero": "Romance"},
    {"id":4,"titulo": "El Señor de los Anillos: El retorno del rey","director": "Peter Jackson","anio": 2003,"genero": "Fantasía"},
    {"id":5,"titulo": "La La Land","director": "Damien Chazelle","anio": 2016,"genero": "Musical"},
    {"id":6,"titulo": "Carol","director": "Todd Haynes","anio": 2015,"genero": "Romance"}
]

#Aqui estamos instanciando la clase Flask y le estamos indicando el nombre del modulo en el que se encuentra el modulo
"""Aquí se crea una instancia de la clase Flask y se asigna a la variable app. 
El argumento __name__ se utiliza para que Flask sepa dónde buscar recursos como plantillas y archivos estáticos."""
app = Flask(__name__)

#Este decorador lo da flask 
#Lo que hace es asociar una url con una funcion de python
#Entonces cuando se visite la ruta "/"(La principal), se mostrará lo que esté en la funcion de abajo
#
@app.route("/")
def index():
    return "Funciona(?)"

#Vamos a definir el get(GENERAL) de nuestra api
#Hay que recordar que con esta linea le estamos diciendo a la instacia de flask que la funcion que este debajo de etsa linea
#Es lo que se va a ejecutar cuando en la pagina coloquen un /peliculas
@app.get("/peliculas")
def get_peliculas():
    return jsonify(peliculas)#Aqui el jsonify CONVIERTE EN FORMATO JSON LA LISTA DE DICCIONARIOS QUE HICIMOS ARRIBA COMO BD

#Ahora vamos a definir la funcion que obtiene una pelicula especifica
#Cuando en la direccion de nuestra pagina escriba/peliculas/(y especifiquen un id debe regresar la pelicula con el id correspondiente)
@app.get("/peliculas/<int:id>")
#Esta funcion OBVIAMENTE RECIBE EL ID
def get_peli(id):
    #Ahora debemos buscar la pelicula especifica
    for peli in peliculas:
        if(peli["id"]==id): #Si la pelicula de la iteracion contiene en el campo id, EL ID RECIBIDO POR PARAMETROS, entonces devuelve la peli
            return peli,200
    return {"Error":"No se pudo encontrar la pelicula"},404

#=======================================================================================================================================================

#Para el metodo post se usa una funcion que recoge el ultimo id y le suma uno, para asignar a la pelicula que se va a añadir
def nuevoId():
    #Esto me lia un poco pero
    #peli["id"] genera una lista de todos los id, 
    #los id salen del bucle que recorre todas las peliculas, al maximo de la lista le suma 1
    return max(peli["id"] for peli in peliculas)+1


@app.post("/peliculas")
def postearPeli():
#Se comprueba si el request es json
    if request.is_json:
        #En caso de serlo se guardará la informacion en la variable pelicula
        pelicula = request.get_json()
        pelicula["id"]=nuevoId()#El id de la peli será el generado por la funcion de arriba
        peliculas.append(pelicula)#Se agrega a la lista de diccionarios la nueva pelicula creada
        return pelicula,201 #Si todo va bien, se muestra la peli y el codigo
    return{"Error":"La solicitud debe ser json"},415 #En caso contrario se mostrará este error

#=======================================================================================================================================================

#Para los metodos que implican modificaciones, o que no sean generales es importante
#ACORDARSE DE QUE LA FUNCION LLEVA EL ID DE LO QUE DEBO MODIFICARRRRRRRRRRRRRRR
@app.put("/peliculas/<int:id>")
@app.patch("/peliculas/<int:id>") #Como esto va a hacer algo muy parecido al put solo se le pone el maquillador y ya (:
def modificarPeli(id):
    if request.is_json:#Como haremos una solicitud para corregir una peli, esta fucnion va a verificar si es json
        peliModificada = request.get_json()#en caso de ser json si la va a guardar en una variable
        for peli in peliculas:#Ahora vamos a recorres la lista de peliculas(diccionarios)
            if peli["id"] ==id:#y en caso de que el campo id de la iteracion SEA == AL ID QUE ME PASAN POR PARAMETROS
                for elemento in peliModificada:#Recorremos todos los elementos de la modificacion
                    if elemento in peli:
                        peli[elemento] = peliModificada[elemento]#Y asiganmos esas modificaciones a la pelicula que estamos modificando
                    else:
                        return {"Error":f"El campo{elemento} no existe en la pelicula"},400
                return peli,200#si va todo bien devolvemos la modificacion y un 200
    return{"Se ha producido un error":"La solicitud debe ser JSON"},415#En caso contrario un tablazo

#Cuando se haga esta solicitud con esta url se ejecutará la funcion de abajo
@app.delete("/peliculas/<int:id>")
def borrarPeli(id):#RECIBIMOS EL DI
    for peli in peliculas:#Recorremos las peliculas
        if peli["id"] == id:#En caso de que el campo id de alguna de las peliculas coincida con el id QUE NOS PASAN POR PARAMETROS
            peliculas.remove(peli)#Eliminamos la peli de la lista
            return {},200 #Y regresamos un diccionario vacio
    return {"Se ha producido un error":"No se pudo encontrar la pelicula"},404 #SI no coincide ningun id mostramos este error


#=======================================================================================================================================================
#Todo lo que vaya a ejecutar debe estar arriba de esto

if __name__ == "__main__":#La lineas de codigo debajo de esta linea se ejecutan si el script se esta ejecutando directamente
    #O sea, si no se está importando desde otro script
    #app.run INICIA EL SERVIDOR DE DESARROLLO DE FLASK
    #El debug=True activa el modo depuracion, da info sobre los errores y reincia el servidor cuando el cogio es modificado
    #EL host=0... hace que la app sea accesible desde any ip, no solo desde la local
    #port=...establece el puerto en el que se ejecutará el servidor
    app.run(debug=True,host="0.0.0.0",port=5050)
    