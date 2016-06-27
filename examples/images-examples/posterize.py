
from simple.PIL import Image

image = Image.open('pug_bw.png')

for pixel in image:
    if pixel.grey < 130:
        pixel.grey = 0
    else:
        pixel.grey = 255

image.save('output.png')
