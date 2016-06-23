
from simple.PIL import images

image = images.open('strawberries.png')

for pixel in image:
    avg = (pixel.red + pixel.green + pixel.blue) / 3
    if pixel.red < pixel.blue + 40:
        pixel.red = avg
        pixel.green = avg
        pixel.blue = avg
    if pixel.red < pixel.green + 40:
        pixel.red = avg
        pixel.green = avg
        pixel.blue = avg

image.save('output.png')
