import os
import random
import string
import unittest

from guolei_py3_images.imgkit import str_to_image
from guolei_py3_images.v1.imgkit import string_to_image


class MyTestCase(unittest.TestCase):
    def test_something(self):

        output_path = string_to_image(
            output_path=os.path.join(os.path.dirname(__file__), "runtime", 'test.png'),
            string="".join(random.choices(string.ascii_letters,k=100))
        )
        print(output_path)
        self.assertTrue(True, "test failed")  # add assertion here


if __name__ == '__main__':
    unittest.main()
