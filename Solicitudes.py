
# Direfentes solicitudes

import requests

url = "https://httpbin.org/"

# POST

r = requests.post(url + "post", data  = {"key": "value"})
print(r.text)

# GET

r = requests.get("https://api.github.com/events")
print(r.text)

# DELETE

r = requests.delete(url + "delete")
print(r.text)

# PUT

r = requests.put(url + "put", data = {"key": "value"})
print(r.text)

# HEAD

r = requests.head(url + "get")
print(r.text)

# OPTIONS

r = requests.options(url + "get")
print(r.text)