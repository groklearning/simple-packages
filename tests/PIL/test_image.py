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
