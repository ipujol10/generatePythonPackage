import unittest
import re
from package_files_generator.regex import starts_with
from package_files_generator.regex import separate_equal
from package_files_generator.regex import ends_with
from package_files_generator.regex import clean_end_list
from package_files_generator.regex import clean_start
from package_files_generator.regex import prepare_list_item
from package_files_generator.regex import is_title
from package_files_generator.regex import get_title


class TestRegex(unittest.TestCase):
    def setUp(self) -> None:
        self.sentence = "A dog can dig"

    def test_find_all(self) -> None:
        self.assertEqual(re.findall(r"d\wg", self.sentence), ["dog", "dig"])
        self.assertEqual(re.findall("\"", self.sentence), [])

    def test_search(self) -> None:
        self.assertTrue(re.search(r"\s", self.sentence))
        self.assertFalse(re.search(r"\s{2,}", self.sentence))
        search = re.search(r"\s", self.sentence)
        position = -1 if search is None else search.start()
        self.assertEqual(position, 1)

    def test_split(self) -> None:
        self.assertEqual(
                re.split(r"\s", self.sentence), ["A", "dog", "can", "dig"])
        self.assertEqual(
                re.split(r"\s", self.sentence, 1), ["A", "dog can dig"])

    def test_sub(self) -> None:
        self.assertEqual(re.sub(r"\s", "9", self.sentence), "A9dog9can9dig")
        self.assertEqual(re.sub(r"\s", "9", self.sentence, 2), "A9dog9can dig")


class TestOwnRegex(unittest.TestCase):
    def setUp(self) -> None:
        self.sentence = "[project]"

    def test_starts_with(self) -> None:
        self.assertTrue(starts_with(r"\[", self.sentence))  # ]
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
        self.assertTrue(ends_with(r"\]", self.sentence))
        self.assertFalse(ends_with("t", self.sentence))
        self.assertTrue(ends_with(r"[\]\}]", self.sentence))

    def test_clean_end_list(self) -> None:
        self.assertEqual(clean_end_list("asdsa,   "), "asdsa")
        self.assertEqual(clean_end_list("asdsa"), "asdsa")
        self.assertEqual(clean_end_list("a b c, "), "a b c")

    def test_clean_start(self) -> None:
        self.assertEqual(
                clean_start("      asdsad asd     "),
                "asdsad asd     "
                )
        self.assertEqual(clean_start("\"as\""), "\"as\"")

    def test_prepare_list_item(self) -> None:
        self.assertEqual(
                prepare_list_item("asds, asd, bds, "),
                "asds, asd, bds, "
                )
        self.assertEqual(prepare_list_item("a"), "a, ")
        self.assertEqual(prepare_list_item("a,      "), "a, ")

    def test_is_title(self) -> None:
        self.assertTrue(is_title("[asdasd]"))
        self.assertTrue(is_title("         [asdas]        "))
        self.assertFalse(is_title("[asdasd"))  # ]
        self.assertFalse(is_title("asdsa]"))
        self.assertFalse(is_title("]"))

    def test_get_title(self) -> None:
        self.assertEqual(get_title("[asd]"), "[asd]")
        self.assertEqual(get_title("    [asd]      "), "[asd]")
