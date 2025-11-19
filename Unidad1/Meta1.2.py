# Palafox Ramirez Elvia Paloma
# 951
# 31/08/2025

#cuartosD son cuartos disponibles y cuartosR son cuartos reservados
# Diccionario de encriptación: letra original -> letra secreta
dic_encriptacion = {
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u',
    'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o',
    'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i',
    's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
    'y': 'b', 'z': 'a', ' ': '_'
}

# Crear diccionario inverso para desencriptar
dic_desencriptacion = {v: k for k, v in dic_encriptacion.items()}

inventario=[]
cuartosD=set(range(1,100))
cuartosR=set()
def reserva(numero):
    if numero in cuartosD:
        cuartosD.remove(numero)
        cuartosR.add(numero)
        print("el cuarto ha sido reservado exitosamete")
    else:
        print("No fue posible reservar ese cuarto, por favor verifique que exista")

def liberar(numero):
    if numero in cuartosR:
        cuartosR.remove(numero)
        cuartosD.add(numero)
        print("Se ha cambiado el estado de la habitacion exitosamente")
    elif numero in cuartosD:
        print("Ese cuarto ya estaba disponible")
    else:
        print("El numero ingresado no corresponde a un cuarto valido")

def disponibilidad():
    print("Cuartos disponibles:", sorted(cuartosD))
    print("Cuartos reservados:", sorted(cuartosR))

def numeroH(opc):
    if opc==1:
        numero = int(input("Ingresa un numero de habitacion"))
        reserva(numero)
    elif opc==2:
        numero = int(input("Ingresa un numero de habitacion"))
        liberar(numero)
    elif opc==3:
        disponibilidad()
    else:
        return

def Ejercicio1():
    while True:
        n = int(input(
            "Ingresa el número de la opción deseada \n[1] Reserva cuarto\n[2] Libera\n[3] Disponibilidad\nIngrese cualquier otro numero para salir\n "))
        if n != 1 and n != 2 and n != 3:
            break
        else:
            numeroH(n)
#==========================================EJERCICIO 2=====================================
def mandador(n):
    mensaje=input("Ingresa el mensaje: ")
    if n==1:
        encriptacion(mensaje)
    else:
        Decifrado(mensaje)

def encriptacion(m):
    m = m.lower()
    resultado = ''
    for letra in m:
        resultado += dic_encriptacion.get(letra, letra)
    print(f"Tu mensaje encriptado es: "+resultado)


def Decifrado(m):
    resultado = ''
    for caracter in m:
        resultado += dic_desencriptacion.get(caracter, caracter)
    print(f"Tu mensaje decifrado es: " + resultado)

def Ejercicio2():
    while True:
        n = int(input(
            "Ingresa el número de la opción deseada \n[1] Encriptar mensaje\n[2] Decifrar mensaje\nIngrese cualquier otro numero para salir\n "))
        if n != 1 and n != 2:
            break
        else:
            mandador(n)
#========================================EJERCICIO3====================================
# Buscar un producto por ID
def buscar_producto(id_producto):
    for producto in inventario:
        if producto["id"] == id_producto:
            return producto
    return None

# Agregar producto (recibe un diccionario)
def agregar_producto(producto):
    if buscar_producto(producto["id"]):
        print(f"El producto con ID {producto['id']} ya existe.")
    else:
        inventario.append(producto)
        print(f"Producto '{producto['nombre']}' agregado correctamente.")

# Editar producto
def editar_producto(id_producto, nuevos_datos):
    producto = buscar_producto(id_producto)
    if not producto:
        print(f"Producto con ID {id_producto} no encontrado.")
        return
    producto.update(nuevos_datos)
    print(f"Producto con ID {id_producto} actualizado correctamente.")

# Eliminar producto
def eliminar_producto(id_producto):
    producto = buscar_producto(id_producto)
    if producto:
        inventario.remove(producto)
        print(f"Producto '{producto['nombre']}' eliminado correctamente.")
    else:
        print(f"Producto con ID {id_producto} no encontrado.")

# Realizar una venta
def realizar_venta(id_producto, cantidad):
    producto = buscar_producto(id_producto)
    if not producto:
        print(f"Producto con ID {id_producto} no encontrado.")
        return
    if producto["cantidad"] < cantidad:
        print(f"No hay suficiente stock. Disponible: {producto['cantidad']}")
        return
    producto["cantidad"] -= cantidad
    total = producto["precio"] * cantidad
    print(f"Venta realizada: {cantidad} unidad(es) de '{producto['nombre']}' por ${total:.2f}")

# Imprimir inventario
def imprimir_inventario():
    print("\nINVENTARIO ACTUAL.")
    if not inventario:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Cantidad: {producto['cantidad']}\n")

# Función para pedir datos al usuario y devolver un diccionario
def pedir_datos_producto():
    id_producto = input("ID del producto: ")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad en stock: "))
    return {
        "id": id_producto,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

# Menú interactivo
def ejercicio3():
    while True:
        opcion = int(input("ingresa el numero de la opcion deseada"
                           "\n1.agregar producto"
                           "\n2Editar producto"
                           "\n3.eliminar producto"
                           "\n4.Realizar venta"
                           "\n5.Imprimir inventario"
                           "\nCUALQUIER OTRO NUMERO PARA SALIR\n:"))

        if opcion == "1":
            producto = pedir_datos_producto()
            agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a editar: ")
            print("Ingrese los nuevos datos (dejar vacío si no desea cambiar algo):")
            nombre = input("Nuevo nombre: ")
            precio_input = input("Nuevo precio: ")
            cantidad_input = input("Nueva cantidad: ")

            nuevos_datos = {}
            if nombre:
                nuevos_datos["nombre"] = nombre
            if precio_input:
                nuevos_datos["precio"] = float(precio_input)
            if cantidad_input:
                nuevos_datos["cantidad"] = int(cantidad_input)

            editar_producto(id_producto, nuevos_datos)

        elif opcion == "3":
            id_producto = input("ID del producto a eliminar: ")
            eliminar_producto(id_producto)

        elif opcion == "4":
            id_producto = input("ID del producto a vender: ")
            cantidad = int(input("Cantidad a vender: "))
            realizar_venta(id_producto, cantidad)

        elif opcion == "5":
            imprimir_inventario()

        elif opcion == "6":
            print("Saliendo del sistema de inventario.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    Ejercicio1()
    Ejercicio2()
    ejercicio3()


