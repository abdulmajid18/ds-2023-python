class Solution:

    def find_min(self, nums):
        l = 0
        r = len(nums) - 1

        while l <= r:

            while nums[l] == nums[r] and l != r:
                l += 1
            if nums[l] <= nums[r]:
                return nums[l]

            mid = (l + r) // 2
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


def main():
    nums = [5, 6, 7, 1, 2, 3, 4]
    solution = Solution()
    print(solution.find_min(nums))



if __name__ == '__main__':
    main()
