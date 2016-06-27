
from simple.PIL import Image

image = Image.open('yawn.png')

for pixel in image:
    pixel.red += 50

image.save('output.png')
