from aocd import get_data, submit

# Constants
YEAR = 2024
DAY = 1

def main():
    # Fetch the input data for the specified day
    input_data = get_data(day=DAY, year=YEAR)

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

    matrix = [datum.split() for datum in data.split('\n')]

    list1,list2 = [[row[i] for row in matrix] for i in range(len(matrix[0]))]


    list1 = [int(item) for item in list1]
    list2 = [int(item) for item in list2]

    list1.sort()
    list2.sort()

    sum = 0
    for i in range(len(list1)):
        sum += abs(list1[i]-list2[i])

    return sum

def solve_part2(data):
    # Implement your solution for part 2 here
    matrix = [datum.split() for datum in data.split('\n')]

    list1, list2 = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

    list1 = [int(item) for item in list1]
    list2 = [int(item) for item in list2]

    list2dict = {item: list2.count(item) for item in set(list2)}

    sum=0
    for item in list1:
        if item in list2dict:
            sum += list2dict[item]*item

    return sum

if __name__ == "__main__":
    main()