import unittest
import os
from package_files_generator.generator import generate, create_dir
import shutil


class Base:
    def remove(self, path: str) -> None:
        if os.path.isdir(path):
            shutil.rmtree(path)


class TestPackaging(unittest.TestCase, Base):
    cases: str

    def setUp(self) -> None:
        path = os.path.dirname(os.path.abspath(__file__))
        self.cases = f"{path}/cases"
        if (not os.path.isdir(self.cases)):
            os.makedirs(self.cases)

    def tearDown(self) -> None:
        shutil.rmtree(f"{self.cases}/test_empty")

    def test_no_directory(self) -> None:
        package_name = "test_empty"
        directory = f"{self.cases}/{package_name}"
        self.assertFalse(os.path.isdir(directory))
        os.makedirs(directory)
        self.assertTrue(os.path.isdir(directory))
        generate(package_name)
        self.assertTrue(os.path.isdir(f"{directory}/src/{package_name}"))
        self.assertTrue(os.path.isdir(f"{directory}/tests"))
        self.assertTrue(os.path.isfile(f"{directory}/LICENSE"))
        self.assertTrue(os.path.isfile(f"{directory}/pyproject.toml"))
        self.assertTrue(os.path.isfile(f"{directory}/README.md"))
        self.assertTrue(os.path.isfile(f"{directory}/src/{package_name}/\
                __init__.py"))


class TestCreateUnits(unittest.TestCase, Base):
    cases: str

    def setUp(self) -> None:
        path = os.path.dirname(os.path.abspath(__file__))
        self.cases = f"{path}/cases"

    def tearDown(self) -> None:
        self.remove(f"{self.cases}/create_dir/test")

    def test_create_dir_no_exists(self) -> None:
        package_name = "create_dir"
        directory = f"{self.cases}/{package_name}"
        self.assertFalse(os.path.isdir(f"{directory}/test"))
        create_dir("test", directory)
        self.assertTrue(os.path.isdir(f"{directory}/test"))

    def test_create_dir_exists(self) -> None:
        package_name = "create_dir"
        directory = f"{self.cases}/{package_name}"
        self.assertTrue(os.path.isdir(f"{directory}/test"))
        create_dir("test", directory)
        self.assertTrue(os.path.isdir(f"{directory}/test"))
