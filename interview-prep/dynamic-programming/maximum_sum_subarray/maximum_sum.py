class Solution:

    def find_sum(self, elems):
        max_here = elems[0]
        max_so_far = elems[0]

        for i in range(1, len(elems)):
             max_here = max(max_here + elems[i], elems[i])
             max_so_far = max(max_here, max_so_far)
        return max_so_far

    def find_sum_2(self, elems):
        result = elems[0]
        sum = elems[0]

        for i in range(1, len(elems)):
            if sum <= 0:
                sum = elems[0]
            else:
                sum += elems[i]
            result = max(result, sum)

        return result


    def find_sum_3(self, elems):
        max = elems[0]
        sum = [] * len(elems)
        sum[0] = 0

        for i in range(1, len(elems)):
            sum[i] = max(elems[i], sum[i-1] + elems[i])
            max = max(max, elems[i])

        return max







def main():
    solution = Solution()
    elems =  [2, 1,-3, 4,-1, 2, 1,-5,4]
    ans = solution.find_sum(elems)
    print(ans)


if __name__ == "__main__":
    main()