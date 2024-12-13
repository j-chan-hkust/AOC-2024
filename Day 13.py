from aocd import get_data, submit
import time
from math import gcd
from fractions import Fraction

def check_solution(a_moves, b_moves, target_x, target_y, ax, ay, bx, by):
    x = a_moves * ax + b_moves * bx
    y = a_moves * ay + b_moves * by
    return x == target_x and y == target_y

def find_min_tokens(ax, ay, bx, by, target_x, target_y, part2=False):
    if not part2:
        # Part 1: brute force up to 100 moves
        for total_moves in range(201):
            for a_moves in range(total_moves + 1):
                b_moves = total_moves - a_moves
                if a_moves > 100 or b_moves > 100:
                    continue
                if check_solution(a_moves, b_moves, target_x, target_y, ax, ay, bx, by):
                    return 3 * a_moves + b_moves
        return None
    else:
        # Part 2: solve using linear equations
        # ax*A + bx*B = target_x
        # ay*A + by*B = target_y
        try:
            # Convert to fractions to handle large numbers
            det = ax * by - ay * bx
            if det == 0:
                return None

            a_moves = Fraction(target_x * by - target_y * bx, det)
            b_moves = Fraction(ax * target_y - ay * target_x, det)

            # Check if solution is integer and non-negative
            if (a_moves.denominator == 1 and b_moves.denominator == 1 and
                a_moves >= 0 and b_moves >= 0):
                return 3 * int(a_moves) + int(b_moves)
        except:
            pass
        return None

def solve_parts(data, part2=False):
    total_tokens = 0
    offset = 10000000000000 if part2 else 0

    machines = data.strip().split('\n\n')
    for machine in machines:
        lines = machine.strip().split('\n')
        ax = int(lines[0].split('X+')[1].split(',')[0])
        ay = int(lines[0].split('Y+')[1])
        bx = int(lines[1].split('X+')[1].split(',')[0])
        by = int(lines[1].split('Y+')[1])
        target_x = int(lines[2].split('X=')[1].split(',')[0]) + offset
        target_y = int(lines[2].split('Y=')[1]) + offset

        tokens = find_min_tokens(ax, ay, bx, by, target_x, target_y, part2)
        if tokens is not None:
            total_tokens += tokens

    return total_tokens

def main():
    input_data = get_data(day=13, year=2024)

    result1 = solve_parts(input_data)
    print(f"Part 1: {result1}")
    submit(result1, part='a', day=13, year=2024)

    result2 = solve_parts(input_data, part2=True)
    print(f"Part 2: {result2}")
    submit(result2, part='b', day=13, year=2024)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"--- {time.time() - start_time:.6f} seconds ---")
