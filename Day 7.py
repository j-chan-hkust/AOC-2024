from aocd import get_data, submit
import time

# Constants
YEAR = 2024
DAY = 7

def main():
    # Fetch the input data for the specified day
    input_data = get_data(day=DAY, year=YEAR)

    print(input_data)

#     input_data = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""
    # Example processing function
    result_part1 = solve_part1(input_data)
    print(f"Part 1: {result_part1}")

    result_part2 = solve_part2(input_data)
    print(f"Part 2: {result_part2}")

    # Submit answers
    submit(result_part1, part='a', day=DAY, year=YEAR)
    submit(result_part2, part='b', day=DAY, year=YEAR)

def get_nth_bit(number, n):
    # Right shift the number by n and apply bitwise AND with 1
    return (number >> n) & 1

def solve_part1(data):
    # Implement your solution for part 1 here
    # brute for calculation
    tests = data.split('\n')
    sum = 0
    for test in tests:
        result,nums = test.split(': ')
        result = int(result)
        nums = [int(num) for num in nums.split()]

        for i in range (2**(len(nums)-1)):
            potential_result = nums[0]
            for j in range(1,len(nums)):
                if 0 == get_nth_bit(i,j-1):
                    potential_result *= nums[j]
                elif 1 == get_nth_bit(i,j-1):
                    potential_result += nums[j]
            if potential_result == result:
                sum += result
                break

    return sum

#clever function
def evaluate_expression(expr):
    # Split the expression into tokens (numbers and operators)
    tokens = expr.split()

    # Initialize the result with the first number
    result = int(tokens[0])

    # Iterate through the tokens, starting from the second one
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        next_number = int(tokens[i + 1])

        # Perform the operation based on the operator
        if operator == '+':
            result += next_number
        elif operator == '*':
            result *= next_number
        elif operator == '||':
            result = int(str(result) + str(next_number))
        else:
            raise ValueError(f"Unknown operator: {operator}")

    return result

# unfortunately this code is slowwwww.... significantly slower than the code for part 1
# is string manipulation just a slow action?
# no - it's because 2^12 = 4096, 3^12 =  531441, literally 3 orders of magnitude difference in efficiency
# worth defaulting to sol 1 first, as you'd be able to skip a whole bunch of long evals.
# then you could start searching the other possibility spaces. It's honestly just a feature of how the data is shaped - there's more valid * and + based solutions than you'd expect
# actually - reviewing other peoples solutions - I should have instead built in a break condition where you'd give up a certain branch of evaluation if the number got too big
# my solution is rediculously inefficient - taking 715 seconds to evaluate, nearly 10 minutes, because I don't prune or abandon bad branches
def solve_part2(data):
    # Implement your solution for part 2 here
    tests = data.split('\n')

    sum = 0

    for test in tests:
        result, nums = test.split(': ')
        result=int(result)
        candidates = [nums]
        print('evaluating.... ' + nums)
        while candidates: #checks if empty
            candidate = candidates.pop()
            if ' ' in candidate:
                candidates.insert(0,candidate.replace(' ', '+',1))
                candidates.insert(0, candidate.replace(' ', '*', 1))
                candidates.insert(0, candidate.replace(' ', '||', 1))
            else: #this candidate can be evaluated now!
                candidate = candidate.replace('+', ' + ').replace('*'," * ").replace('||',' || ')
                value = evaluate_expression(candidate)
                if value == result:
                    sum+=value
                    break

    return sum

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    main()  # Call the main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"--- {execution_time:.6f} seconds ---")  # Print the execution time