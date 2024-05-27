
# Uso de  archivos

import requests

url = "https://httpbin.org/post"
files = {"file": open("Cookies.py", "rb")}  

solicitud = requests.post(url, files = files, verify = False)
print(solicitud.text)

# Codigo de estado

print(solicitud.status_code)
print(solicitud.headers)