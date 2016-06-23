
from simple.PIL import images

image = images.open('strawberries.png')
out = images.new('L', image.width, image.height)

for pixel, outpixel in zip(image, out):
    outpixel.grey = (pixel.red + pixel.green + pixel.blue) / 3

out.save('output.png')
