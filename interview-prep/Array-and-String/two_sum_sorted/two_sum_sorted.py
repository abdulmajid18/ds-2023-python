class TwoSumSorted:

    def bsearch(self, elements, begin, target):
        left = begin
        right = len(elements)-1

        while left < right:
            mid = (left + right) // 2
            if elements[mid] < target:
                left = mid + 1
            else:
                right = mid
        if left == right and elements[left] == target:
            return left
        else:
            return -1



    def two_sum_bsearch_two(self, elements, target):
        for i in range(len(elements)):
            index_2 = self.bsearch(elements, i+1, target-elements[i])
            if index_2 != -1:
                return [i+1, index_2+1]
        return None



    def two_sum_bsearch(self, elements, target):
        left = 0
        right = len(elements) - 1

        while left < right:
            sum = elements[left] + elements[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left+1, right+1]

