class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        dim = len(matrix)

        for i in range(int(dim / 2)):
            matrix[i], matrix[dim - i - 1] = matrix[dim - i - 1], matrix[i]

        for i in range(dim):
            for j in range(i, dim):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(m)
    assert m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
