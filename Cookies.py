
import requests

# Crear nuestras propias cookies

url = "https://httpbin.org/cookies"
cookies = dict(cookies_are = "working")

r = requests.get(url, cookies = cookies)
print("Cookies: \n", r.text)