from pymongo import MongoClient


#establecer conexion con la base de datos local
cliente = MongoClient("mongodb://localhost:27017/")

#seleccionar la base de datos y la coleccion
db = cliente["tiendaLevelUp"]
coleccion = db["catalogo_productos"]


#definir el documento como un diccionario
consola = {
    "nombre": "PlayStation 5",
    "marca": "Sony",
    "precio": 499000,
    "especificaciones": {
        "procesador": "AMD Ryzen Zen 2",
        "color": "Blanco",
    }
}

#ejectuar la insercion del documento en la coleccion
resultado = coleccion.insert_one(consola)

#confirmar la operacion
print(f"Documento insertado con ID_{resultado.inserted_id}")