import unittest
from unittest.mock import patch
from ImagesDownloader import ImageId


class TestImage(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.img1 = ImageId('https://upload.wikimedia.org/wikipedia/commons/7/7e/Bow_bow.jpg')
        self.img2 = ImageId('https://bit.ly/2KiBQxO')
        self.img3 = ImageId('https://upload.wikimedia.org/wikipedia/commons/9/9a/PNG_transparency_demonstration_2.png')

    def tearDown(self):
        pass

    def test_name(self):
        print('test_name')

        self.img1.get_name('test_dir\\')
        self.img2.get_name('test_dir\\')
        self.img3.get_name('test_dir\\')

        # img1
        self.assertEqual(self.img1.name, 'Bow_bow.jpg')
        self.assertEqual(self.img1.output_path, 'test_dir\\Bow_bow.jpg')

        # img2
        self.assertEqual(self.img2.name, '2KiBQxO')
        self.assertEqual(self.img2.output_path, 'test_dir\\2KiBQxO')

        # img3
        self.assertEqual(self.img3.name, 'PNG_transparency_demonstration_2.png')
        self.assertEqual(self.img3.output_path, 'test_dir\\PNG_transparency_demonstration_2.png')

    def test_data(self):
        print('test_data')

        # img1
        self.img1.image_data()
        self.assertEqual(True, self.img1.is_image)
        self.assertEqual('jpeg', self.img1.image_format)

        # img2
        self.img2.image_data()
        self.assertEqual(True, self.img2.is_image)
        self.assertEqual('jpeg', self.img2.image_format)

        # img3
        self.img3.image_data()
        self.assertEqual(True, self.img3.is_image)
        self.assertEqual('png', self.img3.image_format)


if __name__ == '__main__':
    unittest.main()
