import unittest
from boyer_moore_algorithm import BoyerMoore


class Test(unittest.TestCase):

    def test(self):
        input_string = BoyerMoore("Boyer–Moore string-search algorithm is an efficient string-searching algorithm"
                                  "that is the standard benchmark for practical string-search literature")
        self.assertEqual(input_string.boyer_moore_search("efficient"), [42])
        self.assertEqual(input_string.boyer_moore_search("that"), [78])

        input_string = BoyerMoore("Harharharhardhardhardhard")
        self.assertEqual(input_string.boyer_moore_search("hard"), [9, 13, 17, 21])
        self.assertEqual(input_string.boyer_moore_search("har"), [3, 6, 9, 13, 17, 21])


if __name__ == '__main__':
    unittest.main()
