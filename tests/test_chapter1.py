import sys
import unittest

sys.path.append("../")

from scripts.chapter1_array_and_strings import check_all_charac_unique


class TestChapter1Methods(unittest.TestCase):
    """ Tests for all chapter 1 methods """

    def test_check_all_charac_unique(self):
        """ check that the function returns True when all characs are unique, and check that returns
        false when they are not """

        string_unique = "abcdefgh"
        string_not_unique = "aaacssdcsdgdsg"

        self.assertEqual(check_all_charac_unique(string_unique), True)
        self.assertEqual(check_all_charac_unique(string_not_unique), False)
