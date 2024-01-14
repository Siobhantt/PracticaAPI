#CUIDADO CON LAS IMPORTACIONESSS
from flask import Flask
from .Peliculas.rutasPeliculas import bluepPeliculas
from .Escenas.rutasEscenas import bluepEscenas
from .Usuarios.rutasUsuario import bluepUsuarios
from app.funciones import *
from flask_jwt_extended import JWTManager
from app.funciones import *

app = Flask(__name__)
nuevapassword = newpass()
app.config["SECRET_KEY"] = nuevapassword
jwt = JWTManager(app)
app.register_blueprint(bluepPeliculas,url_prefix="/peliculas")
app.register_blueprint(bluepEscenas,url_prefix="/escenas")
app.register_blueprint(bluepUsuarios, url_prefix="/usuarios")