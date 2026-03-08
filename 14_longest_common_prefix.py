class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for string in strs[1:]:
            prefix_lenght = len(prefix)
            if prefix == string[:prefix_lenght]:
                continue

            while True:
                prefix = prefix[:-1]
                prefix_lenght = len(prefix)
                if prefix == "":
                    return ""
                elif prefix == string[:prefix_lenght]:
                    break

        return prefix