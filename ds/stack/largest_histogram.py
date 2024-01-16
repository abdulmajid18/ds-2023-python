def largestRectangleArea(heights):
    stack = []
    max_area = 0
    i = 0

    while i < len(heights):
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top_index = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, heights[top_index] * width)

    while stack:
        top_index = stack.pop()
        width = i if not stack else i - stack[-1] - 1
        max_area = max(max_area, heights[top_index] * width)

    return max_area


def largestRectangleArea2(heights):
    maxArea = 0
    stack = []  # pair: (index, height)

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > heights:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - 1))
    return maxArea
