from aocd import get_data, submit
import time

# Constants
YEAR = 2024
DAY = 10

def main():
    # Fetch the input data for the specified day
    input_data = get_data(day=DAY, year=YEAR)

    print(input_data)

#     input_data = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732"""

    # Example processing function
    result_part1 = solve_part1(input_data)
    print(f"Part 1: {result_part1}")

    result_part2 = solve_part2(input_data)
    print(f"Part 2: {result_part2}")

    # Submit answers
    submit(result_part1, part='a', day=DAY, year=YEAR)
    submit(result_part2, part='b', day=DAY, year=YEAR)

def get_next_points(point,map):
    x,y = point
    candidates = [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
    return_candidates = []
    for candidate in candidates:
        c_x, c_y = candidate
        if all([c_x>=0, c_x<len(map), c_y>=0, c_y<len(map[0])]) :
            if map[c_x][c_y]-map[x][y] == 1:
                return_candidates.append(candidate)
    return return_candidates
def solve_part1(data):
    # Implement your solution for part 1 here
    # Implement your solution for part 1 here
    map = data.split()
    map = [[int(c) for c in row] for row in map]
    candidate_points = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                candidate_points.append(((i, j), (i, j)))

    paths = set()
    while candidate_points:
        print(candidate_points)
        start_point, current_point = candidate_points.pop()
        if map[current_point[0]][current_point[1]] == 9:
            paths.add((start_point, current_point))
            continue
        for point in get_next_points(current_point, map):
            candidate_points.append((start_point, point))

    return len(paths)

def solve_part2(data):
    # Implement your solution for part 2 here
    # Implement your solution for part 1 here
    map = data.split()
    map = [[int(c) for c in row] for row in map]
    candidate_points = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                candidate_points.append((i, j))
    count = 0

    while candidate_points:
        current_point = candidate_points.pop()
        if map[current_point[0]][current_point[1]] == 9:
            count += 1
            continue
        for point in get_next_points(current_point, map):
            candidate_points.append(point)

    return count

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    main()  # Call the main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"--- {execution_time:.6f} seconds ---")  # Print the execution time