# vim: set et nosi ai ts=2 sts=2 sw=2:
# coding: utf-8
import os
import unittest

from simple.PIL import Image

from .utils import ImageTestCase

IMAGE_DIR = 'tests/PIL/images/'

class TestImageConstructors(ImageTestCase):

  def test_open(self):
    img1 = Image.open(os.path.join(IMAGE_DIR, 'strawberries.png'))
    img2 = Image.open(os.path.join(IMAGE_DIR, 'strawberries.png'))

    self.assertImageEqual(img1, img2)

  def test_open_grayscale(self):
    img1 = Image.open(os.path.join(IMAGE_DIR, 'leaves_bw.png'))
    self.assertEqual(img1.mode, 'L')
    self.assertEqual(img1.size, (640, 426))

  def test_frombytes(self):
    img1 = Image.open(os.path.join(IMAGE_DIR, 'strawberries.png'))
    byte_data = img1.tobytes()
    img2 = Image.frombytes(img1.mode, img1.size, byte_data)

    self.assertImageEqual(img1, img2)

  def test_split_merge(self):
    img1 = Image.open(os.path.join(IMAGE_DIR, 'strawberries.png'))
    red, green, blue = img1.split()
    img2 = Image.merge('RGB', (red, green, blue))

    self.assertImageEqual(img1, img2)


class TestImageFunctions(ImageTestCase):

  def test_pixel_generator(self):
    img1 = Image.open(os.path.join(IMAGE_DIR, 'strawberries.png'))
    pixel_list = list(img1)
    self.assertEqual(img1.height * img1.width, len(pixel_list))

    first_pixel = pixel_list[0]
    self.assertEqual(first_pixel.get_coords(), (0, 0))
    self.assertEqual(first_pixel.red, 77)
    self.assertEqual(first_pixel.green, 20)
    self.assertEqual(first_pixel.blue, 9)

    middle_pixel = pixel_list[1960]
    self.assertEqual(middle_pixel.get_coords(), (4, 360))
    self.assertEqual(middle_pixel.red, 41)
    self.assertEqual(middle_pixel.green, 4)
    self.assertEqual(middle_pixel.blue, 11)

    last_pixel = pixel_list[-1]
    self.assertEqual(last_pixel.get_coords(), (img1.width - 1, img1.height - 1))
    self.assertEqual(last_pixel.red, 242)
    self.assertEqual(last_pixel.green, 25)
    self.assertEqual(last_pixel.blue, 34)


class TestPixelIndexing(ImageTestCase):

  def test_index_rgb(self):
    img1 = Image.open(os.path.join(IMAGE_DIR, 'strawberries.png'))
    first_pixel = img1[0, 0]
    self.assertEqual(first_pixel.get_coords(), (0, 0))
    self.assertEqual(first_pixel.red, 77)
    self.assertEqual(first_pixel.green, 20)
    self.assertEqual(first_pixel.blue, 9)

    middle_pixel = img1[4, 360]
    self.assertEqual(middle_pixel.get_coords(), (4, 360))
    self.assertEqual(middle_pixel.red, 41)
    self.assertEqual(middle_pixel.green, 4)
    self.assertEqual(middle_pixel.blue, 11)

    last_pixel = img1[img1.width - 1, img1.height - 1]
    self.assertEqual(last_pixel.get_coords(), (img1.width - 1, img1.height - 1))
    self.assertEqual(last_pixel.red, 242)
    self.assertEqual(last_pixel.green, 25)
    self.assertEqual(last_pixel.blue, 34)

  def test_index_grayscale(self):
    img1 = Image.open(os.path.join(IMAGE_DIR, 'leaves_bw.png'))
    first_pixel = img1[0, 0]
    self.assertEqual(first_pixel.get_coords(), (0, 0))
    self.assertEqual(first_pixel.gray, 44)

    middle_pixel = img1[4, 360]
    self.assertEqual(middle_pixel.get_coords(), (4, 360))
    self.assertEqual(middle_pixel.gray, 67)

    last_pixel = img1[img1.width - 1, img1.height - 1]
    self.assertEqual(last_pixel.get_coords(), (img1.width - 1, img1.height - 1))
    self.assertEqual(last_pixel.gray, 187)

  def test_type_error(self):
    img1 = Image.open(os.path.join(IMAGE_DIR, 'leaves_bw.png'))

    try:
      first_pixel = img1[0]
      self.fail()
    except TypeError as e:
      pass

    try:
      first_pixel = img1[0,]
      self.fail()
    except IndexError as e:
      pass


class TestPixelModifications(ImageTestCase):

  def test_modify_pixel_bw(self):
    img1 = Image.open(os.path.join(IMAGE_DIR, 'leaves_bw.png'))
    pixel1 = img1[4, 360]
    pixel2 = img1[4, 360]
    self.assertEqual(pixel1.get_coords(), (4, 360))
    self.assertEqual(pixel1.gray, 67)
    self.assertEqual(pixel2.get_coords(), (4, 360))
    self.assertEqual(pixel2.gray, 67)

    pixel1.gray = 0
    self.assertEqual(pixel1.gray, 0)
    self.assertEqual(pixel2.gray, 0)

    # Get a new pixel object and check that it's also changed.
    pixel3 = img1[4, 360]
    self.assertEqual(pixel3.gray, 0)

  def test_modify_pixel_rgb(self):
    img1 = Image.open(os.path.join(IMAGE_DIR, 'strawberries.png'))

    pixel1 = img1[4, 360]
    self.assertEqual(pixel1.get_coords(), (4, 360))
    self.assertEqual(pixel1.red, 41)
    self.assertEqual(pixel1.green, 4)
    self.assertEqual(pixel1.blue, 11)

    pixel2 = img1[4, 360]
    self.assertEqual(pixel2.get_coords(), (4, 360))
    self.assertEqual(pixel2.red, 41)
    self.assertEqual(pixel2.green, 4)
    self.assertEqual(pixel2.blue, 11)

    pixel1.red = 10
    pixel1.green = 20
    pixel1.blue = 30

    self.assertEqual(pixel1.red, 10)
    self.assertEqual(pixel1.green, 20)
    self.assertEqual(pixel1.blue, 30)
    self.assertEqual(pixel2.red, 10)
    self.assertEqual(pixel2.green, 20)
    self.assertEqual(pixel2.blue, 30)

  def test_full_image_modification(self):
    actual = Image.open(os.path.join(IMAGE_DIR, 'squirrel.png'))
    expected = Image.open(os.path.join(IMAGE_DIR, 'blueshift_squirrel.png'))

    for pixel in actual:
      pixel.red -= 80
      pixel.green -= 20

    self.assertImageEqual(expected, actual)
