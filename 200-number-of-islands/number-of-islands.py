class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Defensive check
        if not grid:
            return 0
    
        # Helper function - Iterative BFS
        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        # Main function
        n_islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        # Iterate through each cell in the grid and count no of islands
        for r in range(rows):
            for c in range(cols):
                # When find a 1
                if grid[r][c] == '1' and (r, c) not in visit:
                    # Find all surrounding 1 and mark visited
                    bfs(r, c)
                    n_islands += 1
    
        return n_islands