import itertools

from aocd import get_data, submit
import time
from collections import defaultdict, deque

YEAR = 2024
DAY = 12

def get_regions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    regions = defaultdict(list)

    def bfs(r, c, char):
        queue = deque([(r,c)])
        region = set([(r,c)])
        visited.add((r,c))

        while queue:
            r, c = queue.popleft()
            for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                if (0 <= nr < rows and 0 <= nc < cols and
                    (nr,nc) not in visited and
                    grid[nr][nc] == char):
                    queue.append((nr,nc))
                    region.add((nr,nc))
                    visited.add((nr,nc))
        return region

    for i in range(rows):
        for j in range(cols):
            if (i,j) not in visited:
                char = grid[i][j]
                region = bfs(i, j, char)
                regions[char].append(region)

    return regions

def get_perimeter(region, grid):
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for r,c in region:
        for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
            if (nr,nc) not in region:
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    perimeter += 1
                else:
                    if grid[nr][nc] != grid[r][c]:
                        perimeter += 1
    return perimeter

def solve_part1(data):
    grid = [list(line) for line in data.splitlines()]
    regions = get_regions(grid)

    total_price = 0
    for char in regions:
        for region in regions[char]:
            area = len(region)
            perimeter = get_perimeter(region, grid)
            total_price += area * perimeter

    return total_price

def get_corners(region):
    corners = 0
    for r, c in region:  # for each point in the region
        # Check all four possible corner configurations
        corner_checks = [
            # Format: ((r1,c1), (r2,c2), (r3,c3)) - the three cells adjacent to corner
            ((r+1,c), (r+1,c+1), (r,c+1)),  # bottom-right corner
            ((r+1,c), (r+1,c-1), (r,c-1)),  # bottom-left corner
            ((r-1,c), (r-1,c+1), (r,c+1)),  # top-right corner
            ((r-1,c), (r-1,c-1), (r,c-1))   # top-left corner
        ]

        for p1, p2, p3 in corner_checks:
            # All three points must either be in or out of the region for a corner
            if (p1 in region and p3 in region):
                if p2 not in region:
                    corners += 1
            elif (p1 not in region and p3 not in region):
                corners += 1

    return corners


def solve_part2(data):
    # so we have a function that returns regions. If we can convert these points into vertices, then maybe we can calculate the number of sides?
    grid = [list(line) for line in data.splitlines()]
    regions = get_regions(grid)

    total_price = 0
    for char in regions:
        for region in regions[char]:
            area = len(region)
            sides = get_corners(region) # corners == number of sides
            total_price += area * sides

    return total_price

def main():
    input_data = get_data(day=DAY, year=YEAR)

    result_part1 = solve_part1(input_data)
    print(f"Part 1: {result_part1}")
    result_part2 = solve_part2(input_data)
    print(f"Part 2: {result_part2}")
    submit(result_part1, part='a', day=DAY, year=YEAR)
    submit(result_part2, part='b', day=DAY, year=YEAR)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"--- {time.time() - start_time:.6f} seconds ---")
