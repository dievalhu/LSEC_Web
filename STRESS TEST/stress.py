import os

# Lista de configuraciones
configurations = [
    #{"file": "locustfile_ip.py", "host": "http://34.125.169.178", "csv": "swarm_ip_stats"},
    {"file": "locustfile_api.py", "host": "http://34.125.169.178:4200", "csv": "swarm_api_stats"},
    {"file": "locustfile_website.py", "host": "http://ecuadoriansignlanguagefenedif.000webhostapp.com", "csv": "swarm_website_stats"},
    # Puedes agregar más configuraciones según sea necesario
]

# Función para ejecutar Locust
def run_locust(config, duration):
    if duration == "time":
        os.system(f"locust -f {config['file']} --host={config['host']} --csv={config['csv']} --headless --users 50 --spawn-rate 1 -t 1min")
    elif duration == "requests":
        os.system(f"locust -f {config['file']} --host={config['host']} --csv={config['csv']} --headless --users 50 --spawn-rate 1 --stop-after 1000")

# Ejecutar pruebas de tiempo y número de solicitudes para cada configuración
for config in configurations:
    run_locust(config, "time")
    #run_locust(config, "requests")
