
# Uso de  archivos
# en solicitudes

import requests

url = "https://httpbin.org/post"
files = {"file": open("Cookies.py", "rb")}  

r = requests.post(url, files = files, verify = False)
print(r.text)

# Codigo de estado

print(r.status_code)
print(r.headers)