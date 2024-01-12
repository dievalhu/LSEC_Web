import mysql.connector
from decouple import config

class Conexion:
    def __init__(self):
        self.user = config('USER')
        self.pwd = config('PWD')
        self.db_name = config('DB_NAME')
        self.host = config('HOST')
        self.conn = self.crear_conexion()

    def crear_conexion(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.pwd,
                database=self.db_name
            )
            return connection
        except Exception as ee:
            print("Exception:",ee)
            raise Exception(str(ee))
