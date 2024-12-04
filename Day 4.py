from aocd import get_data, submit
import numpy as np
import re

# Constants
YEAR = 2024
DAY = 4

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
    submit(result_part2, part='b', day=DAY, year=YEAR)

def get_match(strings, regex1,regex2):
    sum = 0
    for string in strings:
        string = ''.join(string)
        matches = re.findall(regex1, string)
        sum += len(matches)
        matches = re.findall(regex2, string)
        sum += len(matches)

    return sum

def solve_part1(data):
    # Implement your solution for part 1 here
    # From this grid, there are actually a huge array of substrings - horizontal,vertical, each of the diagonals, and
    # the backwards direction as well
    horizontal_strings = [list(row) for row in data.split()]
    vertical_strings = [[horizontal_strings[j][i] for j in range(len(horizontal_strings))] for i in range(len(horizontal_strings[0]))]
    np_array = np.array(horizontal_strings)
    main_diagonals = [np_array[::-1,:].diagonal(i) for i in range(-np_array.shape[0]+1,np_array.shape[1])]
    anti_diagnoals = [np.fliplr(np_array)[::-1,:].diagonal(i) for i in range(-np_array.shape[0]+1,np_array.shape[1])] # flip array to get anti

    regex1 = r'XMAS' #you can't use OR operator for some reason, it doesn't quite work the way I think it does
    regex2 = r'SAMX'

    return (get_match(horizontal_strings, regex1,regex2)
            + get_match(vertical_strings,regex1,regex2)
            + get_match(main_diagonals,regex1,regex2)
            + get_match(anti_diagnoals,regex1,regex2))

def xmas_detected(square):
    diagonals = [square[0,0]+square[2,2],square[0,2]+square[2,0]]
    horizontals = [square[0,1]+square[2,1],square[1,2]+square[1,0]]

    diagonals_eval = all(['S' in diagonal and 'M' in diagonal for diagonal in diagonals])
    #horizontals_eval = all(['S' in horizontal and 'M' in horizontal for horizontal in horizontals])
    # unfortunately wasted a bunch of time because I misunderstood what they were asking for

    return diagonals_eval #+ horizontals_eval # True + True = 2

def solve_part2(data):
    # Implement your solution for part 2 here
    # what a yucky problem lol
    horizontal_strings = np.array([list(row) for row in data.split()])
    sum = 0
    for i in range(1,len(horizontal_strings)-1):
        for j in range(1,len(horizontal_strings[i])-1):
            if horizontal_strings[i,j] == 'A':
                sum += xmas_detected(horizontal_strings[i-1:i+2, j-1:j+2])

    # you're looking for all the matches where the coordinate of the letter "A" matches a specific pattern

    return sum

if __name__ == "__main__":
    main()