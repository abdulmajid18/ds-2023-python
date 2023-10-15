"""
There are N children standing in a line. Each child is assigned a rating value. You are giving candies to these
children subjected to the following requirements:
1. Each child must have at least one candy. 2. Children with a higher rating get more candies than their
neighbors.
What is the minimum candies you must give?

"""

def candy(ratings):
    arr = [1] * len(ratings)

    for i in range(1, len(ratings)):
        if ratings[i-1] < ratings[i]:
            arr[i] += arr[i-1] + 1

    for i in range(len(ratings)-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            arr[i] = max(arr[i], arr[i+1] + 1)

    return sum(arr)