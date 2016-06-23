
from simple.PIL import images

from PIL import Image

image = images.open('squirrel.png')

for pixel in image:
    pixel.red -= 80
    pixel.green -= 20

image.save('output.png')
