#Carga csv centro costos
from asyncio.windows_events import NULL
from cmath import nan
from numpy import NAN, equal
import pandas as pd
import numpy as np
import mysql.connector
import io
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
import re

def ejecutarSQL(SQL):
    conexion1=mysql.connector.connect(host="localhost", 
                                    user="Ecuadorian_Sign_Language", 
                                    passwd="ESL_P63", 
                                    database="Ecuadorian_Sign_Language")
    cursor1=conexion1.cursor()
    cursor1.execute(SQL)
    conexion1.commit()   
    conexion1.close()
    return True;

def consultarSQL(SQL):
    auxString = ""
    conexion1=mysql.connector.connect(host="localhost", 
                                    user="Ecuadorian_Sign_Language", 
                                    passwd="ESL_P63", 
                                    database="Ecuadorian_Sign_Language")
    cursor1=conexion1.cursor()
    cursor1.execute(SQL)
    for fila in cursor1:
        auxString += str(fila) +"\n"
        #print(fila)
    conexion1.close()
    return auxString;

def consultarSQL_Lista(SQL):
    auxString = []
    conexion1=mysql.connector.connect(host="localhost", 
                                    user="Ecuadorian_Sign_Language", 
                                    passwd="ESL_P63", 
                                    database="Ecuadorian_Sign_Language")
    cursor1=conexion1.cursor()
    cursor1.execute(SQL)
    for fila in cursor1:
        auxString.append(fila)
        #print(fila)
    conexion1.close()
    return auxString;

def isNaN(num):
    return num != num

def clearTables():
  #Dropeo tabla motivo
  ejecutarSQL("DELETE FROM palabra;")
  #Dropeo tabla personal
  ejecutarSQL("DELETE FROM caracter;")

def cargar_inserts_desde_archivo(ruta_archivo):
    # Lee el archivo de texto
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    # Establece la conexión a tu base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="Ecuadorian_Sign_Language",
        passwd="ESL_P63",
        database="Ecuadorian_Sign_Language"
    )
    cursor = conexion.cursor()

    # Ejecuta los comandos INSERT INTO
    try:
        for linea in lineas:
            comando = linea.strip()  # Elimina espacios en blanco y saltos de línea
            ejecutarSQL(comando)
        conexion.commit()
        print("Datos cargados con éxito desde el archivo a la base de datos.")
    except mysql.connector.Error as err:
        print(f"Error al cargar los datos: {err}")

    # Cierra la conexión a la base de datos
    cursor.close()
    conexion.close()

clearTables()
#insertar_caracteres()

# Llama a la función para cargar el archivo CSV a la base de datos
ruta_archivo_csv_caracteres = "Ecuadorian_Sign_Language\BACK-END\caracteres.txt"
ejecutarSQL("ALTER TABLE caracter AUTO_INCREMENT=0")
cargar_inserts_desde_archivo(ruta_archivo_csv_caracteres)

ruta_archivo_csv_palabras = "Ecuadorian_Sign_Language\BACK-END\palabras.txt"
ejecutarSQL("ALTER TABLE palabra AUTO_INCREMENT=0")
cargar_inserts_desde_archivo(ruta_archivo_csv_palabras)

