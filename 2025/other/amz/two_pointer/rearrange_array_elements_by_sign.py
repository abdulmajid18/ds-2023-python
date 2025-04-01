from typing import List


class SolutionBruteForce:
    def rearrangeArrayOne(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []

        # Separate positives and negatives
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)

        # Merge in alternating order
        result = []
        for i in range(len(positives)):
            result.append(positives[i])
            result.append(negatives[i])

        return result

    def rearrangeArrayTwo(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []

        # Separate positives and negatives
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)

        # Merge in alternating order and append to nums
        index = 0
        for i in range(len(positives)):
            nums[index] = positives[i]
            index += 1
            nums[index] = negatives[i]
            index += 1

        return nums


# Example Usage
nums = [3, 1, -2, -5, 2, -4]
sol = SolutionBruteForce()
print(sol.rearrangeArray(nums))  # Output: [3, -2, 1, -5, 2, -4]

from typing import List


class SolutionOptimal:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        res = [0] * len(nums)

        for k in range(len(nums)):
            if nums[k] > 0:
                res[i] = nums[k]
                i += 2
            else:
                res[j] = nums[k]
                j += 2

        return res

