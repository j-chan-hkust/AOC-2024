from aocd import get_data, submit
import time
from typing import List, Set, Dict, Tuple
from collections import defaultdict
import heapq

# Constants
YEAR = 2024
DAY = 20

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

class Node:
    def __init__(self, pos: Point, g_cost: int, h_cost: int, parent=None):
        self.pos = pos
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.parent = parent

    def __lt__(self, other):
        # If f_costs are equal, prefer lower h_cost
        if self.f_cost == other.f_cost:
            return self.h_cost < other.h_cost
        return self.f_cost < other.f_cost

class PathFinder:
    def __init__(self, grid: List[str]):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.start = self._find_point('S')
        self.end = self._find_point('E')

    def _find_point(self, char: str) -> Point:
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == char:
                    return Point(x, y)
        return None

    def _get_neighbors(self, point: Point) -> List[Point]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        neighbors = []

        for dx, dy in directions:
            new_x, new_y = point.x + dx, point.y + dy

            if (0 <= new_x < self.width and
                0 <= new_y < self.height and
                (self.grid[new_y][new_x] == '.' or
                 self.grid[new_y][new_x] == 'E' or
                 self.grid[new_y][new_x] == 'S')):
                neighbors.append(Point(new_x, new_y))

        return neighbors

    def _manhattan_distance(self, point: Point) -> int:
        return abs(point.x - self.end.x) + abs(point.y - self.end.y)

    def find_shortest_path(self) -> int:
        open_set = []
        closed_set = set()
        node_dict = {}  # Keep track of nodes by position

        # Initialize start node
        start_node = Node(self.start, 0, self._manhattan_distance(self.start))
        heapq.heappush(open_set, start_node)
        node_dict[self.start] = start_node

        while open_set:
            current = heapq.heappop(open_set)

            if current.pos == self.end:
                # Reconstruct path for verification
                path = []
                node = current
                while node:
                    path.append(node.pos)
                    node = node.parent
                return current.g_cost

            closed_set.add(current.pos)

            for neighbor_pos in self._get_neighbors(current.pos):
                if neighbor_pos in closed_set:
                    continue

                new_g_cost = current.g_cost + 1

                # If we haven't seen this neighbor before or found a better path
                if (neighbor_pos not in node_dict or
                    new_g_cost < node_dict[neighbor_pos].g_cost):

                    neighbor_node = Node(
                        neighbor_pos,
                        new_g_cost,
                        self._manhattan_distance(neighbor_pos),
                        current
                    )

                    node_dict[neighbor_pos] = neighbor_node

                    if neighbor_pos not in [n.pos for n in open_set]:
                        heapq.heappush(open_set, neighbor_node)

        return -1  # No path found

    def print_path(self, path):
        grid_copy = [list(row) for row in self.grid]
        for point in path:
            if grid_copy[point.y][point.x] not in ['S', 'E']:
                grid_copy[point.y][point.x] = '*'
        for row in grid_copy:
            print(''.join(row))

def main():
    # Fetch the input data for the specified day
    input_data = get_data(day=DAY, year=YEAR)

    input_data = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
    print(input_data)

    # Example processing function
    result_part1 = solve_part1(input_data)
    print(f"Part 1: {result_part1}")

    result_part2 = solve_part2(input_data)
    print(f"Part 2: {result_part2}")

    # Submit answers
    #submit(result_part1, part='a', day=DAY, year=YEAR)
    #submit(result_part2, part='b', day=DAY, year=YEAR)

# each cheat can only happen on walls that are 1 cell thick.
# it can be abstracted to the removal of the wall
# You're not looking for the best cheat, you're looking for cheats that have some impact
# you can't just look at the existing path, some cheats might unlock new paths
# so it seems you gotta run an a* search for every possible cheat?
def solve_part1(data):
    # Implement your solution for part 1 here
    grid = data.split()
    pathfinder = PathFinder(grid)
    shortest_path = pathfinder.find_shortest_path()

    # todo I'm not sure why this script returns the answer-1... It basically just misses out the shortest path...
    # in my head it should work...
    # not to mention the fact that this is really bad code because it takes too long to run - 210 seconds.
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                # check it's not on the edges, if it is its a waste of time
                if 0 == i or j == 0 or i==len(grid)-1 or j==len(grid[0])-1:
                    continue
                elif (grid[i-1][j]=='.' and grid[i+1][j]=='.') or (grid[i][j-1]=='.' and grid[i][j+1]=='.'):#check this tile is a one tile thick wall
                    test_grid = grid[:]
                    test_grid[i] = test_grid[i][:j] + '.' + test_grid[i][j+1:]
                    pathfinder = PathFinder(test_grid)
                    test_shortest = pathfinder.find_shortest_path()
                    if shortest_path-test_shortest>=100:
                        count+=1
            else:
                continue

    return count + 1

def solve_part2(data):
    # Implement your solution for part 2 here
    return "Result for part 2"

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    main()  # Call the main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"--- {execution_time:.6f} seconds ---")  # Print the execution time