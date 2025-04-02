from typing import List


class SolutionBrute:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Step 1: Copy nums2 into nums1
        for i in range(n):
            nums1[m + i] = nums2[i]

        # Step 2: Sort the entire nums1 array
        nums1.sort()


class SolutionBruteTwo:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = [0] * (m + n)
        j = 0
        i1, i2 = 0, 0

        while i1 < m and i2 < n:
            if nums1[i1] < nums2[i2]:
                res[j] = nums1[i1]
                i1 += 1
            else:
                res[j] = nums2[i2]
                i2 += 1
            j += 1

        while i1 < m:
            res[j] = nums1[i1]
            i1 += 1
            j += 1

        while i2 < n:
            res[j] = nums2[i2]
            i2 += 1
            j += 1

        nums1[:] = res


class SolutionOptimal:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2, k = m - 1, n - 1, m + n - 1

        # Merge from the end
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[k] = nums1[i1]
                i1 -= 1
            else:
                nums1[k] = nums2[i2]
                i2 -= 1
            k -= 1

        # If nums2 has remaining elements, copy them
        while i2 >= 0:
            nums1[k] = nums2[i2]
            i2 -= 1
            k -= 1
