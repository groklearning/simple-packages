# vim: set et nosi ai ts=4 sts=4 sw=4 colorcolumn=80:
# coding: utf-8

import unittest

from PIL import ImageChops, ImageOps


class ImageTestCase(unittest.TestCase):

    def assertImageEqual(self, first, second):
        self.assertEqual(
            first.mode, second.mode, 'Images do not have the same mode.')
        self.assertEqual(
            first.size, second.size, 'Images do not have the same dimensions.')
        diff_image = ImageChops.difference(first, second)
        diff_image = ImageOps.grayscale(diff_image)

        pixels = first.height * first.width

        histogram = diff_image.histogram()
        same_pixels = histogram[0]
        self.assertEqual(
            pixels, same_pixels,
            'Number of matching pixels does not match the number of pixels.')
