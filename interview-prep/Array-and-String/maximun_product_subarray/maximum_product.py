class Solution:

    def find_product(self, elems):
        max_here = elems[0]
        min_here = elems[0]
        max_so_far = elems[0]

        for i in range(1, len(elems)):
            mx = max_here
            mn = min_here

            max_here = max(max(elems[i], mx * elems[i]), mn * elems[i])
            min_here = min(min(elems[i], mx * elems[i]), mn * elems[i])
            max_so_far = max(max_here, max_so_far)
        return max_so_far










def main():
    solution = Solution()
    elems =  [2, 1,-3, 4,-1, 2, 1,-5,4]
    ans = solution.find_sum(elems)
    print(ans)


if __name__ == "__main__":
    main()