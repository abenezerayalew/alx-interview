#!/usr/bin/python3
"""Island perimeter computing module.
"""

def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    """
    if not isinstance(grid, list) or not grid:
        return 0
    
    perimeter = 0
    n, m = len(grid), len(grid[0])
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                edges = [
                    (i == 0 or grid[i - 1][j] == 0),
                    (j == m - 1 or grid[i][j + 1] == 0),
                    (i == n - 1 or grid[i + 1][j] == 0),
                    (j == 0 or grid[i][j - 1] == 0),
                ]
                perimeter += sum(edges)
                
    return perimeter
