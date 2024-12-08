guard_markers = ["^", ">", "v", "<"]

def read_input():
    lines = []

    with open("input", "r") as input:
        for line in input.read().splitlines():
            lines.append(list(line))

    return lines

def find_start_of_guard(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] in guard_markers:
                return [[row, col], grid[row][col]]

    return None

def count_xes(grid):
    count = 0
    for row in grid:
        for col in row:
            count += col == "X"

    return count

def get_next_direction(current_direction):
    index = guard_markers.index(current_direction)
    return guard_markers[(index + 1)%len(guard_markers)]

def is_out_of_field(grid_size, next_guard_row, next_guard_col):
    rows = grid_size[0]
    cols = grid_size[1]

    return next_guard_row < 0 or next_guard_col < 0 or next_guard_row >= rows or next_guard_col >= cols

def first_puzzle():
    grid = read_input()
    grid_size = (len(grid), len(grid[0]))
    guard = find_start_of_guard(grid)

    while True:
        guard_row = guard[0][0]
        guard_col = guard[0][1]
        guard_direction = guard[1]
        next_direction = get_next_direction(guard_direction)

        next_guard_row = guard_row
        next_guard_col = guard_col

        if guard[1] == "^":
            next_guard_row = guard_row - 1
        elif guard[1] == "v":
            next_guard_row = guard_row + 1
        elif guard[1] == "<":
            next_guard_col = guard_col - 1
        elif guard[1] == ">":
            next_guard_col = guard_col + 1

        if is_out_of_field(grid_size, next_guard_row, next_guard_col):
            grid[guard_row][guard_col] = "X"
            break

        if grid[next_guard_row][next_guard_col] == "#":
            guard[1] = next_direction
        else:
            grid[guard_row][guard_col] = "X"
            grid[next_guard_row][next_guard_col] = next_direction
            guard[0] = [next_guard_row, next_guard_col]

    return count_xes(grid)
    
def second_puzzle():
    pass
    
def main():
    print(f"First puzzle: {first_puzzle()}")
    print(f"Second puzzle: {second_puzzle()}")

if __name__ == '__main__':
    main()

