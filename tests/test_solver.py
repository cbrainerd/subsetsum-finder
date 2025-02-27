import unittest

from subsetsum_finder import combination_sum


class TestCombinationSum(unittest.TestCase):
    def test_basic_case(self):
        self.assertCountEqual(combination_sum([2, 3, 6, 7], 7), [[7]])

    def test_multiple_combinations(self):
        self.assertCountEqual(
            combination_sum([10, 1, 2, 7, 6, 1, 5], 8),
            [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
        )

    def test_repeated(self):
        self.assertCountEqual(
            combination_sum(
                [
                    1,
                    1,
                    1,
                ],
                3,
            ),
            [[1, 1, 1]],
        )

    def test_no_valid_combination(self):
        self.assertCountEqual(combination_sum([3, 5, 9], 2), [])

    def test_zero_target(self):
        self.assertCountEqual(combination_sum([1, 2, 3], 0), [[]])

    def test_duplicates_in_input(self):
        self.assertCountEqual(combination_sum([4, 4, 4, 1, 2], 5), [[1, 4]])
