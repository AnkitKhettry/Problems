def pacificAtlantic(heights):

        rows = len(heights)
        cols = len(heights[0])
        atlantic_flow = [[False] * cols for i in range(rows)]
        pacific_flow = [[False] * cols for i in range(rows)]

        def is_flow_pacific(coordinates, visited_set):
            visited_set.add(coordinates)
            if pacific_flow[coordinates[0]][coordinates[1]]:
                return True
            else:
                for neighbor in get_neighbors(coordinates):
                    if neighbor not in visited_set and is_flow_pacific(neighbor, visited_set):
                        return True
                return False

        def is_flow_atlantic(coordinates, visited_set):
            visited_set.add(coordinates)
            if atlantic_flow[coordinates[0]][coordinates[1]]:
                return True
            else:
                for neighbor in get_neighbors(coordinates):
                    if neighbor not in visited_set and is_flow_atlantic(neighbor, visited_set):
                        return True
                return False

        def get_neighbors(coordinates):
            n = []
            ci = coordinates[0]
            cj = coordinates[1]

            if ci < len(heights)-1 and heights[ci+1][cj] <= heights[ci][cj]:
                n.append((ci+1, cj))
            if ci > 0 and heights[ci-1][cj] <= heights[ci][cj]:
                n.append((ci-1, cj))
            if cj < len(heights[0])-1 and heights[ci][cj+1] <= heights[ci][cj]:
                n.append((ci, cj+1))
            if cj > 0 and heights[ci][cj-1] <= heights[ci][cj]:
                n.append((ci, cj-1))

            return n

        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    pacific_flow[i][j] = True
                if j == cols - 1 or i == rows - 1:
                    atlantic_flow[i][j] = True

        for i in range(rows):
            for j in range(cols):
                pacific_flow[i][j] = is_flow_pacific((i, j), set([(i, j)]))
                atlantic_flow[i][j] = is_flow_atlantic((i, j), set([(i, j)]))

        required_cells = []

        #print(pacific_flow)
        #print(atlantic_flow)

        for i in range(rows):
            for j in range(cols):
                if pacific_flow[i][j] and atlantic_flow[i][j]:
                    required_cells.append([i, j])

        return required_cells


if __name__ == "__main__":
    print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))


"""
[True, True, True, True, True], 
[True, False, True, True, False], 
[True, True, True, False, False], 
[True, True, False, False, False], 
[True, False, False, False, False]

[False, False, False, False, True], 
[False, False, False, True, True], 
[False, False, True, True, True], 
[True, True, False, True, True], 
[True, True, True, True, True]
"""