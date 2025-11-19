# Palafox Ramirez Elvia Paloma
# 951
# Octubre 2025
# Meta 2.2 conexion a MySQL y modificacion en base de datos olimpiadas
# part 1 menu de pruebas

from ClasesOlimpiadas import PaisSQL, OlimpiadaSQL, ResultadosSQL


def submenu_pais(pais_sql):
    while True:
        print("\n--- MENÚ MODIFICACIONES TABLA PAÍS ---")
        print("1. Crear tabla")
        print("2. Insertar país")
        print("3. Editar países")
        print("4. Eliminar país")
        print("5. Consultar país (filtro)")
        print("6. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            pais_sql.crear_tabla()
        elif opcion == "2":
            pais_sql.insertar()
        elif opcion == "3":
            id_editar = input("ID del país a modificar: ")
            pais_sql.editar(id_editar)
        elif opcion == "4":
            pais_sql.eliminar()
        elif opcion == "5":
            filtro = input("Ingresa el filtro SQL (ej: id=1, nombre='México'): ")
            resultados = pais_sql.consultar(filtro)
            print(resultados)
        elif opcion == "6":
            break
        else:
            print("Opción no válida\n")



def submenu_olimpiada(olimpiada_sql):
    while True:
        print("\n--- MENÚ MODIFICACIONES TABLA OLIMPIADA ---")
        print("1. Crear tabla")
        print("2. Insertar Olimpiada")
        print("3. Editar año")
        print("4. Eliminar Olimpiada")
        print("5. Consultar Olimpiada (filtro)")
        print("6. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            olimpiada_sql.crear_tabla()
        elif opcion == "2":
            olimpiada_sql.insertar()
        elif opcion == "3":
            id_editar = input("ID de la Olimpiada a modificar: ")
            year_nuevo = input("Nuevo año: ")
            olimpiada_sql.editar(id_editar, year_nuevo)
        elif opcion == "4":
            id_eliminar = input("ID de la Olimpiada a eliminar: ")
            olimpiada_sql.eliminar(id_eliminar)
        elif opcion == "5":
            filtro = input("Ingresa el filtro SQL (ej: id=1, year_olimpiada>2000): ")
            resultados = olimpiada_sql.consultar(filtro)
            print(resultados)
        elif opcion == "6":
            break
        else:
            print("Opción no válida\n")




def submenu_resultados(resultados_sql):
    while True:
        print("\n--- MENU MODIFICACIONES TABLA RESULTADOS ---")
        print("1. Crear tabla")
        print("2. Insertar resultado")
        print("3. Editar resultado")
        print("4. Eliminar resultado")
        print("5. Consultar resultado (filtro)")
        print("6. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            resultados_sql.crear_tabla()
        elif opcion == "2":
            idO = input("ID Olimpiada: ")
            idP = input("ID País: ")
            idG = input("ID Género: ")
            oro = input("Oro: ")
            plata = input("Plata: ")
            bronce = input("Bronce: ")
            resultados_sql.insertar(idO, idP, idG, oro, plata, bronce)
        elif opcion == "3":
            idO = input("ID Olimpiada: ")
            idP = input("ID País: ")
            idG = input("ID Género: ")
            oro = input("Oro: ")
            plata = input("Plata: ")
            bronce = input("Bronce: ")
            resultados_sql.editar(idO, idP, idG, oro, plata, bronce)
        elif opcion == "4":
            idO = input("ID Olimpiada: ")
            idP = input("ID País: ")
            idG = input("ID Género: ")
            resultados_sql.eliminar(idO, idP, idG)
        elif opcion == "5":
            filtro = input("Ingresa el filtro SQL (ej: idPais=1 AND idOlimpiada=2): ")
            resultados = resultados_sql.consultar(filtro)
            print(resultados)
        elif opcion == "6":
            break
        else:
            print("Opción no válida\n")



if __name__ == "__main__":
    pais_sql = PaisSQL()
    olimpiada_sql = OlimpiadaSQL()
    resultados_sql = ResultadosSQL()

    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Modificaciones Tabla País")
        print("2. Modificaciones Tabla Olimpiada")
        print("3. Modificaciones Tabla Resultados")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            submenu_pais(pais_sql)
        elif opcion == "2":
            submenu_olimpiada(olimpiada_sql)
        elif opcion == "3":
            submenu_resultados(resultados_sql)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida\n")
