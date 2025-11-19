# Palafox Ramirez Elvia Paloma
# 951
# Octubre 2025
# Meta 2.2 conexion a MySQL y modificacion en base de datos olimpiadas
# part 3 Clases de las tablas de olimpiadas con sus def


from Conexion import SQLConnect
import pymysql

class PaisSQL(SQLConnect):

    def crear_tabla(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Pais (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(150) NOT NULL UNIQUE
            )
        """)
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Tabla Pais creada (o ya existía)\n")

    def insertar(self):
        nombre = input("Nombre del país: ")
        if not nombre:
            print("Debe ingresar un nombre")
            return False

        conexion = self.conectar()
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO Pais (nombre) VALUES (%s)", (nombre,))
            conexion.commit()
            print("País insertado")
            return True
        except pymysql.err.IntegrityError:
            print("El país ya existe")
            return False
        finally:
            cursor.close()
            conexion.close()

    def editar(self, id, nombre_nuevo=None):
        try:
            id = int(id)
        except ValueError:
            print("El ID debe ser un número")
            return False

        if not nombre_nuevo:
            nombre_nuevo = input("Nuevo nombre del país: ")
            if not nombre_nuevo:
                print("Debe ingresar un nombre")
                return False

        conexion = self.conectar()
        cursor = conexion.cursor()

        # Validar que el nombre no exista ya
        cursor.execute("SELECT * FROM pais WHERE nombre=%s", (nombre_nuevo,))
        if cursor.fetchone():
            print("Ese país ya existe")
            cursor.close()
            conexion.close()
            return False

        # Actualizar el nombre
        cursor.execute("UPDATE pais SET nombre=%s WHERE id=%s", (nombre_nuevo, id))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("País actualizado")
        return True

    def eliminar(self):
        id_borrar = input("ID del país a eliminar: ")
        try:
            id_borrar = int(id_borrar)
        except ValueError:
            print("El ID debe ser un número")
            return False

        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Pais WHERE id = %s", (id_borrar,))
        conexion.commit()
        eliminado = cursor.rowcount > 0
        cursor.close()
        conexion.close()
        if eliminado:
            print("País eliminado")
        else:
            print("No se encontró el país con ese ID")
        return eliminado

    def consultar(self, filtro="1"):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM Pais WHERE {filtro}")
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultados


class OlimpiadaSQL(SQLConnect):

    def crear_tabla(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Olimpiada (
                id INT AUTO_INCREMENT PRIMARY KEY,
                year_olimpiada INT NOT NULL CHECK(year_olimpiada > 0),
                UNIQUE(year_olimpiada)
            )
        """)
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Tabla 'Olimpiada' creada (o ya existía)\n")

    def insertar(self, year=None):
        if year is None:
            year = input("Año de la Olimpiada: ")
        try:
            year = int(year)
        except ValueError:
            print("Debe ingresar un número válido")
            return False

        conexion = self.conectar()
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO Olimpiada (year_olimpiada) VALUES (%s)", (year,))
            conexion.commit()
            print("Olimpiada insertada")
            return True
        except pymysql.err.IntegrityError:
            print("Ese año ya existe")
            return False
        finally:
            cursor.close()
            conexion.close()

    def editar(self, id, year_nuevo):
        try:
            year_nuevo = int(year_nuevo)
        except ValueError:
            print("Debe ingresar un número válido")
            return False

        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Olimpiada WHERE year_olimpiada = %s", (year_nuevo,))
        if cursor.fetchone():
            print("Ese año ya existe")
            cursor.close()
            conexion.close()
            return False

        cursor.execute("UPDATE Olimpiada SET year_olimpiada = %s WHERE id = %s", (year_nuevo, id))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Año actualizado")
        return True

    def eliminar(self, id):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Olimpiada WHERE id = %s", (id,))
        conexion.commit()
        eliminado = cursor.rowcount > 0
        cursor.close()
        conexion.close()
        if eliminado:
            print("Olimpiada eliminada")
        else:
            print("No se encontró la Olimpiada con ese ID")
        return eliminado

    def consultar(self, filtro="1"):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM Olimpiada WHERE {filtro}")
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultados

class ResultadosSQL(SQLConnect):

    def crear_tabla(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Resultados (
                idOlimpiada INT,
                idPais INT,
                idGenero INT,
                oro INT NOT NULL CHECK(oro>0),
                plata INT NOT NULL CHECK(plata>0),
                bronce INT NOT NULL CHECK(bronce>0),
                PRIMARY KEY (idOlimpiada, idPais, idGenero),
                FOREIGN KEY (idOlimpiada) REFERENCES Olimpiada(id),
                FOREIGN KEY (idPais) REFERENCES Pais(id),
                FOREIGN KEY (idGenero) REFERENCES Genero(id)
            )
        """)
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Tabla 'Resultados' creada (o ya existía)\n")

    def insertar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        try:
            oro, plata, bronce = int(oro), int(plata), int(bronce)
            if oro < 0 or plata < 0 or bronce < 0:
                raise ValueError
        except ValueError:
            print("Las medallas deben ser números enteros positivos")
            return False

        conexion = self.conectar()
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                INSERT INTO Resultados (idOlimpiada, idPais, idGenero, oro, plata, bronce)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (idOlimpiada, idPais, idGenero, oro, plata, bronce))
            conexion.commit()
            print("Resultado insertado")
            return True
        except pymysql.err.IntegrityError:
            print("Resultado ya existe")
            return False
        finally:
            cursor.close()
            conexion.close()

    def editar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        try:
            oro, plata, bronce = int(oro), int(plata), int(bronce)
            if oro < 0 or plata < 0 or bronce < 0:
                raise ValueError
        except ValueError:
            print("Las medallas deben ser números enteros positivos")
            return False

        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Resultados SET oro=%s, plata=%s, bronce=%s
            WHERE idOlimpiada=%s AND idPais=%s AND idGenero=%s
        """, (oro, plata, bronce, idOlimpiada, idPais, idGenero))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Resultado actualizado")
        return True

    def eliminar(self, idOlimpiada, idPais, idGenero):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            DELETE FROM Resultados 
            WHERE idOlimpiada=%s AND idPais=%s AND idGenero=%s
        """, (idOlimpiada, idPais, idGenero))
        conexion.commit()
        eliminado = cursor.rowcount > 0
        cursor.close()
        conexion.close()
        if eliminado:
            print("Resultado eliminado")
        else:
            print("No se encontró el resultado")
        return eliminado

    def consultar(self, filtro="1"):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM Resultados WHERE {filtro}")
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultados
