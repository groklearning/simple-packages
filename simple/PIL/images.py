# vim: set et nosi ai ts=2 sts=2 sw=2:
# coding: utf-8
"""
Simplified wrapper around the Pillow library.
"""

from PIL import Image as PILImage


def open(filename, **kwargs):
  return Image(PILImage.open(filename, **kwargs))


def new(mode, width, height):
  return Image(PILImage.new(mode, (width, height)))


class Pixel:
  """An individual pixel in an image."""

  def __init__(self, mode, image, x, y):
    self._image = image
    self.mode = mode
    self._x = x
    self._y = y

  @property
  def coordinates(self):
    return (self._x, self._y)

  def get_red(self):
    if 'R' not in self.mode:
      raise ImageModeError('Cannot use the red value of a pixel because the image mode is \'{}\''.format(self.mode))
    return self._image[self.coordinates][0]

  def set_red(self, value):
    if 'R' not in self.mode:
      raise ImageModeError('Cannot use the red value of a pixel because the image mode is \'{}\''.format(self.mode))
    old = self._image[self.coordinates]
    self._image[self.coordinates] = (int(value), old[1], old[2])

  red = property(get_red, set_red, None, 'The red value for RGB and RGBA images.')

  def get_green(self):
    if 'G' not in self.mode:
      raise ImageModeError('Cannot use the green value of a pixel because the image mode is \'{}\''.format(self.mode))
    return self._image[self.coordinates][1]

  def set_green(self, value):
    if 'G' not in self.mode:
      raise ImageModeError('Cannot use the green value of a pixel because the image mode is \'{}\''.format(self.mode))
    old = self._image[self.coordinates]
    self._image[self.coordinates] = (old[0], int(value), old[2])

  green = property(get_green, set_green, None, 'The green value for RGB and RGBA images.')

  def get_blue(self):
    if 'B' not in self.mode:
      raise ImageModeError('Cannot use the blue value of a pixel because the image mode is \'{}\''.format(self.mode))
    return self._image[self.coordinates][2]

  def set_blue(self, value):
    if 'B' not in self.mode:
      raise ImageModeError('Cannot use the blue value of a pixel because the image mode is \'{}\''.format(self.mode))
    old = self._image[self.coordinates]
    self._image[self.coordinates] = (old[0], old[1], int(value))

  blue = property(get_blue, set_blue, None, 'The blue value for RGB and RGBA images.')

  def get_gray(self):
    if 'L' not in self.mode:
      raise ImageModeError('Cannot use the gray value of a pixel because the image mode is \'{}\''.format(self.mode))
    return self._image[self.coordinates]

  def set_gray(self, value):
    if 'L' not in self.mode:
      raise ImageModeError('Cannot use the gray value of a pixel because the image mode is \'{}\''.format(self.mode))
    self._image[self.coordinates] = int(value)

  gray = property(get_gray, set_gray, None, 'The blue value for L (grayscale) images.')


class ImageModeError(Exception):
  def __init__(self, msg):
    self.msg = msg

  def __str__(self):
    return self.msg


class Image:

  def __init__(self, image):
    self._image = image
    self._pixel_access = image.load()

  def __getattr__(self, attr):
    # Delegate to self._image
    return getattr(self._image, attr)

  def __iter__(self):
    for x in range(self.width):
      for y in range(self.height):
        yield Pixel(self._image.mode, self._pixel_access, x, y)
