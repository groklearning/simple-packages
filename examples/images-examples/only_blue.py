
from simple.PIL import images

image = images.open('dragonfly.png')

for pixel in image.pixels():
    pixel.green = pixel.blue
    pixel.red = pixel.blue

images.save('output.png')
