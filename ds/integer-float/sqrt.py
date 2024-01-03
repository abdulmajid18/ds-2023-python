def mySqrt(x):
    if x == 0:
        return 0

    left, right = 1, x
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right  # When we exit the loop, right will be the floor(sqrt(x))


# Example usage:
result = mySqrt(8)
print(result)
