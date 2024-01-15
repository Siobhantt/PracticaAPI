import secrets
import string
from flask import *
#ficheroPeliculas = "ConstruirConFlask\peliculas.json"
def mensaje():
    print("Opciones disponibles: \n"+"1.Obtener todas la peliculas\n"+"2.Obtener una pelicula\n"+"3.Agregar una pelicula\n"+"4.Modificar todos los campos de una pelicula\n"+"5.Modificar un campo de una pelicula\n"+"6.Borrar una pelicula\n"+"0.Salir") 

def datosEscena():
    nombre = input("Por favor introduzca el titulo de la pelicula:")
    duracion = input("Por favor introduzca el director de la pelicula:")
    idPelicula = input("Por favor introduzca el anio de la pelicula:")
    escena = {"nombre":nombre,"duracion":duracion,"idPelicula":idPelicula}
    return escena

def datosPelicula():
    titulo = input("Por favor introduzca el titulo de la pelicula:")
    director = input("Por favor introduzca el director de la pelicula:")
    anio = input("Por favor introduzca el anio de la pelicula:")
    genero = input("Por favor introduzca el genero de la pelicula:")
    peli = {"titulo":titulo,"director":director,"anio":anio,"genero":genero}
    return peli

def leeFichero(fichero):
    with open(fichero,"r")as openfile:#El archivo abierto se guarda en la varible
        peliculas = json.load(openfile)#carga el contenido del json en la variable como una lista de diccionarios
    return peliculas

def escribeFichero(lista,fichero):
    with open(fichero,"w")as openfile:
        json.dump(lista,openfile)#Esto escribe la pelicula recibida por parametro en el fichero

def newpass():
    letras = string.ascii_letters
    digitos = string.digits
    especiales = string.punctuation
    alfabeto = letras+digitos + especiales
    #fijamos lalongitud de la contrasena
    passlength = 12
    trypass = ''
    for i in range (passlength):
        trypass = ''.join(secrets.choice(alfabeto))
    return(trypass)