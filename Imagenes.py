
# Obtener imagenes desde url

import requests
from PIL import Image
from io import BytesIO

url = "https://i.pinimg.com/564x/95/bf/29/95bf29e5082831a8d9f99c88274b8b40.jpg"
solicitud = requests.get(url, stream = True)
img = Image.open(BytesIO(solicitud.content))

print("Info url:", img)