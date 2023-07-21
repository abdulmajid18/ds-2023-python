""" Given an array of integers, find two numbers such that they add up to a specific target
number.
The function twoSum should return indices of the two numbers such that they add up to
the target, where index1 must be less than index2. Please note that your returned answers
(both index1 and index2) are not zero-based"""


class TwoSum:
    def two_brute_force(self, elements: list, target: int):
        for i in range(len(elements)):
            for j in range(len(elements)):
                if i == j:
                    continue
                number = abs(target - elements[i])
                if elements[j] == number:
                    return [i+1, j+1]

    def two_sum_hashtable(self, elements: list, target: int):
        hash_map = {}
        for index, value in enumerate(elements):
            cache_number = target - value
            if cache_number in hash_map:
                return [hash_map[cache_number]+1, index+1]
            else:
                hash_map[value] = index
        return None


