# Palafox Ramirez Elvia Paloma
# 951
# Octubre 2025
# Meta 2.2 conexion a MySQL y modificacion en base de datos olimpiadas
# part 2 Conexion con la base de datos olimpiadas.sql en MySQL

import pymysql

class SQLConnect:
    def __init__(self, host="localhost", user="root", password="admin123", database="olimpiadas", port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def conectar(self):
        return pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )
