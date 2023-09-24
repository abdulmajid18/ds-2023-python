def longest_1(string):
    char_set = set()
    l = 0
    res = 0

    for r in range(len(string)):
        while string[r] in char_set:
            char_set.remove(string[l])
            l += 1
        char_set.add(string[r])
        res = max(res, r - l + 1)
    return res;


def longest_2(string):
    char_set = set()

# public int lengthOfLongestSubstring(String s) {
#  boolean[] exist = new boolean[256];
#  int i = 0, maxLen = 0;
#  for (int j = 0; j < s.length(); j++) {
#  while (exist[s.charAt(j)]) {
#  exist[s.charAt(i)] = false;
#  i++;
#  }
#  exist[s.charAt(j)] = true;
#  maxLen = Math.max(j - i + 1, maxLen);
#  }
#  return maxLen;
# }
