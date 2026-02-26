class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        max_str = []
        unique_str = set()

        for i, char in enumerate(s):
            if char in unique_str:
                char_index = max_str.index(char)
                for unique_char in max_str[:char_index]:
                    unique_str.remove(unique_char)
                max_str = max_str[char_index+1:]
            else:
                unique_str.add(char)

            max_str.append(char)
            
            if len(max_str) > result:
                result = len(max_str)

        return result
