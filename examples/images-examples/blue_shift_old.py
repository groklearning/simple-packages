
from PIL import Image


image = Image.open('squirrel.png')
red = image.split()[0]
green = image.split()[1]
blue = image.split()[2]
for y in range(image.height):
    for x in range(image.width):
        value = red.getpixel((x, y)) - 80
        red.putpixel((x, y), value)
        value = green.getpixel((x, y)) - 20
        green.putpixel((x, y), value)
result = Image.merge('RGB', (red, green, blue))
result.save('output.png')
