import heapq
from aocd import get_data, submit
import time

# Constants
YEAR = 2024
DAY = 18

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

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(blocks, start, end, max_size=71):
    # Priority queue entries should be (f_score, counter, position) to break ties
    counter = 0  # Tie breaker for equal f_scores
    open_list = [(manhattan_distance(start, end), counter, start)]
    closed_set = set()

    came_from = {}
    g_score = {start: 0}
    f_score = {start: manhattan_distance(start, end)}

    while open_list:
        _, _, current = heapq.heappop(open_list)

        if current in closed_set:
            continue

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        closed_set.add(current)

        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (x + dx, y + dy)

            if (not 0 <= neighbor[0] < max_size or
                not 0 <= neighbor[1] < max_size or
                neighbor in blocks or
                neighbor in closed_set):
                continue

            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                counter += 1
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f = tentative_g_score + manhattan_distance(neighbor, end)
                f_score[neighbor] = f
                heapq.heappush(open_list, (f, counter, neighbor))

    return None

def solve_part1(data):
    # Implement your solution for part 1 here
    blocks = [block.split(',') for block in data.split('\n')]
    blocks = [(int(block[0]),int(block[1])) for block in blocks]
    blocks = set(blocks[:1024])
    current_position = (0,0)
    goal = (70,70)

    path = astar(blocks,current_position,goal)

    return len(path)-1

def solve_part2(data):
    # we're going to implement a binary split search - looking for the byte that breaks.
    blocks = [block.split(',') for block in data.split('\n')]
    blocks = [(int(block[0]), int(block[1])) for block in blocks]
    current_position = (0, 0)
    goal = (70, 70)

    #exporation range
    floor = 0
    ceiling = len(blocks)

    while floor != ceiling:
        candidate = (floor + ceiling) // 2
        if astar(set(blocks[:candidate]), current_position, goal) is None: #no path
            ceiling = candidate
        else:
            floor = candidate+1

    return data.split('\n')[candidate]

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    main()  # Call the main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"--- {execution_time:.6f} seconds ---")  # Print the execution time