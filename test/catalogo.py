from pymongo import MongoClient


#establecer conexion con la base de datos local
cliente = MongoClient("mongodb://localhost:27017/")

#seleccionar la base de datos y la coleccion
db = cliente["tiendaLevelUp"]
coleccion = db["catalogo_productos"]

#definir 2 documentos como diccionarios
consola = [{
    "nombre": "Nintendo Switch",
    "marca": "Nintendo",
    "precio": 299000,
    "especificaciones": {
        "procesador": "NVIDIA Custom Tegra",
        "color": "Negro"
    }
},
{
    "nombre": "Xbox Series X",
    "marca": "Microsoft",
    "precio": 499000,
    "especificaciones": {
        "procesador": "AMD Ryzen Zen 2",
        "color": "Negro", 
    }
}
]


#ejectuar la insercion de los 2 documentos en la coleccion
# insert_many se utiliza para insertar varios documentos a la vez
resultado = coleccion.insert_many(consola)             

#confirmar la operacion
print(f"Documentos insertados con IDs: {resultado.inserted_ids}")