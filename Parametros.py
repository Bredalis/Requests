
import requests

payload = {"key1": "value1", "key2": "value2"}
solicitud = requests.get("https://httpbin.org/get", params = payload)

print("URL:", solicitud.url)