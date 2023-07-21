from unittest import TestCase
import valid_palindrome


class TestSolution(TestCase):
    def test_is_valid_palindrome(self):
        solution = valid_palindrome.Solution()
        input = "A man, a plan, a canal: Panama"
        expected = True
        self.assertTrue(solution.is_valid_palindrome(input))

