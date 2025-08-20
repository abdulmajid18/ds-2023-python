
nums = [2,5,2,2,3,3]
def counting_sort(nums):
    l = min(nums)
    r = max(nums)
    freq_range = r - l + 1
    n = len(nums)
    freq = [0] * freq_range

    for i in range(n):
        freq[nums[i] - l] += 1
    sorted_nums = []

    for i in range(freq_range):
        sorted_nums.extend(freq[i] * [i + l])

    return sorted_nums


counting_sort(nums)

def counting_sort_two(nums):
    l = min(nums)
    r = max(nums)
    freq_range = r - l + 1
    n = len(nums)
    freq = [0] * freq_range

    for i in range(n):
        freq[nums[i] - l] += 1

    for i in range(1, freq_range):
        freq[i] = freq[i-1] + freq[i]

    # for i in range(1, freq_range):
    #     freq[i] += freq[i - 1]

    output = [0] * n
    for i in range(n - 1, -1, -1):
        val = nums[i]
        idx = freq[val - l] - 1
        output[idx] = val
        freq[val - l] -= 1

    return output

counting_sort_two(nums)
