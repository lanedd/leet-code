class Solution:
    def romanToInt(self, s: str) -> int:
        special = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer = 0
        index = 0
        index_alt = 2
        while index < len(s):
            if index_alt <= len(s):
                value = special.get(s[index:index_alt])
                if value is not None:
                    integer += value
                    index += 2
                    index_alt += 2
                    continue
            integer += mapping[s[index]]
            index += 1
            index_alt += 1
        return integer

    # def romanToInt(self, s: str) -> int:
    #     special = [("IV", 4), ("IX", 9), ("XL", 40), ("XC", 90), ("CD", 400), ("CM", 900)]
    #     mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    #     integer = 0
    #     for letters, value in reversed(special):
    #         index = s.find(letters)
    #         if index != -1:
    #             integer += value
    #             s = s[:index] + s[index + 2:]
    #     integer += sum([mapping[x] for x in s])
    #     return integer


# s = "XIVt"
# index = s.find("IV")
# s = s[:index] + s[index + 2:]
print(Solution().romanToInt("MCMXCIV"))

