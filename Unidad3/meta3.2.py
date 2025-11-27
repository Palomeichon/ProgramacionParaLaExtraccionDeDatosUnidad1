# -------------------------------------------------------------
# Nombre: Elvia Paloma Palafox Ramirez
# Grupo: 951
# Fecha: 14/11/2025
# Meta 3.2 - Implementar índices y funciones loc e iloc en pandas
# -------------------------------------------------------------

import pandas as pd
import random

def generar_datos():
    # Meses modificados
    meses = ["Abril", "Mayo", "Junio"]
    # Productos modificados
    productos = ["X", "Y", "Z"]

    # Generación de ventas aleatorias
    ventas = {
        prod: [random.randint(150, 1200) for _ in meses]
        for prod in productos
    }

    df = pd.DataFrame(ventas, index=meses)
    print("\n--- Datos Generados ---")
    print(df)
    return df


def seleccionar_loc(df):
    print("\n--- Selección con LOC ---")

    # Venta del producto X en Abril
    venta_abril = df.loc["Abril", "X"]
    print(f"Ventas del producto X en Abril: {venta_abril}")

    # Ventas de todos los productos en Mayo
    ventas_mayo = df.loc["Mayo", ["X", "Y", "Z"]]
    print(f"\nVentas de los productos X, Y y Z en Mayo:\n{ventas_mayo}")

    # Ventas de Abril y Junio
    ventas_abril_junio = df.loc[["Abril", "Junio"], ["X", "Y", "Z"]]
    print(f"\nVentas en Abril y Junio:\n{ventas_abril_junio}")


def seleccionar_iloc(df):
    print("\n--- Selección con ILOC ---")

    # Primer mes
    primer_mes = df.iloc[0, :]
    print(f"Ventas del primer mes (todas las categorías):\n{primer_mes}")

    # Ventas del segundo producto
    segundo_producto = df.iloc[:, 1]
    print(f"\nVentas del segundo producto (Y):\n{segundo_producto}")

    # Ventas del segundo y tercer mes del primer producto
    meses_2_3 = df.iloc[1:3, 0]
    print(f"\nVentas del primer producto en Mayo y Junio:\n{meses_2_3}")


def modificar_datos(df):
    print("\n--- Modificación de Datos ---")
    # Cambiar valor específico
    df.loc["Junio", "Y"] = 1300
    print(f"Datos tras modificación:\n{df}")
    return df


if __name__ == "__main__":
    datos = generar_datos()
    seleccionar_loc(datos)
    seleccionar_iloc(datos)
    datos_modificados = modificar_datos(datos)
