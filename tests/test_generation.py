import unittest
import os


class TestPackaging(unittest.TestCase):
    def setUp(self) -> None:
        path = os.path.dirname(os.path.abspath(__file__))
        self.cases = f"{path}/cases"
        if (not os.path.isdir(self.cases)):
            os.makedirs(self.cases)

    def test_no_directory(self) -> None:
        dir = f"{self.cases}/empty"
        self.assertFalse(os.path.isdir(dir))
        os.makedirs(dir)
        self.assertTrue(os.path.isdir(dir))
