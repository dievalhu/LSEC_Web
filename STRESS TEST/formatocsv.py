import csv

# Lista de configuraciones
configurations = [
    #{"csv": "swarm_ip_stats"},
    {"csv": "swarm_api_stats"},
    {"csv": "swarm_website_stats"},
    # Puedes agregar más configuraciones según sea necesario
]

# Importar y ejecutar función para cambiar delimitador en archivos CSV generados por Locust
def cambiar_delimitador(archivo_entrada, archivo_salida, delimitador):
    with open(archivo_entrada, 'r', newline='', encoding='utf-8') as f_entrada:
        lector_csv = csv.reader(f_entrada)
        datos = [fila for fila in lector_csv if fila]  # Excluir filas en blanco

    with open(archivo_salida, 'w', newline='', encoding='utf-8') as f_salida:
        escritor_csv = csv.writer(f_salida, delimiter=delimitador)
        escritor_csv.writerows(datos)

# Llamar a la función para cambiar delimitador en cada archivo CSV generado por Locust
for config in configurations:
    cambiar_delimitador(f"{config['csv']}_stats.csv", f"{config['csv']}_stats_modificado.csv", ';')
