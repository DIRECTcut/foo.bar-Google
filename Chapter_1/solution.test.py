"""Solution test suite"""

import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    """Solution test class"""

    def test_solution(self):
        values = [
            (
                "The quick brown fox jumps over the lazy dog",
                "000001011110110010100010000000111110101001010100100100101000000000110000 \
                1110101010100101111011100000001101001010101011010000000101101010011011001 \
                1110001110000000010101011100110001011101000000001111011001010001000000011 \
                1000100000101011101111000000100110101010110110",
            ),
            ("code", "100100101010100110100010"),
            ("Braille", "000001110000111010100000010100111000111000100010"),
        ]

        for list_of_panels, expected in values:
            actual = solution(list_of_panels)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
