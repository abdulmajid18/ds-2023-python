"""Problem Statement: The problem asks us to find the next lexicographical permutation of a given array of integers.
In simpler terms, we need to rearrange the numbers to get the smallest possible permutation that is greater than the
current one. If the array is sorted in descending order (i.e., it's the largest possible permutation), then we return
the smallest permutation by sorting the array in ascending order.

Example: For instance, if the input array is [1, 2, 3], the next permutation would be [1, 3, 2]. However,
if the input is [3, 2, 1], the array is already the largest permutation, so the result should be [1, 2, 3].

Approach:
The problem can be broken down into a few logical steps:

Identify the Pivot:

First, I traverse the array from right to left to find the first element that is smaller than the element next to it.
This element is crucial because it marks where the array stops increasing and starts decreasing. This is the "pivot"
where the next permutation change needs to occur. For example, in the array [1, 2, 3], the pivot is at index 1 where
the value is 2 because 2 < 3. Find the Rightmost Successor to Swap:

Next, I need to find the smallest element on the right side of the pivot that is larger than the pivot value. This
ensures that when we swap these two values, we get the next greater permutation. In the same example, the rightmost
successor for 2 is 3. Swap the Pivot and Successor:

After identifying the rightmost successor, I swap it with the pivot. This gives us the next permutation, but it might
not be the smallest possible permutation after the swap. Swapping in our example results in [1, 3, 2]. Reverse the
Suffix:

Finally, to ensure we get the smallest permutation after the swap, I reverse the part of the array that comes after
the pivot. Since this part was originally in decreasing order, reversing it puts it in ascending order, making the
permutation as small as possible. In our example, since there’s only one element after 3, no reversal is needed,
and the result is [1, 3, 2]."""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        for k in range(len(nums) - 2, -1, -1):
            if nums[k] < nums[k + 1]:
                i = k
                break

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1:] = reversed(nums[i + 1:])