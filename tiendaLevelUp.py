from pymongo import MongoClient


#establecer conexion con la base de datos local
cliente = MongoClient("mongodb://localhost:27017/")

#seleccionar la base de datos y la coleccion
db = cliente["tiendaLevelUp"]
coleccion = db["catalogo_productos"]


def agregarVideojuego():
    nombre = input("Ingrese el nombre del producto: \n ->")
    marca = input("Ingrese la marca del producto: \n ->")
    precio = float(input("Ingrese el precio del producto: \n ->"))
    stock = int(input("Ingrese el stock del producto: \n ->"))

    catalogo = {
        "nombre": nombre,
        "marca": marca,
        "precio": precio,
        "stock": stock
    }

    coleccion.insert_one(catalogo)
    print(f"Producto '{nombre}' agregado al catálogo con éxito.")

def agregarConsola():
    nombre = input("Ingrese el nombre del producto: \n ->")
    marca = input("Ingrese la marca del producto: \n ->")
    precio = float(input("Ingrese el precio del producto: \n ->"))
    stock = int(input("Ingrese el stock del producto: \n ->"))
    almacenamiento = input("Ingrese el almacenamiento de la consola: \n ->")
    color = input("Ingrese el color de la consola: \n ->")

    especificaciones = {
        "almacenamiento": almacenamiento,
        "color": color
    }

    catalogo = {
        "nombre": nombre,
        "marca": marca,
        "precio": precio,
        "stock": stock,
        "especificaciones": especificaciones
    }

    coleccion.insert_one(catalogo)
    print(f"Producto '{nombre}' agregado al catálogo con éxito.")
 
def agregarProducto():
    from tiendaLevelUp import agregarConsola, agregarVideojuego

    seleccion = input("¿El producto es una consola o un videojuego? \n" \
                      "\n 1. Consola" \
                      "\n 2. videojuego" \
                      "\n Ingresa el numero correspondiente: ")
    
    if seleccion == "1":
        agregarConsola()
    elif seleccion == "2":
        agregarVideojuego()
    else:
        print("Opción no válida. Por favor, ingresa 1 para consola o 2 para videojuego.")
 
def mostrarCatalogo():
    productos = coleccion.find()
    print("\nCatálogo de Productos:")
    for producto in productos:
        print(f"ID: {producto['_id']}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Marca: {producto['marca']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Stock: {producto['stock']}")
        if "especificaciones" in producto:
            print("Especificaciones:")
            for key, value in producto["especificaciones"].items():
                print(f"  {key.capitalize()}: {value}")
        print("-"*30)


def actualizarCatalogo():
    id_producto = input("Ingrese el ID del producto a actualizar: \n ->")
    campo = input("Ingrese el campo a actualizar (nombre, marca, precio, stock): \n ->")
    nuevo_valor = input("Ingrese el nuevo valor: \n ->")

    if campo in ["precio", "stock"]:
        nuevo_valor = float(nuevo_valor) if campo == "precio" else int(nuevo_valor)

    resultado = coleccion.update_one(
        {"_id": id_producto},
        {"$set": {campo: nuevo_valor}}
    )

    if resultado.modified_count > 0:
        print(f"Producto con ID {id_producto} actualizado exitosamente.")
    else:
        print(f"No se encontró un producto con ID {id_producto} o no se realizaron cambios.")        

def eliminarProducto():

#ahora solo mostrar las IDs de los productos para que el usuario pueda elegir cual eliminar
    productos = coleccion.find()
    print("\nProductos disponibles:")
    for producto in productos:
        print(f"ID: {producto['_id']} - Nombre: {producto['nombre']}")
               
    id_producto = input("Ingrese el ID del producto a eliminar: \n ->")
    resultado = coleccion.delete_one({"_id": id_producto})

    if resultado.deleted_count > 0:
        print(f"Producto con ID {id_producto} eliminado exitosamente.")
    else:
        print(f"No se encontró un producto con ID {id_producto}.")

def menu():
    while True:
        print("="*10, "Bienvenido a la tienda Level Up ", "="*10)

        print("Seleccione una opción:\n" \
        "1. Agregar producto\n" \
        "2. Mostrar catálogo\n" \
        "3. Actualizar producto\n" \
        "4. Eliminar producto\n" \
        "5. Salir")

        opc = input("Ingrese el número de la opción deseada: \n ->")

        if opc == "1":
            agregarProducto()
        elif opc == "2":
            mostrarCatalogo()
        elif opc == "3":
            actualizarCatalogo()
        elif opc == "4":
            eliminarProducto()
        elif opc == "5":
            print("¡Gracias por usar la tienda Level Up! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 5.")