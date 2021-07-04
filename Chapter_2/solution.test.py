"""Solution test suite"""

from functools import reduce
import random
import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    """Solution test class"""

    MAX_AMOUNT_PANELS = 50
    MAX_PANEL_POWER = 50
    MIN_PANEL_POWER = -50

    @staticmethod
    def _multiply(i_list):
        """Returns the product of all integers in the list, excluding zeroes."""
        i_list = list(filter(lambda x: x != 0, i_list))
        return int(reduce(lambda a, b: a * b, i_list))

    def test_solution_all_positive(self):
        self.assertEqual(solution([2, 0, 2, 2, 0]), "8")

    def test_solution_odd_negative_without_zero(self):
        self.assertEqual(solution([-2, -3, 4, -5]), "60")

    def test_solution_even_negative_without_zero(self):
        self.assertEqual(solution([-2, -3, 4, 5]), "30")

    def test_solution_odd_negative_with_zero(self):
        self.assertEqual(solution([-2, -3, 4, -5, 0]), "60")

    def test_solution_even_negative_with_zero(self):
        self.assertEqual(solution([-2, -3, 4, 5, 0]), "120")

    def test_solution_large_numbers(self):
        xs = [12345657687, 1235652345, -512356235, 0, 1283756238456]
        self.assertEqual(solution(xs), "19583625511076864906220956232840")

    def test_solution_random_numbers(self):
        max_panel_power = TestSolution.MAX_PANEL_POWER
        min_panel_power = TestSolution.MIN_PANEL_POWER
        amount_panels = TestSolution.MAX_AMOUNT_PANELS

        for _ in range(100):

            list_of_panels = [
                random.randint(min_panel_power, max_panel_power)
                for _ in range(amount_panels)
            ]

            lists_with_one_panel_excluded = [
                list_of_panels[0:x] + list_of_panels[x + 1 :]
                for x in range(amount_panels)
            ]

            products = [
                TestSolution._multiply(l) for l in lists_with_one_panel_excluded
            ]

            actual = str(max(products))
            expected = solution(list_of_panels)

            try:
                self.assertEqual(actual, expected)
            except AssertionError:
                print(
                    """Assertion failed!
    Input:    {}
    Expected: {}
    Got:      {}
                """.format(
                        list_of_panels, expected, actual
                    )
                )


if __name__ == "__main__":
    unittest.main()
