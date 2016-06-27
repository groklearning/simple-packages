
from simple.PIL import Image

image = Image.open('yawn.png')

for pixel in image:
    pixel.green = 0
    pixel.red = 0

image.save('output.png')
