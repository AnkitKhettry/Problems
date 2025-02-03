class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        num_rows = len(grid)
        num_cols = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        from collections import deque
        num_islands = 0

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == '1':
                    num_islands+=1
                    queue = deque([(i, j)])
                    while queue:
                        x , y = queue.popleft()
                        if (0 <= x < num_rows) and (0 <= y < num_cols) and grid[x][y] == '1':
                            grid[x][y] = '0'    # Marking as visited
                            for dx, dy in directions:
                                queue.append((x+dx, y+dy))

        return num_islands


if __name__ == "__main__":
    assert Solution().numIslands(
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]) == 3
    assert(Solution().numIslands([
        ["1", "1", "1", "1", "1", "0", "1", "1", "1", "1"],
        ["1", "0", "1", "0", "1", "1", "1", "1", "1", "1"],
        ["0", "1", "1", "1", "0", "1", "1", "1", "1", "1"],
        ["1", "1", "0", "1", "1", "0", "0", "0", "0", "1"],
        ["1", "0", "1", "0", "1", "0", "0", "1", "0", "1"],
        ["1", "0", "0", "1", "1", "1", "0", "1", "0", "0"],
        ["0", "0", "1", "0", "0", "1", "1", "1", "1", "0"],
        ["1", "0", "1", "1", "1", "0", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1", "1", "1", "1", "0", "1"],
        ["1", "0", "1", "1", "1", "1", "1", "1", "1", "0"]
    ])) == 2
