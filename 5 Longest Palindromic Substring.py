class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal_len = 0
        max_pal_str = ""
        for i in range(len(s)):
            pal_len, pal_str = pal_check(s, i, i + 1, 0)
            if pal_len > max_pal_len:
                max_pal_len = pal_len
                max_pal_str = pal_str
            pal_len, pal_str = pal_check(s, i - 1, i + 1, 1)
            if pal_len > max_pal_len:
                max_pal_len = pal_len
                max_pal_str = pal_str
        return max_pal_str


def pal_check(s: str, i: int, j: int, pal_len: int) -> tuple:
    while i >= 0 and j < len(s):
        if s[i] == s[j]:
            pal_len += 2
            i -= 1
            j += 1
        else:
            break
    i += 1
    # j -= 1
    if pal_len == 0:
        pal_str = ""
    elif pal_len == 1 and i + 1 < len(s):
        pal_str = s[i + 1]
    else:
        pal_str = s[i: j]
    return pal_len, pal_str


obj = Solution()
my_input = "babad"
output = obj.longestPalindrome(my_input)
print(output)


