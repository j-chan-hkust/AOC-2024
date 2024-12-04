import re

from aocd import get_data, submit

# Constants
YEAR = 2024
DAY = 3

def main():
    # Fetch the input data for the specified day
    input_data = get_data(day=DAY, year=YEAR)

    print(input_data)

    # Example processing function
    result_part1 = solve_part1(input_data)
    print(f"Part 1: {result_part1}")

    #input_data = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
    result_part2 = solve_part2(input_data)
    print(f"Part 2: {result_part2}")

    # Submit answers
    submit(result_part1, part='a', day=DAY, year=YEAR)
    submit(result_part2, part='b', day=DAY, year=YEAR)

def solve_part1(data):
    # Implement your solution for part 1 here
    # pull all regex matches
    pattern = r'mul\(\d+,\d+\)'
    matches = re.findall(pattern, data)
    print(matches)

    pattern = r'\d+,\d+'

    sum = 0
    for match in matches:
        match = re.findall(pattern,match)
        num1,num2 = [int(num) for num in match[0].split(',')]
        sum += num1*num2

    return sum

def solve_part2(data):
    # Implement your solution for part 2 here
    pattern = r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))'
    matches = re.findall(pattern, data)
    print(matches)
    do=True

    pattern = r'\d+,\d+'
    sum=0

    for match in matches:
        if match == "don't()":
            do=False
        elif match == "do()":
            do = True
        else:
            match = re.findall(pattern, match)
            num1, num2 = [int(num) for num in match[0].split(',')]
            sum += num1 * num2 * do
    return sum

if __name__ == "__main__":
    main()