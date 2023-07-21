from unittest import TestCase
import two_sum


class Test(TestCase):
    def test_two_sum(self):
        solution = two_sum.TwoSum()
        target = 7
        nums = [1, 3, 2, -7, 5]
        expected = [3, 5]
        self.assertEqual(solution.two_brute_force(nums, target), expected)
        self.assertEqual(solution.two_sum_hashtable(nums, target), expected)
        print('Success: test_two_sum')

