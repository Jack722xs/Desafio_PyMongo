from pymongo import MongoClient
from tiendaLevelUp import *

#establecer conexion con la base de datos local
cliente = MongoClient("mongodb://localhost:27017/")

#seleccionar la base de datos y la coleccion
db = cliente["tiendaLevelUp"]
coleccion = db["catalogo_productos"]


menu()