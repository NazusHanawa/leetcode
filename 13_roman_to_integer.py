class Solution:
    def romanToInt(self, s: str) -> int:
        roman_value = {
            "I": 1, 
            "V": 5, 
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        lenght = len(s) - 1
        decimal_value = roman_value[s[-1]]

        for i in range(lenght):
            value = roman_value[s[i]]
            next_value = roman_value[s[i+1]]

            if value >= next_value:
                decimal_value += value
            else:
                decimal_value -= value

        return decimal_value