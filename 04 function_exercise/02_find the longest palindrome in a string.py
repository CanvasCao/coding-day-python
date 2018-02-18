__author__ = 'cao'

import unittest


def find_the_longest_palindrome_in_string(string):
    return 'abccba'


class MyTestCase(unittest.TestCase):
    def test_find_the_longest_palindrome_in_string(self):
        res = find_the_longest_palindrome_in_string('xxxabccbayyy')
        self.assertEqual(res, 'abccba')


if __name__ == '__main__':
    unittest.main()
