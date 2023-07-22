import unittest
import os
from package_files_generator.generator import generate
import shutil


class TestPackaging(unittest.TestCase):
    def setUp(self) -> None:
        path = os.path.dirname(os.path.abspath(__file__))
        self.cases = f"{path}/cases"
        if (not os.path.isdir(self.cases)):
            os.makedirs(self.cases)

    def tearDown(self) -> None:
        shutil.rmtree(f"{self.cases}/test_empty")

    def test_no_directory(self) -> None:
        package_name = "test_empty"
        dir = f"{self.cases}/{package_name}"
        self.assertFalse(os.path.isdir(dir))
        os.makedirs(dir)
        self.assertTrue(os.path.isdir(dir))
        generate(package_name)
        self.assertTrue(os.path.isdir(f"{dir}/src/{package_name}"))
        self.assertTrue(os.path.isdir(f"{dir}/tests"))
        self.assertTrue(os.path.isfile(f"{dir}/LICENSE"))
        self.assertTrue(os.path.isfile(f"{dir}/pyproject.toml"))
        self.assertTrue(os.path.isfile(f"{dir}/README.md"))
        self.assertTrue(os.path.isfile(f"{dir}/src/{package_name}/\
                __init__.py"))
