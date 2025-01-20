from aocd import get_data, submit
import time

from fontTools.subset import intersect

# Constants
YEAR = 2024
DAY = 23

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
    # we're really looking to construct a list of all the unique 3 pairs. One way to approach might be:
    # for each pair, it can form a unique 3 pair if both share a connection.
        # how to avoid double counting? How to track that things are duplicated? How to have tuples that don't care about order?
    # once you have the full list of tuples, you can count how many of them contain a "t" computer.

    connections = data.split()
    routings = dict()
    for connection in connections:
        computer1, computer2 = connection.split('-')
        if computer1 not in routings:
            routings[computer1] = {computer2}
        else:
            routings[computer1].add(computer2)

        # you want to have a list of all bindings
        if computer2 not in routings:
            routings[computer2] = {computer1}
        else:
            routings[computer2].add(computer1)

    count = 0
    for connection in connections:
        computer1, computer2 = connection.split('-')
        #these are 2 sets
        c1connected = routings[computer1]
        c2connected = routings[computer2]
        # we want the intersection of them, mutually connnected!
        intersections = c1connected & c2connected
        for element in intersections:
            if computer1[0] == 't' or computer2[0] == 't' or element[0] == 't':
                count += 1
                print(computer1, computer2, element)

    return count//3 # everything should get triple counted..

import networkx as nx

def solve_part2(data):
    # Implement your solution for part 2 here
    # how to check if all elements are mutually connected?
    connections = data.split()
    connections =[tuple(connection.split('-')) for connection in connections]

    G = nx.Graph(connections)
    cliques = nx.find_cliques(G)
    largest_clique = max(cliques, key=len)

    return ','.join(sorted(list(largest_clique)))

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    main()  # Call the main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"--- {execution_time:.6f} seconds ---")  # Print the execution time