import bcrypt
from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required
from app.funciones import *

fUsuarios = "Proyecto/app/Ficheros/escenas.json"

bluepUsuarios = Blueprint("usuarios",__name__)

@bluepUsuarios.post("/")
def regisUsuario():
    usuarios = leeFichero(fUsuarios)
    if request.is_json():
        un1Usuario = request.get_json()
        password = un1Usuario["password"].encode("utf-8")
        salt = bcrypt.gensalt()
        hashPassword = bcrypt.hashpw(password,salt).hex()
        un1Usuario["password"] = hashPassword
        usuarios.append(un1Usuario)
        escribeFichero(usuarios,fUsuarios)
        token = create_access_token(identity=un1Usuario["username"])
        return{"token":token},201
    return{"Se ha producido un error":"La solicitud debe ser JSON"},415

@bluepUsuarios.get("/")
def loginUser():
    usuarios = leeFichero(fUsuarios)
    if request.is_json():
        usuario = usuarios["username"]
        contrasenia = usuarios["password"].encode("utf-8")
        for archivoUsuario in usuarios:
            if archivoUsuario["username"]==usuario:
                passwordFile = archivoUsuario["password"]
                if bcrypt.checkpw(contrasenia,bytes.fromhex(passwordFile)):
                    token = create_access_token(identity=usuario)
                    return{"token":token},200
                else:
                    return{"Se ha producido un error":"No esta autorizado para acceder"},401
        return {"Se ha producido un error":"Usuario no encontrado"}
    return{"Se ha producido un error":"La solicitud debe ser JSON"}        
