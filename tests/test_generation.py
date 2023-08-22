import unittest
import datetime
import os
from package_files_generator.generator import create_dir
from package_files_generator.generator import generate
from package_files_generator.generator import get_final_path
from package_files_generator.generator import get_file_content
from package_files_generator.generator import create_file
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
        generate(package_name, "ipujol10")
        self.assertTrue(os.path.isdir(f"{directory}/src/{package_name}"))
        self.assertTrue(os.path.isdir(f"{directory}/tests"))
        self.assertTrue(os.path.isfile(f"{directory}/LICENSE"))
        self.assertEqual(
                get_file_content("LICENSE", directory),
                self.right_license().split("\n")
            )
        self.assertTrue(os.path.isfile(f"{directory}/pyproject.toml"))
        self.assertTrue(os.path.isfile(f"{directory}/README.md"))
        self.assertTrue(os.path.isfile(f"{directory}/src/{package_name}/\
                __init__.py"))

    def right_license(self) -> str:
        year = datetime.datetime.now().year
        return f"""MIT License

Copyright (c) {year} ipujol10

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


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

    def test_create_empty_file(self) -> None:
        current = "create_empty_file"
        directory = f"{self.cases}/{current}"
        create_dir(directory)
        create_file("empty.txt", directory=directory)
        self.assertEqual(get_file_content("empty.txt", directory), [])
        file = f"{directory}/empty.txt"
        os.remove(file)
        self.assertFalse(os.path.isfile(file))

    def test_create_file(self) -> None:
        current = "create_file"
        directory = f"{self.cases}/{current}"
        create_dir(directory)
        create_file("test.txt", "test1\ntest2", directory)
        self.assertEqual(
                get_file_content("test.txt", directory), ["test1", "test2"]
            )
        file = f"{directory}/test.txt"
        os.remove(file)
        self.assertFalse(os.path.isfile(file))


class TestFileContents(unittest.TestCase):
    def setUp(self) -> None:
        self.files = "tests/files"
        if not os.path.isdir(self.files):
            os.mkdir(self.files)

    def test_empty_file(self) -> None:
        contents = get_file_content("empty.txt", self.files)
        self.assertEqual(contents, [])

    def test_not_empty(self) -> None:
        contents = get_file_content("not_empty.txt", self.files)
        self.assertEqual(contents, ["123", "abc", "test"])


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
