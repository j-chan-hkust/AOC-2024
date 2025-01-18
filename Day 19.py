from aocd import get_data, submit
import time
from functools import cache

# Constants
YEAR = 2024
DAY = 19

def main():
    # Fetch the input data for the specified day
    input_data = get_data(day=DAY, year=YEAR)

#     input_data = """r, wr, b, g, bwu, rb, gb, br
#
# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu
# bwurrg
# brgr
# bbrgwb"""
    print(input_data)

    # Example processing function
    result_part1 = solve_part1(input_data)
    print(f"Part 1: {result_part1}")

    result_part2 = solve_part2(input_data)
    print(f"Part 2: {result_part2}")

    # Submit answers
    submit(result_part1, part='a', day=DAY, year=YEAR)
    submit(result_part2, part='b', day=DAY, year=YEAR)

towels = []

@cache
def resolvable(pattern, max_len):
    global towels
    if pattern in towels:
        return True
    else:
        maximum = min(max_len, len(pattern))
        for i in reversed(range(1,maximum+1)):
            if pattern[:i] in towels:
                if resolvable(pattern[i:],max_len):
                    return True
        return False

def solve_part1(data):
    # Implement your solution for part 1 here
    global towels
    towels, patterns = data.split('\n\n')
    towels = towels.split(', ')
    patterns = patterns.split()
    max_len = 0
    sum = 0

    for towel in towels:
        if len(towel)>max_len:
            max_len = len(towel)

    for pattern in patterns:
        if resolvable(pattern, max_len):
            sum+=1

    return sum

@cache
def solutions(pattern, max_len)->int:
    global towels
    #base case
    if len(pattern)==0:
        return 1
    if len(pattern) == 1:
        if pattern in towels:
            return 1
        else:
            return 0


    sum = 0

    maximum = min(max_len, len(pattern))
    for i in reversed(range(1,maximum+1)):
        if pattern[:i] in towels:
            sum += solutions(pattern[i:],max_len)
    return sum

def solve_part2(data):
    # Implement your solution for part 2 here

    global towels
    towels, patterns = data.split('\n\n')
    towels = towels.split(', ')
    patterns = patterns.split()
    max_len = 0
    sum = 0

    for towel in towels:
        if len(towel) > max_len:
            max_len = len(towel)

    for pattern in patterns:
        sum += solutions(pattern, max_len)

    return sum

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    main()  # Call the main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"--- {execution_time:.6f} seconds ---")  # Print the execution time