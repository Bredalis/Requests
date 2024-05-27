
import requests

url = "https://api.github.com/some/endpoint"
encabezados = {"user-agent": "my-app/0.0.1"}

# Crear solicitud

solicitud = requests.get(url, headers = encabezados)
print(solicitud.content)