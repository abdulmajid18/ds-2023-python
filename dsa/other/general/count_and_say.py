class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        def get_next_sequence(s):
            result = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                result.append(str(count) + s[i])
                i += 1
            return ''.join(result)

        current_sequence = "1"
        for i in range(2, n + 1):
            print("In range " + str(i) + " With string  " + current_sequence)
            current_sequence = get_next_sequence(current_sequence)

        return current_sequence


s = Solution()
print(s.countAndSay(4))


# def get_next_sequence(s):
#     result = []
#     i = 0
#     while i < len(s):
#         count = 1
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             i += 1
#             count += 1
#         result.append(str(count) + s[i])
#         i += 1
#     return ''.join(result)
#
#
# #
# #
# print("******************************")
# a = get_next_sequence("11")
# print(a)
