import unittest
import re


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
