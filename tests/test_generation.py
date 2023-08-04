from math import log10
from math import log10
import unittest
import os
from package_files_generator.generator import create_dir
from package_files_generator.generator import generate
from package_files_generator.generator import get_final_path
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
            os.mkdir(self.cases)

    def tearDown(self) -> None:
        shutil.rmtree(f"{self.cases}/test_empty")

    def test_no_directory(self) -> None:
        package_name = "test_empty"
        directory = f"{self.cases}/{package_name}"
        self.assertFalse(os.path.isdir(directory))
        os.mkdir(directory)
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
        if not os.path.isdir(self.cases):
            os.mkdir(self.cases)

    def test_create_dir_no_exists(self) -> None:
        current = "create_dir_no_exists"
        directory = f"{self.cases}/{current}"
        self.assertFalse(os.path.isdir(directory))
        create_dir(current, self.cases)
        self.assertTrue(os.path.isdir(directory))
        self.remove(f"{self.cases}/{current}")

    def test_create_dir_exists(self) -> None:
        current = "create_dir_exists"
        self.assertTrue(os.path.isdir(self.cases))
        directory = f"{self.cases}/{current}"
        if not os.path.isdir(directory):
            os.mkdir(directory)
        create_dir(current, self.cases)
        self.assertTrue(os.path.isdir(directory))

    def test_create_double_dir(self) -> None:
        current = "create_dir_double"
        directory = f"{self.cases}/{current}"
        self.assertFalse(os.path.isdir(directory))
        create_dir("test", directory)
        self.assertTrue(os.path.isdir(f"{directory}/test"))
        self.remove(directory)

    @unittest.skip("Need to have the file checker")
    def test_create_empty_file(self) -> None:
        current = "create_empty_file"
        directory = f"{self.cases}/{current}"
        create_dir(directory)
        raise NotImplementedError("Need to have the file checker")


# class TestFileContents(unittest.TestCase):
#     raise NotImplementedError


class TestUtils(unittest.TestCase):
    primary: str
    secondary: str

    def setUp(self) -> None:
        self.primary = "primary"
        self.secondary = "secondary"

    def test_primary(self) -> None:
        self.assertEqual(get_final_path(self.primary, None), "primary")
        self.assertEqual(get_final_path(self.primary, ""), "primary")

    def test_both(self) -> None:
        self.assertEqual(
                get_final_path(self.primary, self.secondary),
                "secondary/primary"
            )

    def test_incorrect(self) -> None:
        with self.assertRaises(TypeError):
            get_final_path(extra=self.secondary)

        with self.assertRaises(ValueError):
            get_final_path("", self.secondary)

        with self.assertRaises(ValueError):
            get_final_path("", None)
