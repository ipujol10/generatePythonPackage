import unittest
import re
from package_files_generator.regex import starts_with
from package_files_generator.regex import separate_equal
from package_files_generator.regex import ends_with


class TestRegex(unittest.TestCase):
    def setUp(self) -> None:
        self.sentence = "A dog can dig"

    def test_find_all(self) -> None:
        self.assertEqual(re.findall("d\wg", self.sentence), ["dog", "dig"])
        self.assertEqual(re.findall("\"", self.sentence), [])

    def test_search(self) -> None:
        self.assertTrue(re.search("\s", self.sentence))
        self.assertFalse(re.search("\s{2,}", self.sentence))
        search = re.search("\s", self.sentence)
        position = -1 if search is None else search.start()
        self.assertEqual(position, 1)

    def test_split(self) -> None:
        self.assertEqual(
                re.split("\s", self.sentence), ["A", "dog", "can", "dig"])
        self.assertEqual(
                re.split("\s", self.sentence, 1), ["A", "dog can dig"])

    def test_sub(self) -> None:
        self.assertEqual(re.sub("\s", "9", self.sentence), "A9dog9can9dig")
        self.assertEqual(re.sub("\s", "9", self.sentence, 2), "A9dog9can dig")


class TestOwnRegex(unittest.TestCase):
    def setUp(self) -> None:
        self.sentence = "[project]"

    def test_starts_with(self) -> None:
        self.assertTrue(starts_with("\[", self.sentence))  # ]
        self.assertFalse(starts_with("p", self.sentence))

    def test_separate_equal(self) -> None:
        self.assertEqual(
                separate_equal("name = \"package_files_generator\""),
                ["name", "\"package_files_generator\""]
                )
        self.assertEqual(
                separate_equal(
                    "\"Homepage\" = "
                    "\"https//:something.com/123isahd=123nasbd=\""
                    ),
                [
                    "\"Homepage\"",
                    "\"https//:something.com/123isahd=123nasbd=\""
                    ]
                )
        self.assertEqual(
                separate_equal("desc = \"Something = Something\""),
                ["desc", "\"Something = Something\""]
                )

    def test_ends_with(self) -> None:
        self.assertTrue(ends_with("\]", self.sentence))
        self.assertFalse(ends_with("t", self.sentence))
