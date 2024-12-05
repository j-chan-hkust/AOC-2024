from aocd import get_data, submit
import time

# Constants
YEAR = 2024
DAY = 5

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

def solve_part1(data):
    # Implement your solution for part 1 here
    rules, updates = data.split('\n\n')
    rules = [rule.split('|') for rule in rules.split()]
    updates = [update.split(',') for update in updates.split()]

    sum = 0
    for update in updates:
        valid = True
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0])>update.index(rule[1]):
                    valid = False
                    break
        sum += valid*int(update[int(len(update)/2)])

    return sum

def solve_part2(data):
    # Implement your solution for part 2 here
    # is it enough to assume that a lazy swap of the values is enough to fix everything?
    rules, updates = data.split('\n\n')
    rules = [rule.split('|') for rule in rules.split()]
    updates = [update.split(',') for update in updates.split()]

    sum = 0
    for update in updates:
        valid = True
        for i in range(23):  #incredibly lazy hack to run the fix as many rules there are to sort of guarantee it works?
                                        #is there some kind of guarantee I can get?
                                        #the slightly less lazy hack is iterate by number of elements.
                                        # Kind of like bubble sort,the most times you need to iterate is by the number of elements?
            for rule in rules:
                if rule[0] in update and rule[1] in update:
                    i1,i2 = update.index(rule[0]),update.index(rule[1])
                    if i1 > i2:
                        valid = False
                        update[i1],update[i2] = update[i2],update[i1]
        if not valid:
            sum += int(update[int(len(update) / 2)])

        #the non-lazy method is to generate an ordering from the rules - and then you can generate an ordering of elements based on them
    return sum

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    main()  # Call the main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"--- {execution_time:.6f} seconds ---")  # Print the execution time