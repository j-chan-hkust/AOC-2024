from aocd import get_data, submit
import time

# Constants
YEAR = 2024
DAY = 6

def main():
    # Fetch the input data for the specified day
    input_data = get_data(day=DAY, year=YEAR)

    print(input_data)

    # Example processing function
    result_part1 = solve_part1(input_data)
    print(f"Part 1: {result_part1}")

#     input_data = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

    result_part2 = solve_part2(input_data)
    print(f"Part 2: {result_part2}")

    # Submit answers
    submit(result_part1, part='a', day=DAY, year=YEAR)
    submit(result_part2, part='b', day=DAY, year=YEAR)

def rotate(dir):
    if dir == (-1,0):
        return (0,1)
    elif dir == (0,1):
        return (1,0)
    elif dir == (1,0):
        return (0,-1)
    else:
        return (-1,0)


def solve_part1(data):
    # Implement your solution for part 1 here
    map = [list(datum) for datum in data.split('\n')]
    x,y = 0,0
    dir = (-1,0)

    for i in range(len(map)):
        if '^' in map[i]:
            x = i
            y = map[i].index('^')

    while x in range(len(map)) and y in range(len(map[0])):
        next_x = x + dir[0]
        next_y = y + dir[1]
        if next_x not in range(len(map)) or next_y not in range(len(map[0])):
            map[x][y] = 'X'
            break
        if map[next_x][next_y] == '#':
            dir = rotate(dir)
            continue
        map[x][y]='X'
        x,y = next_x,next_y

    count = 0
    for row in map:
        for cell in row:
            if cell =='X':
                count+=1

    return count


def solve_part2(data):
    # Implement your solution for part 2 here
    map = [list(datum) for datum in data.split('\n')]
    count = 0

    for i in range (len(map)):
        for j in range(len(map[0])):
            x, y = 0, 0
            dir = (-1, 0)

            for index in range(len(map)):
                if '^' in map[index]:
                    x = i
                    y = map[index].index('^')

            if x == i and y == j: # break if you replace the guard
                continue

            map = [list(datum) for datum in data.split('\n')]
            map[i][j] = '#'

            prev_positions = set()

            while True:
                if (dir, x,y) in prev_positions:
                    count+=1
                    print(i,j)
                    break
                else:
                    prev_positions.add((dir,x,y))
                next_x = x + dir[0]
                next_y = y + dir[1]
                if next_x not in range(len(map)) or next_y not in range(len(map[0])):
                    break
                if map[next_x][next_y] == '#':
                    dir = rotate(dir)
                    continue
                x, y = next_x, next_y

    return count

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    main()  # Call the main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"--- {execution_time:.6f} seconds ---")  # Print the execution time