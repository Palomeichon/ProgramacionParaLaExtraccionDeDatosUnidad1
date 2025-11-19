# Nombre: Palafox Ramirez Elvia Paloma
# Grupo: 951
# Fecha: 2 de noviembre
# Descripción: Meta 3.1 Ejercicios de agrupamiento, tablas resumen y transformación

import pandas as pd

def creacion():

    d = {
        "Tienda":     ["A", "A", "B", "C", "B", "A", "C", "B"],
        "Producto":   ["Manzana", "Plátano", "Naranja", "Manzana", "Plátano", "Naranja", "Manzana", "Naranja"],
        "Categoría":  ["Fruta", "Fruta", "Fruta", "Fruta", "Fruta", "Fruta", "Fruta", "Fruta"],
        "Precio":     [30, 20, 35, 25, 30, 45, 35, 25],
        "Cantidad Vendida": [50, 30, 20, 60, 25, 35, 55, 30],
        "Calificación": ["A", "A", "B", "B", "A", "C", "C", "A"]
    }

    df = pd.DataFrame(d)
    return df

def asignacion_codigo(df: pd.DataFrame):

    df["Código Tienda"] = df["Tienda"].map({"A": 1, "B": 2, "C": 3})

    # Convertir calificaciones a valores numéricos
    df["Calificación Numérica"] = df["Calificación"].map({"A": 3, "B": 2, "C": 1})

    return df

def total_ventas_tiendas(df: pd.DataFrame):
    df["Total Venta"] = df["Precio"] * df["Cantidad Vendida"]
    total_ventas_tienda = df.groupby("Tienda")["Total Venta"].sum()
    return total_ventas_tienda


def precio_promedio_producto_tienda(df: pd.DataFrame):
    precio_promedio = df.groupby(["Tienda", "Producto"])["Precio"].mean()
    #df.groupby("Tienda")["Precio"].mean()
    return precio_promedio

def cantidad_pivot_tienda(df: pd.DataFrame):
    #Crea una tabla pivot para la Cantidad Vendida por Producto y Tienda.
    cantidad_pivot = df.pivot_table(
        values="Cantidad Vendida",
        index="Producto",
        columns="Tienda",
        aggfunc="sum",
        fill_value=0
    )
    return cantidad_pivot


def ventas_pivot_tienda(df: pd.DataFrame):
    #Crea una tabla pivot para el Total de Venta por Producto y Tienda.
    # Se asume que la columna "Total Venta" ya fue calculada en el main.
    ventas_pivot = df.pivot_table(
        values="Total Venta",
        index="Producto",
        columns="Tienda",
        aggfunc="sum",
        fill_value=0
    )
    return ventas_pivot

if __name__ == "__main__":
    df=creacion()
    print("dataframe original")
    print(df)

    dfCodigos=asignacion_codigo(df)
    print("\nAgregacion de columna con codigo")
    print(dfCodigos)

    VentasPorTienda=total_ventas_tiendas(dfCodigos)
    print("\nVentas por tienda")
    print(VentasPorTienda)

    PrecioPromedioProductoTienda= precio_promedio_producto_tienda(dfCodigos)
    print("\nPrecio promedio de producto por tienda")
    print(PrecioPromedioProductoTienda)

    print("\nTABLA PIVOT: Cantidad Vendida por Producto y Tienda:")
    CantidadPivot = cantidad_pivot_tienda(dfCodigos)
    print(CantidadPivot)

    print("\nTABLA PIVOT: Total de Ventas por Producto y Tienda:")
    VentasPivot = ventas_pivot_tienda(dfCodigos)
    print(VentasPivot)