from typing import List


def threeSumBrute(nums: List[int]):
    three_sums = {}
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    sorted_answer = sorted([nums[i], nums[j], nums[k]])
                    three_sums[str(sorted_answer)] = [nums[i], nums[j], nums[k]]
    return three_sums.values()


def threeSum(nums):
    nums.sort()  # Sort the input list in ascending order
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates to avoid duplicate triplets

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1  # Skip duplicates on the left
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1  # Skip duplicates on the right

                left += 1
                right -= 1

    return result


def threeSum2(self, nums: List[int]) -> List[List[int]]:
    sorted_nums = sorted(nums)
    three_sums = []
    for i in range(len(sorted_nums)):
        # avoid duplicates
        if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
            continue
        target = -sorted_nums[i]
        l, r = i + 1, len(sorted_nums) - 1
        while l < r:
            if sorted_nums[l] + sorted_nums[r] == target:
                three_sums.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                l += 1
                # avoid duplicates again
                while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                    l += 1
            elif sorted_nums[l] + sorted_nums[r] < target:
                l += 1
            else:
                r -= 1
    return three_sums

def threeSum3(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1

        while j < k:
            if k < len(nums) - 1 and nums[k] == nums[k + 1]:
                k -= 1
                continue

            if nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

    return result


# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))

if __name__ == '__main__':
    for i in range(20, 5):
        print(i)
