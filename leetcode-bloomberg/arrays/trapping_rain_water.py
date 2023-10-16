def solutionOne(nums):
    maxRight = [0] * len(nums)
    maxLeft = [0] * len(nums)
    minLeftRight = [0] * len(nums)

    leftMax = 0
    for i in range(1, len(nums)):
        leftMax = max(leftMax, nums[i-1])
        maxLeft[i] = leftMax

    rightMax = 0
    for j in range(len(nums)-2, -1, -1):
        rightMax = max(rightMax, nums[j + 1])
        maxRight[j] = rightMax

    for k in range(len(nums)):
        minLeftRight[k] = min(maxRight[k], maxLeft[k])

    trappedWater = 0
    for i in range(len(nums)):
        trapped = minLeftRight[i] - nums[i]
        if trapped >= 0:
            trappedWater += trapped

    print(maxLeft)
    print(maxRight)
    print(minLeftRight)
    print(trappedWater)

def solutionTwoPointer(height):
    if not height:
        return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]

    return res

if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    solutionOne(height)
