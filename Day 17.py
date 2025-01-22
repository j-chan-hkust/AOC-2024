from sqlite3 import register_adapter

from aocd import get_data, submit
import time

# Constants
YEAR = 2024
DAY = 17

def main():
    # Fetch the input data for the specified day
    input_data = get_data(day=DAY, year=YEAR)

    input_data = '''Register A: 17
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0'''
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
    registers, program = data.split('\n\n')
    registers = [int(register.split(': ')[1]) for register in registers.split('\n')]

    register_A, register_B, register_C = registers

    def operand_value(operand) -> int:
        match operand:
            case 4:
                return register_A
            case 5:
                return register_B
            case 6:
                register_C
            case _:
                return operand

    program = [int(command) for command in program.split(': ')[1].split(',')]

    i=0
    output = []
    while i < len(program):
        opcode, operand = program[i], program[i+1]

        match opcode:
            case 0:
                register_A = register_A//2**operand_value(operand)
            case 1:
                register_B = register_B ^ operand
            case 2:
                register_B = operand_value(operand)%8
            case 3:
                if register_A == 0:
                    i+=2
                    continue
                else:
                    i = operand
                    continue
            case 4:
                 register_B = register_B ^ register_C
            case 5:
                output.append(str(operand_value(operand)%8))
            case 6:
                register_B = register_A // 2 ** operand_value(operand)
            case 7:
                register_C = register_A // 2 ** operand_value(operand)
        i += 2
    return ','.join(output)

#todo my solution is just brute force - it works alright in the case of the test case, with short programs.
# it seems in the context of long programs it doesn't really work though. What's the smarter mechanism?
# I guess the answer is to think about it in terms the raw bits that are getting moved around - because that's what all these functions do.
# because ultimately, all the math is operations on a binary string

# researching other people's solutions - the key thing to note is that each output number only consumes the closest 8 bit digits of A
# I guess if i spent more time looking into binary representations I might have found an interesting pattern. ANYWAY

# question - for any arbitrary computer program, is it possible to identify the input that makes the program output itself?
def solve_part2(data):
    return ''
    # Implement your solution for part 2 here
    registers, original_program = data.split('\n\n')
    registers = [int(register.split(': ')[1]) for register in registers.split('\n')]

    _, register_B, register_C = registers

    def operand_value(operand) -> int:
        match operand:
            case 4:
                return register_A
            case 5:
                return register_B
            case 6:
                register_C
            case _:
                return operand

    original_program = original_program.split(': ')[1]
    program = [int(command) for command in original_program.split(',')]

    candidate_A = 0
    register_A = candidate_A
    while True:
        i = 0
        output = []
        while i < len(program):
            opcode, operand = program[i], program[i + 1]

            match opcode:
                case 0:
                    register_A = register_A // 2 ** operand_value(operand)
                case 1:
                    register_B = register_B ^ operand
                case 2:
                    register_B = operand_value(operand) % 8
                case 3:
                    if register_A == 0:
                        i += 2
                        continue
                    else:
                        i = operand
                        continue
                case 4:
                    register_B = register_B ^ register_C
                case 5:
                    output.append(str(operand_value(operand) % 8))
                    if len(output)>len(program)+1:
                        break
                case 6:
                    register_B = register_A // 2 ** operand_value(operand)
                case 7:
                    register_C = register_A // 2 ** operand_value(operand)
            i += 2
        if ','.join(output) == original_program:
            return candidate_A
        else:
            candidate_A += 1
            register_A = candidate_A
            _, register_B, register_C = registers

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    main()  # Call the main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"--- {execution_time:.6f} seconds ---")  # Print the execution time