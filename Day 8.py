from aocd import get_data, submit
import time

# Constants
YEAR = 2024
DAY = 8

def main():
    # Fetch the input data for the specified day
    input_data = get_data(day=DAY, year=YEAR)

    print(input_data)

    # Example processing function
    result_part1 = solve_part1(input_data)
    print(f"Part 1: {result_part1}")

    result_part2 = solve_part2(input_data)
    print(f"Part 2: {result_part2}")

    # Submit answers
    #submit(result_part1, part='a', day=DAY, year=YEAR)
    #submit(result_part2, part='b', day=DAY, year=YEAR)

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

    for key in antennas:
        nodes = antennas[key]

    return "Result for part 1"

def solve_part2(data):
    # Implement your solution for part 2 here
    return "Result for part 2"

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    main()  # Call the main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"--- {execution_time:.6f} seconds ---")  # Print the execution time