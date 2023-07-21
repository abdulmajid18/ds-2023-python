from unittest import TestCase
import coin_change, coin_change_recursion


class TestCoinChangeRecursion(TestCase):
    def test_coin_change(self):
        coins = [1,3,4]
        target = 10
        expected = 3
        solution = coin_change.Solution()
        solution_recursion = coin_change_recursion.CoinChangeRecursion()
        self.assertEqual(solution.coin_change_dp(coins, target), 3)
        self.assertEqual(solution_recursion.coin_change(coins, target), 3)

