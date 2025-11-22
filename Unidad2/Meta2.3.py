"""
Nombre: Palafox Ramirez Elvia Paloma
Grupo: 951
Fecha: 26 de Octubre del 2025
Descripción:
Preprocesamiento de datos relacionados con valores nulos y duplicidad
en DataFrames. Incluye detección de nulos, duplicados, eliminación de
columnas por porcentaje de nulos, imputación de datos y eliminación de
filas y renglones repetidos.
"""

import pandas as pd
import numpy as np

def crear_nulos():
    d = {
        "No.Empleado":[101,101,None,103,np.nan,105,106,None,108,109],
        "Nombre": ["Jesus","Jesus",np.nan,"Paloma","Yendy","Chacon",None,None,"Armando","Chomina"],
        "Sueldo": [3500,3500,2500,None,2790,4500,2100,3600,2300,2750],
        "Edad":[21,21,22,23,24,25,26,27,28,29],
        "Departamento":["TI","TI","RH","TI","RH",np.nan,"ADMIN","RH","TI","ADMIN"],
        "Direccion": [None, np.nan, "Villas del sol", np.nan, "Lomas Taurinas", None, np.nan, None, np.nan, None]
    }
    return pd.DataFrame(d)


def porcentaje_nulos(df: pd.DataFrame):
    nulos=df.isnull().sum() / len(df)
    return nulos


def numero_duplicados(df: pd.DataFrame):
    duplicados=df.duplicated().sum()
    return duplicados


def eliminar_columnas_por_nulos(df: pd.DataFrame, max_porc: float):
    if not (0 <= max_porc <= 1):
        raise ValueError("El porcentaje máximo debe estar entre 0 y 1.")

    porc_nulos = porcentaje_nulos(df)
    cols_eliminar = porc_nulos[porc_nulos >= max_porc].index.tolist()

    df.drop(columns=cols_eliminar, inplace=True)
    return cols_eliminar


def eliminar_filas_si_nulos(df: pd.DataFrame, columnas: list):
    #Elimina filas donde las columnas especificadas tengan valores nulos.
    #Retorna la cantidad de filas eliminadas.

    antes = len(df)
    df.dropna(subset=columnas, inplace=True)
    despues = len(df)
    return antes - despues


def reemplazar_nulos(df: pd.DataFrame, columnas: list, metodo: str):
    metodo = metodo.lower()

    if metodo not in ["mean", "ffill", "bfill"]:
        raise Exception("Método inválido. Debe ser 'mean', 'ffill' o 'bfill'.")

    for col in columnas:
        if metodo == "mean":
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].fillna(df[col].mean())
            else:
                raise Exception(f"No se puede aplicar mean a columna no numérica: {col}")

        elif metodo == "ffill":
            df[col] = df[col].ffill()

        elif metodo == "bfill":
            df[col] = df[col].bfill()

    return df


def eliminar_duplicados(df: pd.DataFrame):
    antes = len(df)
    df.drop_duplicates(inplace=True)
    despues = len(df)
    return antes - despues

if __name__ == "__main__":

    df = crear_nulos()
    print("DataFrame creado")
    print(df, "\n")

    # ELIMINAR FILAS DONDE No.Empleado O Nombre TENGAN NULOS
    # elimine el por No.empleado y Nombre porque siento que son los principales y mas importantes
    print("ELIMINAR FILAS POR NULOS EN COLUMNAS CLAVE (No.Empleado, Nombre):")
    filas_eliminadas = eliminar_filas_si_nulos(df, ["No.Empleado", "Nombre"])
    print("Filas eliminadas:", filas_eliminadas)
    print(df)


    print("\n1) PORCENTAJE DE NULOS POR COLUMNA:")
    print(porcentaje_nulos(df))


    print("\n2) NÚMERO DE RENGLONES DUPLICADOS:")
    print(numero_duplicados(df))


    print("\n3) ELIMINAR COLUMNAS SEGÚN PORCENTAJE DE NULOS:")
    eliminadas = eliminar_columnas_por_nulos(df, 0.3)
    print("Columnas eliminadas:", eliminadas, "\n")
    print(df)


    print("\n4) REMPLAZAR NULOS (Método: ffill):")
    df = reemplazar_nulos(df, ["Sueldo", "Departamento"], "ffill")
    print(df)


    print("\n5) ELIMINAR RENGLONES DUPLICADOS:")
    eliminados = eliminar_duplicados(df)
    print("Renglones eliminados:", eliminados)
    print(df)