from itertools import product

from aocd import get_data, submit
import time

# Constants
YEAR = 2024
DAY = 14

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

grid_width = 101
grid_height = 103
def solve_part1(data):
    # Implement your solution for part 1 here
    robots = data.split('\n')
    final_position = []
    for robot in robots:
        point, velocity = robot.split()
        point = point.split('=')[1]
        velocity = velocity.split('=')[1]
        px,py = [int(c) for c in point.split(',')]
        vx,vy = [int(c) for c in velocity.split(',')]
        px += 100*vx
        px = px%grid_width
        py += 100*vy
        py = py%grid_height
        final_position.append([px,py])
    q1,q2,q3,q4 = 0,0,0,0
    for position in final_position:
        px,py = position
        if px < (grid_width-1)/2:
            if py < (grid_height-1)/2:
                q1 += 1
            elif py > (grid_height-1)/2:
                q3 += 1
        elif px > (grid_width-1)/2:
            if py < (grid_height-1)/2:
                q2 += 1
            elif py > (grid_height-1)/2:
                q4 += 1
    return q1*q2*q3*q4

def solve_part2(data):
    # Implement your solution for part 2 here
    robots = data.split('\n')
    time_step = 0
    while True:
        final_positions = set()
        for robot in robots:
            point, velocity = robot.split()
            point = point.split('=')[1]
            velocity = velocity.split('=')[1]
            px, py = [int(c) for c in point.split(',')]
            vx, vy = [int(c) for c in velocity.split(',')]
            px += time_step * vx
            px = px % grid_width
            py += time_step * vy
            py = py % grid_height
            final_positions.add((px,py))
        if len(final_positions)==len(robots): #essentially just do a lazy check if the robots are all in different positions
            return time_step
        else:
            time_step+=1

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    main()  # Call the main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"--- {execution_time:.6f} seconds ---")  # Print the execution time