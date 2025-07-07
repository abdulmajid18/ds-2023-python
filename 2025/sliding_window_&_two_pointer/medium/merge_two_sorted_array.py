def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


def mergeBruteForce(nums1, m, nums2, n):
    merged = []
    i = j = 0

    while i < m and j < n:
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    while i < m:
        merged.append(nums1[i])
        i += 1

    while j < n:
        merged.append(nums2[j])
        j += 1

    # Copy back into nums1
    for i in range(m + n):
        nums1[i] = merged[i]
