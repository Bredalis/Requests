
# Obtener imagenes 
# desde url

# Librerias

import requests
from PIL import Image
from io import BytesIO

r = requests.get("https://i.pinimg.com/564x/95/bf/29/95bf29e5082831a8d9f99c88274b8b40.jpg", stream = True)
img = Image.open(BytesIO(r.content))

print("Info url:", img)