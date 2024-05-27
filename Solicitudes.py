
# Direfentes solicitudes

import requests

url = "https://httpbin.org/"

def mostrar_solicitud():
	print(solicitud.text)

# POST

solicitud = requests.post(url + "post", data  = {"key": "value"})
mostrar_solicitud()

# GET

solicitud = requests.get("https://api.github.com/events")
mostrar_solicitud()

# DELETE

solicitud = requests.delete(url + "delete")
mostrar_solicitud()

# PUT

solicitud = requests.put(url + "put", data = {"key": "value"})
mostrar_solicitud()
# HEAD

solicitud = requests.head(url + "get")
mostrar_solicitud()

# OPTIONS

solicitud = requests.options(url + "get")
mostrar_solicitud()