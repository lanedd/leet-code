class Solution:
    def convert(self, s: str, numRows: int) -> str:
        letter_i = 0
        lists = ["" for x in range(numRows)]
        while letter_i < len(s):
            for list_i in range(numRows):
                lists[list_i] += s[letter_i]
                letter_i += 1
                if letter_i >= len(s):
                    break
            if letter_i >= len(s):
                break
            for list_i in range(numRows-2, 0, -1):
                lists[list_i] += s[letter_i]
                letter_i += 1
                if letter_i >= len(s):
                    break
        combined_list = ""
        for sub_list in lists:
            combined_list += sub_list
        return combined_list


my_string = "PAYPALISHIRING"
rows = 3
obj = Solution()
answer = Solution().convert(my_string, rows)
print(answer)

