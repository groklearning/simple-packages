
from simple.PIL import images

image = images.open('yawn.png')

for pixel in image:
    pixel.red += 50

image.save('output.png')
