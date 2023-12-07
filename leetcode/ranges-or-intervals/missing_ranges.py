def findMissingRanges(nums, lower, upper):
    missing_ranges = []

    # Check if nums is empty or if the first element is greater than lower
    if not nums or nums[0] > lower:
        missing_ranges.append(format_range(lower, nums[0] - 1))

    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 1:
            missing_ranges.append(format_range(nums[i - 1] + 1, nums[i] - 1))

    # Check if the last element is less than upper
    if nums and nums[-1] < upper:
        missing_ranges.append(format_range(nums[-1] + 1, upper))

    return missing_ranges


def format_range(start, end):
    if start == end:
        return str(start)
    else:
        return str(start) + "->" + str(end)




class Solution:
    def get_range(self, start, end):
        if start == end:
            return str(start)
        return str(start) + "->" + str(end)

    def find_ranges(self, elements, start, end):
        ranges = []
        prev = start - 1
        for i in range(len(elements)):
            if i == len(elements):
                cur = end + 1
            else:
                cur = elements[i]
            if cur - prev >= 2:
                ranges.append(self.get_range(prev + 1, cur - 1))
            prev = cur
        return ranges

def findMissingRangesB(nums, lower, upper):
    result = []
    start = lower

    if lower == float('inf'):
        return result

    for i in range(len(nums)):
        # Handle duplicates, e.g., [1,1,1] lower=1 upper=1
        if i < len(nums) - 1 and nums[i] == nums[i + 1]:
            continue

        if nums[i] == start:
            start += 1
        else:
            result.append(getRange(start, nums[i] - 1))
            if nums[i] == float('inf'):
                return result
            start = nums[i] + 1

    if start <= upper:
        result.append(getRange(start, upper))

    return result


def getRange(start, end):
    if start == end:
        return str(start)
    else:
        return str(start) + "->" + str(end)


if __name__ == "__main__":
    # Example usage:
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    result = findMissingRanges(nums, lower, upper)
    print(result)  # Output: ["2", "4->49", "51->74", "76->99"]
    # x = Solution()
    # ans = x.find_ranges(nums, lower, upper)
    # print(ans)