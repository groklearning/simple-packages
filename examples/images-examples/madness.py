
from simple.PIL import Image

image = Image.open('yawn.png')
red, green, blue = image.split()

out_image = Image.merge('RGB', (green, red, blue))
out_image.save('output.png')
