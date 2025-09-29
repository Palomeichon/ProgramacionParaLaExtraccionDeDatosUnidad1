# PALAFOX RAMIREZ ELVIA PALOMA
# GRUPO 951
# 31/08/2025
# META 1.1

from collections import Counter
import statistics

class Estadistica:
    def __init__(self, numeros):
        self.numeros = numeros
        self.frec = Counter(numeros)

    def frecuencia(self):
        return list(self.frec.items())


    def moda(self):
        return statistics.mode(self.numeros)

    def histograma(self):
        for num, cantidad in self.frec.items():
            print((num, "*" * cantidad))


class HojaDeCalculo:
    def __init__(self):
        self.historial = []  # pila de cambios
        self.celdas = {}  # contenido actual de las celdas

    def registrar_cambio(self, celda, nuevo_valor):
        # Guardar el valor anterior (o None si no existía)
        valor_anterior = self.celdas.get(celda, None)

        # Registrar solo si el valor cambia
        if valor_anterior != nuevo_valor:
            self.historial.append((celda, valor_anterior))
            self.celdas[celda] = nuevo_valor
            print(f"Cambio registrado: Celda {celda} cambió de {valor_anterior} a {nuevo_valor}")
        else:
            print(f"No hay cambio en {celda}, sigue siendo {nuevo_valor}")

    def deshacer_cambio(self):
        if self.historial:
            celda, valor_anterior = self.historial.pop()
            # Restaurar valor anterior o eliminar si era None
            if valor_anterior is None:
                self.celdas.pop(celda)
            else:
                self.celdas[celda] = valor_anterior
            print(f"Deshecho: Celda {celda} vuelve a {valor_anterior}")
        else:
            print("No hay cambios que deshacer.")

    def mostrar_historial(self):
        print("Historial actual:", self.historial)

    def mostrar_celdas(self):
        print("Contenido actual de las celdas:", self.celdas)


