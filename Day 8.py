from itertools import combinations
import numpy as np
from aocd import get_data, submit
import time

# Constants
YEAR = 2024
DAY = 8

def main():
    # Fetch the input data for the specified day
    input_data = get_data(day=DAY, year=YEAR)

    print(input_data)

#     input_data = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............"""
    # Example processing function
    result_part1 = solve_part1(input_data)
    print(f"Part 1: {result_part1}")

    result_part2 = solve_part2(input_data)
    print(f"Part 2: {result_part2}")

    # Submit answers
    submit(result_part1, part='a', day=DAY, year=YEAR)
    submit(result_part2, part='b', day=DAY, year=YEAR)

def solve_part1(data):
    # Implement your solution for part 1 here
    # get all the unique antenna types
    # get all the locations of each antenna types
    # calculate the mix of locations of each antinodes
    # count the ones that are in the map

    antennas = {item:[] for item in (list(data))}
    del antennas['\n']
    del antennas['.']

    map = data.split('\n')
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] != '.':
                antennas[map[i][j]] += [(i,j)]
    print(antennas)

    antinodes = set()
    for key in antennas:
        nodes = antennas[key]
        pairs = list(combinations(nodes, 2))
        for pair in pairs:
            p1,p2 = pair
            p1 = np.array(p1)
            p2 = np.array(p2)
            vector = p2-p1
            antinode1 = p1-vector
            antinode2 = p1+2*vector
            antinodes.add(tuple(antinode1))
            antinodes.add(tuple(antinode2))

    result = 0
    for antinode in antinodes:
        x,y = antinode
        if x<0 or x>=len(map) or y<0 or y>=len(map[0]):
            continue
        else:
            result += 1
    return result


def solve_part2(data):
    # Implement your solution for part 2 here
    antennas = {item: [] for item in (list(data))}
    del antennas['\n']
    del antennas['.']

    map = data.split('\n')
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] != '.':
                antennas[map[i][j]] += [(i, j)]
    print(antennas)

    antinodes = set()
    for key in antennas:
        nodes = antennas[key]
        pairs = list(combinations(nodes, 2))
        for pair in pairs:
            p1, p2 = pair
            p1 = np.array(p1)
            p2 = np.array(p2)
            vector = p2 - p1
            candidate_antinode = p1
            n = 0
            while not(candidate_antinode[0] < 0 or candidate_antinode[0] >= len(map) or candidate_antinode[1] < 0 or candidate_antinode[1] >= len(map[0])):
                n+=1
                antinodes.add(tuple(candidate_antinode))
                candidate_antinode = p1-n*vector

            candidate_antinode = p1
            n=0
            while not(candidate_antinode[0] < 0 or candidate_antinode[0] >= len(map) or candidate_antinode[1] < 0 or candidate_antinode[1] >= len(map[0])):
                n += 1
                antinodes.add(tuple(candidate_antinode))
                candidate_antinode = p1 + n * vector

    print(antinodes)
    result = len(antinodes)
    return result

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    main()  # Call the main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"--- {execution_time:.6f} seconds ---")  # Print the execution time