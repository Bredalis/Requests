
import requests

jar = requests.cookies.RequestsCookieJar()

jar.set("tasty_cookie", "yum", domain = "httpbin.org", path = "/cookies")
jar.set("gross_cookie", "blech", domain = "httpbin.org", path = "/elsewhere")

url = "https://httpbin.org/cookies"
solicitud = requests.get(url, cookies = jar)
print(solicitud.text)