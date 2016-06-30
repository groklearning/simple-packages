
from simple.PIL import Image

image = Image.open('strawberries.png')
out = Image.new('L', image.width, image.height)

for pixel, outpixel in zip(image, out):
    outpixel.grey = (pixel.red + pixel.green + pixel.blue) / 3

out.save('output.png')
