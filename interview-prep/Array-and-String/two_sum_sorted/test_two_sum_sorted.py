from unittest import TestCase
import two_sum_sorted


class TestTwoSumSorted(TestCase):
    def test_two_sum_bsearch(self):
        solution = two_sum_sorted.TwoSumSorted()
        target = 9

        nums = sorted([2,7,11,15])
        expected = [1, 2]
        self.assertEqual(solution.two_sum_bsearch(nums, target), expected)
        self.assertEqual(solution.two_sum_bsearch_two(nums, target), expected)
        print('Success: test_two_sum')
