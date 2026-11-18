class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        rows: list = [[1]]
        for i in range(1, numRows):
            pre_row = rows[i - 1]
            curr_row = [1]*(i + 1)
            for j in range(1, i):
                curr_row[j] = pre_row[j - 1] + pre_row[j]
            rows.append(curr_row)
        return rows