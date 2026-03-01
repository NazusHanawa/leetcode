class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ["" for row in range(numRows)]
        
        rows_map = []
        for i in range(numRows):
            rows_map.append(i)
        for i in range(numRows-2,0,-1):
            rows_map.append(i)
        
        n = len(rows_map)
        for i, char in enumerate(s):
            row_i = rows_map[i % n]
            rows[row_i] += char

        result = ""
        for row in rows:
            result += row
        return result