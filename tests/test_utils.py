import unittest
from pyit import utils


class TestUtils(unittest.TestCase):

    def test_get_color_tuple(self):
        rgb = (255, 255, 255)
        rgba = (255, 255, 255, 0.5)
        hex_code = '#FFFFFF'
        # rgb format
        self.assertEqual(utils.get_color_tuple(rgb), rgb)
        # rgba format
        self.assertEqual(utils.get_color_tuple(rgba), rgba)
        # hexadecimal format
        self.assertEqual(utils.get_color_tuple(hex_code), rgb)

        # tuple length exception
        self.assertRaises(ValueError, utils.get_color_tuple, rgb[:2])
        self.assertRaises(ValueError, utils.get_color_tuple, rgb[:2] * 3)

        # tuple color value range exception
        self.assertRaises(ValueError, utils.get_color_tuple, (2.5, 255, 255))

        # tuple alpha value range exception
        self.assertRaises(ValueError,
            utils.get_color_tuple, (255, 255, 255, 10))

        # hexadecimal code length exception
        self.assertRaises(ValueError, utils.get_color_tuple, hex_code[:2])
        self.assertRaises(ValueError, utils.get_color_tuple, hex_code * 2)

        # invalid hexadecimal color format
        self.assertRaises(ValueError, utils.get_color_tuple, '#$%^&*<')

    def test_get_web_color(self):
        # rgb tuple
        self.assertEqual(utils.get_web_color((255, 255, 255)), '#ffffff')

        # rbga tuple
        self.assertEqual(
            utils.get_web_color((255, 255, 255, 0.5)),
            'rgba(255, 255, 255, 0.5)'
        )

        # hexadecimal code
        self.assertEqual(utils.get_web_color('#FFFFFF'), '#ffffff')

    def test_get_color_similarity(self):
        # Hexadecimal code
        self.assertEqual(utils.get_color_similarity(
            '#FFFFFF', '#FFFFFF'), 1)

        # Alpha and rgb tuple
        self.assertEqual(utils.get_color_similarity(
            (0, 0, 0, 0), (0, 0, 0)), 1)

        # Totally different colors
        self.assertEqual(utils.get_color_similarity(
            (0, 0, 0), '#FFFFFF'), 0)


if __name__ == '__main__':
    unittest.main()
