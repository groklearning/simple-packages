
from simple.PIL import Image

image = Image.open('squirrel.png')

for pixel in image:
    pixel.red -= 80
    pixel.green -= 20

image.save('output.png')
