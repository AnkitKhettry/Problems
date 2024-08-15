"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""


class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        set_rows = set()
        set_cols = set()

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == 0:
                    set_rows.add(i)
                    set_cols.add(j)

        for idx in set_rows:
            row_with_all_zeroes = [0 for x in range(num_cols)]
            matrix[idx] = row_with_all_zeroes

        for idx in set_cols:
            for i in range(num_rows):
                matrix[i][idx] = 0


if __name__ == "__main__":
    s = Solution()
    m1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    s.setZeroes(m1)
    assert m1 == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    m2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s.setZeroes(m2)
    assert m2 == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
