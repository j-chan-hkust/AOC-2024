from functools import cache

from aocd import get_data, submit
import time

# Constants
YEAR = 2024
DAY = 11

def main():
    # Fetch the input data for the specified day
    input_data = """125 17"""

    input_data = get_data(day=DAY, year=YEAR)

    print(input_data)

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
    stones = data.split()
    prev_sols = dict()
    for i in range(25):
        next_iter = []
        for stone in stones:
            if stone in prev_sols:
                next_iter += prev_sols[stone]
            else:
                if len(stone)%2 == 0:
                    left = stone[0:len(stone)//2]
                    right = str(int(stone[len(stone)//2:]))
                    prev_sols[stone] = [left,right]
                    next_iter += prev_sols[stone]
                elif stone == '0':
                    prev_sols[stone] = ['1']
                    next_iter += prev_sols[stone]
                else:
                    next_stone = [str(int(stone)*2024)]
                    prev_sols[stone] = next_stone
                    next_iter += prev_sols[stone]
        stones = next_iter
    return len(stones)

#I completely forgot how to do recursive functions haha
#so essentially cache will save previous answers to different inputs
#it saves different input output solutions
#I did do something sort of similar - but really it wasn't implemented very well because it
# saved everything! including many, many replicated strings.
# even though it made calls easier - you had to use SO much memory
# Saving just the tree structure, of nested calls is much much more memory efficient
# actually - using @cache for a lot of API call scripts might make them run MUCH quicker!
# I really gotta start trying to use this!


@cache #in this case - the @ symbol represents syntactic sugar that helps reduce repeated calls
def stones(c, n):
    if n==0:
        return 1
    elif c=='0':
        return stones('1', n-1)
    elif len(c)%2:
        return stones(str(int(c)*2024), n-1)

    return stones(c[:len(c)//2], n-1) + stones(str(int(c[len(c)//2:])), n-1)

def solve_part2(data):
    # Implement your solution for part 2 here
    stns = data.split()
    prev_sols = dict()

    return sum(stones(c, 75) for c in stns)

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    main()  # Call the main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"--- {execution_time:.6f} seconds ---")  # Print the execution time