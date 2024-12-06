guard_markers = ["^", "v", "<", ">"]

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

def first_puzzle():
    grid = read_input()
    grid_size = (len(grid), len(grid[0]))
    guard = find_start_of_guard(grid)

    while True:
        if guard[1] == "^":
            new_row = guard[0][0] - 1
            if new_row < 0:
                grid[guard[0][0]][guard[0][1]] = "X"
                break

            if grid[new_row][guard[0][1]] == "#":
                guard[1] = ">"
            else:
                grid[guard[0][0]][guard[0][1]] = "X"
                grid[new_row][guard[0][1]] = "^"
                guard[0] = [new_row, guard[0][1]]

        elif guard[1] == "v":
            new_row = guard[0][0] + 1
            if new_row >= grid_size[0]:
                grid[guard[0][0]][guard[0][1]] = "X"
                break

            if grid[new_row][guard[0][1]] == "#":
                guard[1] = "<"
            else:
                grid[guard[0][0]][guard[0][1]] = "X"
                grid[new_row][guard[0][1]] = "v"
                guard[0] = [new_row, guard[0][1]]

        elif guard[1] == "<":
            new_col = guard[0][1] - 1
            if new_col < 0:
                grid[guard[0][0]][guard[0][1]] = "X"
                break

            if grid[guard[0][0]][new_col] == "#":
                guard[1] = "^"
            else:
                grid[guard[0][0]][guard[0][1]] = "X"
                grid[guard[0][0]][new_col] = "<"
                guard[0] = [guard[0][0], new_col]

        elif guard[1] == ">":
            new_col = guard[0][1] + 1
            if new_col >= grid_size[1]:
                grid[guard[0][0]][guard[0][1]] = "X"
                break

            if grid[guard[0][0]][new_col] == "#":
                guard[1] = "v"
            else:
                grid[guard[0][0]][guard[0][1]] = "X"
                grid[guard[0][0]][new_col] = ">"
                guard[0] = [guard[0][0], new_col]

    return count_xes(grid)
    
def second_puzzle():
    pass
    
def main():
    print(f"First puzzle: {first_puzzle()}")
    print(f"Second puzzle: {second_puzzle()}")

if __name__ == '__main__':
    main()

