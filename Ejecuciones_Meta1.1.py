# PALAFOX RAMIREZ ELVIA PALOMA
# GRUPO 951
# 31/08/2025
# META 1.1
from Ejercicio1 import Estadistica, HojaDeCalculo

# ---------------- Lista de números ----------------
def pedir_lista():
    numeros = []
    cantidad = int(input("¿Cuántos números deseas ingresar en la lista? "))

    for i in range(cantidad):
        numero = int(input(f"Ingrese el número en la posición {i + 1}: "))
        numeros.append(numero)

    return numeros

def imprimir_contenido(lista_estadistica):
    print("\nFrecuencia:", lista_estadistica.frecuencia())
    print("Moda:", lista_estadistica.moda())
    print("Histograma:")
    lista_estadistica.histograma()

# ---------------- Hoja de cálculo ----------------
def simular_hoja():
    hoja = HojaDeCalculo()

    while True:
        print("\nOpciones Hoja de Cálculo:")
        print("1. Agregar/Modificar celda")
        print("2. Deshacer último cambio")
        print("3. Ver contenido actual")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            celda = input("Ingresa la celda (ej. A1): ").upper()
            valor = input("Ingresa el valor: ")
            hoja.registrar_cambio(celda, valor)
        elif opcion == "2":
            hoja.deshacer_cambio()
        elif opcion == "3":
            hoja.mostrar_celdas()
        elif opcion == "4":
            print("Saliendo de Hoja de Cálculo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# ---------------- Almacén ----------------
class Almacen:
    def __init__(self, mapa):
        self.mapa = mapa
        self.filas = len(mapa)
        self.columnas = len(mapa[0])
        self.inicio_x = 0
        self.inicio_y = 0
        self.productos_totales = sum(fila.count('P') for fila in mapa)

    def verificar_movimientos(self, movimientos):
        x, y = self.inicio_x, self.inicio_y
        productos_recogidos = set()

        for mov in movimientos:
            if mov == 'R':
                y += 1
            elif mov == 'L':
                y -= 1
            elif mov == 'D':
                x += 1
            elif mov == 'U':
                x -= 1
            else:
                print(f"Movimiento inválido: {mov}")
                return False

            # Verificar límites
            if x < 0 or x >= self.filas or y < 0 or y >= self.columnas:
                return False

            # Verificar obstáculos
            if self.mapa[x][y] == '#':
                return False

            # Recoger producto
            if self.mapa[x][y] == 'P':
                productos_recogidos.add((x, y))

        # Verificar si recogió todos los productos y regresó al inicio
        return len(productos_recogidos) == self.productos_totales and (x, y) == (self.inicio_x, self.inicio_y)

def simular_almacen():
    # Definir el almacén
    mapa_almacen = [
        ['.', '.', '#', 'P'],
        ['.', '#', '.', '.'],
        ['P', '.', 'P', '.'],
        ['#', '.', '#', '.']
    ]

    movimientos = input("Ingresa la secuencia de movimientos (R,D,L,U): ").upper()
    movimientos_lista = list(movimientos)

    almacen = Almacen([fila[:] for fila in mapa_almacen])  # copia para que no se modifique original
    resultado = almacen.verificar_movimientos(movimientos_lista)

    if resultado:
        print("¡Todos los productos fueron recogidos y el robot volvió al inicio!")
    else:
        print("Movimiento inválido o no se recogieron todos los productos.")

# ---------------- Menú principal ----------------
if __name__ == '__main__':
    while True:
        print("\nOpciones principales:")
        print("1. Lista con números (frecuencia, moda, histograma)")
        print("2. Hoja de Cálculo")
        print("3. Almacén")
        print("4. Salir")
        opc = input("Ingresa una opción: ")

        if opc == "1":
            contenido = pedir_lista()
            lista = Estadistica(contenido)
            imprimir_contenido(lista)
        elif opc == "2":
            simular_hoja()
        elif opc == "3":
            simular_almacen()
        elif opc == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
