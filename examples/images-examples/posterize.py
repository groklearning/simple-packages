
from simple.PIL import images

image = images.open('pug_bw.png')

for pixel in image:
    value = pixel.grey
    if value < 130:
        pixel.grey = 0
    else:
        pixel.grey = 255

image.save('output.png')
