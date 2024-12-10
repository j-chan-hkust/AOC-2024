from aocd import get_data, submit
import time

# Constants
YEAR = 2024
DAY = 9

def main():
    # Fetch the input data for the specified day
    input_data = get_data(day=DAY, year=YEAR)

    print(input_data)

    #input_data = "2333133121414131402"
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
    count = 0
    blocks = []
    for i in range(len(data)//2):
        file_length = int(data[2*i])
        gap_length = int(data[2*i+1])
        blocks += [count] * file_length
        blocks += [None] * gap_length
        count += 1
    blocks += [count] * int(data[-1]) #need to account for the last file!

    block_index = 0
    result = 0
    while block_index<len(blocks):
        if blocks[block_index] == 0: #it's 0, continue
            pass
        elif blocks[block_index]:
            result += block_index*blocks[block_index]
        else: # it's none, find the next block by popping the end
            candidate_next = blocks.pop()
            while candidate_next is None: #not a valid number
                candidate_next = blocks.pop() # this will fail in a reallly nasty way for some configurations, as it doesn't handle the case where the last item is Nones, but there aren't anymore blocks to fill in
            result += block_index*candidate_next
        block_index += 1
    return result

def arithmetic_series_sum(a, n): #a, first num, n, number of terms
    return (n / 2) * (2 * a + (n - 1))

def solve_part2(data):
    # Implement your solution for part 2 here
    file_name_count = 0
    index = 0
    gaps = []
    blocks = []

    for i in range(len(data)//2):
        file_length = int(data[2*i])
        gap_length = int(data[2*i+1])
        blocks += [(file_name_count, index, file_length)]
        gaps += [(index+file_length, gap_length)]
        file_name_count += 1
        index += file_length+gap_length
    blocks += [(file_name_count, index, int(data[-1]))] #need to account for the last file!

    for i in range(len(blocks)):
        for j in range(len(gaps)):
            if blocks[-i-1][2]<=gaps[j][1] and blocks[-i-1][1]>gaps[j][0]: #missed this small bit of logic that wasn't well handled
                blocks[-i-1] = (blocks[-i-1][0],gaps[j][0],blocks[-i-1][2])
                gaps[j] = (gaps[j][0]+blocks[-i-1][2],gaps[j][1]-blocks[-i-1][2])
                break

    # sum the result of the blocks!
    result = 0
    for block in blocks:
        file_id, index, length = block
        result += arithmetic_series_sum(index, length)*file_id
    return int(result)

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    main()  # Call the main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"--- {execution_time:.6f} seconds ---")  # Print the execution time