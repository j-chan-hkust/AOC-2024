from aocd import get_data, submit
import time

# Constants
YEAR = 2024
DAY = 1

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
    submit(result_part1, part='a', day=DAY, year=YEAR)
    #submit(result_part2, part='b', day=DAY, year=YEAR)

def solve_part1(data):
    # Implement your solution for part 1 here
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