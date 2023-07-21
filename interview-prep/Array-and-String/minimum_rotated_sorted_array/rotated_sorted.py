class Solution:
    def find_min(self, nums: list[int]):
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] < nums[l]:
                r = mid - 1
            else:
                l = mid + 1
        return res

    def find_min_2(self, nums):
        l = 0
        r = len(nums) - 1

        while l < r and nums[l] > nums[r]:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

    def find_min_3(self, nums):
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]

            mid = (l + r) // 2
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid
        return nums[l]






def main():
    nums =  [5,6,7,1,2,3,4]
    solution = Solution()
    print(solution.find_min_2(nums))
    print(solution.find_min(nums))
    print(solution.find_min_3(nums))

if __name__ == '__main__':
    main()