
from simple.PIL import images

image = images.open('leaves_bw.png')

for pixel in image:
    pixel.grey = 255 - pixel.grey

image.save('output.png')
