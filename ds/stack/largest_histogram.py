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
