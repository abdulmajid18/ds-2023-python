def product_except_itself(nums):
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res


def product_except_self_bruteforce(nums):
    output = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        output.append(product)
    return output


def productExceptSelf(nums):
    n = len(nums)
    result = [0] * n

    # Initialize the result array with 1 at the end.
    result[n - 1] = 1

    # Calculate the right products for each element.
    for i in range(n - 2, -1, -1):
        result[i] = result[i + 1] * nums[i + 1]

    left = 1

    # Update the result array with the left products and right products.
    for i in range(n):
        result[i] = result[i] * left
        left = left * nums[i]

    return result


# Example usage:
nums = [1, 2, 3, 4]
result = productExceptSelf(nums)
print(result)  # Output: [24, 12, 8, 6]
