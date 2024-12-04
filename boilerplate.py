from aocd import get_data, submit

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
    #submit(result_part1, part='a', day=DAY, year=YEAR)
    #submit(result_part2, part='b', day=DAY, year=YEAR)

def solve_part1(data):
    # Implement your solution for part 1 here
    return "Result for part 1"

def solve_part2(data):
    # Implement your solution for part 2 here
    return "Result for part 2"

if __name__ == "__main__":
    main()