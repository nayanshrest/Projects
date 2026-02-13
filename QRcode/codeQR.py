import qrcode
from pathlib import Path

url = input("Enter a url: ").strip()
name=input("Name you qrcode: ")
dest = Path.home()/"OneDrive"/"Pictures"/"qrcodes"
img = qrcode.make(url)
type(img) # qrcode.image.pil.PilImage

img.save(f"{dest}\\{name}.png")