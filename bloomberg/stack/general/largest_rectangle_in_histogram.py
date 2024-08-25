def largestRectangleArea(heights):
    # Add sentinel values to facilitate the algorithm ie edge cases
    heights = [0] + heights + [0]
    print(heights)
    stack = []
    max_area = 0

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1  # Calculate the width of the rectangle
            max_area = max(max_area, h * w)
        stack.append(i)

    return max_area


# Example usage
heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))  # Output: 10
