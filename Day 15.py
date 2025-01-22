from aocd import get_data, submit
import time

# Constants
YEAR = 2024
DAY = 15

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
    #submit(result_part2, part='b', day=DAY, year=YEAR)

class Warehouse:
    def __init__(self, layout):
        self.grid = [list(row) for row in layout.strip().split('\n')]
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.robot_pos = self.find_robot()  # Store robot position as instance variable

    def find_robot(self):
        """Find the initial position of the robot (@)"""
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == '@':
                    return (y, x)
        raise ValueError("No robot found in layout")

    def move_object(self, y, x, direction):
        """Attempt to move an object (robot or box) at position (y,x)"""
        dy, dx = self._get_direction_vector(direction)
        new_y, new_x = y + dy, x + dx

        # Check if move is within bounds
        if not (0 <= new_y < self.height and 0 <= new_x < self.width):
            return False

        # If empty space, move object
        if self.grid[new_y][new_x] == '.':
            self._move_to(y, x, new_y, new_x)
            if self.grid[new_y][new_x] == '@':
                self.robot_pos = (new_y, new_x)
            return True

        # If wall, can't move
        if self.grid[new_y][new_x] == '#':
            return False

        # If box, try to push it
        if self.grid[new_y][new_x] == 'O':
            # Try to move the box first
            if self.move_object(new_y, new_x, direction):
                # If box moved, move the pushing object
                self._move_to(y, x, new_y, new_x)
                if self.grid[new_y][new_x] == '@':
                    self.robot_pos = (new_y, new_x)
                return True

        return False

    def _move_to(self, old_y, old_x, new_y, new_x):
        """Move object from old position to new position"""
        self.grid[new_y][new_x] = self.grid[old_y][old_x]
        self.grid[old_y][old_x] = '.'

    def _get_direction_vector(self, direction):
        """Convert direction character to movement vector"""
        directions = {
            '^': (-1, 0),  # up
            'v': (1, 0),   # down
            '<': (0, -1),  # left
            '>': (0, 1)    # right
        }
        return directions[direction]

    def calculate_gps_sum(self):
        """Calculate sum of GPS coordinates for all boxes"""
        total = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 'O':
                    total += (100 * y + x)
        return total

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.grid)

class Wide_Warehouse:
    def __init__(self, layout):
        self.grid = [list(row) for row in layout.strip().split('\n')]
        self.height = len(self.grid)
        self.width = len(self.grid[0]*2)
        for i in range(self.height):
            wide_row = ''
            for char in self.grid[i]:
                if char == 'O':
                    wide_row = wide_row + '[]'
                elif char == '#':
                    wide_row = wide_row + '##'
                elif char == '@':
                    wide_row = wide_row + '@.'
                elif char == '.':
                    wide_row = wide_row + '..'
            self.grid[i] = list(wide_row)
        self.robot_pos = self.find_robot()  # Store robot position as instance variable

    def find_robot(self):
        """Find the initial position of the robot (@)"""
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == '@':
                    return (y, x)
        raise ValueError("No robot found in layout")

    def move_object(self, y, x, direction):
        """Attempt to move an object (robot or box) at position (y,x)"""
        dy, dx = self._get_direction_vector(direction)
        new_y, new_x = y + dy, x + dx

        # Check if move is within bounds
        if not (0 <= new_y < self.height and 0 <= new_x < self.width):
            return False

        # If empty space, move object
        if self.grid[new_y][new_x] == '.':
            self._move_to(y, x, new_y, new_x)
            if self.grid[new_y][new_x] == '@':
                self.robot_pos = (new_y, new_x)
            return True

        # If wall, can't move
        if self.grid[new_y][new_x] == '#':
            return False

        # If box, try to push it
        if direction == '<' or direction == '>': # if it's moving left or right, logic is similar.
            if self.grid[new_y][new_x] == '[' or self.grid[new_y][new_x] == ']':
                # Try to move the box first
                if self.move_object(new_y, new_x, direction):
                    # If box moved, move the pushing object
                    self._move_to(y, x, new_y, new_x)
                    if self.grid[new_y][new_x] == '@':
                        self.robot_pos = (new_y, new_x)
                    return True
        else:
            if self.grid[new_y][new_x] == '[':
                # get the left side and right side.
                box_left_y, box_left_x = new_y, new_x
                box_right_y, box_right_x = new_y, new_x+1

                #check if both sides can be moved
                #todo I think you can't just call the move_object function, because it will allow '[' to move up without
                # the other side. You need to restructure it to check first that both sides are moveable, and then move.
                if self.move_object(box_left_y, box_left_x, direction) and self.move_object(box_right_y, box_right_x, direction):
                    self._move_to(y, x, new_y, new_x)

            elif self.grid[new_y][new_x] == ']':
                # get left side and right side
                box_left_y, box_left_x = new_y, new_x-1
                box_right_y, box_right_x = new_y, new_x
                # Try to move the box first
                # if it's moving up or down, logic is different
                # check if it's left or right side.
                # check if the other side can be moved.
                if self.move_object(new_y, new_x, direction):
                    # If box moved, move the pushing object
                    self._move_to(y, x, new_y, new_x)
                    if self.grid[new_y][new_x] == '@':
                        self.robot_pos = (new_y, new_x)
                    return True

        return False

    def _move_to(self, old_y, old_x, new_y, new_x):
        """Move object from old position to new position"""
        self.grid[new_y][new_x] = self.grid[old_y][old_x]
        self.grid[old_y][old_x] = '.'

    def _get_direction_vector(self, direction):
        """Convert direction character to movement vector"""
        directions = {
            '^': (-1, 0),  # up
            'v': (1, 0),   # down
            '<': (0, -1),  # left
            '>': (0, 1)    # right
        }
        return directions[direction]

    def calculate_gps_sum(self):
        """Calculate sum of GPS coordinates for all boxes"""
        total = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 'O':
                    total += (100 * y + x)
        return total

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.grid)

def solve_part1(data):
    # Split input into warehouse layout and instructions
    warehouse_layout, instructions = data.split('\n\n')

    # Create warehouse instance
    warehouse = Warehouse(warehouse_layout)

    # Clean up instructions
    instructions = ''.join(instructions.split())

    # Process each move
    for direction in instructions:
        robot_y, robot_x = warehouse.robot_pos
        warehouse.move_object(robot_y, robot_x, direction)

    return warehouse.calculate_gps_sum()


def solve_part2(data):
    # Implement your solution for part 2 here
    # Split input into warehouse layout and instructions
    warehouse_layout, instructions = data.split('\n\n')

    # Create warehouse instance
    wide_warehouse = Wide_Warehouse(warehouse_layout)

    # Clean up instructions
    instructions = ''.join(instructions.split())

    # Process each move
    for direction in instructions:
        robot_y, robot_x = wide_warehouse.robot_pos
        wide_warehouse.move_object(robot_y, robot_x, direction)

    return wide_warehouse.calculate_gps_sum()

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    main()  # Call the main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"--- {execution_time:.6f} seconds ---")  # Print the execution time