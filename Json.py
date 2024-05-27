
# Obtener los datos en formato json

import requests

solicitud = requests.get("https://api.github.com/events")
print(solicitud.json())