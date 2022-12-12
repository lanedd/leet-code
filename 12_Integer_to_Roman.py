class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = [
            ("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10), ("XL", 40), ("L", 50),
            ("XC", 90), ("C", 100), ("CD", 400), ("D", 500), ("CM", 900), ("M", 1000)
        ]
        numerals = list()
        for letter, value in reversed(mapping):
            qty = num // value
            if qty > 0:
                numerals.extend([letter] * qty)
                num = num % value
        numerals = "".join(numerals)
        return numerals


for i in range(100):
    print(f"{i} -> {Solution().intToRoman(i)}")

i = 1994
print(f"{i} -> {Solution().intToRoman(i)}")